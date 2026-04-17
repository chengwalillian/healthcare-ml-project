import os

from dotenv import load_dotenv

from database.db_connection import get_engine
from scripts.clean import load_raw, clean, save_cleaned
from scripts.fetch import fetch_from_kaggle

load_dotenv()

RAW_PATH = os.getenv("RAW_PATH")
CLEANED_PATH = os.getenv("CLEANED_PATH")

COLUMN_MAP = {
    "Age": "age",
    "Gender": "gender",
    "Blood Type": "blood_type",
    "Medical Condition": "medical_condition",
    "Insurance Provider": "insurance_provider",
    "Billing Amount": "billing_amount",
    "Admission Type": "admission_type",
    "Medication": "medication",
    "Test Results": "test_result",
}


def ingest() -> None:
    print("Ingesting data...")
    df = load_raw(RAW_PATH)
    df = clean(df)
    save_cleaned(df, CLEANED_PATH)

    df = df.rename(columns=COLUMN_MAP)

    df.to_sql(
        name="health",
        con=get_engine(),
        if_exists="replace",
        index=False,
        method="multi",
    )

    print(f"Ingested {len(df)} records into patients table.")


if __name__ == "__main__":
    fetch_from_kaggle()
    ingest()
