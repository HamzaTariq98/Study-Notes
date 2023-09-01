

def binary_search(arr, value):
    left = 0
    right = len(arr)-1
    while(left <= right):
        middle = (right+left)//2
        if value == arr[middle]:
            return middle
        elif value > arr[middle]:
            left = middle + 1
        else:
            right = middle -1
    return -1
    

arr = [0,5,8,9,10,12,15]

print(binary_search(arr,5)) # 1
print(binary_search(arr,15)) # 6
print(binary_search(arr,20)) # -1 "not found"