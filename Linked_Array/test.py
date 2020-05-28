class Node:
    def __init__(self, value):
        self.value = value
        self.N_node = None


class llist_ops:
    def __int__(self):
        self.head = None

    def append(self, data):
        new_data = Node(data)
        if self.head is None:
            self.head = new_data
            return
        last_node = self.head
        while last_node.N_node:  # working until the last_node.N_node becoming None
            last_node = last_node.N_node
        last_node.N_node = new_data  # pointing to the new node


'''
a = Node(1)
b = Node(2)
c = Node(3)

a.N_node = b
b.N_node = c
'''

llist = llist_ops()
llist.append("a")
