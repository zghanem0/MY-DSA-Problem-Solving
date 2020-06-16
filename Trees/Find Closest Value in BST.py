# Find Closest Value in BST
class Node:
    def __init__(self, key, value, parent):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if self.root:
            self._insert(key, value, self.root)
        else:
            self.root = Node(key, value, None)

    def _insert(self, key, value, currentNode):
        if key < currentNode.key:
            if currentNode.left:
                self._insert(key, value, currentNode.left)
            else:
                currentNode.left = Node(key, value, parent=currentNode)

        else:
            if currentNode.right:
                self._insert(key, value, currentNode.right)
            else:
                currentNode.right = Node(key, value, parent=currentNode)

    def __setitem__(self, key, value):
        self.insert(key, value)

# Find Closest Value in BST Recusively , but not recommended the itertive approach is best
#        In Average Case    :     the Time Complexity is O(Log N) and The Space Complexity is O(Log N)
#        In the worest Case :     the Time Complexity is O(N) and The Space Complexity is O(N)

    '''

    def Find_Closest_Value_in_BST(self, target):
        if self.root:
            if target != self.root.key:
                return self.Find_Closest_Value_in_BST_Helper(float("inf"),target,self.root )
            else:
                return self.root.key
        else:
            return print("the tree is empty")
    def Find_Closest_Value_in_BST_Helper(self,closest,target,currentNode ):

        if currentNode:
            # there is ( closest - target  - currentNode after recursion) == (prev-cur-next)
            if abs(closest - target) > abs(
                    target - currentNode.key):  # as if i said abs(prev-target) > abs(target-next)
                closest = currentNode.key
            if currentNode.key > target:
                return self.Find_Closest_Value_in_BST_Helper(closest,target,currentNode.left )

            if currentNode.key < target:
                return self.Find_Closest_Value_in_BST_Helper(closest,target,currentNode.right )
            else:
                return currentNode.key
        else:
            return closest
'''

# Find Closest Value in BST Recusively , but not recommended the itertive approach is best
#        In Average Case    :     the Time Complexity is O(Log N) and The Space Complexity is O(1)
#        In the worest Case :     the Time Complexity is O(N) and The Space Complexity is O(1)
    def Find_Closest_Value_in_BST(self, target):
        if self.root:
            if target != self.root.key:
                self.currentNode = self.root
                closest = float("inf")
                while self.currentNode is not None:
                    if abs(closest - target) > abs(target - self.currentNode.key):
                        closest = self.currentNode.key
                    if self.currentNode.key > target:
                        self.currentNode = self.currentNode.left
                    elif self.currentNode.key < target:
                        self.currentNode = self.currentNode.right
                    else:
                        return self.currentNode.key
            else:
                return self.root.key
        else:
            return print("the tree is empty")
        return closest


bst = BST()
bst.insert(4, "d")
bst[3] = "c"  # that happened py the  " __setitem__ " method

bst.insert(1, "a")
bst.insert(5, "e")
bst.insert(2, "b")
bst.insert(10, "g")

bst.insert(6, "f")
bst.insert(15, "g")

print(bst.Find_Closest_Value_in_BST(15))