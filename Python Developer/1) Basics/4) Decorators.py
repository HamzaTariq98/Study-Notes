from time import time

"""
Higher Order Function:
any function that accept other functions as parameters or returns a function
ex. (map, reduce, filter), are HOF as they accepts other function as parameter
"""

# Creating my own map function using the concept of HOF
def my_map(func,iterable):
    return [func(element) for element in iterable]
x = [1,2,3,4,5,6]
print('my_map output: ',my_map(lambda x:x*2,x))


# Creating a decorator to measure function execution time

def performance(func):
    def wrapper(*arg,**kwarg):
        t1 = time()
        result = func(*arg,**kwarg)
        t2 = time()
        print(t2-t1)
        return result
    return wrapper

x = range(2000000)

@performance
def sum_list(lst):
    counter = 0
    for i in lst:
        counter+= i
    return counter

print(sum_list(x))
