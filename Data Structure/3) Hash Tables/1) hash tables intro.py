# Hash tables works by assigning cartain memory based on key value 
# The memory value calculated via hash function encoding md5 hash generator 
# Note that cann't go bacl from the encoded memory to the key value (idempotent)

import hashlib

encoded = hashlib.md5(b'GeeksforGeeks')
print(encoded.hexdigest())  # O(1) Output f1e069787ece74531d112559945c6871 which will provide a fast data access


def hello():
    print('helloooo')
    return 'he said hello'


hash_map = {
    5: 54,
    'name': 'hamza',
    hello: hello()
}

hash_map[hello]
print(hash_map)
