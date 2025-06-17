import os
import numpy as np
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from medic_pipeline.logger import logger

log = logger('model_trainer')
model_dir = '/app/project/medic_pipeline/results'
model_file = 'logistic_regression_model.pkl'

def train_model(**kwargs):
    log.info('Запуск шага 3 конвейера: обучение модели')
    ti = kwargs['ti']
    
    try:
        X = ti.xcom_pull(task_ids='preprocess_data', key='X')
        y = ti.xcom_pull(task_ids='preprocess_data', key='y')
        
        X = np.array(X)
        y = np.array(y)
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        
        model = LogisticRegression(random_state=42, max_iter=1000)
        model.fit(X_train, y_train)
        
        os.makedirs(model_dir, exist_ok=True)
        
        model_path = os.path.join(model_dir, model_file)
        
        joblib.dump(model, model_path)
        
        ti.xcom_push(key='model_path', value=model_path)
        ti.xcom_push(key='data_split', value=(X_train.tolist(), X_test.tolist(), y_train.tolist(), y_test.tolist()))
        
    except Exception as e:
        log.error(f'При выполнении шага 3 конвейера: обучение модели произошла ошибка - {e}')
        
    log.info('Завершение шага 3 конвейера: обучение модели')
