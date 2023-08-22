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

arr = MyArr()
arr.append('a')
arr.append('b')
arr.append('c')
print(arr)