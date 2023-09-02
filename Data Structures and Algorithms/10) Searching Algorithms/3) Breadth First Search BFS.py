

class Node():
    next_node = None
    prev_node = None

    def __init__(self,data):
        self.data = data

    def __repr__(self):
        return f'{self.data}'

class Queue(): # Implementing BFS using Queues as first elemnt would be processed !

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


class Tree_Node():
    left = None
    right = None


    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'{self.value}'

class BinaryTree():
    root = None


    def __init__(self, value):
        self.root = Tree_Node(value)


    def insert(self, value):
        inserted_node = Tree_Node(value)
        prev_node = self.root

        while(True):
            if inserted_node.value > prev_node.value:
                if prev_node.right == None:
                    prev_node.right = inserted_node
                    return inserted_node
                else:
                    prev_node = prev_node.right
            else:
                if prev_node.left == None:
                    prev_node.left = inserted_node
                    return inserted_node
                else:
                    prev_node = prev_node.left

    def lookup(self, value):
        current_node = self.root
        rout = ['Root']

        while(current_node):
            if value == current_node.value:
                return rout
            elif value > current_node.value:
                current_node = current_node.right
                rout.append('Right')
            else:
                current_node = current_node.left
                rout.append('Left')
        return f'Value {value} was not found in yr tree'

    def remove(self, value): # Not completed... as when delete a value all of its child are deleted too
        rout = ['Root']
        if self.root.value == value:
            self.root = None
            return rout

        current_node = self.root
        # prev_node = current_node

        while(current_node):

            if value == current_node.value:
                if value > prev_node.value:
                    prev_node.right = None
                    return rout
                else:
                    prev_node.left = None
                    return rout

            elif value > current_node.value:
                prev_node = current_node
                current_node = current_node.right
                rout.append('Right')
            else:
                prev_node = current_node
                current_node = current_node.left
                rout.append('Left')

        return f'Value {value} was not found in yr tree'
    


# BFS O(n) ==> [9,4,20,1,6,15,170]
# Higher memory as need to remember child nodes ==> O(n)
# Good when searching for shorsets path (Google Maps, recomendations engines)


def bredth_depth_search(tree): # Implementing BFS using Queues as first elemnt would be processed !!!!
    memory = [tree.root] # Implementing BFS using Queues as first elemnt would be processed !!!!
    print(memory[0], end= ' ')
    while(len(memory) is not 0):

        if memory[-1].left:
            memory.insert(0,memory[-1].left)
            print(memory[0], end= ' ')
        if memory[-1].right:    
            memory.insert(0,memory[-1].right)
            print(memory[0], end= ' ')
        memory.pop()
    print()

def bredth_depth_search_recursive(tree_node):

    if tree_node is tree.root:
        print(tree_node, end= ' ')

    if tree_node is None:
        return

    if tree_node.left is not None:
        print(tree_node.left, end= ' ')
    if tree_node.right is not None:
        print(tree_node.right, end= ' ')

    bredth_depth_search_recursive(tree_node.left)
    bredth_depth_search_recursive(tree_node.right)


tree = BinaryTree(9)
tree.insert(20)
tree.insert(15)
tree.insert(170)
tree.insert(4)
tree.insert(6)
tree.insert(1)

#      9
#   4     20
# 1  6  15  170


bredth_depth_search(tree)  # 9 4 20 1 6 15 170
bredth_depth_search_recursive(tree.root) # 9 4 20 1 6 15 170