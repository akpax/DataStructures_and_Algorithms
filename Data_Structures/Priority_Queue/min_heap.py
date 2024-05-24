"""
This is a minimum binary heap.
"""


class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def insert(self, element):
        """
        Inserts element into heap. Element starts at last position
        and bubbles up until the heap invariant is met
        """
        self.heap.append(element)
        self.size += 1
        if self.size == 1:
            return
        pos = self.size - 1
        # bubble up until heap invariant satisfied
        self.bubble_up(pos)

    def left_child(self, pos):
        """
        Return position of left child
        """
        return 2 * pos + 1

    def right_child(self, pos):
        """
        Return position of right child
        """
        return 2 * pos + 2

    def _get_element(self, pos):
        """
        Returns element at given position if exists. Returns None if not.
        """
        if pos < self.size:
            return self.heap[pos]
        return None

    def parent(self, pos):
        """
        Returns position of parent element
        """
        return (pos - 1) // 2

    def is_leaf(self, pos):
        """
        Returns True if element is a leaf node, returns false otherwise
        """
        return pos >= (self.size // 2) and pos <= self.size

    # Method to swap two nodes of the heap
    def swap(self, fpos, spos):
        """
        Swaps element at fpos with element at spos
        """
        print(
            f" Swapping {self.heap[fpos]} at {fpos} with {self.heap[spos]} at {spos} "
        )
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]

    def bubble_down(self, pos):
        """
        Reorders heap after extracting min from root of heap
        Bubbles down the new root until heap invariant is satisfied.
        """
        if not self.is_leaf(pos):
            # check if current element is larger than children
            if (
                self.heap[pos] > self.heap[self.left_child(pos)]
                or self.heap[pos] > self.heap[self.right_child(pos)]
            ):
                # use try statement to account for case when only 1 left child node.
                # the right node does not exist and will return index error when attempting comparison
                try:
                    # find which child is smaller and swap with that element before calling bubble_down again
                    if (
                        self.heap[self.left_child(pos)]
                        < self.heap[self.right_child(pos)]
                    ):
                        self.swap(pos, self.left_child(pos))
                        self.bubble_down(self.left_child(pos))
                    else:
                        self.swap(pos, self.right_child(pos))
                        self.bubble_down(self.right_child(pos))
                except IndexError:
                    self.swap(pos, self.left_child(pos))

    def bubble_up(self, pos):
        if pos != 0:
            # check if child is less than parent (violates heap invariant)
            if self.heap[pos] < self.heap[self.parent(pos)]:
                self.swap(pos, self.parent(pos))
                self.bubble_up(self.parent(pos))

    def determine_bubble_direction(self, pos):
        """
        Determines appropriate bubble directions and bubbles in that direction
        """
        if pos == 0:
            return self.bubble_down(pos)
        if self.is_leaf(pos):
            return self.bubble_up(pos)
        if self.heap[pos] < self.heap[self.parent(pos)]:
            return self.bubble_up(pos)
        else:
            self.bubble_down(pos)

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
                # swap specified element with last position
                if pos != self.size - 1:
                    self.swap(pos, self.size - 1)
                element = self.heap.pop()
                self.size -= 1
                self.determine_bubble_direction(pos)
                return element

        print("Element not found in heap")
        return

    def extract_min(self):
        """
        Removes minimum element at root of the heap.
        Reorders heap so heap invariant is maintained
        Terminology: also known as poll
        """
        if self.size == 0:
            print("Heap is empty. Nothing to extract")
            return
        self.swap(0, self.size - 1)
        min = self.heap.pop(-1)
        self.size -= 1
        self.bubble_down(0)
        return min

    def print_heap(self):
        print(f"FULL HEAP: {self.heap}")
        for i in range(0, (self.size // 2)):
            print(
                " PARENT : "
                + str(self.heap[i])
                + " LEFT CHILD : "
                + str(self._get_element(self.left_child(i)))
                + " RIGHT CHILD : "
                + str(self._get_element(self.right_child(i)))
            )


if __name__ == "__main__":
    pass
