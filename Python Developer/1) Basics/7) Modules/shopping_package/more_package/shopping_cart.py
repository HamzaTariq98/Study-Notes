
def buy_item(item,cart):
    cart.append(item)
    return cart


def remove_item(item,cart):
    if item in cart:
        cart.remove(item)
        return cart
    else:
        print(f'{item}, not in the cart: {cart}')


