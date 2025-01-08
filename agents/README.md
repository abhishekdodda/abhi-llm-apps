**CrewAI Multi-Agent System: Customer Support and Research Article Writer**

This project demonstrates the use of **CrewAI** to develop two distinct AI-powered multi-agent systems:
1. **Customer Support Agent**: A robust system for providing high-quality, friendly, and comprehensive customer support.
2. **Research Article Writer**: An intelligent framework for planning, writing, and editing high-quality research articles or blog posts.

Both systems leverage CrewAI's multi-agent capabilities to deliver efficient and reliable outputs by assigning specialized roles to each agent.

---

**## Key Features**

**Customer Support Agent**

- **Senior Support Representative**: Answers customer inquiries with detailed, accurate, and friendly responses.
- **Support Quality Assurance Specialist**: Reviews the support representative's responses to ensure they meet high-quality standards.
- **Integrated Tools**: Uses website scraping tools (e.g., `ScrapeWebsiteTool`) to provide informed answers.

**Research Article Writer**
- **Content Planner**: Creates a structured content outline, audience analysis, and SEO strategy.
- **Content Writer**: Produces a compelling and factually accurate article based on the content plan.
- **Editor**: Reviews and edits the article to align with journalistic best practices and the brand's voice.

---

## Installation

### Prerequisites

- Python 3.8+

- OpenAI API Key

- Required Python Libraries:
  - `crewai==0.28.8`
  - `crewai_tools==0.1.6`
  - `langchain_community==0.0.29`

### Steps
```bash
   git clone https://github.com/your-username/crewai-multi-agent-system.git
   
   cd crewai-multi-agent-system
   
   pip install -r requirements.txt
```
**Running the Systems**

**Customer Support Agent**

The Customer Support Agent system provides comprehensive support to customers, ensuring high quality and reliability.

**Set API Key:** Configure your OpenAI API key in the get_openai_api_key() function.

**Run the Support System:**
```bash
crew.kickoff(inputs={
    "customer": "Customer Name",
    "person": "Customer Representative Name",
    "inquiry": "Customer Inquiry Details"
})
```

**The system outputs**

Support Representative's Response
Quality Assurance Review


**Research Article Writer**

The Research Article Writer system generates well-structured and factually accurate blog articles.

Set API Key: Configure your OpenAI API key in the get_openai_api_key() function.
Run the Writing System:
```bash
crew.kickoff(inputs={"topic": "Topic of the Research Article"})
```
**The system outputs**

Content Plan
Written Article
Edited and Ready-to-Publish Article

**Example Use Cases**

**Customer Support Agent**

Handle complex customer inquiries with friendly and detailed responses.
Ensure customer satisfaction with a rigorous quality assurance process.

**Research Article Writer**

Generate blog articles or research papers on technical or trending topics.
Automate the content creation process with role-specific agents.

**Dependencies**

**crewai:** Core library for creating and managing agents and tasks.
**crewai_tools:** Utility tools for web scraping and search.
**langchain_community:** For enhanced LLM integration.
```bash
pip install crewai==0.28.8 crewai_tools==0.1.6 langchain_community==0.0.29
```
**Contributing**

I welcome contributions to enhance the project! To contribute:

Fork the repository.

Create a feature branch

git checkout -b feature-name

Commit your changes and push the branch.

Open a pull request.

**License**
This project is distributed under the MIT License. See LICENSE for details.

**Contact**
For any questions, suggestions, or support, feel free to contact abhishek.dodda1@gmail.com
