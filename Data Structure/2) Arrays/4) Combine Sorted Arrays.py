

# O(1)
def mix_sorted(arr1,arr2):
    n1 = 0
    n2 = 0
    arr3 = []
    while(True):
        
        # Append the least number of index (n1 in array1, n2 in array2)
        if arr1[n1] <= arr2[n2]:
            arr3.append(arr1[n1])
            n1 += 1 # Increment array indexing when append its value
        else:
            arr3.append(arr2[n2])
            n2 += 1 # Increment array indexing when append its value   

        # When reach the end of any of the two arrays just extend the remain part of the other array
        if n1 == len(arr1):
            arr3.extend(arr2[n2:])
            return arr3

        if n2 == len(arr2):
            arr3.extend(arr1[n1:])
            return arr3 
        


arr1 = [1,3,5,7]
arr2 = [2,4,6,8,10,12]

print(mix_sorted(arr1,arr2)) # Output ==> [1, 2, 3, 4, 5, 6, 7, 8, 10, 12]