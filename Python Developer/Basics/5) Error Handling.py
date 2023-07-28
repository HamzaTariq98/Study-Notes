"""
while (True):
    try:
        age = int(input('enter age: '))
        print((1/age)*age*age)
        break
    except ValueError:
        pass
    except ZeroDivisionError:
        print("age cann't be zero")

"""

def my_sum(num1,num2):
    try:
        return num1 + num2
    except TypeError:
        print('Type error ')

print(my_sum(1,[5,5]))
