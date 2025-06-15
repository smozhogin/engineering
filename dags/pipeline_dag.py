from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta
from medic_pipeline.etl.data_loader import load_data
from medic_pipeline.etl.data_preprocessor import preprocess_data

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'medic_pipeline',
    default_args=default_args,
    catchup=False
) as dag:    
    
    load_data = PythonOperator(
        task_id='load_data',
        python_callable=load_data
    )
    
    preprocess_data = PythonOperator(
        task_id='preprocess_data',
        python_callable=preprocess_data
    )
    
    load_data >> preprocess_data
