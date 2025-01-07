from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig
import sqlite3
import uuid

# Initialize Presidio engines
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

# Database setup
def setup_database():
    conn = sqlite3.connect('pii_mapping.db')
    cursor = conn.cursor()
    # Drop the table if it already exists (optional, if you want to start fresh)
    cursor.execute('DROP TABLE IF EXISTS pii_mapping')
    # Create the table with the correct schema
    cursor.execute('''
        CREATE TABLE pii_mapping (
            uuid TEXT PRIMARY KEY,
            pii_type TEXT,
            original_value TEXT,
            confidence REAL
        )
    ''')
    conn.commit()
    return conn

def anonymize_pii(text, conn):
    # Analyze text for PII
    results = analyzer.analyze(
        text=text,
        language="en",
        entities=[
            "PHONE_NUMBER",
            "LOCATION",
            "CREDIT_CARD",
            "US_SSN",
            "EMAIL_ADDRESS",
            "DATE_TIME",
            "PERSON"
        ])

    # Prepare anonymization configuration
    cursor = conn.cursor()
    print((results))
    # Prepare anonymization configuration
    operators = {"default": OperatorConfig(operator_name="replace", params={"new_value": "<ANONYMIZED>"})}

    # Anonymize text
    anonymized_result = anonymizer.anonymize(
        text=text,
        analyzer_results=results,
        operators=operators
    )

    # Store original and anonymized mappings in the database
    for result in results:
        cursor.execute(
            "INSERT INTO pii_mapping (uuid, pii_type, original_value, confidence) VALUES (?, ?, ?, ?)",
            (str(uuid.uuid4()), result.entity_type, text[result.start:result.end], result.score)
        )
    conn.commit()
    return anonymized_result.text, [(result.entity_type, result.score) for result in results]

def main():
    conn = setup_database()
    text = "John is in Texas and his phone number is 555-555-5555"
    anonymized_text, _ = anonymize_pii(text, conn)
    print("Anonymized Text:", anonymized_text)
    # Close the database connection
    conn.close()

if __name__ == "__main__":
    main()
