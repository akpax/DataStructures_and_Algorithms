def recursive_binary_search(input: list, target: int) -> int:
    """
    Returns true if target in input, else false
    """
    input.sort()
    if len(input) == 0:
        return False
    else:
        midpoint = len(input)//2
        if input[midpoint] == target:
            return True
        if input[midpoint] < target:
            return recursive_binary_search(input[midpoint+1:],target)
        else:
            return recursive_binary_search(input[:midpoint],target)
    
if __name__=="__main__":
    input = [1,2,3,4,5,6,7,8,9,10]
    # test algo
    print(recursive_binary_search(input, 4))
    print(recursive_binary_search(input, 11))