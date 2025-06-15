import pandas as pd

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
    
    return X, y
