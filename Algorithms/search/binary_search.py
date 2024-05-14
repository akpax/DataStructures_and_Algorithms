def binary_search(input: list, target)->int:
    """
    Returns index position of target if found. else returns None
    Note: This is an iterative solution.
    """
    input.sort() # sort list
    first = 0
    last = len(input) - 1
    while first <= last:
        mid_ind = int((first+last)/2)
        if input[mid_ind] == target:
            return mid_ind
        if input[mid_ind] < target:
            first = mid_ind + 1
        if input[mid_ind] > target:
            last = mid_ind - 1 
    return None
    
if __name__=="__main__":
    input = [1,2,3,4,5,6,7,8,9,10]
    # test algo
    for target in range(1,11):
        assert binary_search(input, target) == target-1
    assert binary_search(input, 12) == None
