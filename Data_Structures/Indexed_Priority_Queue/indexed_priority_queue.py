"""
Min Indexed D-ary Heap Implementation

The min indexed binary heap is a data structure that efficiently supports the insertion, deletion, and lookup of 
key-value pairs. This implementation uses a bi-directional hash table to map keys to key indices (ki) and vice versa.

A d-ary heap is a generalization of a binary heap where each node has d children. This implementation allows 
the degree of the heap (number of children per node) to be specified, making it flexible for various use cases.

Key Operations:
- `insert(ki, value)`: Inserts a key index (ki) and value into the heap.
- `delete(ki)`: Deletes the specified key index (ki) and its value from the heap.
- `update(ki, value)`: Updates the value associated with the specified key index (ki).
- `decreaseKey(ki, value)`: Decreases the value associated with the specified key index (ki).
- `increaseKey(ki, value)`: Increases the value associated with the specified key index (ki).
- `peekMinKeyIndex()`: Returns the key index (ki) with the smallest value.
- `pollMinKeyIndex()`: Removes and returns the key index (ki) with the smallest value.
- `peekMinValue()`: Returns the smallest value in the heap.
- `pollMinValue()`: Removes and returns the smallest value in the heap.

The heap invariant is maintained using the `_swim` and `_sink` methods, which ensure that the heap property 
is preserved after insertions and deletions.

Attributes:
- `D`: Degree of the heap (number of children per node).
- `max_size`: Maximum size of the heap.
- `size`: Current number of elements in the heap.
- `child`: Lookup array for the first child of each node.
- `parent`: Lookup array for the parent of each node.
- `pm`: Position map that maps key indices (ki) to their node index (ni) in the heap.
- `im`: Inverse map that maps node index (ni) in the heap to key indices (ki).
- `value`: Array of values associated with the key indices (ki).

Methods:
- `_clear_node(ki)`: Clears data for the specified key index (ki).
- `_swim(ni)`: Moves a node at index (ni) up the heap until the heap invariant is maintained.
- `_sink(ni)`: Moves a node at index (ni) down the heap until the heap invariant is maintained.
- `_smallest_child_ni(parent_ni)`: Returns the index of the smallest child node.
- `_swap(ni1, ni2)`: Swaps nodes at indices (ni1) and (ni2).
- `_parent_value(ni)`: Returns the value of the parent node of the node at index (ni).
- `_node_value(ni)`: Returns the value of the node at index (ni).
- `print_binary()`: Prints the binary heap structure.
"""


