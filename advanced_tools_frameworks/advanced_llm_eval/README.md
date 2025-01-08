# Evaluating LLM Applications with RAGAS, LLM as a judge

Welcome to the project on **Evaluating LLM Applications** using the **LLM-as-a-Judge** framework with **RAGAS** and **NVIDIA AI Endpoints**. code demonstrates an efficient evaluation framework for Retrieval-Augmented Generation (RAG) systems, focusing on **answer relevancy**, **faithfulness**, and **retrieval precision**. The implementation leverages models like **NVIDIA Llama 3.1** and **Mistral Mixtral**.

## Overview

project showcases an end-to-end evaluation pipeline designed to assess the performance of RAG-based LLM systems. By using **RAGAS**, a specialized library for RAG evaluation, combined with **NVIDIA AI Endpoints**, the framework ensures robust and precise evaluation metrics tailored for real-world use cases. 

Key highlights include:
- Generating test datasets with LLMs, RAGAS and LangChain integration.
- Assessing answer relevancy and faithfulness with custom prompts.
- Employing NVIDIA models for high-quality evaluation and embeddings.
- Customizing evaluation metrics like retrieval precision for targeted assessments.

## Highlights

### 1. **LLM-as-a-Judge Concept**
The framework applies the **LLM-as-a-Judge** methodology, utilizing powerful language models as evaluators to analyze and grade generated outputs. This ensures objective and consistent evaluation across metrics.

### 2. **Answer Relevancy and Faithfulness**
- **Answer Relevancy**: Measures how relevant the generated answers are to the provided query.
- **Faithfulness**: Ensures that generated answers are grounded in the provided context and do not hallucinate information.

### 3. **Retrieval Precision**
Custom-defined metrics evaluate the accuracy of retrieved contexts, determining if they would appear on the first page of search results.

### 4. **NVIDIA AI Models**
- **Llama 3.1** and **Mistral Mixtral** are used for language generation and evaluation.
- **NV-EmbedQA-E5-V5** provides high-quality embeddings for vector-based evaluations.

### 5. **Biomedicine Use Case**
The framework is demonstrated on a **biomedical dataset** (`MACCROBAT_biomedical_ner`) to evaluate its capabilities in a specialized domain.

## Key Features

- **Testset Generation**: Automatically generate test datasets with LangChain integration and RAGAS testset utilities.
- **Custom Metrics**: Extend evaluation capabilities with bespoke metrics like `retrieval_precision`.
- **Structured LLM Responses**: Use structured outputs for precision-driven evaluations.
- **Domain-Specific Evaluation**: Tailor evaluations to specific domains like healthcare and biomedicine.

## Applications

- **Healthcare and Biomedicine**:
  - Evaluate RAG systems for accuracy and reliability in sensitive domains.
  - Assess the quality of answers and retrieved information in medical datasets.
- **Search Engine Optimization**:
  - Analyze retrieval precision for ranking results effectively.
- **General AI Applications**:
  - Evaluate RAG systems for diverse domains, ensuring high-quality and trustworthy outputs.

## How It Works

1. **Dataset Loading**:
   - Use HuggingFace datasets to load domain-specific data.
   - Prepare datasets for evaluation using LangChain loaders.

2. **Testset Generation**:
   - Generate test datasets with RAGAS utilities, leveraging `TestsetGenerator` for consistency and quality.

3. **Evaluation Metrics**:
   - Apply RAGAS metrics like answer relevancy, faithfulness, and retrieval precision.
   - Customize metrics for specific use cases.

4. **NVIDIA AI Models**:
   - Use Llama 3.1 and Mistral Mixtral for text generation and evaluation.
   - Employ NVIDIA embedding models for contextual similarity and analysis.

## Getting Started

1. **Prerequisites**:
   - Python 3.8+
   - Libraries: `ragas`, `langchain_community`, `datasets`, `langchain_nvidia_ai_endpoints`

2. **Setup**:
   - Clone the repository and install required dependencies:
     ```bash
     git clone https://github.com/abhishekdodda/abhi-llm-apps.git
     cd abhi-llm-apps/advanced_tools_frameworks/advanced_llm_eval
     pip install -r requirements.txt
     ```

3. **Run Evaluation**:
   - Load your dataset, generate test sets, and execute the evaluation pipeline.

## Conclusion

This repository provides a robust framework for evaluating Retrieval-Augmented Generation (RAG) systems, ensuring high-quality, reliable, and relevant outputs. With its focus on metrics like answer relevancy, faithfulness, and retrieval precision, it serves as a critical tool for assessing AI systems in sensitive and domain-specific applications.

For further details and examples, explore the codebase and blog post linked above. Let’s build trustworthy AI together!
