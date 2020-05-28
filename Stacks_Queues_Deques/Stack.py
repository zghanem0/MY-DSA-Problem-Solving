class Stack():
    def __int__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self): # to get the last-in element in the stack
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def S_content(self):
        return self.items

s = Stack()
s.items=[]
s.push("1")
s.push("2")
s.push("3")
s.push("4")
s.push("5")

print(s.pop())
print(s.S_content())
