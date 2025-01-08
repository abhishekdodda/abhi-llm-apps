**Mixture-of-Agents LLM App**

This code demonstrates a **Mixture-of-Agents** approach for generating high-quality responses by aggregating outputs from multiple open-source Large Language Models (LLMs). 
The app is built with **Streamlit** to provide a user-friendly interface for querying multiple LLMs and synthesizing their responses.

**Key Features**

- **Multi-Model Querying**: Sends a user prompt to multiple LLMs to gather diverse responses.
- **Response Aggregation**: Combines individual model outputs into a single, refined, high-quality response using an aggregator model.
- **Interactive Interface**: Streamlit-based UI for seamless interaction with the system.
- **Customizable Models**: Easily swap or configure reference and aggregator models.

## Models Used

The app utilizes the following reference models:
- `Qwen/Qwen2-72B-Instruct`
- `Qwen/Qwen1.5-72B-Chat`
- `mistralai/Mixtral-8x22B-Instruct-v0.1`
- `databricks/dbrx-instruct`

The aggregator model:
- `mistralai/Mixtral-8x22B-Instruct-v0.1`

## How It Works

1. **User Query**: Enter a question in the input field.
2. **Model Responses**: The app sends the query to multiple reference models and retrieves individual responses.
3. **Aggregation**: The aggregator model synthesizes the individual responses into a single comprehensive reply.
4. **Display**: Both individual responses and the aggregated response are displayed in the app.

## Installation

To set up and run the project locally, follow these steps:
   git clone https://github.com/your-username/mixture-of-agents.git
   cd mixture-of-agents
   pip install -r requirements.txt
   streamlit run app.py

Interface Walkthrough
Main Page:

Enter your Together API Key to authenticate.
Input a question or prompt to query the MoA system.
View individual LLM responses and the aggregated result.
Sidebar:

Learn about MoA and how it works.
MoA Models Used
The app utilizes the following models:

Reference Models:
Qwen/Qwen2-72B-Instruct
Qwen/Qwen1.5-72B-Chat
mistralai/Mixtral-8x22B-Instruct-v0.1
databricks/dbrx-instruct
Aggregator Model:
mistralai/Mixtral-8x22B-Instruct-v0.1
Use Cases
Mixture of Agents is ideal for scenarios where quality outweighs latency, including:

Synthetic Data Generation: Produces diverse and high-quality datasets.
Detailed Research: Synthesizes nuanced perspectives from multiple models.
Balanced Decision-Making: Mitigates biases by incorporating insights from multiple LLMs.
Contributing
We welcome contributions to this project! To contribute:

Fork the repository.
Create a feature branch:
bash
Copy code
git checkout -b feature-name
Commit your changes and push the branch.
Open a pull request.
License
This project is distributed under the MIT License. See LICENSE for more details.

Contact
For any questions, suggestions, or support, feel free to contact [your-email@example.com].


