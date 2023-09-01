

def fact(value):
    print(value)
    if value <= 1:
        return 1
    return value*fact(value-1)

print(fact(4))


