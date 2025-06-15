def preprocess_data(df):
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]
    
    X = df.drop('target', axis=1)
    y = df['target']
    
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    
    return X, y
