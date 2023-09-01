# If yr list is almost sorted ==> O(n)
# Creating a sub sorted list and keep inserting values in it based on its correct position

def sort_insertion(arr): # O(n^2)
    sorted_arr = []
    for value in arr:
        flag = 1
        for index, sorted_value in enumerate(sorted_arr):
            if value < sorted_value:
                sorted_arr.insert(index, value)
                flag = 0
                break
        if flag:
            sorted_arr.append(value)
    return sorted_arr

if __name__ == '__main__':  
    arr = [5,7,1,0,-2,5,10,0]

    print(arr) # [5, 7, 1, 0, -2, 5, 10, 0]
    print(sort_insertion(arr)) # [-2, 0, 0, 1, 5, 5, 7, 10]