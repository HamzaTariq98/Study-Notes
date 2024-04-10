import os
import pandas as pd
import joblib
from prediction_model.config import config
from sklearn.model_selection import train_test_split

# DataSet loading
def load_dataset(file_name):
    _data = pd.read_csv(config.DATAPATH/file_name)
    return _data


# Load X,y
def load_xy(data):
    """
    Returns tuple (X,y)
    """
    X = data.copy()
    y = X[config.TARGET]
    return X,y


# Data Split
def data_split(X,y):
    """
    Retunrs X_train, X_test, y_train, y_test
    """
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=10)

    X_train = X_train.reset_index(drop=True)
    X_test = X_test.reset_index(drop=True)
    y_train = y_train.reset_index(drop=True)
    y_test = y_test.reset_index(drop=True) 

    return X_train, X_test, y_train, y_test

# Serialization
def save_pipeline(pipeline_to_save):
    saved_path = config.SAVED_MODEL_PATH/config.SAVED_MODEL_NAME
    joblib.dump(pipeline_to_save,saved_path)
    print(f'Model saved in {saved_path}')


# Deserialization
def load_pipeline():
    pipeline_path = config.SAVED_MODEL_PATH/config.LOADED_MODEL_NAME
    loaded_model = joblib.load(pipeline_path)
    print(f'Model loaded => {pipeline_path}')
    return loaded_model