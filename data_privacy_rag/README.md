# Data Privacy for LLM Applications using Microsoft Presidio

This project demonstrates how to incorporate robust **data privacy mechanisms** into LLM applications using the open-source **Microsoft Presidio** library. By identifying and anonymizing Personally Identifiable Information (PII), this project ensures data privacy compliance and protects sensitive user information. 

The project includes two primary approaches:

1. **Using Faker Library**: Anonymizes PII by replacing sensitive data with realistic synthetic values (e.g., fake names, phone numbers).

2. **Generic Anonymization**: Replaces PII with placeholders (e.g., `<ANONYMIZED>`), suitable for applications requiring stricter anonymization.

---

## Features

- **PII Detection**: Utilizes Microsoft Presidio’s `AnalyzerEngine` to identify sensitive data, including:
  - Phone Numbers
    
  - Locations
    
  - Credit Card Numbers
    
  - Social Security Numbers (SSN)
    
  - Email Addresses
    
  - Dates/Times
    
  - Personal Names
    
- **Anonymization**:

  - **Faker Library**: Generates realistic fake data for anonymized replacement.
    
  - **Generic Replacement**: Uses predefined placeholders (`<ANONYMIZED>`) for anonymization.
    
  - **Database Mapping**: Tracks original and anonymized values in a SQLite database for audit and traceability.
    
  - **Customizable Configurations**: Easily extendable to add more PII types or adjust anonymization behavior.

---

## Installation

### Prerequisites

- Python 3.8+
- Required Python Libraries:
  - `presidio-analyzer`
  - `presidio-anonymizer`
  - `faker`
  - `sqlite3`

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/abhishekdodda/abhi-llm-apps.git
   cd abhi-llm-apps/data_privacy_rag
   pip install -r requirements.txt
    ```

**Usage**

Approach 1: Using Faker Library for Realistic Anonymization

Purpose: Replaces sensitive data with realistic fake values (e.g., fake names, phone numbers).

Execution: Run the faker_anonymization.py script:
```bash
python faker_anonymization.py
```
Example: 
Input:
"John is in Texas and his phone number is 555-555-5555"

Output:
"Brian Johnson is in 123 Elm Street and his phone number is 123-456-7890"

Database: Tracks the mapping of original and fake values in pii_mapping.db.

Approach 2: Generic Anonymization with <ANONYMIZED> Placeholders

Purpose: Replaces sensitive data with <ANONYMIZED> placeholders.

Execution: Run the generic_anonymization.py script:
```bash
python generic_anonymization.py
```
Example: Input:
"Abhishek Dodda is in Texas and his phone number is 555-555-5555"

Output:
<ANONYMIZED> is in <ANONYMIZED> and his phone number is <ANONYMIZED>

Database: Tracks original values and anonymization details in pii_mapping.db.

**Supported PII Types**

PHONE_NUMBER

LOCATION

CREDIT_CARD

US_SSN

EMAIL_ADDRESS

DATE_TIME

PERSON

**Customization**

Adding New PII Types: Update the analyzer.analyze method to include additional entities.

Custom Fake Data: Modify the generate_fake_data function to customize how fake data is generated for each PII type.

Anonymization Operators: Change the OperatorConfig in the generic anonymization approach to use other techniques like masking or redaction.

Example Database Schema

SQLite database (pii_mapping.db) tracks the following:

**uuid**: Unique identifier for the PII record.

**pii_type**: Type of the detected PII (e.g., PHONE_NUMBER).

**original_value**: The original sensitive data.

**fake_value**: The anonymized replacement value (for Faker-based anonymization).

**confidence**: Confidence score for the PII detection.

**Applications**

Data Privacy Compliance:

Ensure compliance with GDPR, HIPAA, or other privacy regulations.

LLM Applications:

Anonymize input data for training or inference in large language models.

Data Sharing:

Safely share datasets containing sensitive information.

**Contributing**

We welcome contributions to improve the project. To contribute:

Fork the repository.

Create a feature branch:
```bash
git checkout -b feature-name
```
Commit your changes and push the branch.

Open a pull request.

License
This project is licensed under the MIT License. See LICENSE for details.

Contact
For any questions, suggestions, or support, feel free to contact abhishek.dodda1@gmail.com

