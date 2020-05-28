class Queue():
    def __int__(self):
        self.items = []

    def enqueue(self, item):  # such as push element in the queue
        self.items.insert(0, item)

    def dequeue(self):  # poll : that last element will be pulled may from servers or other processes such as SQS
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def q_content(self):
        return self.items


q = Queue()
q.items = []
q.enqueue("1")
q.enqueue("2")
q.enqueue("3")
q.enqueue("4")
q.enqueue("5")
print(q.dequeue())
print(q.q_content())

