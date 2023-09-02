
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

# DFS space O(h)

def in_order(tree_node): # [1,4,6,9,15,20,170]
    if tree_node is None:
        return

    if tree_node.left:
        in_order(tree_node.left)
    print(tree_node, end= ' ')
    if tree_node.right:
        in_order(tree_node.right)


def pre_order(tree_node): # [9,4,1,6,20,15,170] usful when want to copy yr tree
    if tree_node is None:
        return

    print(tree_node, end= ' ')
    pre_order(tree_node.left)
    pre_order(tree_node.right)


def post_order(tree_node): # [1,6,4,15,170,20,9]
    if tree_node is None:
        return
        
    if tree_node.left:
        post_order(tree_node.left)
    if tree_node.right:
        post_order(tree_node.right)
    print(tree_node, end= ' ')


in_order(tree.root) # 1 4 6 9 15 20 170
print()

pre_order(tree.root) # 9 4 1 6 20 15 170 
print()

post_order(tree.root) # 1 6 4 15 170 20 9
print()
