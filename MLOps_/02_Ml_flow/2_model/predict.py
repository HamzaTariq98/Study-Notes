import mlflow
logged_model = 'runs:/515c3a16c7fe46c89df7412f1131620b/my_model'

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Predict on a Pandas DataFrame.
import pandas as pd

data = [[1,1]]

print(loaded_model.predict(pd.DataFrame(data)))
