import os
import joblib
import json
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from medic_pipeline.logger import logger

log = logger('model_evaluator')
metrics_dir = '/app/project/medic_pipeline/results'
metrics_file = 'metrics.json'

def evaluate_model(**kwargs):
    log.info('Запуск шага 4 конвейера: оценка модели')

    ti = kwargs['ti']
    
    try:
        model_path = ti.xcom_pull(task_ids='train_model', key='model_path')
        X_train, X_test, y_train, y_test = ti.xcom_pull(task_ids='train_model', key='data_split')
        
        model = joblib.load(model_path)
        
        y_pred = model.predict(X_test)
        
        metrics = {
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred),
            'recall': recall_score(y_test, y_pred),
            'f1_score': f1_score(y_test, y_pred)
        }
    
        os.makedirs(metrics_dir, exist_ok=True)
    
        metrics_path = os.path.join(metrics_dir, metrics_file)
    
        with open(metrics_path, 'w') as f:
            json.dump(metrics, f)

    except Exception as e:
        log.error(f'При выполнении шага 4 конвейера: оценка модели произошла ошибка - {e}')

    log.info('Завершение шага 4 конвейера: оценка модели')
