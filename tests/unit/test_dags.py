import pytest
from airflow.models import DagBag
from airflow.utils.dates import days_ago
from airflow.utils.session import create_session

def test_dags_load_with_no_errors():
    dag_bag = DagBag(dag_folder='dags', include_examples=False)
    assert len(dag_bag.import_errors) == 0, f"DAG import errors: {dag_bag.import_errors}"
    
def test_fraud_detection_dag():
    dag_bag = DagBag(dag_folder='dags', include_examples=False)
    dag = dag_bag.get_dag(dag_id='fraud_detection_pipeline')
    assert dag is not None
    
    # Test DAG structure
    task_ids = [task.task_id for task in dag.tasks]
    assert 'ingest_transactions' in task_ids
    assert 'process_transactions' in task_ids
    assert 'train_model' in task_ids 