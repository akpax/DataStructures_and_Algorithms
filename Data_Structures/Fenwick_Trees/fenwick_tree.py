"""
Fenwick Tree (Binary Indexed Tree) Implementation

A Fenwick Tree, also known as a Binary Indexed Tree (BIT), is a data structure that provides efficient methods 
for cumulative frequency tables. It allows querying prefix sums and updating elements in logarithmic time. 
The Fenwick Tree is particularly useful for scenarios where there are frequent updates and prefix sum queries.

Key Features:
- Space-efficient: Requires O(n) space, where n is the number of elements.
- Supports point updates and prefix sum queries in O(log n) time.
- Suitable for problems involving dynamic cumulative frequency tables, such as range sum queries and updates.

How it works:
- The tree is represented as an array where each index stores the sum of a range of elements.
- The parent-child relationship is determined by the binary representation of the indices.
- The least significant bit (LSB) of an index determines the range of elements it covers.
- To update an element, propagate the change to all relevant indices in the tree.
- To get a prefix sum, accumulate the values from relevant indices up to the desired position.

Operations:
- `update(index, delta)`: Adds `delta` to the element at `index` and updates the tree accordingly.
- `query(index)`: Returns the prefix sum from the start up to the given `index`.
- `range_query(left, right)`: Returns the sum of elements in the range [left, right].

This implementation is 1-based while the user-supplied values are zero-based.
The user will interact with the data structure using zero-based indexing.
After the Fenwick Tree is initialized with the user-specified values, indexes 
cannot be added or removed from the tree.
"""

import copy


class FenwickTree:
    def __init__(self, values: list):
        # store original values for future reference
        self.values = values
        self.size = len(self.values)
        self.tree = self.construct(self.values)

    def construct(self, values):
        """
        Takes sums of values and converts into a Fenwick tree
        Note: Fenwick Tree is assumed to be 1-based internally

        Takes O(n)
        """
        tree = copy.deepcopy(values)
        # Fenwick trees are 1 -based so we add a null value to front of tree
        tree.insert(0, 0)
        print(tree)
        for i in range(1, self.size):
            j = i + self._LSB(i)
            if j <= self.size:
                # add child value to parent
                # decrease index by 1 since byte integers are 1 based
                tree[j] += tree[i]

        return tree

    def range_query(self, start, stop):
        """
        Finds the sum of the values in range [start, stop] inclusive
        Note:
        - Indices are 0-based to correspond to the value indices.
        - The Fenwick Tree is assumed to be 1-based internally.
        Takes O(log n)
        """
        try:
            # prefix sum of start is exclusive bc we want to include the start
            # value in the sum
            return self._prefix_sum(stop) - self._prefix_sum(start - 1)
        except IndexError:
            print(f"Indices provided must be in range 0-{self.size-1}")
            return

    def point_update(self, index, new_value):
        """
        Adds new_value to values at index (zero-based) and adds new value
        to tree at i (1-based)

        Takes O(n) time
        """
        # update values array
        self.values[index] += new_value
        # convert index from 0-based to 1-based array
        i = index + 1
        while i <= self.size:
            self.tree[i] += new_value
            i = i + self._LSB(i)

    def _prefix_sum(self, index):
        """
        Performs the cumulative sum  of all elements from beginning of array to specified index.
        Takes O(log n)
        """
        sum = 0
        # Convert user's zero-based index to 1-based index for Fenwick tree
        i = index + 1
        while i != 0:
            sum += self.tree[i]
            i = i - self._LSB(i)
        return sum

    def _LSB(self, num):
        """
        Returns the position of the least significant bit.
        Note: The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:
        The negative byte representation is it's two's complement.
        The two's complement is found buy inverting all bits of the number (bitwise NOT operation)
        and then adding 1 to the least significant bit.
        example: num = 12 (1100 in binary)
        Find two's complement:
            Invert num -> 0011
            Add 1 to LSB -> 0011 + 0001 = 0100
            Result: 0100 (int: 4)
        Perform bitwise & operation:
            1100 & 0100 = 0100

        Takes O(1)
        """
        return num & -num

    def print_tree(self):
        """
        Prints a human-readable representation of the tree.
        Each node with Least Significant Bit at Position 1 is printed
        along with all parents.

        Takes O(n)
        """
        for i in range(1, self.size, 2):
            family = []
            while i <= self.size:
                if self._LSB(i) == 1:
                    family.append(f"Child[@{i}]: {self.tree[i]}")
                else:
                    family.append(f"Parent[@{i}]: {self.tree[i]}")
                i += self._LSB(i)
            print(" -> ".join(family))
        return


if __name__ == "__main__":
    pass
