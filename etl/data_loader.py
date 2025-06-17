import pandas as pd
from sklearn.datasets import load_breast_cancer
from medic_pipeline.logger import logger

log = logger('data_loader')

def load_data(**kwargs):
    log.info('Запуск шага 1 конвейера: загрузка данных')
    
    ti = kwargs['ti']
    
    try:
        data = load_breast_cancer()
        
        df = pd.DataFrame(data.data, columns=data.feature_names)
        df['target'] = data.target
        
        ti.xcom_push(key='data', value=df.to_json())
        
    except Exception as e:
        log.error(f'При выполнении шага 1 конвейера: загрузка данных произошла ошибка - {e}')
        
    log.info('Завершение шага 1 конвейера: загрузка данных')
