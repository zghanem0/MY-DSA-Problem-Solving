class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode = None


# CREATE CYCLE LIST Cases the are 2 Cases
# CYCLE LIST Case
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a  # Cycle Here!

# CREATE NON CYCLE LIST Case
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z

'''
def cycle_check(node):
    # Begin both markers at the first node
    marker1 = node
    marker2 = node
'''


class Solution:
    # @param head, a ListNode
    # @return a boolean

    def hasCycle(self, head):  # the will take the head of the list

        slow = fast = head  # the markers (marker1=slow,marker2=fast) will be == to the head of the list
        while fast and fast.nextnode:  # this statement == >> while fast != None and fast.nextnode != None :
            slow = slow.nextnode
            fast = fast.nextnode.nextnode
            if slow is fast:
                return True

        return False  # means that there is the end for this linked-nodes and not cyclic linked-list


# print(a.value)
t = Solution()
print("test case 1 : ", t.hasCycle(a))  # test Case (1)
print("test case 2 : ", t.hasCycle(x))  # test Case (1)
