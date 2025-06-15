import os
import pandas as pd
from sklearn.datasets import load_breast_cancer

def load_data():
    data = load_breast_cancer()
    
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    
    df.info()
    
    print("\n")
    print(df.head(10))
    
    return df.to_json()

load_data()
