def quicksort(values):
    """
    Recursively picks first value in list as pivot then sorts into
    less than and greater than sub-lists. Base case is reached when
    list length is 1 or 0. Then sub-lists are re-merged in order.
    Best Case (when pivot is at midpoint): Takes O(n log n)
    Worst Case (pivot reduces list by 1): Takes O(n^2)
    """
    # base case
    if len(values) <= 1:
        return values
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    # recursive case
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)
