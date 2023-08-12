import random
from shopping_package.more_package.shopping_cart import buy_item,remove_item
from utility_module import devision,multiplication

if __name__ =='__main__':
    multiplication(4,5)
    devision(4,5)
    cart = list()

    print('adding',buy_item('item1', cart))
    print('adding', buy_item('item2', cart))
    print(remove_item('item2', cart))

x = [1,2,3,4]
random.shuffle(x)
print(x)


import pyjokes
print(pyjokes.__version__)