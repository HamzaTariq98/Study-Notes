

def sort_merge(arr):
    lenght = len(arr)
    if lenght == 1:
        return arr

    left = arr[:lenght//2]
    right = arr[lenght//2:]
    return merge(sort_merge(left), sort_merge(right))


def merge(left, right):
    sorted_arr = []
    ind1 = 0
    ind2 = 0
    
    while (True):
        if left[ind1] > right[ind2]:
            sorted_arr.append(right[ind2])
            ind2 += 1
        else:
            sorted_arr.append(left[ind1])
            ind1 += 1 

        if ind1 == len(left):
            sorted_arr.extend(right[ind2:])
            return sorted_arr
        if ind2 == len(right):
            sorted_arr.extend(left[ind1:])
            return sorted_arr
        



if __name__ == '__main__':
    arr = [1,5,9,1,0,5,5,0,-5,0,0,0,5,4,8]

    print(arr) # [1, 5, 9, 1, 0, 5, 5, 0, -5, 0, 0, 0, 5, 4, 8]
    print(sort_merge(arr)) # [-5, 0, 0, 0, 0, 0, 1, 1, 4, 5, 5, 5, 5, 8, 9]