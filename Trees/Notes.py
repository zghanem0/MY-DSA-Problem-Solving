'''What is a Tree? Trees are abstract data structures, used to manage data in a hierarchical way, making data
retrieving much more efficient than other data structure methods.A tree is a collection of nodes that are linearly
connected and don't have any cyclic relations as shown in Figure 1. These nodes contain information and are usually
arranged in a key-value structure. The key serves as an identifier for the data, and value is the actual data that
you want to store.

>> common types of tree :
1. General Tree: If no constraint is placed on the hierarchy of the tree, a tree is called
a general tree. Every node may have infinite numbers of children in General Tree

2. Binary TreeIf no constraint is placed on the hierarchy of the tree, a tree is called a general tree. Every node may
have infinite numbers of children in General Tree The binary tree is the kind of tree in which most two children can be found for each parent.
The kids are known as the left kid and right kid

3. Binary Search Tree Binary Search Tree (BST) is a binary tree extension with several optional restrictions. The
left child value of a node should in BST be less than or equal to the parent value and the right child value should
always be greater than or equal to the parent’s value. This Binary Search Tree property makes it ideal for search
operations since we can accurately determine at each node whether the value is in the left or right sub-tree. This is
why the Search Tree is named.

>> what makes trees is efficient: because the order is O(log n)
look at that digram below :
there are 4 levels so the worest case will be only 4 operations :
if the the node is size is 16 the operations will be 4 that's why, log 16 =4  which log for base 2


                            2
                           / \
                         /     \
                        1       3
                       / \     / \
                      0   7   9   1
                     /   / \  / \ / \
                    2   1   0 7  8   8




4.  AVL Tree AVL tree is a binary search tree self-balancing. On behalf of the inventors Adelson-Velshi and Landis,
the name AVL is given. This was the first tree that balanced dynamically. A balancing factor is allocated for each
node in the AVL tree, based on whether the tree is balanced or not. The height of the node kids is at most 1. AVL
vine. In the AVL tree, the correct balance factor is 1, 0 and -1. If the tree has a new node, then it will be rotated
to ensure that the tree is balanced. It will then be rotated. Common operations such as viewing, insertion,
and removal take O(log n) time in the AVL tree. It is mostly applied when working with Lookups operations.

5. Red-Black Tree
Another kind of auto-balancing tree is red-black. The red-black name is given because the Red-black tree has either red or Black painted on each node according to the red-black tree’s properties. It maintains the balance of the forest. Even though this tree is not a fully balanced tree, the searching operation only takes O (log n) time. When the new nodes are added in Red-Black Tree then nodes will be rotated again to maintain the Red-Black Tree’s properties.


'''
