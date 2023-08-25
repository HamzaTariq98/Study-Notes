class Node():

    next_node = None
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f'{self.data}'


class LinkedList():
    head = None
    def __init__(self, value = None):
        if value:
            self.head = Node(value)


    def prepend(self, value): # O(1)
        prepend_node = Node(value)
        prepend_node.next_node = self.head
        self.head = prepend_node


    def append(self, value): # O(n) due to tail not defined in my LinkedList

        append_node = Node(value)
        node = self.head
        if node:
            while (node.next_node):
                node = node.next_node
            node.next_node = append_node
        else:
            self.prepend(value)

    def lookup(self, value):  # O(n)
        node_index = 0
        for node in self.nodes():
            if node.data == value:
                return node_index
            node_index += 1
        return -1

    def insert(self, value, index): # O(n) consider O(1) as only 2 pointers needed to be updated !

        lenght = len(self.nodes())
        if index == 0:
            self.prepend(value)

        elif index == lenght:
             self.append(value)

        elif index > lenght or index < 0:
             raise IndexError(f'{index} out of Linked list range (0-{lenght})')

        else:
            left_node = self.head
            insert_node = Node(value)
            for node_index in range(index-1):
                left_node = left_node.next_node
            right_node = left_node.next_node

            insert_node.next_node = right_node
            left_node.next_node = insert_node


    def delete(self, index): # O(n) consider O(1) as only 2 pointers needed to be updated at most
        lenght = len(self.nodes())
        left_node = self.head

        if index == 0:
            self.head = left_node.next_node

        elif index > lenght-1 or index < 0:
            raise IndexError(f'{index} out of Linked list range (0-{lenght-1})')
        
        else:
            for node_index in range(index-1):
                left_node = left_node.next_node

            delete_node = left_node.next_node
            right_node = delete_node.next_node
            left_node.next_node = right_node



    def nodes(self):
        nodes = []
        node = self.head
        while(node):
            nodes.append(node)
            node = node.next_node
        return nodes


    def __str__(self):
        return f'{self.nodes()}'

    def reverse(self):
        reversed_linked_list = LinkedList()
        nodes = self.nodes()
        for node in nodes[::-1]:
            reversed_linked_list.append(node.data)
        return reversed_linked_list



linked_list = LinkedList()
linked_list.prepend(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

linked_list.insert(2.5,2)


print(linked_list.lookup(5)) # -1 as 5 is not in linked list
print(linked_list.lookup(3)) # 3
print(linked_list.head) # 1
print(linked_list) # [1, 2, 2.5, 3, 4]

linked_list.delete(0)
print(linked_list) # [2, 2.5, 3, 4]

print(linked_list.reverse())