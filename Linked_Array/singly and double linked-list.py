class S_Node:
    def __init__(self, value):
        self.value = value
        self.N_node = None


a = S_Node(1)
b = S_Node(2)
c = S_Node(3)

a.N_node = b
b.N_node = c
print(b.N_node.value)


# ---------------------------------------------------
#  Doubly linked-list
class D_Node:
    def __init__(self, value):
        self.value = value
        self.N_node = None
        self.P_node = None


d = S_Node(4)
e = S_Node(5)
f = S_Node(6)
g = S_Node(7)

d.P_node = None
d.N_node = e

e.P_node = d
e.N_node = f

f.P_node = d
f.N_node = g

g.P_node = f
g.N_node = None

print(d.N_node.N_node.N_node.value)
