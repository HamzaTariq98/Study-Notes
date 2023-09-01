# swap only 2 values to be sorted through the list, keep iterating (n-1)^2 times

# Simplist / least eff
def sort_bubble(arr): # O(n^2)
    right = len(arr)-1
    left = 0

    for inter in range(right):
        x0 = 0
        x1 = 1
        for inner_iter in range(right):
            if arr[x0] > arr[x1]:
                temp = arr[x1]
                arr[x1] = arr[x0]
                arr[x0] = temp
            x0 += 1
            x1 += 1

        right += -1
    return arr

if __name__ == '__main__':
    arr = [9,5,1,0,-2,5,1,0,5,4,6,8,4,6,8,4,5]
    print(arr) # [9, 5, 1, 0, -2, 5, 1, 0, 5, 4, 6, 8, 4, 6, 8, 4, 5]
    print(sort_bubble(arr)) # [-2, 0, 0, 1, 1, 4, 4, 4, 5, 5, 5, 5, 6, 6, 8, 8, 9]
