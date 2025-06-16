import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def train_model(**kwargs):
        ti = kwargs['ti']
        X = ti.xcom_pull(task_ids='preprocess_data', key='X')
        y = ti.xcom_pull(task_ids='preprocess_data', key='y')
        
        X = np.array(X)
        y = np.array(y)
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = LogisticRegression(random_state=42, max_iter=1000)
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        
        return model, (X_train, X_test, y_train, y_test, y_pred)
