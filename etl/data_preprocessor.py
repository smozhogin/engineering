import pandas as pd
from sklearn.preprocessing import StandardScaler
from medic_pipeline.logger import logger

log = logger('data_preprocessor')

def preprocess_data(**kwargs):
    log.info('Запуск шага 2 конвейера: предобработка данных')
    ti = kwargs['ti']
    
    try:
        df_json = ti.xcom_pull(task_ids='load_data', key='data')
        df = pd.read_json(df_json)
        
        df.dropna(axis=0, inplace=True)
        
        X = df.drop('target', axis=1)
        y = df['target']
        
        scaler = StandardScaler()
        X = scaler.fit_transform(X)
        
        ti.xcom_push(key='X', value=X.tolist())
        ti.xcom_push(key='y', value=y.tolist())

    except Exception as e:
        log.error(f'При выполнении шага 2 конвейера: предобработка данных произошла ошибка - {e}')
        
    log.info('Завершение шага 2 конвейера: предобработка данных')
