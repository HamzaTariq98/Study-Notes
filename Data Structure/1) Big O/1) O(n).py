import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def find_nemo(lst):
    '''
    Linear Search in single list, and return algorithm efficiency as execution time
    '''
    start_time = time.time()
    for char in lst:
        if char == 'nemo':
            return time.time() - start_time
    else:
        return time.time() - start_time


def find_nemo_loop(sample_size_list,result):
    '''
    Perform Linear search in multiple sample lists
    '''
    for size in sample_size_list:
        my_list = np.random.randint(0,10,size=(size))
        fnc_time = find_nemo(my_list)
        result.append({
            'size':size,
        'fnc_time':fnc_time
        })

# Run the model by inputting search list, and result empty list container
result = []
sample_size_list = range(1,300000,20000)
find_nemo_loop(sample_size_list,result)

#interpret results as df and as scatter plot
result = pd.DataFrame(result)
print(result)
plt.scatter(result['size'],result['fnc_time'])
plt.show()