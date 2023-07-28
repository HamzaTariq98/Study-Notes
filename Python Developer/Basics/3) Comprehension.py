from collections import Counter

# Create a list of even squares of numbers from [0-10)
my_list = [num**2 for num in range(10) if num%2==0]
print(my_list)



my_list = [char.upper() for char in 'hello']
print(my_list)


# Convert a list of tuples (enumerate output) into dictionary using dictionary comprehension
my_dict = {key:value for key,value in enumerate('3487') if int(value)>=4}
print(my_dict)

# Find duplicated values in most efficient way using built in Counter function that returns each unique value with its count
# then we use this dictionary to list out all of the values have count greater than 1
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
counter = Counter(some_list)
duplicates = [value for value,count in counter.items() if count>1]
print(duplicates)
