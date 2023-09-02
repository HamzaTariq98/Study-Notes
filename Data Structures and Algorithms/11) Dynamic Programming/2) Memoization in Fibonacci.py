# By help of wrapping we actually managed to cache result after each single mini stack execution !!!!

# Dynamic programming = (Devide & Conquer) + (Memoization) !!
# Dynamic Programming applicable when:
    # 1) Devidable into sub problems same steps
    # 2) Input for these steps are repetitive

def memoize(func):

    cache = {}

    def wrapper(value):
        if value in cache:
            return cache[value]

        else:
            result = func(value)
            cache[value] = result
            return result

    return wrapper


@memoize
def fibonacci(value):
    global counter
    counter += 1

    if value < 2:
        return value
    
    return fibonacci(value-1) + fibonacci(value-2)

counter = 0

print(fibonacci(250)) # 7896325826131730509282738943634332893686268675876375
print(counter) # 251