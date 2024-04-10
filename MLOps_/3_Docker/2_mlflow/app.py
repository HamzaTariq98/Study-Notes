print('HELOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import mlflow
import pandas as pd
import mlflow.sklearn
print(f"pandas vesrion is : {pd.__version__}")

model = LinearRegression()

data = pd.read_csv('train.csv')
X = data[['x']]
y = data['y']

model.fit(X,y)

y_pred = model.predict([[-5],[10],[3],[5],[-9]])
y_true = [0,15,8,10,-4]
score = mean_absolute_error(y_true,y_pred)
print(f"Pandas ver is: {pd.__version__}")
print(f"model score is {score}")

# mlflow.set_tracking_uri('http://127.0.0.1:5000')
# mlflow.set_experiment('linear_model2')

with mlflow.start_run() as run:
    mlflow.log_metric('mae',score)
    mlflow.sklearn.log_model(model,'linear')
    mlflow.log_artifact('train.csv')
