from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta
from medic_pipeline.etl.data_loader import load_data
from medic_pipeline.etl.data_preprocessor import preprocess_data
from medic_pipeline.etl.model_trainer import train_model
from medic_pipeline.etl.model_evaluator import evaluate_model

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'Medic_Pipeline',
    default_args=default_args,
    catchup=False
) as dag:    
    
    load_data_task = PythonOperator(
        task_id='load_data',
        python_callable=load_data
    )
    
    preprocess_data_task = PythonOperator(
        task_id='preprocess_data',
        python_callable=preprocess_data
    )

    train_model_task = PythonOperator(
        task_id='train_model',
        python_callable=train_model
    )

    evaluate_model_task = PythonOperator(
        task_id='evaluate_model',
        python_callable=evaluate_model
    )
    
    load_data_task >> preprocess_data_task >> train_model_task >> evaluate_model_task
