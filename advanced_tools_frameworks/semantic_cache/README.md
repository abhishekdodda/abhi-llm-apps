# Semantic Cache for LLM Inference: Cost Savings and Fast Retrieval

This repository demonstrates the use of a **semantic cache** to optimize inference workflows with Large Language Models (LLMs). By leveraging semantic similarity and intelligent caching mechanisms, this approach reduces redundant computations, decreases inference costs, and enhances retrieval speeds.

## Key Features

- **Inference Cost Optimization**: Minimizes redundant API calls to LLMs by caching semantically similar queries.
- **Fast Retrieval**: Implements a high-performance caching layer using FAISS for real-time query matching.
- **Scalability**: Designed for seamless integration into LLM-based applications.

## Installation

To set up the project locally, follow these steps:
```bash
   git clone https://github.com/abhishekdodda/semantic-cache.git
   cd semantic-cache
   pip install -r requirements.txt
```
**Open the Jupyter Notebook**
jupyter notebook LLMs_semantic_cache.ipynb

**Dependencies**
The project requires the following libraries:
faiss-cpu
sentence_transformers
transformers

Ensure these are installed before running the notebook.

**Contributing**
Contributions are welcome! Please fork the repository and create a pull request for any enhancements or bug fixes.

**License**
This project is licensed under the MIT License.

**Contact**
For questions or support, please reach out to abhishek.dodda1@gmail.com
