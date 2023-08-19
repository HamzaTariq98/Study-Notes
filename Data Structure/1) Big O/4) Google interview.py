arr1 = [1,2,3,9]
arr2 = [1,2,4,4]

def find_pairs(arr):
    fours = 0
    for number in arr[::-1]:
        if number == 4:
            arr.remove(number)            
            fours += 1
        if fours >= 2: return 'Yes'

    arr = list(set(arr))
    while (len(arr) >=2):
        for number in arr[1:]:
            if arr[0] + number == 8:
                return 'Yes'
        arr = arr[1:]
    return  'No'

print(f'Have sum of 8? {arr1}: {find_pairs(arr1)}')
print(f'Have sum of 8? {arr2}: {find_pairs(arr2)}')
