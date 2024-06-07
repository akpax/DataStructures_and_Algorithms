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
