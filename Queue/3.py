class PriorityQueue:
    def __init__(self):
        self.queue = []
 
    def insert(self, val, priority):
        self.queue.append((priority, val))
 
    def remove(self):
        max_idx = 0
        for i in range(1, len(self.queue)):
            if self.queue[i][0] > self.queue[max_idx][0]:
                max_idx = i
        val = self.queue[max_idx][1]
        while max_idx < len(self.queue) - 1:
            self.queue[max_idx] = self.queue[max_idx + 1]
            max_idx += 1
        self.queue.pop()
        return val
 
pq = PriorityQueue()
pq.insert('Task 1', 4)
pq.insert('Task 2', 2)
pq.insert('Task 3', 1)
pq.insert('Task 4', 3)
print(pq.remove())  
print(pq.remove())  
print(pq.remove())  
print(pq.remove())