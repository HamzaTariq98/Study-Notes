# Caching: Store values that can be used later (Grap yr pen in your backpack instead of return home)
# Memoization: Caching the return value of certain function params


def memoize(func):  # Predefined fnc by help of (ChatGPT)
    cache = {}

    def wrapper(value):
        if value in cache: # Run our param into the cache to avoid rerun the same long operation !
            return cache[value]

        else:
            print('long time process') # To avoid running this long time step we do Memoization
            result = func(value)
            cache[value] = result
            return result
    
    return wrapper


@memoize
def add_80(value):
    return value + 80





print(add_80(5))
print(add_80(5))
print(add_80(5))