# Google Question
# Given an array = [2,5,1,2,3,5,1,2,4]:
# It should return 2

# Given an array = [2,1,1,2,3,5,1,2,4]:
# It should return 1

# Given an array = [2,3,4,5]:
# It should return undefined


arr1 = [2,5,1,2,3,5,1,2,4]
arr2 = [2,1,1,2,3,5,1,2,4]
arr3 = [2,3,4,5]


def first_recurring(arr):  # O(n)
    counter = {}
    for value in arr:
        if value in counter:
            return value
        counter[value] = [1]
    return 'undefined'


print(f'{arr1}: {first_recurring(arr1)}')
print(f'{arr2}: {first_recurring(arr2)}')
print(f'{arr3}: {first_recurring(arr3)}')