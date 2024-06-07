"""
Union-Find (Disjoint Set Union) Implementation

The Union-Find data structure, also known as Disjoint Set Union (DSU), is a data structure that keeps track of 
a partition of a set into disjoint (non-overlapping) subsets. It provides efficient methods for union and 
find operations, which are used to merge sets and determine the set membership of an element, respectively.

Key Features:
- Path Compression: Flattens the structure of the tree whenever find is called, making future operations faster.
- Union by Size: Always attaches the smaller tree under the root of the larger tree, keeping the tree balanced.

Path Compression:
Path compression is an optimization technique used in the find operation to make the tree structure flatter,
thus speeding up future operations. When a find operation is executed, it not only returns the root of the element
but also makes each node on the path from the element to the root point directly to the root. This reduces the 
tree's height and ensures that subsequent operations are more efficient.

Key Operations:
- `find_and_compress(element)`: Finds the root of the set containing the element and applies path compression.
- `union(e1, e2)`: Merges the sets containing elements e1 and e2.
- `connected(e1, e2)`: Checks if elements e1 and e2 are in the same set.
- `componentSize(element)`: Returns the size of the set containing the element.
- `number_components()`: Returns the number of disjoint sets.

The implementation below provides these basic operations along with necessary helper methods.

Attributes:
- `size`: The total number of elements in the Union-Find structure.
- `num_components`: The current number of disjoint sets.
- `id`: The array representing the parent of each element.
- `sz`: The array representing the size of each component.
"""


class UnionFind:
    def __init__(self, size):
        self.size = size
        self.num_componets = self.size
        # id[i] is parent of i
        self.id = list(range(self.size))
        # sz[i] is size of each componet (group)
        # each
        self.sz = [1] * self.size

    def find_and_compress(self, element):
        """
        Finds root element of element and performs path compression as well.
        Path compression is performed by each componet's parent that we traverse to the
        root element
        Takes O(⍺(n))
        """
        if self.size == 0:
            print("Union Find is Empty")
            return
        # element does not exist
        if element >= self.size:
            print("Element does not exist. Cannot perform find.")
            return

        if self._parent(element) == element:
            return element
        else:
            root = self.find_and_compress(self._parent(element))
            self._set_parent(element, root)
            return root

    def union(self, e1, n2):
        """
        Finds roots of e1 and n2 and merges the smaller componet into the larger one
        Takes O(⍺(n))
        """
        if e1 >= self.size or n2 >= self.size:
            return

        root1 = self.find_and_compress(e1)
        root2 = self.find_and_compress(n2)
        if root1 == root2:
            return

        if self.sz[root1] > self.sz[root2]:
            self._set_parent(root2, root1)
            self.sz[root1] += self.sz[root2]
        else:
            self._set_parent(root1, root2)
            self.sz[n2] += self.sz[e1]

        self.num_componets -= 1
        return

    def number_componets(self):
        """
        Returns number of componets
        Takes O(1)
        """
        return self.num_componets

    def connected(self, e1, n2):
        """
        Returns wether or not elements e1 and n2 are in the same componet/set
        Takes O(⍺(n))
        """
        return self.find_and_compress(e1) == self.find_and_compress(n2)

    def componetSize(self, element):
        """
        Returns componet size that specified element belongs to
        Takes O(⍺(n))
        """
        return self.sz[self.find_and_compress(element)]

    def _parent(self, element):
        """
        Finds parent of element
        Takes O(1)
        """
        try:
            return self.id[element]
        except IndexError:
            print("Element is not present in Union Find")
            return None

    def _set_parent(self, element, parent):
        """
        Sets parent of element in id array
        """
        self.id[element] = parent

    def print_uf(self):
        """
        Print human readable representation of the data structure
        """
        for i in range(self.size):
            print(
                f"Element: {i} || Parent: {self._parent(i)} || Componet Size: {self.componetSize(i)}"
            )


if __name__ == "__main__":
    uf = UnionFind(5)
    uf.print_uf()
    uf.union(2, 3)
    uf.union(2, 1)

    print(uf.find_and_compress(100))

    print(uf.number_componets())
    uf.print_uf()
