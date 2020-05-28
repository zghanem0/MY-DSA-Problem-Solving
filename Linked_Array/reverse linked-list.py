'''
Reverse a singly linked list.
Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:
>> A linked list can be reversed either iteratively or recursively. Could you implement both?
>> Solution Explaination : pre>cur>nxt , should be in the other side (current.nextnode) and reverse the linke
1- we will move "nxt" first to the other side(current.nextnode) : nxt=cur.nextnode
2- reverse the the linke form the cur to the cur.next to be cur to pre : cur.nextnode = pre
3- move the pre to the curent : pre=cur
4- then move the cur to the next side (current.nextnode) :
** summary **
move nxt,reverse the linke to point to prev instade of the cur.nextnode , move the pre to cur , then move the cur to nxt
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Iteratively
# Time Complexity - O(n), Space Complexity - O(1)

class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode = None


# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d


def reverse(head):
    cur = head
    pre, nxt = None, None
    while cur:  # watch out
        nxt = cur.nextnode  # هنا محتاجين nxt علشان لما نفصل ال link بين ال cur وال nextnode.ابقا اساوي ال cur بيه(nxt)
        cur.nextnode = pre  # to break the link between the curr and the next and redirect the link to previous node
        pre = cur  # move the prev link to the cur ()
        cur = nxt  # move the current to the next
    return pre.value  # watch out
    pass


print(reverse(a))  # that line is must convert the linked list to be recursive
print(d.value)
print(c.value)
print(b.value)
print(a.value)
# Recursively
# Time Complexity - O(n), Space Complexity - O(n)
'''class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        reversedList = self.reverseList(head.next)
        head.next.next, head.next = head, None
        return reversedList


'''
