from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def dummy_task():
    print("Task executed successfully!")

with DAG(
    'fraud_detection_pipeline',
    default_args=default_args,
    description='Fraud Detection Pipeline',
    schedule_interval=timedelta(days=1),
    catchup=False
) as dag:

    task = PythonOperator(
        task_id='dummy_task',
        python_callable=dummy_task,
    ) 