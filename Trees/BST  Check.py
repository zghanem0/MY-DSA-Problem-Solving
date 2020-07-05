'''
the best resources : https://www.freecodecamp.org/news/these-are-the-best-free-courses-to-learn-data-structures-and-algorithms-in-depth-4d52f0d6b35a/
A binary search tree (BST) is a node based binary tree data structure which has the following properties.
• The left subtree of a node contains only nodes with keys less than the node’s key.
• The right subtree of a node contains only nodes with keys greater than the node’s key.
• Both the left and right subtrees must also be binary search trees.


Solution Here is a simple solution- If a tree is a binary search tree, then traversing the tree inorder should lead
to sorted order of the values in the tree. So, we can perform an inorder traversal and check whether the node values
are sorted or not.

tree_vals = []

def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        tree_vals.append(tree.getRootVal())
        inorder(tree.getRightChild())

def sort_check(tree_vals):
    return tree_vals == sorted(tree_vals)

inorder(tree)
sort_check(tree_vals)

'''


#  ---------------------- Solution 2 ()Classic Solution -------------------------


def validate_BST(root):
    return validate_BST_helpper(root,float("-inf"),float("inf"))

def validate_BST_helppeinvertr(currentNode,min,max):
    if currentNode is None: # the base case and means it reaches to the end
        return True
    if currentNode.key >max or currentNode.key<min:
        return False
    leftisvalid=validate_BST_helpper(currentNode.left,min,currentNode.key)
#    rightisvalid=validate_BST_helpper(currentNode.right,currentNode.key,max)
    return leftisvalid and validate_BST_helpper(currentNode.right,currentNode.key,max)

# some times the currentNode.key will be the the min or mix for the next node



root = Node(10, "Hello")
root.left = Node(5, "Five")
root.right = Node(30, "Thirty")

print(validate_BST(root))  # prints True, since this tree is valid

root = Node(10, "Ten")
root.right = Node(20, "Twenty")
root.left = Node(5, "Five")
root.left.right = Node(15, "Fifteen")

print(validate_BST(root))  # prints False, since 15 is to the left of 10