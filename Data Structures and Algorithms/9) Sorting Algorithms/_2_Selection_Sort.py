# Swap minimum value into the start of the array n-1 times


def sort_selection(arr): # O(n^2)
    lengh = len(arr)

    for x1 in range(lengh-1):
        temp = x1+1
        for x2 in range(x1+1,lengh):
            if arr[temp] < arr[x2]:
                x2 = temp
                
        if arr[x2] < arr[x1]:
            temp_ = arr[x1]
            arr[x1] = arr[x2]
            arr[x2] = temp_

    return arr

if __name__ == '__main__':
    arr = [9,5,1,0,-2]
    print(arr) # [9, 5, 1, 0, -2]
    print(sort_selection(arr)) # [-2, 1, 0, 5, 9]
