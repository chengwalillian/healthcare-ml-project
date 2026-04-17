import kagglehub
import os
from dotenv import load_dotenv

load_dotenv()

DATASET_PATH = 'data/raw'

if os.getenv("KAGGLE_KEY"):
    print("Kaggle authenticated via environment")
else:
    kagglehub.login()

def fetch_from_kaggle():
    print("Fetching dataset from Kaggle...")
    dataset = "prasad22/healthcare-dataset"
    kagglehub.dataset_download(dataset, output_dir=DATASET_PATH)
    print(f"Dataset {dataset} downloaded successfully")
    return True