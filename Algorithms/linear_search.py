def linear_search(input: list, target: int)->int:
    """
    Returns index position of target if found. else returns None
    """
    for i,item in enumerate(input):
        if item == target:
            return i
    return None


if __name__=="__main__":
    test_list = [1,2,3,4,5,6,7,8]
    print(linear_search(test_list, 4))
    print(linear_search(test_list, 10))
    