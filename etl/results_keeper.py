import os
import configparser
import yadisk

config = configparser.ConfigParser()
config.read('/app/project/medic_pipeline/config.ini')

OAUTH_TOKEN = config['KEEPER'].get('OAUTH_TOKEN')
LOCAL_DIR = '/app/project/medic_pipeline/data'
REMOTE_DIR = 'medic_pipeline/data'
MODEL_FILE = 'logistic_regression_model.pkl'
METRICS_FILE = 'metrics.json'

local_model_file_path = os.path.join(LOCAL_DIR, MODEL_FILE)
remote_model_file_path = os.path.join(REMOTE_DIR, MODEL_FILE)
local_metrics_file_path = os.path.join(LOCAL_DIR, METRICS_FILE)
remote_metrics_file_path = os.path.join(REMOTE_DIR, METRICS_FILE)

def keep_results():
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
            print(f'Не удалось загрузить файлы: {e}')
