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
