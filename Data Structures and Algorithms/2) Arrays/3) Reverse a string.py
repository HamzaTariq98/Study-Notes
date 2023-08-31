

def reverse_me(string): # Time complexity of O(n)
    temp = []
    for char in range(len(string)-1,-1,-1):
        temp.append(string[char])
    return ''.join(temp)


string = 'hi my name is hamza'
print(reverse_me(string)) # azmah si eman ym ih

# or simply we can use string[::-1]