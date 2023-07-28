from collections import Counter, defaultdict, OrderedDict
import datetime
from array import array
import pdb


def sum(a,b):
    pdb.set_trace()
    return a+b

# Eff way of getting unique count
x = [1,1,2,4,5,4,96,8,4,5,1,2]
unique = dict(Counter(x))

# Avoid getting an error while calling a key not in a dict
y = defaultdict(lambda: 'not exit',unique)


# Ordinary dict ignores the order of keys, to consider the order of keys we use OrderedDict
a = OrderedDict({
    1: 1,
    2: 2
})



print(datetime.date.today())


print(sum(1,'1'))


