import random


def is_sorted(list):
    """
    Checks if list is sorted in ascending order.
    Takes O(n) time
    """
    for i in range(1, len(list)):
        if list[i] < list[i - 1]:
            return False
    return True


def bogo_sort(list):
    """
    Randomly shuffles a list until sorted.
    Example of bad algorithm. Does not make progress
    It will keep shuffling despite having nearly all items matching except one.
    """
    while not is_sorted(list):
        random.shuffle(list)
    return list
