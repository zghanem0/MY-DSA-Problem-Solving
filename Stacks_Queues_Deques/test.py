'''
deque : provide a capability of adding or removing the items at either head(front) or tail(rear)

'''


class Deque():
    def __int__(self):
        self.items = []

    def addFront(self, item):  # such as push element in the queue
        self.items.append(item)

    def addRear(self, item):  # such as push element in the queue
        self.items.insert(0, item)

    def removeHead(self):
        return self.items.pop()

    def removeTail(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def D_content(self):
        return self.items


d = Deque()
d.items = []
d.addFront("1")
d.addFront("2")
d.addFront("3")
d.addRear("4")
d.addRear("5")
print(d.D_content())
print(d.removeHead())
print(d.removeTail())
print(d.D_content())
