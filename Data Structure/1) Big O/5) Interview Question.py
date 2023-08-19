'''
We are given two arrays. We have to find if these two arrays contain any matching elements.
For example, array1 = ['a','b','c','x'] , array2 = ['x','y','z']
This should return True as element 'x' appears in both arrays.
'''

import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Prebuilt by help of ChatGPT
def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (low + high) // 2
        if item == arr[middle]:
            return 'Yes'
        elif item > arr[middle]:
            low = middle + 1
        else:
            high = middle - 1

    return 'No'


def find_common(arr1,arr2):
    start_time = time.time()
    for item in arr1:
        if binary_search(arr2,item) == 'Yes':
            return time.time() - start_time
    return time.time() - start_time


def run_trials(sample_size_list):
    result = []
    for size in sample_size_list:
        arr1 = list(np.random.randint(0,10,size=(size)))
        arr2 = list(np.random.randint(11,20,size=(size)))
        fnc_time = find_common(arr1,arr2)
        result.append({'size':size,'fnc_time':fnc_time})
    return pd.DataFrame(result)


sample_size_list = range(2,100000,10000)
result = run_trials(sample_size_list)

print(result)
plt.scatter(result['size'],result['fnc_time'], label = 'Function Time O(nlog(n))')
plt.legend()
plt.show()
