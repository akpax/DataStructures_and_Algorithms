"""
Hash table implemented using separate chaining to handle hash collisions. 
In this implementation, we use an array, but some implementations use one or a mixture of
binary trees, arrays, linked lists, self-balancing trees, etc.
"""


class HashTable:
    def __init__(self, size, max_capacity=0.75):
        self.size = size
        self.empty_slots = self.size
        self.data = [None] * self.size
        self.max_capacity = max_capacity

    def _hash(self, key):
        """
        Hashes key and returns hash value.
        Uses self.size which is adjusted in _increase_size()
        function to dynamically increase the hash table capacity.
        """
        key = str(key)
        char_sum = 0
        for char in key:
            char_sum += ord(char)
        return char_sum % self.size

    def set(self, key, value):
        """
        This function sets a new key value pair into the hash table.
        After the new entry is added, the capacity is checked and resized
        if necessary.  If a key already exists, the value will be updated
        with the specified value.

        Takes O(1) on average and O(n) for worst case.
        Note: average case only true if you have a good uniform hash function.
        """
        new_entry = {"key": key, "value": value}
        hash = self._hash(key)
        print(f"{key}, {hash}")
        if self.data[hash]:
            for entry in self.data[hash]:
                # check if key is already in table
                if entry["key"] == key:
                    # update value if allready in table
                    entry["value"] = value
                    return
            # if key not in table create new entry and append to array
            self.data[hash].append(new_entry)
        # case when hash is None
        else:
            # initialize array to store and entries and add entry
            self.data[hash] = [new_entry]
            self.empty_slots -= 1
            # checks max capacity not exceed and resizes if necessary
            self._check_capacity()

    def get(self, key):
        """
        Gets the value corresponding to the specified key.
        If the key is not present in the hash table, null is returned.

        Takes O(1) on average and O(n) for worst case.
        Note: average case only true if you have a good uniform hash function.
        """
        hash = self._hash(key)
        if self.data[hash]:
            for entry in self.data[hash]:
                # check if key is already in table
                if entry["key"] == key:
                    return entry["value"]
        print(f"Key: {key} not found in hash table")
        return

    def remove(self, key):
        """
        Removes and returns the specified key if present
        Takes O(1) on average and O(n) for worst case.
        Note: average case only true if you have a good uniform hash function.
        """
        hash = self._hash(key)
        if self.data[hash]:
            for i, entry in enumerate(self.data[hash]):
                # check if key is already in table
                if entry["key"] == key:
                    # increase empty slots if array contains one entry
                    if i == 0:
                        self.empty_slots += 1
                    return self.data[hash].pop(i)
        print(f"Key: {key} not found in hash table")
        return

    def keys(self):
        """
        Returns all keys in the hash table
        Takes O(n) time
        """
        keys_array = []
        for i in range(self.size):
            if self.data[i]:
                for entry in self.data[i]:
                    keys_array.append(entry["key"])
        return keys_array

    def values(self):
        """
        Returns all values in the hash table
        Takes O(n) time
        """
        values_array = []
        for i in range(self.size):
            if self.data[i]:
                for entry in self.data[i]:
                    values_array.append(entry["value"])
        return values_array

    def _get_entries(self):
        """
        Private function to pull all entries from the hash table for resize
        Takes O(n) time
        """
        entries_array = []
        for i in range(self.size):
            if self.data[i]:
                for entry in self.data[i]:
                    entries_array.append(entry)
        return entries_array

    def _increase_size(self, resize_factor):
        """
        Increases the size of the hash table by extracting all entries,
        creates a new empty hash table and resets global variables, then
        sets the entries into the new hash table.
        Takes O(n) time
        """
        entries = self._get_entries()
        self.size *= resize_factor
        self.empty_slots = self.size
        self.data = [None] * self.size
        for entry in entries:
            self.set(**entry)
        return

    def _check_capacity(self):
        """
        Checks that current hash table capacity (slot filled)
        is less than the maximum capacity.
        If maximum capacity is exceeded, the hash table is resized
        """
        current_capacity = 1 - self.empty_slots / self.size
        if current_capacity >= self.max_capacity:
            print("Capacity exceeded. Increasing Hash Table size by factor of 10")
            self._increase_size(10)


if __name__ == "__main__":
    h = HashTable(5)
    h.set("apple", "big")
    h.set("tod", "small")
    h.set("55", "numbers")
    h.set("j", "characters")
    h.set("purple goatee", "characters")
    print(h.remove("55"))
    print(h.data)
    h.set("j", "people")
    print(h.data)
