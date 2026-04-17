from ml.predict import load_artifacts
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder

pipeline: Pipeline = None
label_encoder: LabelEncoder = None


def init_models() -> None:
    global pipeline, label_encoder
    pipeline, label_encoder = load_artifacts()


def get_pipeline() -> Pipeline:
    return pipeline


def get_label_encoder() -> LabelEncoder:
    return label_encoder
