

def linear_search(arr, value):
    for index,arr_value in enumerate(arr):
        if value == arr_value:
            return index
    return -1

arr = [4,0,5,7,0,5,7]

print(linear_search(arr,5)) # 2
print(linear_search(arr,7)) # 3
print(linear_search(arr,99)) # -1 "not found"