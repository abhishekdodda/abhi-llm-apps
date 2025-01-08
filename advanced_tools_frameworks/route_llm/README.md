# RouteLLM App

The **RouteLLM App** is an innovative chatbot application that leverages **efficient router models** to dynamically select between stronger and weaker Large Language Models (LLMs) during inference. 
This approach balances cost and response quality, making it a practical solution for deploying LLMs in real-world applications.

---

## What is RouteLLM?

Large language models (LLMs) exhibit impressive capabilities across a wide range of tasks, yet selecting the right model often involves a trade-off between performance and cost:
- **Stronger Models**: Deliver higher-quality responses but are more expensive to run.
- **Weaker Models**: Are cost-effective but may compromise response quality.

To address this dilemma, **RouteLLM** employs router models that:
1. Dynamically decide whether to use a stronger or weaker model for each query.
2. Optimize cost savings without compromising response quality.

### Key Innovations:
- **Dynamic Routing**: Router models make decisions in real-time to balance cost and performance.
- **Training Framework**: Leveraging human preference data and data augmentation techniques, the routers are trained to optimize decision-making.
- **Transfer Learning**: Routers maintain performance even when the underlying strong and weak models are swapped during testing.

Our evaluation on benchmarks demonstrates:
- **Cost Reductions**: Savings of over 2x in certain cases.
- **Quality Preservation**: Comparable response quality to always using a strong model.

---

## Key Features

- **Dynamic Model Selection**: Routes queries to the optimal model based on cost-performance trade-offs.
- **Streamlit Interface**: Provides an interactive and user-friendly chat experience.
- **Chat History**: Displays user and assistant messages along with model usage.
- **Customizable Models**: Easily update the strong and weak models as per your requirements.

---

## Installation

**Prerequisites**
- Python 3.8+
- OpenAI API Key
- TogetherAI API Key

**Steps**
```bash
   git clone https://github.com/abhishekdodda/routellm-chat-app.git
   cd routellm-chat-app
   pip install -r requirements.txt
   streamlit run app.py
```
**Interface Walkthrough**

Chat History: Displays user and assistant messages along with the model used for each response.

Chat Input: Enter your query, and RouteLLM will dynamically decide which model to use for the response.

**How It Works**

**Routing Decision:** The router determines whether the query should be processed by the strong or weak model.

**Model Inference:** The chosen model generates the response.

**Response Display:** The app shows the assistant's reply alongside the name of the model used.

**Models Used**

**Strong Model:** gpt-4o-mini

**Weak Model:** Meta-Llama-3.1-70B-Instruct-Turbo

**Router:** Trained to optimize the balance between cost and response quality.

**Use Cases**

**The RouteLLM Chat App is ideal for:**

**Cost-Effective Applications:** Deploy LLMs efficiently for use cases like customer support and interactive chatbots.

**Research and Evaluation:** Test dynamic routing with different strong and weak model configurations.

**Scalable AI Solutions:** Minimize costs while delivering high-quality outputs at scale.

**Contributing**

We welcome contributions to enhance the project! To contribute:

Fork the repository.

**Create a feature branch:**
```bash
git checkout -b feature-name
```
Commit your changes and push the branch.

Open a pull request.

**License**

This project is distributed under the MIT License. See LICENSE for more details.

**Contact**

For any questions, suggestions, or support, feel free to contact abhishek.dodda1@gmail.com.
