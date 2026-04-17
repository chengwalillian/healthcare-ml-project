from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from ml.train import train

with DAG(
    dag_id="weekly_model_retrain",
    start_date=datetime(2026, 4, 16),
    schedule="0 12 * * 6",
    catchup=False,
    tags=["healthcare", "ml"],
    default_args={
        "owner": "aineah",
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
) as dag:

    retrain = PythonOperator(
        task_id="retrain_model",
        python_callable=train,
    )