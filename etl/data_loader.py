import pandas as pd
from sklearn.datasets import load_breast_cancer

def load_data(**kwargs):
    ti = kwargs['ti']
    
    data = load_breast_cancer()
    
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    
    df.info()
    
    print('\n')
    print(df.head(10))
    
    ti.xcom_push(key='data', value=df.to_json())
