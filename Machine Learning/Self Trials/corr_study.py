import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression,Ridge,Lasso

class Func():

    @staticmethod
    def linear(x):
        return x*50+500

    @staticmethod
    def poly(x):
        return x**2

def study(x,fnc):
    y = list(map(fnc,x))
    plt.scatter(x,y)
    result.append({'model':fnc.__name__, 'corr':np.corrcoef(x,y)[0][1]})


x = np.linspace(-100,100,30)
result = []

study(x,Func.linear)
study(x,Func.poly)

print(pd.DataFrame(result))
plt.grid()
plt.show()
