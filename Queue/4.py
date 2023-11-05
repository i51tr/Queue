class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def insertRear(self, item):
        self.items.append(item)

    def insertFront(self, item):
        self.items.insert(0, item)

    def deletionFront(self):
        return self.items.pop(0)

    def deletionRear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

d = Deque()
print(d.isEmpty())
d.insertRear(8)
d.insertRear(5)
d.insertFront(7)
d.insertFront(10)
print(d.size())
print(d.isEmpty())
d.insertRear(11)
print(d.deletionRear())
print(d.deletionFront())
d.insertFront(55)
d.insertRear(45)
print(d.items)