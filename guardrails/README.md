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
    ```bash
    python -m spacy download en_core_web_lg
    ```

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/llm-guardrails.git
