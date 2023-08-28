class Node():
    next_node = None
    prev_node = None

    def __init__(self,data):
        self.data = data

    def __repr__(self):
        return f'{self.data}'

class Queue():
    head = None
    tail = None


    def prepend(self, value):
        prepend_node = Node(value)
        head_node = self.head

        if head_node:
            prepend_node.next_node = head_node
            head_node.prev_node = prepend_node
            self.head = prepend_node
            
        else:
            self.head = prepend_node
            self.tail = prepend_node

    def pop(self):

        if self.tail != None and self.tail == self.head:
            self.tail = None
            self.head = None

        elif self.tail:
            prev_node = self.tail.prev_node
            self.tail = prev_node
            self.tail.next_node = None

        else:
            raise IndexError('pop from empty Queue')

    def peak(self):
        return self.tail

    def nodes(self):
        nodes = []
        node = self.head
        while(node):
            nodes.append(node)
            node = node.next_node
        return nodes

    def __repr__(self):
        return f'{self.nodes()}'


q1 = Queue()
q1.prepend(1)
q1.prepend(2)
q1.prepend(3)
q1.prepend(4)
q1.pop()
q1.pop()


print(q1) # [4, 3]
print(q1.peak()) # [3]

