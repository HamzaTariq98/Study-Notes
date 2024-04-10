import pytest
import hashlib
import numpy as np
import pandas as pd
from prediction_model import predict
from prediction_model.config import config
from prediction_model.processing.data_handling import load_dataset



#### Fextures ####

@pytest.fixture
def check_test_data():
    test_data = load_dataset(config.TEST_DATA)
    load_dataset(config.TEST_DATA)
    test_hash = hashlib.sha256(test_data.to_json().encode()).hexdigest()
    check = test_hash == '446358eb0be910b8bafecf83d0363f9fb885fc17a5df11e82b25133c2f3b1196'
    return check


@pytest.fixture
def perform_test_prediction():
    test_data = load_dataset(config.TEST_DATA)
    for col in config.NUMERIC_COLUMNS:
        test_data[col] = test_data[col].astype(np.float32)
    return predict.perform_predictions(test_data)[0]



### predict.py  ###

def test_check_test_data_hash(check_test_data):
    assert check_test_data == True



### predict.py  ###

def test_check_predict_not_null(perform_test_prediction):
    assert perform_test_prediction is not None



def test_check_predict_dtype(perform_test_prediction):
    assert isinstance(perform_test_prediction,np.int64)



def test_check_predict_output_range(perform_test_prediction):
    assert perform_test_prediction in [0,1]



def test_check_predict_example(perform_test_prediction):
    assert perform_test_prediction == 1



if __name__ == '__main__':
    pass