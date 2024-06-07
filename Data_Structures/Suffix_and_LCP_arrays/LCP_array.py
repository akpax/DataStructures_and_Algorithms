"""
Longest Common Prefix (LCP) Array Implementation

The Longest Common Prefix (LCP) array is a data structure used in conjunction with the suffix array to efficiently 
solve various string processing problems. The LCP array stores the lengths of the longest common prefixes between 
consecutive suffixes in the sorted suffix array.

Key Features:
- Efficiently constructs the LCP array based on the given suffix array and the original string.
- Supports various applications such as pattern matching, finding the longest repeated substring, and more.

How it works:
- The LCP array is built by comparing each suffix with the previous one in the sorted suffix array.
- The LCP array stores the length of the longest common prefix between each pair of consecutive suffixes.

Key Operations:
- `construct()`: Constructs the LCP array by comparing each suffix with the previous one in the sorted suffix array.
- `_recreate_suffixes()`: Recreates the suffixes from the original string based on the suffix array.

Attributes:
- `suffix_array`: The suffix array of the original string.
- `string`: The original string for which the LCP array is constructed.
- `array`: The constructed LCP array.

"""

from suffix_array import SuffixArray


class LCParray:
    def __init__(self, suffix_array, string):
        self.suffix_array = suffix_array
        self.string = string
        self.array = self.construct()

    def construct(self):
        suffixes = self._recreate_suffixes()
        LCP = []
        prev_suffix = " "
        for suffix in suffixes:
            match_count = 0
            for i in range(1, len(suffix)):
                if suffix[:i] == prev_suffix[:i]:
                    match_count += 1
                else:
                    break
            LCP.append(match_count)
            prev_suffix = suffix
        return LCP

    def _recreate_suffixes(self):
        suffixes = []
        for i in range(len(self.suffix_array)):
            suffixes.append(self.string[self.suffix_array[i] :])
        return suffixes


if __name__ == "__main__":
    s = SuffixArray("ABABBBAA")
    print(s.array, s.string)
    l = LCParray(s.array, s.string)
    print(l.array)
    print(l._recreate_suffixes())
    print(l.suffix_array)
