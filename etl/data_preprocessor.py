import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(**kwargs):
    ti = kwargs['ti']
    df_json = ti.xcom_pull(task_ids='load_data')
    df = pd.read_json(df_json)
    
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]
    df.dropna(axis=0, inplace=True)

    X = df.drop('target', axis=1)
    y = df['target']
    
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    
    print(X)
    print("\n")
    print(y)
    
    ti.xcom_push(key='X', value=X.tolist())
    ti.xcom_push(key='y', value=y.tolist())
