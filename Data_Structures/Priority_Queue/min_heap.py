"""
Min Binary Heap Implementation

A minimum binary heap is a complete binary tree where the value of each node is less than or equal to the values of its children. 
This property makes it a useful data structure for implementing priority queues. The root node is the minimum element in the heap.

Key Operations:
- `insert(element)`: Adds an element to the heap and maintains the heap invariant.
- `extract_min()`: Removes and returns the minimum element (root) from the heap.
- `remove(element)`: Removes a specified element from the heap.
- `print_heap()`: Prints the heap in a readable format.

This implementation uses a dynamic array to store the elements of the heap.
"""


class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def insert(self, element):
        """
        Inserts element into heap. Element starts at last position
        and bubbles up until the heap invariant is met
        Takes O(log n)
        """
        self.heap.append(element)
        self.size += 1
        if self.size == 1:
            return
        pos = self.size - 1
        # bubble up until heap invariant satisfied
        self._bubble_up(pos)

    def _left_child(self, pos):
        """
        Return position of left child
        Takes O(1)
        """
        return 2 * pos + 1

    def _right_child(self, pos):
        """
        Return position of right child
        Takes O(1)
        """
        return 2 * pos + 2

    def _get_element(self, pos):
        """
        Returns element at given position if exists. Returns None if not.
        Takes O(1)
        """
        if pos < self.size:
            return self.heap[pos]
        return None

    def parent(self, pos):
        """
        Returns position of parent element
        Takes O(1)
        """
        return (pos - 1) // 2

    def _is_leaf(self, pos):
        """
        Returns True if element is a leaf node, returns false otherwise
        """
        return pos >= (self.size // 2) and pos <= self.size

    # Method to _swap two nodes of the heap
    def _swap(self, fpos, spos):
        """
        swaps element at fpos with element at spos
        Takes O(1)
        """
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]

    def _bubble_down(self, pos):
        """
        Moves the node at position pos downwards through the heap
        until heap invariant is satisfied.
        Takes O(log n)
        """
        if not self._is_leaf(pos):
            # check if current element is larger than children
            if (
                self.heap[pos] > self.heap[self._left_child(pos)]
                or self.heap[pos] > self.heap[self._right_child(pos)]
            ):
                # use try statement to account for case when only 1 left child node.
                # the right node does not exist and will return index error when attempting comparison
                try:
                    # find which child is smaller and _swap with that element before calling bubble_down again
                    if (
                        self.heap[self._left_child(pos)]
                        < self.heap[self._right_child(pos)]
                    ):
                        self._swap(pos, self._left_child(pos))
                        self._bubble_down(self._left_child(pos))
                    else:
                        self._swap(pos, self._right_child(pos))
                        self._bubble_down(self._right_child(pos))
                except IndexError:
                    self._swap(pos, self._left_child(pos))

    def _bubble_up(self, pos):
        """
        Moves the node at position pos upwards through the heap
        until heap invariant is satisfied.
        Takes O(log n)
        """
        if pos != 0:
            # check if child is less than parent (violates heap invariant)
            if self.heap[pos] < self.heap[self.parent(pos)]:
                self._swap(pos, self.parent(pos))
                self._bubble_up(self.parent(pos))

    def _maintain_heap_invariant(self, pos):
        """
        Determines appropriate bubble directions and bubbles in that direction
        Takes O(log n)
        """
        if pos == 0:
            return self._bubble_down(pos)
        if self._is_leaf(pos):
            return self._bubble_up(pos)
        if self.heap[pos] < self.heap[self.parent(pos)]:
            return self._bubble_up(pos)
        else:
            self._bubble_down(pos)

    def remove(self, element):
        """
        Removes and returns specified element if found.
        Takes O(n) but can be reduced to O(log n) if using hash table {value: [positions]}
        """
        if self.size == 0:
            print("Heap is empty. Nothing to remove.")
            return
        # checks if element is root
        if element == self.heap[0]:
            self.extract_min()
            return
        for pos in range(0, self.size):
            if self.heap[pos] == element:
                # _swap specified element with last position
                if pos != self.size - 1:
                    self._swap(pos, self.size - 1)
                element = self.heap.pop()
                self.size -= 1
                self._maintain_heap_invariant(pos)
                return element

        print("Element not found in heap")
        return

    def extract_min(self):
        """
        Removes minimum element at root of the heap.
        Reorders heap so heap invariant is maintained
        Also known as poll
        takes O(log n)
        """
        if self.size == 0:
            print("Heap is empty. Nothing to extract")
            return
        self._swap(0, self.size - 1)
        min = self.heap.pop(-1)
        self.size -= 1
        self._bubble_down(0)
        return min

    def print_heap(self):
        print(f"FULL HEAP: {self.heap}")
        for i in range(0, (self.size // 2)):
            print(
                " PARENT : "
                + str(self.heap[i])
                + " LEFT CHILD : "
                + str(self._get_element(self._left_child(i)))
                + " RIGHT CHILD : "
                + str(self._get_element(self._right_child(i)))
            )


if __name__ == "__main__":
    pass
