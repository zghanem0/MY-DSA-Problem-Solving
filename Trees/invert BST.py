class Node:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def is_left(self):
        return self.parent.left

    def is_right(self):
        return self.parent.right

    def has_right(self):
        return self.right

    def has_left(self):
        return self.left

    def is_leaf(self):
        return not (self.left or self.right)

    def hasAnyChildren(self):
        return self.right or self.left

    def hasBothChildren(self):
        return self.right and self.left


class BST:
    def __init__(self):
        self.root = None

    def trav_preorder(self):
        if self.root == None:
            print("the tree is empty")
        else:
            currentNode = self.root
            return self._trav_preorder(currentNode)

    def _trav_preorder(self, currentNode):
        if currentNode:
            print(currentNode.key)
            self._trav_preorder(currentNode.left)
            self._trav_preorder(currentNode.right)

    def trav_inorder(self):
        if self.root == None:
            print("the tree is empty")
        else:
            currentNode = self.root
            self._trav_inorder(currentNode)

    def _trav_inorder(self, currentNode):
        if currentNode != None:
            self._trav_inorder(currentNode.left)
            print(currentNode.key)
            self._trav_inorder(currentNode.right)

    def insert_iter(self, key, value):
        currentNode = self.root
        newNode = Node(key, value)
        if self.root == None:
            self.root = newNode
        else:
            while True:
                if newNode.key < currentNode.key:
                    if currentNode.left == None:
                        currentNode.left = newNode
                        return
                    else:
                        currentNode = currentNode.left
                else:
                    if currentNode.right == None:
                        currentNode.right = newNode
                        return
                    else:
                        currentNode = currentNode.right

    def put(self, key, value):
        currentNode = self.root
        newNode = Node(key, value)
        if self.root != None:
            self._put(currentNode, newNode)
        else:
            self.root = Node(key, value)
            return

    def _put(self, currentNode, newNode):
        if newNode.key < currentNode.key:
            if currentNode.left:
                self._put(currentNode.left, newNode)
            else:
                currentNode.left = newNode
                currentNode.left.parent = currentNode
        else:
            if currentNode.right:
                self._put(currentNode.right, newNode)
            else:
                currentNode.right = newNode
                currentNode.right.parent = currentNode

    # deletion cases{is leaf,has only one child , has 2 childs}
    def delete(self, key):
        targetNode = self.search(key)
        if targetNode:
            if targetNode.is_leaf():
                if targetNode.is_left():
                    targetNode.parent.left = None
                else:
                    targetNode.parent.right = None


            elif targetNode.hasAnyChildren() and not targetNode.hasBothChildren():
                print("has 1 childs")
                if targetNode.parent.right == targetNode:
                    if targetNode.has_right():
                        targetNode.right.parent = targetNode.parent
                        targetNode.parent.right = targetNode.right
                    else:
                        targetNode.left.parent = targetNode.parent
                        targetNode.parent.right = targetNode.left
                    targetNode = None
                else:
                    if targetNode.parent.left == targetNode:
                        print(".....1")
                        if targetNode.has_right():
                            targetNode.right.parent = targetNode.parent
                            targetNode.parent.left = targetNode.right
                        else:
                            print(".....2")
                            targetNode.left.parent = targetNode.parent
                            targetNode.parent.left = targetNode.left
                        targetNode = None

            else:
                print("has 2 childs")
                succ = self.find_secc(targetNode)
                targetNode.key = succ.key
                targetNode.value = succ.value

        else:
            return "the node not found"

    def find_secc(self, node):
        node = node.left
        while node.right:
            node = node.right
        node.parent.right = None
        temp_node = node
        return temp_node

    def search(self, key):
        currentNode = self.root
        return self._search(key, currentNode)

    def _search(self, key, currentNode):
        if currentNode == None:
            return None
        elif key == currentNode.key:
            return currentNode
        elif key < currentNode.key:
            return self._search(key, currentNode.left)
        else:
            return self._search(key, currentNode.right)


bst = BST()
bst.put(5, "E")
bst.put(10, "h")
bst.put(2, "b")
bst.put(6, "g")
bst.put(3, "c")
bst.put(8, "f")
bst.put(12, "i")
bst.put(1, "a")
bst.put(4, "d")


# print(bst.root.left.parent.key)


class Node:
    def __init__(self, k, val):
        self.key = k
        self.value = val
        self.left = None
        self.right = None


# time= O(N) , Space=O(N)
def invert_bst_iter(root):
    q = [root]
    while q:
        node = q.pop(0)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
        invert_bst_swap(node)

    return bst.trav_inorder()


# time= O(N) , Space=O(d) (the best)
def invert_bst(node):
    invert_bst_recursively(node)
    return bst.trav_inorder()


def invert_bst_recursively(node):
    if node is None:
        return
    invert_bst_swap(node)
    invert_bst_recursively(node.left)
    invert_bst_recursively(node.right)


def invert_bst_swap(node):
    node.left, node.right = node.right, node.left


invert_bst_iter(bst.root)
