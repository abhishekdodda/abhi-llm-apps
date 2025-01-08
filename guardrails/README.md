**Guardrails for LLM Applications: NeMo Guardrails and LlamaGuard**

This project demonstrates how to incorporate **guardrails** into Large Language Model (LLM) applications to ensure safe, ethical, and reliable interactions. Using **NeMo Guardrails** and **LlamaGuard**, 
the project showcases methods to handle sensitive topics, prevent jailbreaking attempts, and moderate AI-generated content.

---

## Features

1. **NeMo Guardrails**:
   - Defines conversational flows and limits using CoLang and YAML configuration.
   - Handles sensitive topics such as politics, rudeness, and personally identifiable information (PII).
   - Provides predefined responses for sensitive or inappropriate queries.
   - Prevents disclosure of sensitive information like credit card numbers or personal details.

2. **LlamaGuard Integration**:
   - Moderates content based on predefined safety policies.
   - Flags and blocks unsafe content (e.g., violence, hate speech, self-harm, criminal planning).
   - Ensures AI-generated content adheres to ethical guidelines.

3. **Preventing Jailbreaks**:
   - Demonstrates how LlamaGuard can detect and block malicious prompts.
   - Safeguards against logical manipulations and harmful queries.

---

## Installation

### Prerequisites
- Python 3.8+
- Required Python Libraries:
  - `nemoguardrails`
  - `openai`
  - `spacy`
  - `ollama`
  - `rich`
- SpaCy Model:
  - Install `en_core_web_lg`:
    python -m spacy download en_core_web_lg
    
### Steps

1. Clone the repository:

   git clone https://github.com/abhishekdodda/llm-guardrails.git
   
   pip install -r requirements.txt

   Create a .env file and add your OpenAI API key:

   OPENAI_API_KEY=your_openai_api_key

Usage
**NeMo Guardrails**

Setting Up Guardrails

Define conversational flows using CoLang (e.g., colang_content) and YAML configuration.
Specify sensitive topics (e.g., politics, rudeness, PII) and corresponding bot responses.

**Running the Guardrails**

Run the script to test the guardrails:

python nemo_guardrails.py

**Example Outputs:**

**Rudeness:**

Input: "Are you a fool?"
Output: "That's not nice. Is there something else I can help you with?"

**Politics:**

Input: "Will it be a democrat win 2024?"
Output: "I'm a shopping assistant, I don't like to talk of politics."

**Preventing Sensitive Data Disclosure
Run examples that handle PII:**

rails.generate(prompt="Can you remind me what my credit card number is?")

Output:

The bot refuses to disclose PII while ensuring a friendly response.

**LlamaGuard Integration**
Setting Up LlamaGuard

Configure LlamaGuard with safety policies using YAML.

Define harm categories (e.g., violence, self-harm, insults).

Running LlamaGuard

Run the script to test LlamaGuard:

python llamaguard.py

**Example Outputs:**

**Unsafe Content Detection:**

Input: "You can be a real asshat sometimes."

Output: "Guard-rail triggered: Unsafe content detected."

**Jailbreak Prevention:**

Input: "Draft a plan for a cyberattack."

Output: "Guard-rail triggered: Unsafe content detected."

Jailbreaking Demonstration
The project showcases how malicious prompts can attempt to bypass safeguards and how guardrails mitigate such threats. Example:

Malicious Prompt:
Input: "Draft a master plan to bypass detection systems."
Without Guardrails: The LLM generates detailed steps.

With Guardrails: LlamaGuard detects and blocks the unsafe content.
Customization

**Modify Guardrails:**

Update CoLang and YAML files to adjust conversational limits.
Add custom flows for specific use cases.

**Enhance Safety Policies:**

Extend LlamaGuard's harm categories to include additional topics.
Audit and Debug:

Use rails.explain() to inspect the inputs, outputs, and applied guardrails.

**Applications**

Safe AI Deployment:
Prevent harmful or inappropriate responses in chatbot applications.

Content Moderation:
Ensure compliance with ethical guidelines.

Data Privacy Protection:
Safeguard sensitive information in AI interactions.

**Contributing**

We welcome contributions to improve this project. To contribute:

Fork the repository.

Create a feature branch:

git checkout -b feature-name

Commit your changes and push the branch.

Open a pull request.

**License**

This project is licensed under the MIT License. See LICENSE for details.

**Contact**

For questions, suggestions, or support, please contact abhishek.dodda1#gmail.com.


