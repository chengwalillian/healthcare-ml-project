import os
from dotenv import load_dotenv

import joblib
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

from database.db_connection import get_engine
from ml.evaluate import evaluate
from ml.preprocess import load_features_from_db, encode_labels, build_preprocessor

load_dotenv()

PIPELINE_PATH = os.getenv("MODEL_PIPELINE_PATH")
PACKAGE_PATH = os.getenv("MODEL_PACKAGE_PATH")

def train() -> None:
    print("Training model...")
    engine = get_engine()
    X, y = load_features_from_db(engine)

    y_encoded, le = encode_labels(y)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42
    )

    xgb = XGBClassifier(
        n_estimators=100,
        max_depth=6,
        learning_rate=0.3,
        eval_metric="mlogloss",
    )

    pipeline = Pipeline(steps=[
        ("preprocessor", build_preprocessor()),
        ("model", xgb),
    ])

    pipeline.fit(X_train, y_train)
    evaluate(pipeline, X_test, y_test, le)

    os.makedirs(os.path.dirname(PIPELINE_PATH), exist_ok=True)
    os.makedirs(os.path.dirname(PACKAGE_PATH), exist_ok=True)

    joblib.dump(pipeline, PIPELINE_PATH)
    joblib.dump({"preprocessor": pipeline.named_steps["preprocessor"], "model": xgb, "label_encoder": le}, PACKAGE_PATH)

    print("Models saved.")


if __name__ == "__main__":
    train()