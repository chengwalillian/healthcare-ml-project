from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import pandas as pd

NUMERIC_FEATURES = ["Age", "Billing Amount"]

CATEGORICAL_FEATURES = [
    "Gender",
    "Blood Type",
    "Medical Condition",
    "Insurance Provider",
    "Admission Type",
    "Medication",
]


def build_preprocessor() -> ColumnTransformer:
    return ColumnTransformer(
        transformers=[
            ("num", "passthrough", NUMERIC_FEATURES),
            ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL_FEATURES),
        ]
    )


def encode_labels(y: pd.Series) -> tuple:
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)
    return y_encoded, le


def load_features_from_db(engine) -> tuple:
    df = pd.read_sql("SELECT * FROM health", con=engine)
    df = df.rename(columns={
        "age": "Age",
        "gender": "Gender",
        "blood_type": "Blood Type",
        "medical_condition": "Medical Condition",
        "insurance_provider": "Insurance Provider",
        "billing_amount": "Billing Amount",
        "admission_type": "Admission Type",
        "medication": "Medication",
        "test_result": "Test Results",
    })
    X = df[NUMERIC_FEATURES + CATEGORICAL_FEATURES]
    y = df["Test Results"]
    return X, y
