# Branch Sum  The Time and Space Complexity is O(N)
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

    def SUM(self):
        sums=[]
        if self.root:
            self._SUM(self.root,0,sums)
            return sums
        else:
            print("there is no tree exist")

    def _SUM(self,currentNode,temp_sum,sums):
        if currentNode:
            temp_sum+=currentNode.key
            print(temp_sum,temp_sum,currentNode.key,sums)
            if currentNode.left is None and currentNode.right is None:
                sums.append(temp_sum)
                print(sums)
                return  # that is what making me around myself ??!!!! " that is the base case "
            self._SUM(currentNode.left,temp_sum,sums)
            self._SUM(currentNode.right, temp_sum, sums)
        else :
            return

    def __setitem__(self, key, value):
        self.insert(key, value)


bst = BST()
bst.insert(4, "d")
bst[3] = "c"  # that happened py the  " __setitem__ " method

bst.insert(1, "a")
bst.insert(5, "e")
bst.insert(2, "b")
bst.insert(10, "g")

bst.insert(6, "f")
bst.insert(15, "g")

print(bst.SUM())
