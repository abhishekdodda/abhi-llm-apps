from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig
import sqlite3
import uuid
from faker import Faker

# Initialize Presidio engines
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()
faker = Faker()

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
            fake_value TEXT,
            confidence REAL
        )
    ''')
    conn.commit()
    return conn

def generate_fake_data(pii_type):
    if pii_type == "PHONE_NUMBER":
        return faker.phone_number()
    elif pii_type == "LOCATION":
        return faker.address()
    elif pii_type == "CREDIT_CARD":
        return faker.credit_card_number()
    elif pii_type == "US_SSN":
        return faker.ssn()
    elif pii_type == "EMAIL_ADDRESS":
        return faker.email()
    elif pii_type == "DATE_TIME":
        return faker.date_time().isoformat()
    elif pii_type == "PERSON":
        return faker.name()
    else:
        return "<ANONYMIZED>"

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

    cursor = conn.cursor()
    fake_values = {}
    for result in results:
        fake_value = generate_fake_data(result.entity_type)
        fake_values[result.start] = (result.end, fake_value)
        cursor.execute(
            "INSERT INTO pii_mapping (uuid, pii_type, original_value, fake_value, confidence) VALUES (?, ?, ?, ?, ?)",
            (str(uuid.uuid4()), result.entity_type, text[result.start:result.end], fake_value, result.score)
        )
    conn.commit()

    # Replace original PII with fake data
    anonymized_text = text
    for start, (end, fake_value) in sorted(fake_values.items(), reverse=True):
        anonymized_text = anonymized_text[:start] + fake_value + anonymized_text[end:]

    return anonymized_text, [(result.entity_type, result.score) for result in results]

def main():
    conn = setup_database()
    text = "John is in Texas and his phone number is 555-555-5555"
    anonymized_text, pii_details = anonymize_pii(text, conn)
    print("Anonymized Text:", anonymized_text)

    # Print the PII details in a table format
    print(f"{'PII Type':<15} {'Original Value':<30} {'Anonymized Value':<30} {'Start':<10} {'End':<10} {'Score':<10}")
    print("-" * 115)
    for result in analyzer.analyze(text=text, language="en"):
        fake_value = generate_fake_data(result.entity_type)
        print(f"{result.entity_type:<15} {text[result.start:result.end]:<30} {fake_value:<30} {result.start:<10} {result.end:<10} {result.score:<10.2f}")

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    main()
