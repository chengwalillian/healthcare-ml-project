import os

import joblib
import pandas as pd
from dotenv import load_dotenv
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder

load_dotenv()


PIPELINE_PATH = os.getenv("MODEL_PIPELINE_PATH")
PACKAGE_PATH = os.getenv("MODEL_PACKAGE_PATH")


def load_artifacts() -> tuple[Pipeline, LabelEncoder]:
    pipeline = joblib.load(PIPELINE_PATH)
    package = joblib.load(PACKAGE_PATH)
    return pipeline, package["label_encoder"]


def predict(input_data: dict, pipeline: Pipeline, le: LabelEncoder) -> str:
    df = pd.DataFrame([input_data])
    encoded = pipeline.predict(df)
    return le.inverse_transform(encoded)[0]
