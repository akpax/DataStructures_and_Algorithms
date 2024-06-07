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
