import pathlib
import os
import prediction_model



PACKAGE_ROOT = pathlib.Path(prediction_model.__file__).parent

DATAPATH = PACKAGE_ROOT/'datasets'
DATA_FILE = 'data.csv'
TEST_DATA = 'test_data.csv'

SAVED_MODEL_PATH = PACKAGE_ROOT / 'trained_models'
SAVED_MODEL_NAME = 'model_0.pkl'
LOADED_MODEL_NAME = 'model_0.pkl'

DROPED_COLUMNS = ['survived','alive']
TARGET = 'survived'

BOOL_COLUMNS = ['alone','adult_male']

NUM_TO_OBJ_COLUMNS = ['pclass']


FEATURES = ['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare',
       'embarked', 'class', 'who', 'adult_male', 'deck', 'embark_town','alone']
       
NUMERIC_COLUMNS = ['age', 'sibsp', 'parch', 'fare']
CATEGORICAL_COLUMNS = ['sex', 'embarked', 'class','who', 'deck',
    'embark_town','pclass', 'adult_male', 'alone']




APPLY_CAT_IMPUTER = False
APPLY_NUM_IMPUTER = False
APPLY_SCALER = True


# Numeric columns to impute
IMPUTED_NUM_COLUMNS = NUMERIC_COLUMNS

# Numeric columns to scale
SCALED_NUM_COLUMNS = NUMERIC_COLUMNS