class MinIndexedDHeap:
    def __init__(self, degree, max_size):
        # degree
        self.D = max(degree, 2)
        # max size
        self.max_size = max(self.D + 1, max_size)

        # number of elements in the heap
        self.size = 0
        # lookup array for first child of each node
        self.child = []
        # lookup array for parent of each node
        self.parent = [None]

        for i in range(self.max_size):
            self.child.append(self.D * i + 1)
            # root node parent is None
            if i != 0:
                self.parent.append((i - 1) // self.D)

        # Position map which maps Key Index (ki) to where the position of the
        # key is located in the priority queue in domain [0,sz)
        self.pm = [None] * self.max_size
        # Inverse map which maps location of key in priority queue in domain [0,sz)
        # to the key Index (ki)
        # 'im' and 'pm' are inverses of each other pm[im[i]] = im[pm[i]] = i
        self.im = [None] * self.max_size

        # values which are associated with the keys
        # indexed using 'ki' this is so that the values array
        # does not require adjustment during swaps
        self.value = [None] * self.max_size

    def insert(self, ki, value):
        """
        Inserts key index (ki) and value into heap
        Takes O(log n
        """
        self.pm[ki] = self.size
        self.im[self.size] = ki
        self.value[ki] = value
        self._swim(self.size)
        self.size += 1

    def delete(self, ki):
        """
        Delete ki and value from the heap.
        Deletions are performed by swapping the node to be deleted
        with the node in the last position, removing the deleted node
        which is now in the last position, and then sinking or swimming
        the swapped node which is now located where the deleted node used to be.

        Returns the deleted ki, value
        Takes O(log n)
        """
        if self.contains(ki):
            # delete ki in last position it can be removed without swapping
            if ki == self.im[self.size - 1]:
                return self._clear_node(ki)

            # get key of last position for swap
            ki_swap = self.im[self.size - 1]
            # swap node to remove and last node
            self._swap(self.pm[ki], self.pm[ki_swap])

            # clear node in last position
            ki, delete_val = self._clear_node(ki)

            # perform both swim and sink to ensure heap invariant is maintained
            current_ni = self._swim(self.pm[ki_swap])
            self._sink(current_ni)
            return ki, delete_val
        else:
            print("Key index is not in heap ")
            return

    def _clear_node(self, ki):
        """
        Clears data on given key index (ki).
        Returns cleared ki and value
        """
        self.im[self.pm[ki]] = None
        self.pm[ki] = None
        delete_val = self.value[ki]
        self.value[ki] = None
        self.size -= 1

        return ki, delete_val

    def valueOf(self, ki):
        """
        Returns value of key index (ki) if exists and none if
        ki not present
        Takes O(1)
        """
        try:
            if self.value[ki] != None:
                return self.value[ki]
        except IndexError as I:
            print(I)
            return
        else:
            return

    def contains(self, ki):
        """
        Returns True if key index (ki) exists, otherwise returns false
        Takes O(1)
        """
        try:
            if self.value[ki] != None:
                return True
        except IndexError as I:
            print(I)
            return False
        else:
            return False

    def peekMinKeyIndex(self):
        """
        Returns key index (ki) of smallest value in heap
        Takes O(1)
        """
        if self.size == 0:
            print("No elements in heap")
            return
        else:
            return self.im[0]

    def pollMinKeyIndex(self):
        """
        Deletes and returns the ki associated with the
        minimum value (top of the heap)
        Takes O(log n)
        """
        if self.size > 0:
            ki, _ = self.delete(self.im[0])
            return ki
        else:
            print("Heap is empty")
            return

    def peekMinValue(self):
        """
        Returns smallest value
        Takes O(1)
        """
        if self.size > 0:
            return self._node_value(0)
        else:
            print("No elements in heap")
            return

    def pollMinValue(self):
        """
        Deletes and returns the minimum value (top of the heap)
        Takes O(log n)
        """
        if self.size > 0:
            _, value = self.delete(self.im[0])
            return value
        else:
            print("Heap is empty")
            return

    def update(self, ki, value):
        """
        Updates key index (ki) with value
        Takes O(log n
        """
        try:
            if not self.contains(ki):
                return self.insert(ki, value)
            else:
                self.value[ki] = value
                # sink and swim values to maintain heap invariant
                self._swim(self.pm[ki])
                self._sink(self.pm[ki])
                return
        except IndexError as I:
            print(I)
            return

    def decreaseKey(self, ki, value):
        """
        Decreases the specified ki only if the new value
        is less than the current value
        Takes O(log n
        """
        if self.contains(ki):
            if value < self.value[ki]:
                self.value[ki] = value
                self._swim(self.pm[ki])
                return
        else:
            print("Key index (ki) not in heap")
            return

    def increaseKey(self, ki, value):
        """
        Increases the specified ki only if the new value
        is greater than the current value
        Takes O(log n
        """
        if self.contains(ki):
            if value > self.value[ki]:
                self.value[ki] = value
                self._sink(self.pm[ki])
                return
        else:
            print("Key index (ki) not in heap")
            return

    def _swim(self, ni):
        """
        Swims node at node index (ni) up until heap invariant is maintained

        Returns node index of new node location
        """
        if self.parent[ni] != None:
            if self._parent_value(ni) > self._node_value(ni):
                self._swap(ni, self.parent[ni])
                self._swim(self.parent[ni])
        return ni

    def _sink(self, ni):
        """
        Sinks node at node index (ni) down until heap invariant is maintained
        Swaps with smallest child node
        Returns node index of new node location
        """
        smallest_child_ni = self._smallest_child_ni(ni)
        if smallest_child_ni != None:
            if self._node_value(ni) > self._node_value(smallest_child_ni):
                self._swap(ni, smallest_child_ni)
                self._sink(smallest_child_ni)
        return ni

    def _smallest_child_ni(self, parent_ni):
        """
        Returns node index (ni) of smallest child node
        If no child nodes are present, none is returned
        """
        smallest_ni = None
        smallest_val = None
        # range of child node indices (ni)
        for ni in range(self.child[parent_ni], self.child[parent_ni] + self.D):
            current_val = self._node_value(ni)
            if current_val != None:
                if smallest_ni == None:
                    smallest_ni = ni
                    smallest_val = current_val
                else:
                    if current_val < smallest_val:
                        smallest_val = current_val
                        smallest_ni = ni
        return smallest_ni

    def _swap(self, ni1, ni2):
        """
        Swaps node at node index ni1 with node
        at node index ni2
        """
        # get key indexes to adjust key index (ki)
        # based arrays (value and position map)
        ki1 = self.im[ni1]
        ki2 = self.im[ni2]
        # swap node indices (ni) in position map
        self.pm[ki1], self.pm[ki2] = self.pm[ki2], self.pm[ki1]
        # swap keys (ki) in inverse map
        self.im[ni1], self.im[ni2] = self.im[ni2], self.im[ni1]

    def _parent_value(self, ni):
        """
        Returns the parent value of node index (ni)
        """
        try:
            if self.parent[ni] != None:
                return self.value[self.im[self.parent[ni]]]
        except IndexError as I:
            print(I)
            return

    def _node_value(self, ni):
        """
        Returns the current value of node index (ni)
        """
        try:
            # ensure that key exists
            if self.im[ni] != None:
                return self.value[self.im[ni]]
        except IndexError as I:
            print(I)
            return

    def print_binary(self):
        for ni in range(0, (self.size // self.D)):
            print(
                " PARENT: key: "
                + str(self.im[ni])
                + " value: "
                + str(self._node_value(ni))
                + "|| LEFT CHILD: "
                + str(self.im[self.child[ni]])
                + " value: "
                + str(self._node_value(self.child[ni]))
                + "|| RIGHT CHILD: "
                + str(self.im[self.child[ni] + 1])
                + " value: "
                + str(self._node_value(self.child[ni] + 1))
            )


if __name__ == "__main__":
    pass
