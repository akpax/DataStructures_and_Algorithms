"""
Union Find 
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
        Path compression is performed by each componets parent that we traverse to the
        root element
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
        """
        return self.num_componets

    def connected(self, e1, n2):
        """
        Returns wether or not elements e1 and n2 are in the same componet/set
        """
        return self.find_and_compress(e1) == self.find_and_compress(n2)

    def componetSize(self, element):
        """
        Returns componet size that specified element belongs to
        """
        return self.sz[self.find_and_compress(element)]

    def _parent(self, element):
        """
        Finds parent of element
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
