import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def read_first_element(lst):
    start_time = time.time()
    lst[0]
    return time.time() - start_time



def run_trials(sample_size_list):
    '''
    Run certain function multiple times on different lists sizes
    '''
    for size in sample_size_list:
        start_time = time.time()
        my_list = np.random.randint(0,10,size=(size))
        fnc_time = read_first_element(my_list)
        result.append({'size':size,'fnc_time':fnc_time,'array_time':time.time() - start_time})

# Run the model by inputting search list, and result empty list container
result = []
sample_size_list = range(1,10000000,500000)
run_trials(sample_size_list)

#interpret results as df and as scatter plot
result = pd.DataFrame(result)
print(result)
plt.scatter(result['size'],result['fnc_time'], label = 'Function Time O(1)')
plt.scatter(result['size'],result['array_time'], label = 'Array Creating Time O(n)')

plt.legend()
plt.show()