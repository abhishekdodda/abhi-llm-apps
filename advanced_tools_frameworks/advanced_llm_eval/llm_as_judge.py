from langchain_community.document_loaders import HuggingFaceDatasetLoader
from langchain_community.document_loaders import HuggingFaceDatasetLoader
from langchain_nvidia_ai_endpoints import ChatNVIDIA, NVIDIAEmbeddings
from ragas import evaluate, answer_relevancy, faithfulness  # Import evaluate and metrics
from ragas.testset.generator import TestsetGenerator
from ragas.testset.evolutions import simple
from datasets import Dataset, DatasetDict  # Import Dataset and DatasetDict
from dataclasses import dataclass, field
from langchain.prompts import Prompt
from ragas.metrics import MetricWithLLM, EvaluationMode
# Load NVIDIA API key from environment variable
nvidia_api_key = os.getenv("NVIDIA_API_KEY")

if not nvidia_api_key:
    raise ValueError("NVIDIA API key not found. Please set the NVIDIA_API_KEY environment variable.")
import typing as t
 
dataset_name = "abhi-dodda/MACCROBAT_biomedical_ner"
page_content_column = "full_text"
 
loader = HuggingFaceDatasetLoader(dataset_name, page_content_column)
dataset = loader.load()

critic_llm = ChatNVIDIA(model="meta/llama-3.1-8b-instruct")
generator_llm = ChatNVIDIA(model="mistralai/mixtral-8x7b-instruct-v0.1")
embeddings = NVIDIAEmbeddings(model="nv-embedqa-e5-v5", truncate="END")
 
generator = TestsetGenerator.from_langchain(
     generator_llm,
     critic_llm,
     embeddings,
     chunk_size=512
)
 
# generate testset
testset = generator.generate_with_langchain_docs(dataset,  test_size=10, is_async=False, raise_exceptions=False, distributions={simple: 1.0})

# answer relevance and faithfulness metrics ignore ground truth, so just fill it with empty values
ground_truth = ['']*len(dataset)
answers = []
contexts = []
queries = ["query1", "query2"]  # Define your queries here

# Define the query_rag function
def query_rag(query):
    return {
        'results': [{
            'answer': 'sample answer',
            'retrieved_document_context': 'sample context'
        }]
    }

# Run queries in search endpoint and collect context and results 
for query in queries:
    json_data = query_rag(query)

    response = json_data['results'][0]['answer']
    answers.append(response)

    seq_str = []
    seq_str.append(json_data['results'][0]['retrieved_document_context'])
    contexts.append(seq_str)

# Store all data in HF dataset for RAGAS
data = {
    "question": queries,
    "answer": answers,
    "contexts": contexts,
    "ground_truth": ground_truth
}

dataset = DatasetDict()
dataset['eval'] = Dataset.from_dict(data)

# Override OpenAI LLM and embedding with NVIDIA AI endpoints
nvidia_llm = ChatNVIDIA(model="meta/llama-3.1-8b-instruct")
nvidia_embeddings = NVIDIAEmbeddings(model="nvidia/nv-embedqa-e5-v5", truncate="END")

result = evaluate(
    dataset["eval"],
    metrics=[answer_relevancy, faithfulness],
    llm=nvidia_llm,
    embeddings=nvidia_embeddings,
    raise_exceptions=False,
    is_async=False,
)

# Ensure 'doc' is defined before using it
doc = dataset[0]  # Example definition, adjust as needed
testset = generator.generate_with_langchain_docs([doc], test_size=10, is_async=False, raise_exceptions=False, distributions={simple: 1.0})

RETRIEVAL_PRECISION = Prompt(
    name="retrieval_precision",
    instruction="""if a user put this query into a search engine, is this result relevant enough that it could be in the first page of results? Answers should STRICTLY be either '1' or '0'. Answer '0' if the provided summary does not contain enough information to answer the question and answer '1' if the provided summary can answer the question.""",
    input_keys=["question", "context"]
)

@dataclass
class RetrievalPrecision(MetricWithLLM):
    name: str = "retrieval_precision"  # type: ignore
    evaluation_mode: EvaluationMode = EvaluationMode.qc  # type: ignore
    context_relevancy_prompt: Prompt = field(default_factory=lambda: RETRIEVAL_PRECISION)
 
    async def _ascore(self, row: t.Dict, callbacks: t.Any, is_async: bool) -> float:
        score = row['response'][0]  # first token is the result [0,1]
        if score.isnumeric():
            return int(score)
        else:
            return 0

retrieval_precision = RetrievalPrecision()

nvidia_llm = ChatNVIDIA(model="meta/llama-3.1-8b-instruct")
nvidia_embeddings = NVIDIAEmbeddings(model="nvidia/nv-embedqa-e5-v5", truncate="END")
 
score = evaluate(dataset["eval"], metrics=[retrieval_precision], llm=nvidia_llm, embeddings=nvidia_embeddings, raise_exceptions=False, is_async=False)

import enum
import os
 
class Choices(enum.Enum):
    Y = "Y"
    N = "N"
 
structured_llm = nvidia_llm.with_structured_output(Choices)
 
structured_llm.invoke("if a user put this query into a search engine, is this result relevant enough that it could be in the first page of results? Answer 'N' if the provided summary does not contain enough information to answer the question and answer 'Y' if the provided summary can answer the question.")
