"""
Suffix Array Implementation

A suffix array is a data structure that provides a sorted array of all suffixes of a given string. It is widely 
used in various string processing applications such as pattern matching, data compression, and bioinformatics.

Key Features:
- Constructs the suffix array by generating all suffixes of the string and sorting them.
- Provides an efficient way to handle and manipulate suffixes for various applications.

How it works:
- The suffix array is constructed by creating all possible suffixes of the input string.
- These suffixes are then sorted lexicographically.
- The suffix array stores the starting indices of these sorted suffixes.

Key Operations:
- `construct()`: Constructs the suffix array by generating and sorting all suffixes of the input string.

Attributes:
- `string`: The original string for which the suffix array is constructed.
- `array`: The constructed suffix array, which contains the starting indices of the sorted suffixes.
"""

import copy


class SuffixArray:
    def __init__(self, string):
        self.string = string
        self.array = self.construct()

    def construct(self):
        array = []
        string = copy.deepcopy(self.string)
        for i in range(len(string)):
            array.append((string[i:], i))
        array.sort()
        indices = [suffix[1] for suffix in array]
        return indices


if __name__ == "__main__":
    s = SuffixArray("howdy")
    print(s.array)
