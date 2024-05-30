"""
Fenwick tree implementation. 
Note: The Fenwick tree is 1-based while the user supplied values are zero-based.
The user will interact with the data structure using zero-based indexing.
After the Fenwick tree is initialized with the user-specified values, indexes 
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
        # tree = copy.deepcopy(values)
        # print(tree)
        # for i in range(1, self.size):
        #     j = i + self._LSB(i)
        #     if j <= self.size:
        #         # add child value to parent
        #         # decrease index by 1 since byte integers are 1 based
        #         tree[j - 1] += tree[i - 1]

        # return tree
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
        """
        try:
            # prefix sum of start is exlusive bc we want to include the start
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
        The
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
