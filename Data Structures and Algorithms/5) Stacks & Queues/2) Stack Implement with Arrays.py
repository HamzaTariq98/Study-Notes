class Stack():
    data = []
    lenght = 0
    def add(self, value):
        self.data.append(value)
        self.lenght +=1

    def pop(self):
        if self.lenght:
            self.lenght += -1
            return self.data.pop()
            
        else:
            raise IndexError('yr stack is empty..')

    def peak(self):
        if self.data:
            return self.data[self.lenght-1]
        else:
            return None
    def __repr__(self):
        return f'{self.data}'


stack = Stack()
stack.add(1)
stack.add(2)
stack.add(3)
stack.add(4)
stack.add(5)

print(stack) # [1, 2, 3, 4, 5]
print(stack.pop()) # 5
print(stack) # [1, 2, 3, 4]
print(stack.pop()) # 4
print(stack.pop()) # 3
print(stack.pop()) # 2
print(stack.pop()) # 1
print(stack.peak()) # None