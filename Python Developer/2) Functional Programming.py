from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


print(list(map(str.capitalize,my_pets)))



#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
my_numbers.sort()
zipper = list(zip(my_strings,my_numbers))
print(zipper)

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
print(list(filter(lambda x:x>19,scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
print(reduce(lambda acc,x:x+acc,my_numbers+scores))


#5 Find the square values of elements of a list using lambda
x = [5,4,3]
print(list(map(lambda num: num**2,x)))

#6 List of tuples sorting using lambda
my_list = [(100,2), (4,3), (9,9), (10,-1)]
my_list.sort(key= lambda x:x[1])
print(my_list)