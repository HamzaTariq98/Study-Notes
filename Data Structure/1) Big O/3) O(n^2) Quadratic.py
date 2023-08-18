import time,pdb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def log_items(lst):
    start_time = time.time()
    logged_list = []
    for i in lst:
        for j in lst:
            logged_list.append((i,j))
    return  time.time() - start_time


def run_trials(sample_size_list):
    result = []
    for size in sample_size_list:
        my_list = np.random.randint(0,10,size=(size))
        fnc_time = log_items(my_list)
        result.append({'size':size,'fnc_time':fnc_time})
    return pd.DataFrame(result)

# Run the model by inputting search list, and result empty list container
sample_size_list = range(1,2000,90)
result = run_trials(sample_size_list)

#interpret results as df and as scatter plot
print(result)
plt.scatter(result['size'],result['fnc_time'], label = 'Function Time O(n^2)')
plt.legend()
plt.show()