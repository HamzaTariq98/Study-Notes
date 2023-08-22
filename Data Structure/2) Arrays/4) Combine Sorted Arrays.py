

# O(1)
def mix_sorted(arr1,arr2):
    n1 = 0
    n2 = 0
    arr3 = []
    while(True):
        
        if arr1[n1] <= arr2[n2]:
            arr3.append(arr1[n1])
            n1 += 1
        else:
            arr3.append(arr2[n2])
            n2 += 1            

        if n1 == len(arr1):
            arr3.extend(arr2[n2:])
            return arr3

        if n2 == len(arr2):
            arr3.extend(arr1[n1:])
            return arr3 
        


arr1 = [1,3,5,7]
arr2 = [2,4,6,8,10,12]

print(mix_sorted(arr1,arr2)) # [1, 2, 3, 4, 5, 6, 7, 8, 10, 12]