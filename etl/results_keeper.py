import os
import configparser
import yadisk
from medic_pipeline.logger import logger

log = logger('results_keeper')
config = configparser.ConfigParser()
config.read('/app/project/medic_pipeline/config.ini')

OAUTH_TOKEN = config['KEEPER'].get('OAUTH_TOKEN')
LOCAL_DIR = '/app/project/medic_pipeline/results'
REMOTE_DIR = 'medic_pipeline/data'
MODEL_FILE = 'logistic_regression_model.pkl'
METRICS_FILE = 'metrics.json'

local_model_file_path = os.path.join(LOCAL_DIR, MODEL_FILE)
remote_model_file_path = os.path.join(REMOTE_DIR, MODEL_FILE)
local_metrics_file_path = os.path.join(LOCAL_DIR, METRICS_FILE)
remote_metrics_file_path = os.path.join(REMOTE_DIR, METRICS_FILE)

def keep_results():
    log.info('Запуск шага 5 конвейера: сохранение результатов')
    client = yadisk.Client(token=OAUTH_TOKEN)
    
    with client:
        if client.check_token():
            print('Токен действителен, можно приступать к работе с файлами на Яндекс.Диск')
        else:
            print('Токен недействителен, попробуйте получить его заново')
        
        try:
            client.upload(local_model_file_path, remote_model_file_path, overwrite=True)
            client.upload(local_metrics_file_path, remote_metrics_file_path, overwrite=True)
            
            print(f'Файлы успешно загружены на Яндекс.Диск по пути: {REMOTE_DIR}')
        except Exception as e:
            log.error(f'При выполнении шага 5 конвейера: сохранение результатов произошла ошибка - {e}')
            print(f'Не удалось загрузить файлы: {e}')

    log.info('Завершение шага 5 конвейера: сохранение результатов')
