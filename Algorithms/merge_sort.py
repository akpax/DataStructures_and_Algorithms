def merge_sort(list):
    """
    Sorts a list in ascending order

    Divide: Find midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in the previous step
    Combine: Merge the sorted sublists created in the previous step

    Takes O(n log n) time, in python this takes O(kn log n) due to O(k) slicing in split func
    """
    # stopping condition
    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right)


def split(list):
    """
    Divide the unsorted lists at midpoint into sublists
    Returns two sublists - left and right

    Takes overall O(log n) time, in python this takes O(k log n )
    """
    midpoint = len(list) // 2
    # slicing operation has runtime O(k)
    return list[:midpoint], list[midpoint:]


def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list

    Takes overall O(n) time
    """
    l = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    # case when left longer than right
    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l


def verify_sort(list):
    # if list is 0,1 long it is naively sorted
    if len(list) <= 1:
        return True
    return list[0] <= list[1] and verify_sort(list[1:])


if __name__ == "__main__":
    l = [54, 23, 4, 3, 1, 6, 7, 3, 4, 523]
    sorted_l = merge_sort(l)
    print(verify_sort(l))
    print(verify_sort(sorted_l))
