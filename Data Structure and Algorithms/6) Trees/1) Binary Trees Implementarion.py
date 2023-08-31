# Each node have (0-2) Childs
# Each node have 1 parent

# Perfect Binary Tree, all nodes have 2 childs expect for leafs
# Full Binary Tree, all nodes have 2 or 0 childs


# Pefrect Binary Tree:

    # number of nodes doubles when you move forward nodes = 2^level
    # (nodes in last level) = (number of other nodes + 1)
    # nodes in tree = 2^h-1


    # Right child > Parent
    # Left child < Parent

# Heaps: similar to binary tree but nodes insertion are from left to right, and if node value greater than parent it keep bubble up until parent is greater
# in Heaps child is less than parent and can be (left or right)
# Heaps useful in Priority queues (Airplane VIP, Hospital Emergency)



# Trie useful for text auto completion, a tree of other possible characters
# Space efficient as single char can be split into many words


class Node():
    left = None
    right = None


    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'{self.value}'


class BinaryTree():
    root = None


    def __init__(self, value):
        self.root = Node(value)


    def insert(self, value):
        inserted_node = Node(value)
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
    


tree = BinaryTree(10)

tree.insert(15)
tree.insert(12)
tree.insert(55)

tree.insert(5)
tree.insert(4)
tree.insert(7)




print(tree.lookup(4)) # ['Root', 'Left', 'Left']
print(tree.lookup(40)) # Value 40 was not found in yr tree

print(tree.remove(7)) # ['Root', 'Left', 'Right'] ((fnc remove return the rout of deleted value))
print(tree.root.left.right) # None ((Since we already removed before))

