from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from ETL.main import run_etl
from ETL.load import upload_to_s3
from ETL.extract import extract_data
from ETL.transform import read_csv

# create a DAG instance

with DAG(
    dag_id="air_dag", start_date=datetime(2025, 7, 8), schedule="@daily", catchup=False
) as dag:

    # Define the task to upload data to S3
    upload_task = PythonOperator(
        task_id="upload_to_s3_DAG",
        python_callable=run_etl,
    )
