counter = 3
def func():
    
    global counter
    counter += -1
    print(counter)
    if counter <= 0:
        print('done')
        return 'done' # 1) Base case return
    return func() # 2) Recursive return
    print(counter)


print(func())