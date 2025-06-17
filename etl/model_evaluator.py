import os
import joblib
import json
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

metrics_dir = '/app/project/medic_pipeline/data'
metrics_file = 'metrics.json'

def evaluate_model(**kwargs):
    ti = kwargs['ti']
    
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
    
    metrics_json = json.dumps(metrics)
    
    os.makedirs(metrics_dir, exist_ok=True)
    
    metrics_path = os.path.join(metrics_dir, metrics_file)
    
    joblib.dump(metrics_json, metrics_path)
