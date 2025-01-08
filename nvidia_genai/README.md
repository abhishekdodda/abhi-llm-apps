# LLM Applications with NVIDIA Ecosystem

This project demonstrates building advanced Large Language Model (LLM) applications using the NVIDIA ecosystem. By leveraging NVIDIA NIM and VILA, the project showcases two key functionalities:
1. **Rerank Functionality**: Enhances retrieval results with NVIDIA NIM and the Mistral 7B model.
2. **Vision-Language Model (VLM)**: Demonstrates VILA (Vision and Language Applications) for multimedia content understanding.

---

## Features

### Rerank Functionality with Retrieval (NVIDIA NIM)
- **Retrieval with FAISS**:
  - Splits documents into chunks for vector search.
  - Utilizes NVIDIA embeddings for efficient indexing and querying.
- **Reranking with NIM**:
  - Reranks the retrieved documents using a Mistral 7B parameter model.
  - Improves the relevance of search results for enhanced user experience.

### Vision-Language Model (VILA)
- **Multimedia Content Understanding**:
  - Supports analyzing images and videos with descriptive queries.
  - Leverages NVIDIA VILA to interpret multimedia content and generate detailed explanations.

---

## Installation

### Prerequisites
- Python 3.8+
- Required Python Libraries:
  - `langchain`
  - `langchain_nvidia_ai_endpoints`
  - `faiss-gpu`
  - `requests`

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/nvidia-llm-apps.git
   cd nvidia-llm-apps
   pip install -r requirements.txt
   NVIDIA_API_KEY=your_nvidia_api_key```

Usage

**Rerank Functionality with Retrieval**

Step 1: Load and Split Documents

Load a PDF document and split it into manageable chunks

Step 2: Perform Retrieval

Index the document chunks using FAISS and perform retrieval

Step 3: Rerank Results

Use NVIDIA’s Rerank module to improve retrieval results

Step 4: Generate Final Response

Integrate reranking with a Retrieval-based QA chain

**Vision-Language Model (VILA)**

**Step 1: Upload Multimedia Files**

Upload images or videos for analysis:

python test.py sample1.png sample2.png

**Step 2: Analyze video Content**

Send descriptive queries to VILA for content analysis:

python test.py sample.mp4

query = "Describe the scene"

**Step 3: Retrieve and Display Results**

The output provides a detailed description of the uploaded video content:

"content": "This is an indoor scene showing a conference room with multiple people engaged in discussion."

**Customization**

**Rerank Module**

Adjust the chunk size and overlap in RecursiveCharacterTextSplitter.
Customize the search_kwargs parameter to modify the number of retrieved documents.

**VILA**

Extend supported media formats in the kSupportedList dictionary.
Modify query parameters (e.g., temperature, max_tokens) for tailored outputs.

**Applications**

Enhanced Document Search:
Rerank functionality improves the accuracy of search results in knowledge bases or archives.

Multimedia Analysis:
VILA enables querying and understanding multimedia content, such as video surveillance or image-based datasets.

Contributing
Welcome contributions to improve this project. To contribute:

Fork the repository.
Create a feature branch:
bash
Copy code
git checkout -b feature-name

Commit your changes and push the branch.

Open a pull request.

**License**

This project is licensed under the MIT License. See LICENSE for details.

**Contact**

For questions, suggestions, or support, feel free to contact abhishek.dodda1@gmail.com.

