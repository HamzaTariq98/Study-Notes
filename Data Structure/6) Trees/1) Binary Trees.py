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


class Node():
    left = None
    right = None

    def __init__(self, value):
        self.value = value


class BinaryTree():
    root = None

    def __init__(self, value):
        self.root = Node(value)


tree = BinaryTree(10)
print(tree)