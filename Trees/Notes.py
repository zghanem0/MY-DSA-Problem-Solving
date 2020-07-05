'''
What is a Tree? Trees are abstract data structures, used to manage data in a hierarchical way, making data
retrieving much more efficient than other data structure methods.A tree is a collection of nodes that are linearly
connected and don't have any cyclic relations as shown in Figure 1. These nodes contain information and are usually
arranged in a key-value structure. The key serves as an identifier for the data, and value is the actual data that
you want to store.
- Trees are well-known as a non-linear data structure. They don’t store data in a linear way. They organize data hierarchically.
-


>> Common 3 traverse patterns:
- preorder
- inorder
-postorder

>> common types of tree :
1. General Tree: If no constraint is placed on the hierarchy of the tree, a tree is called
a general tree. Every node may have infinite numbers of children in General Tree

2. Binary Tree(complete tree) :If no constraint is placed on the hierarchy of the tree, a tree is called a general tree.
 Every node may have infinite numbers of children in General Tree The binary tree is the kind of tree in which most
 two childrencan be found for each parent. The kids are known as the left kid and right kid
>> types of binary tree :
 - Complete Binary Tree: A Binary Tree is complete Binary Tree if all levels are completely filled except possibly the last level
   and the last level has all keys as left as possible means the tree filled each level from left to right respectively
 - Perfect Binary Tree: A Binary tree is Perfect Binary Tree in which all internal nodes have two children and all leaves are at the same level.
 - Balanced Binary Tree: A binary tree is balanced if the height of the tree is O(Log n) where n is the number of nodes
    such as Balanced Binary Search trees ,AVL Tree
3. Binary Search Tree Binary Search Tree (BST) is a binary tree extension with several optional restrictions. The
left child value of a node should in BST be less than or equal to the parent value and the right child value should
always be greater than or equal to the parent’s value. This Binary Search Tree property makes it ideal for search
operations since we can accurately determine at each node whether the value is in the left or right sub-tree. This is
why the Search Tree is named.
    - binary tree and BST aren't efficient because they unbalanced
>> what makes trees is efficient: because the order is O(log n) if it balanced
look at that digram below :
there are 4 levels so the worest case will be only 4 operations :
if the the node is size is 16 the operations will be 4 that's why, log 16 =4  which log for base 2

    - if the tree balanced means : the left height(levels) nearly equal to the right ,the Order will be O(log n), in case of lookup,insertion and deletion
    - if the tree unbalanced means : the left height completely not equal to the right, the Order will be O(n), in case of lookup,insertion and deletion

                            2
                           / \
                         /     \
                        1       3
                       / \     / \
                      0   7   9   1
                     /   / \  / \ / \
                    2   1   0 7  8   8
                Unbalanced tree ()

4.  AVL Tree AVL tree is a binary search tree self-balancing. On behalf of the inventors Adelson-Velshi and Landis,
the name AVL is given. This was the first tree that balanced dynamically. A balancing factor is allocated for each
node in the AVL tree, based on whether the tree is balanced or not. The height of the node kids is at most 1. AVL
vine. In the AVL tree, the correct balance factor is 1, 0 and -1. If the tree has a new node, then it will be rotated
to ensure that the tree is balanced. It will then be rotated. Common operations such as viewing, insertion,
and removal take O(log n) time in the AVL tree. It is mostly applied when working with Lookups operations.

5. Red-Black Tree
Another kind of auto-balancing tree is red-black. The red-black name is given because the Red-black tree has either red or Black painted on each node according to the red-black tree’s properties. It maintains the balance of the forest. Even though this tree is not a fully balanced tree, the searching operation only takes O (log n) time. When the new nodes are added in Red-Black Tree then nodes will be rotated again to maintain the Red-Black Tree’s properties.

>> when to use binary Heaps: when we need priorities , may from smaller to larger or vice versa
 - in case of MIN model : means the smaller number is have a high priority and the tree start from the smaller number
 - in case of MAX model : means the larger number is have a high priority and the tree start from the larger number

>> the difference between the AVL and Red Black Tree
    AVL:

        are more strict in terms of balance: the heights of the two child subtrees of any node differ by at most 1 (one)
        so it does more CPU instructions per operation (insert/delete) at average
        so AVL faster for lookup operations because they are more strictly balanced
    Red-Black:

        less balanced. Does less CPU inscructions per insert/delete operation: so faster for modifying operations
        keep more data (require 1 additional bit in every node)
        slower for lookup operations

>>> tree Operations :
    >> The Insertion :
        #Here’s the code:

        def insert_left(self, value):
            if self.left_child == None:
                self.left_child = BinaryTree(value)
            else:
                new_node = BinaryTree(value)
                new_node.left_child = self.left_child
                self.left_child = new_node
        Again, if the current node doesn’t have a left child, we just create a new node and set it to the current node’s left_child.
         Or else we create a new node and put it in the current left child’s place. Allocate this left child node to the new node’s left child.


'''
