import pdb
class MyArr():

    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(list(self.data.values()))

    # Return an element by index O(1)
    def get(self, index):
        value = self.data[index]
        return value

    # Add element at the end of array O(1)
    def append(self,value):
        self.data[self.length] = value
        self.length += 1

    # Del last element O(1)
    def pop(self):
        del self.data[self.length - 1]
        self.length += -1

    # Insert element in cetrain index O(n)
    def insert(self, value, index):
        assert 0 <= index <= self.length, f'index {index} out of range 0-{self.length}' # Raise err if insertion index is out of range
        if index == self.length:
            self.append(value)
        else:
            for ind in range(self.length,index,-1):
                self.data[ind] = self.data[ind-1]

        self.data[index] = value
        self.length += 1

arr = MyArr()

arr.append('asdasdb')
arr.append('c')
arr.insert('a',0)
print(arr.get(2))
print(arr) # ['a', 'asdasdb', 'c']