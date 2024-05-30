"""
Hash table implemented using open addressing to handle hash collisions. 
In this implementation, we use linear probing to implement open addressing.
We will use P(x) = x for the linear probing to prevent cycles. 
However, other methods to implement open addressing include:
double hashing, quadratic probing, and pseudo random number generation.
"""


class Tombstone:
    """
    Dummy object to represent a deleted key in the hash table
    """

    def __init__(self):
        pass


class HashTableLinearProbe:
    def __init__(self, size, max_capacity=0.75):
        self.size = size
        # empty slots include null slots only and do not include tombstones
        self.empty_slots = self.size
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.max_capacity = max_capacity

    def _hash(self, key):
        """
        Hashes key and returns hash value.
        Uses self.size which is adjusted in _increase_size()
        function to dynamically increase the hash table capacity.

        Takes O(1)
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
        hash = self._hash(key)
        # convert key, value to str if not str already
        if not isinstance(key, str):
            key = str(key)
        if not isinstance(value, str):
            value = str(value)
        x = 0
        # store tombstone index as t
        T = None
        while True:
            i = (hash + x) % self.size
            # saves index of first Tombstone
            if isinstance(self.keys[i], Tombstone) and T == None:
                T = i

            # key already exists in the table
            if self.keys[i] == key:
                # If there is a first tombstone index, replace the key and updated value
                # put tombstone in previous key location
                # this will require less probing for future lookup
                if T:
                    self.keys[T] = key
                    self.values[T] = value
                    self.keys[i] = Tombstone()
                    self.values[i] = None
                    self.empty_slots -= 1
                    self._check_capacity()
                    return
                else:
                    self.values[i] = value
                    return
            # Either on null value or hit a tombstone
            elif self.keys[i] is None or isinstance(self.keys[i], Tombstone):
                if T != None:
                    self.keys[T] = key
                    self.values[T] = value
                else:
                    self.keys[i] = key
                    self.values[i] = value
                    self.empty_slots -= 1
                    self._check_capacity()
                return
            x += 1

    def get(self, key):
        """
        Gets the value corresponding to the specified key.
        If the key is not present in the hash table, null is returned.

        Takes O(1) on average and O(n) for worst case.
        Note: average case only true if you have a good uniform hash function.
        """
        hash = self._hash(key)
        x = 0
        # store tombstone index as t
        T = None
        while True:
            i = (hash + x) % self.size
            if isinstance(self.keys[i], Tombstone) and T == None:
                T = i
            if self.keys[i] == key:
                # case when first Tombstone is encountered
                if T:
                    # swap k,v into first Tombstone position
                    self.keys[T] = self.keys[i]
                    self.values[T] = self.values[i]
                    # Open slots in previous k,v position
                    self.keys[i] = None
                    self.values[i] = None
                    return self.values[T]
                else:
                    return self.values[i]
            if self.keys[i] == None:
                print("Key is not present in Hash Table")
                return
            x += 1

    def remove(self, key):
        """
        Removes key, value pair and returns the corresponding value if present.
        Key is replaced with Tombstone object and value is set to None.

        Takes O(1) on average and O(n) for worst case.
        Note: average case only true if you have a good uniform hash function.
        """
        hash = self._hash(key)
        x = 0
        while True:
            i = (hash + x) % self.size
            if self.keys[i] == key:
                self.keys[i] = Tombstone()
                deleted_value = self.values[i]
                self.values[i] = None
                return deleted_value

            if self.keys[i] == None:
                print("Key is not present in Hash Table")
                return

            x += 1

    def get_keys(self):
        """
        Returns all non-null and non-Tombstone keys in the hash table

        Takes O(n) time
        """
        keys_array = []
        for key in self.keys:
            if key != None and not isinstance(key, Tombstone):
                keys_array.append(key)
        return keys_array

    def get_values(self):
        """
        Returns all non-null values in the hash table

        Takes O(n) time
        """
        values_array = []
        for value in self.values:
            if value != None:
                values_array.append(value)
        return values_array

    def _increase_size(self, resize_factor):
        """
        Increases the size of the hash table by extracting all k,v pairs,
        reinitializes keys and values arrays with null values incorporating
        new size factor, then sets the entries into the new hash table.

        Takes O(n) time
        """
        kv_pairs = zip(self.get_keys(), self.get_values())
        self.size *= resize_factor
        self.empty_slots = self.size
        self.keys = [None] * self.size
        self.values = [None] * self.size
        for pair in kv_pairs:
            self.set(*pair)
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
    h = HashTableLinearProbe(10)
    h.set("apple", "big")
    h.set("apple", "small")
    h.set("55", "numbers")
    h.set("j", "characters")
    h.remove("j")
    h.set("tall", "short")
    h.set("43434", 12123123)
    h.set("target", "amazon")
    h.set("target12", "amazon12")
    h.remove("apple")
    h.set("target212", "amazon22")
    h.set("purple goatee", "characters")
    h.set("tall1", "short")
    h.set("434341", 12123123)
    h.remove("purple goatee")
    print(h.get_keys())
    print(h.get_values())
