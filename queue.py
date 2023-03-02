from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer)==0

    def size(self):
        return len(self.buffer)

pq = Queue()

pq.enqueue({
    'company':'ayolayo',
    'timestamp':'15 apr, 11:02 AM',
    'price':'12 billion pounds'
})
pq.enqueue({
    'company':'ayolayo',
    'timestamp':'15 apr, 11:03 AM',
    'price':'27 billion pounds'
})
pq.enqueue({
    'company':'ayolayo',
    'timestamp':'15 apr, 11:04 AM',
    'price':'43 billion pounds'
})
print(pq.buffer)