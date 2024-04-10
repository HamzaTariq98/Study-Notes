from prediction_model.processing.data_handling import load_pipeline,data_split, load_xy,load_dataset
from prediction_model.config import config
from sklearn.metrics import accuracy_score
import pandas as pd

pd.options.mode.copy_on_write = True

def perform_predictions(data_input = None):
    """
    data_input is DataFrame, should contain all of the needed prediction features
    """
    data_input = pd.DataFrame(data_input)
    loaded_pipeline = load_pipeline()
    flag=0
    if data_input is None:
        data_ = load_dataset(config.DATA_FILE)
        X,y = load_xy(data_)
        _, data_input, _, y_test = data_split(X,y)
        flag=1

    predictions = loaded_pipeline.predict(data_input[config.FEATURES])
    if flag:
        print(f'returned pred is {predictions}')
        print(f'Acc is {accuracy_score(y_test,predictions)}')
    else:
        print(f'returned pred is {predictions}')

    return predictions


if __name__ == '__main__':
    data = None
    # data = pd.read_csv(config.DATAPATH/config.PREDICTION_DATA)
    perform_predictions(data)

