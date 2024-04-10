import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder as Sklearn_OneHotEncoder
from sklearn.preprocessing import MinMaxScaler as SklearnMinMaxScaler
from sklearn.base import BaseEstimator,TransformerMixin
from prediction_model.config import config
from prediction_model.processing import data_handling



class DropColumns(BaseEstimator,TransformerMixin):
    def __init__(self,dropped_columns=None):
        self.dropped_columns = dropped_columns
    
    def fit(self,X,y=None):
        return self

    def transform(self,X):
        for col in self.dropped_columns:
            if col in X.columns:
                X.drop([col],axis=1,inplace=True)
        return X


class BoolToNum(BaseEstimator,TransformerMixin):
    def __init__(self,bool_columns=None):
        self.bool_columns = bool_columns
    
    def fit(self,X,y=None):
        return self

    def transform(self,X):
        for col in self.bool_columns:
            X[col] = X[col].apply(lambda x: 1 if x==True else 0)
        return X


class NumToObj(BaseEstimator,TransformerMixin):
    def __init__(self,num_to_obj_columns=None):
        self.num_to_obj_columns = num_to_obj_columns
    
    def fit(self,X,y=None):
        return self

    def transform(self,X):
        X[self.num_to_obj_columns] = X[self.num_to_obj_columns].astype('object')
        return X




class MeanImputer(BaseEstimator,TransformerMixin):
    def __init__(self,numeric_cols = None):
        self.numeric_cols = numeric_cols

    def fit(self,X,y=None):
        self.mean_values = {}
        X = X.copy()
        for col in self.numeric_cols:
            self.mean_values[col] = X[col].mean()
        return self

    def transform(self,X):
        for col in self.numeric_cols:
            X[col].fillna(self.mean_values[col],inplace=True)
        return X



class ModeImputer(BaseEstimator,TransformerMixin):
    def __init__(self,categorical_cols = None):
        self.categorical_cols = categorical_cols

    def fit(self,X,y=None):
        self.mode_values = {}
        X = X.copy()
        for col in self.categorical_cols:
            self.mode_values[col] = X[col].mode()[0]
        return self

    def transform(self,X):
        for col in self.categorical_cols:
            X[col].fillna(self.mode_values[col],inplace=True)
        return X




class OneHotEncoder(BaseEstimator,TransformerMixin):
    def __init__(self,categorical_cols = None):
        self.categorical_cols = categorical_cols
        self.sklearn_encoder = Sklearn_OneHotEncoder(sparse_output=False,handle_unknown='ignore')

    def fit(self,X,y=None):
        self.sklearn_encoder.fit(X[self.categorical_cols])
        return self

    def transform(self,X):
        columns_names = self.sklearn_encoder.get_feature_names_out()
        X_labels = pd.DataFrame(self.sklearn_encoder.transform(X[self.categorical_cols]),columns=columns_names)
        X = X.drop(self.categorical_cols,axis=1)
        X = pd.concat([X,X_labels],axis=1)
        return X





class MinMaxScaler(BaseEstimator,TransformerMixin):
    def __init__(self,numeric_cols=None):
        self.numeric_cols = numeric_cols
        self.sklearn_model = SklearnMinMaxScaler()

    def fit(self,X,y=None):
        
        self.sklearn_model.fit(X[self.numeric_cols])
        return self

    def transform(self,X):
        
        X[self.numeric_cols] = self.sklearn_model.transform(X[self.numeric_cols])
        return X

