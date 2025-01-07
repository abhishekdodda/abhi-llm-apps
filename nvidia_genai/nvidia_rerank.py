!pip install langchain
!pip install langchain_nvidia_ai_endpoints
!pip install faiss-gpu

from langchain_community.document_loaders import PyPDFLoader

document = PyPDFLoader("/content/VILA.pdf").load()

import getpass
import os

os.environ["NVIDIA_API_KEY"] = "xxxx"

from langchain_nvidia_ai_endpoints import ChatNVIDIA

llm = ChatNVIDIA(model="mistralai/mixtral-8x7b-instruct-v0.1")

from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=200)
texts = text_splitter.split_documents(document)

from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
from langchain_community.vectorstores import FAISS

embeddings = NVIDIAEmbeddings()
db = FAISS.from_documents(texts, embeddings)

retriever = db.as_retriever(search_kwargs={"k": 5})

query = "Where is the A100 GPU used?"
docs = retriever.invoke(query)

docs[2]

from langchain_nvidia_ai_endpoints import NVIDIARerank
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever

reranker = NVIDIARerank()
compression_retriever = ContextualCompressionRetriever(
    base_compressor=reranker, base_retriever=retriever
)

reranked_chunks = compression_retriever.invoke(query)

reranked_chunks

from langchain.chains import RetrievalQA
from langchain_nvidia_ai_endpoints import ChatNVIDIA

chain = RetrievalQA.from_chain_type(
    llm=ChatNVIDIA(temperature=0), retriever=compression_retriever
)
result = chain({"query": query})
print(result.get("result"))
