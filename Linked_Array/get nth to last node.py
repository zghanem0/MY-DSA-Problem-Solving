class Node:
    def __init__(self, value):
        self.value = value
        self.nextnode = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e


def nth_to_last_node(n, head):
    left_pointer = head
    right_pointer = head

    # Set right pointer at n nodes away from head
    for i in range(n):

        # Check for edge case of not having enough nodes!
        if not right_pointer.nextnode:
            raise LookupError('Error: n is larger than the linked list.')

        # Otherwise, we can set the block
        right_pointer = right_pointer.nextnode  # to iterate to the end of the range

    # Move the block down the linked list
    while right_pointer:
        left_pointer = left_pointer.nextnode 
        right_pointer = right_pointer.nextnode

    # Now return left pointer, its at the nth to last element!
    return left_pointer.value


print(nth_to_last_node(n=4, head=a))
