'''
logic stepts:
1- there is node needed to putted in left or right >> t = BinaryTree(newNode) << create an instance for the new node
2- before considering to putted in left or right , reserve the key that the new node will replace >> self.rightChild = t
3- so the >> t.leftChild = self.leftChild



'''


class BinaryTree(object):
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode) # create t Node
            t.leftChild = self.leftChild  # before said root left = t Node(c), i'll make rootchild(b)=leftchild
            self.leftChild = t  # rootleft=t.key
    def traverse(self):
        if self.leftChild:
            print(self.leftChild.key)
            self.leftChild.traverse()
        if self.rightChild:
            print(self.rightChild.key)
            self.rightChild.traverse()

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild.key

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

r = BinaryTree('a')
print(r.getRootVal())
#print(r.getLeftChild())
r.insertLeft('b')
print(r.leftChild.key)
r.insertLeft('c')
print(r.leftChild.key)
r.insertLeft('d')
print(r.getLeftChild())
r.insertRight('e')
r.insertRight('f')
r.insertRight('g')
print(r.traverse())

'''

r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())
'''