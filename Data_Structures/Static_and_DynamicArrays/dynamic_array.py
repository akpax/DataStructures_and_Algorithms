"""
Dynamic and Static Arrays

A static array has a fixed size and cannot be resized. It requires the size to be known at the time of creation. 
Memory is allocated at the time of array creation, and operations like insertion and deletion require shifting elements, 
which can be inefficient. Static arrays offer fast access times (O(1)) for reading and writing elements by index.

A dynamic array, on the other hand, does not have a fixed size and can grow or shrink as needed. 
It typically starts with a small size and automatically resizes itself when it becomes full. 
Resizing usually involves allocating a new array of double the current size and copying elements over. 
Dynamic arrays offer amortized O(1) time complexity for appending elements, though individual resizes take O(n) time. 
Access times remain O(1), similar to static arrays, but they provide the flexibility to handle varying amounts of data efficiently.
"""


class DynamicArray:
    def __init__(self):
        self.arr = [None]
        self.count = 0  # number elements in array
        self.size = 1  # actual array size

    def _resize(self):
        """
        Doubles size of array and copies elements into new array\
        Takes O(n)
        """
        self.size *= 2  # double current array size
        new_array = [None] * self.size
        for i, item in enumerate(self.arr):
            new_array[i] = item
        self.arr = new_array

    def append(self, new_item):
        """
        Appends a new item to the end of the array. Resizes if array is full.
        Takes O(1)
        """
        if self.count == self.size:
            self._resize()
        self.arr[self.count] = new_item
        self.count += 1

    def search(self, item):
        """
        Returns index of first occurence of item, else returns None
        Takes O(n)
        """
        current = 0
        while current <= self.count:
            if self.arr[current] == item:
                return current
            current += 1
        return None

    def deleteAt(self, index):
        """
        Delete element at index, if index larger than list return False
        Takes O(n)
        """
        if index > self.count:
            return False
        new_array = [None] * self.size
        current = 0
        self.count = self.count - 1  # adjust count for deletion
        while current < self.count:
            if current < index:
                new_array[current] = self.arr[current]
            else:
                new_array[current] = self.arr[current + 1]
            current += 1
        self.arr = new_array

    def insertAt(self, index, value):
        """
        Inserts value at specified index. Returns False if index not in array
        Takes O(n)
        """
        if index == self.count:
            return self.append()
        if index > self.count:
            return False
        # update count for new element
        self.count += 1
        # resize if necessary
        if self.count > self.size:
            self.size *= (
                2  # do not use resize func bc we will use New array to insert into
            )
        new_array = [None] * self.size
        current = 0
        while current < self.count:
            if current < index:
                new_array[current] = self.arr[current]
            elif current == index:
                new_array[current] = value
            else:
                new_array[current] = self.arr[current - 1]
            current += 1
        self.arr = new_array

    def __repr__(self):
        return f"{self.arr}"


if __name__ == "__main__":
    pass
