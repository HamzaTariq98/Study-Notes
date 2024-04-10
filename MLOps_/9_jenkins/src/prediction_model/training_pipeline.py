from prediction_model import pipeline
from prediction_model.processing.data_handling import save_pipeline,load_dataset,load_xy,data_split
import numpy as np
import pandas as pd
from prediction_model.config import config
import prediction_model.processing.data_preprocessing as pp


def train_pipeline():
    
    _data = load_dataset(config.DATA_FILE)
    X,y = load_xy(_data)
    X_train, X_test, y_train, y_test = data_split(X,y)

    model_pipeline = pipeline.generate_pipeline()
    model_pipeline.fit(X_train,y_train)
    save_pipeline(model_pipeline)


if __name__=='__main__':
    train_pipeline()