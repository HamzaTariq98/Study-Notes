from sklearn.pipeline import Pipeline
import prediction_model.processing.data_preprocessing as pp
from prediction_model.config import config
from sklearn.ensemble import HistGradientBoostingClassifier
import numpy as np




def generate_pipeline():

    steps = [
        ('drop_cols',pp.DropColumns(config.DROPED_COLUMNS)),
        ('bool_num',pp.BoolToNum(config.BOOL_COLUMNS)),
        ('num_obj',pp.NumToObj(config.NUM_TO_OBJ_COLUMNS)),
        ('onehot_encoding',pp.OneHotEncoder(config.CATEGORICAL_COLUMNS))        
    ]

    if config.APPLY_NUM_IMPUTER:
        steps.insert(3, ('mean_imputer', pp.MeanImputer(config.IMPUTED_NUM_COLUMNS)))
    
    if config.APPLY_CAT_IMPUTER:
        steps.insert(4, ('mode_imputer', pp.ModeImputer(config.CATEGORICAL_COLUMNS)))
    
    if config.APPLY_SCALER:
        steps.append(('min_max_scaler', pp.MinMaxScaler(config.SCALED_NUM_COLUMNS)))
    
    steps.append(('prediction_model',HistGradientBoostingClassifier()))
    pipeline = Pipeline(steps)

    return pipeline