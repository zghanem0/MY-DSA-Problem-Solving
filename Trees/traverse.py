'''
https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/

Tree Traversals (Inorder, Preorder and Postorder) Unlike linear data structures (Array, Linked List, Queues, Stacks,
etc) which have only one logical way to traverse them, trees can be traversed in different ways. Following are the
generally used ways for traversing trees.

                           1
                          / \
                        2    3
                       / \
                      4   5

Depth First Traversals:
(a) Inorder (Left, Root, Right) : 4 2 5 1 3
(b) Preorder (Root, Left, Right) : 1 2 4 5 3
(c) Postorder (Left, Right, Root) : 4 5 2 3 1

Breadth First or Level Order Traversal : 1 2 3 4 5
Please see this post for Breadth First Traversal.



Inorder Traversal (Practice):

Algorithm Inorder(tree) 1. Traverse the left subtree, i.e., call Inorder(left-subtree) 2. Visit the root. 3. Traverse
the right subtree, i.e., call Inorder(right-subtree) Uses of Inorder In case of binary search trees (BST),
Inorder traversal gives nodes in non-decreasing order. To get nodes of BST in non-increasing order, a variation of
Inorder traversal where Inorder traversal s reversed can be used. Example: Inorder traversal for the above-given
figure is 4 2 5 1 3.


Preorder Traversal (Practice):

Algorithm Preorder(tree) 1. Visit the root. 2. Traverse the left subtree, i.e., call Preorder(left-subtree) 3.
Traverse the right subtree, i.e., call Preorder(right-subtree) Uses of Preorder Preorder traversal is used to create
a copy of the tree. Preorder traversal is also used to get prefix expression on of an expression tree. Please see
http://en.wikipedia.org/wiki/Polish_notation to know why prefix expressions are useful. Example: Preorder traversal
for the above given figure is 1 2 4 5 3.


Postorder Traversal (Practice):

Algorithm Postorder(tree) 1. Traverse the left subtree, i.e., call Postorder(left-subtree) 2. Traverse the right
subtree, i.e., call Postorder(right-subtree) 3. Visit the root. Uses of Postorder Postorder traversal is used to
delete the tree. Please see the question for deletion of tree for details. Postorder traversal is also useful to get
the postfix expression of an expression tree. Please see http://en.wikipedia.org/wiki/Reverse_Polish_notation to for
the usage of postfix expression.

'''


# Python program to for tree traversals

# A class that represents an individual node in a
# Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # A function to do inorder tree traversal


def printInorder(root): # print the tree inorder
    if root:
        print("a")
        # First recur on left child
        print("left value : ",root.val)
        printInorder(root.left)
        print("b")
        # then print the data of node
        print(root.val)
'''
        # now recur on right child
        printInorder(root.right)
        print("c")
    # A function to do postorder tree traversal'''


def printPostorder(root): # will print the current.value(root.value) when not found either left or right , so print the leafs
    if root:
        # First recur on left child
        printPostorder(root.left)

        # the recur on right child
        printPostorder(root.right)

        # now print the data of node
        print(root.val),

    # A function to do preorder tree traversal


def printPreorder(root): # shows u the tree shap or i u want to create the tree
    if root:
        # First print the data of node
        print(root.val),

        # Then recur on left child
        printPreorder(root.left)
        # Finally recur on right child
        printPreorder(root.right)

    # Driver code


root = Node(1)
root.left = Node(2)
root.right = Node(5)
root.right.left = Node(6)
root.right.left.left = Node(7)
root.right.right = Node(8)
root.left.left = Node(3)
root.left.right = Node(4)


print("\nInorder traversal of binary tree is")
printInorder(root)
print("Preorder traversal of binary tree is")
printPreorder(root)


print("\nPostorder traversal of binary tree is")

printPostorder(root)