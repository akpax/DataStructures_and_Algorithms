def selection_sort(values):
    """
    Finds minimum value in values, adds it to sorted,
    and then removes it from values.
    This is repeated until all values are sorted.
    Takes O(n^2)
    """
    sorted = []
    for i in range(len(values)):
        min_index = index_of_min(values)
        sorted.append(values.pop(min_index))
    return sorted


def index_of_min(values):
    """
    Finds index of minimum value in values
    """
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index
