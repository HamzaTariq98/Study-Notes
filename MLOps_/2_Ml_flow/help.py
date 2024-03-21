import mlflow
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import mean_absolute_error,r2_score
import numpy as np
import matplotlib.pyplot as plt
import datetime
import time
import argparse
import os
from tensorflow.keras.models import Model


model2 = Model()

def main(parsed_args):

    X = np.concatenate([np.expand_dims(np.linspace(0,10,50),axis=1),np.expand_dims(np.linspace(20,20,50),axis=1)],axis=1)

    y = (X+0.5*np.random.rand(50,2)).sum(axis=1)


    X_train = X[:30]
    X_test = X[30:]
    y_train = y[:30]
    y_test = y[30:]


    now = datetime.datetime.now()

    _y = str(now.year)
    _d = str(now.day)
    _h = str(now.hour)
    _m = str(now.minute)
    _s = str(now.second)


    models_dict = {
        'decision_tree': DecisionTreeRegressor,
        'hist': HistGradientBoostingRegressor,
        'linear': LinearRegression
    }

    sklearn_model = models_dict[parsed_args.param1]
    mlflow.set_tracking_uri('http://127.0.0.1:5000/')
    # mlflow.create_experiment('test_experiement')
    mlflow.set_experiment('linear_model')

    with mlflow.start_run(run_name=_y+'-'+_d+'-'+_h+'-'+_m+'m-'+_s+'s'+sklearn_model.__name__) as run:
        

        model = sklearn_model()
        tic = time.time()
        model.fit(X_train,y_train)
        training_time = (time.time() - tic)*100
        y_pred = model.predict(X_test)

        mae = mean_absolute_error(y_test,y_pred)
        r2 = r2_score(y_test,y_pred)

        plt.plot(X.T[0],y,label='True')
        plt.plot(X_test.T[0],y_pred,label='Pred')
        plt.legend()
        plt.show()    
        
        mlflow.log_params({
            'model':sklearn_model.__name__,
            'num': parsed_args.param2            
            })

        mlflow.log_metrics({
            'train_time':training_time,
            'mae':mae,
            'r2':r2
        })

        mlflow.set_tag('Tech','ML-Ensemble')
        mlflow.sklearn.log_model(model,"Trained_model:D")
        # os.makedirs('dummy',exist_ok=False)

        # with open('dummy/txt.txt','wt') as f:
        #     f.write(f'Artifact created at {time.asctime()}')
        # mlflow.log_artifacts("dummy")
 

if __name__=='__main__':
    arg = argparse.ArgumentParser()
    arg.add_argument("--param1","-p1",type=str,default='decision_tree')
    arg.add_argument("--param2","-p2",type=int,default=5)
    parsed_args = arg.parse_args()
    main(parsed_args)
