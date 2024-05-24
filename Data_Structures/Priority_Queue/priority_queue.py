from min_heap import MinHeap


class PriorityQueue:
    def __init__(self):
        self.queue = MinHeap()

    def enqueue(self, data):
        self.queue.insert(data)
