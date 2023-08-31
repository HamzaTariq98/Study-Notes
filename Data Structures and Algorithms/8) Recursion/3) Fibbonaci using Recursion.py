# 0 1 2 3 4 5 6
# 0 1 1 2 3 5 8 


def fibonaci_iterative(value): # O(n)
    if value < 2:
        return value

    x1 = 0
    x2 = 1
    for i in range(value-1):
        temp = x2+x1
        x1 = x2
        x2 = temp
    return x2

def fibonaci_recursive(value): # O(2^n)
    if value < 2:
        return value

    return fibonaci_recursive(value-1) + fibonaci_recursive(value-2)

value = 30
print(fibonaci_iterative(value)) # 832040
print(fibonaci_recursive(value)) # 832040