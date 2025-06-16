import os
import numpy as np
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

model_dir = 'data'
model_file = 'logistic_regression_model.pkl'

def train_model(**kwargs):
    ti = kwargs['ti']
    X = ti.xcom_pull(task_ids='preprocess_data', key='X')
    y = ti.xcom_pull(task_ids='preprocess_data', key='y')
    
    X = np.array(X)
    y = np.array(y)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    model = LogisticRegression(random_state=42, max_iter=1000)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    model_path = os.path.join(model_dir, model_file)
    
    joblib.dump(model, model_path)
    
    ti.xcom_push(key='model_path', value=model_path)
    ti.xcom_push(key='data_split', value=(X_train.tolist(), X_test.tolist(), y_train.tolist(), y_test.tolist()))
    ti.xcom_push(key='predictions', value=y_pred.tolist())
