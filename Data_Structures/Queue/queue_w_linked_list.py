"""
Queue Implementation

A queue is a linear data structure that follows the First In First Out (FIFO) principle. This means that the first element added 
to the queue will be the first one to be removed. It is similar to a real-world queue, like a line of people waiting for a service, 
where the person who arrives first is served first.

Key Operations:
- `enqueue(data)`: Adds an element to the back of the queue.
- `dequeue()`: Removes and returns the front element of the queue.
- `peek()`: Returns the front element without removing it.
- `contains(data)`: Checks if an element is present in the queue.
- `remove(data)`: Removes a specific element from the queue.
- `is_empty()`: Checks if the queue is empty.
- `__repr__()`: Returns a string representation of the queue.

This implementation uses a linked list to store the elements of the queue, ensuring efficient O(1) time complexity for 
both enqueue and dequeue operations.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"[{self.data}]"


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, data):
        """
        Adds data to the back of the queue.
        Terminology: enqueue = adding = offering
        Takes O(1)
        """
        new_node = Node(data)
        if self.length == 0:
            self.last = new_node
            self.first = self.last
            self.length += 1
            return
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1
            return

    def dequeue(self):
        """
        Returns and removes the first element of the queue
        Terminology: dequeue = polling
        Takes O(1)
        """
        if self.is_empty():
            print("Queue is empty. Nothing to dequeue")
            return
        if self.last == self.first:
            self.last = None
        first_node = self.first
        self.first = self.first.next
        self.length -= 1
        return first_node.data

    def peek(self):
        """
        Returns first element without dequeueing
        Takes O(1)
        """
        if self.is_empty():
            print("Queue is Empty")
            return
        return self.first.data

    def contains(self, data):
        """
        Returns True if data in queue, otherwise returns False
        Takes O(n)
        """
        if not self.is_empty():
            current = self.first
            while current:
                if current.data == data:
                    return True
                current = current.next
        return False

    def remove(self, data):
        """
        Remove data if present in queue
        Takes O(n)
        """
        if self.is_empty():
            print("Queue is empty.")
            return
        current = self.first
        # checks if first node to be removed
        if current.data == data:
            self.first = current.next
            self.length -= 1
            return
        try:
            while current:
                # find node before node to be removed
                if current.next.data == data:
                    # reset tail if delete node is last
                    if current.next == self.last:
                        self.last = current
                    current.next = current.next.next
                    self.length -= 1
                    return
                current = current.next
        except AttributeError as a:
            print(f"Data not found in queue")
            return

    def is_empty(self):
        """
        Checks if Queue is empty.
        Takes O(n)
        """
        return self.first == None

    def __repr__(self):
        """
        Print human-readable representation of the queue
        Takes O(n)
        """
        if self.is_empty():
            return "Queue is empty"
        nodes = []
        current = self.first
        for _ in range(0, self.length):
            nodes.append(f"[{current.data}]")
            current = current.next
        return "->".join(nodes)


if __name__ == "__main__":
    pass
