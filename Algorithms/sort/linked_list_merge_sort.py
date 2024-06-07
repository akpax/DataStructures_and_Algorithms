from Data_Structures.Singly_and_Doubly_LInkedLists.linked_list import LinkedList


def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    - Recursively divide the linked list into sublists containing a single node
    - Repeatedly merge sublists to produce sorted sublists until one remains

    Returns a sorted linked list
    Runs in O(kn log n)
    """

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists
    Takes O(k log n ) due to list traversal O(k) and splits O(log n)
    """
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
    else:
        mid = linked_list.size() // 2
        mid_node = linked_list.node_at_index(mid - 1)
        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

    return left_half, right_half


def merge(left, right):
    """
    Merges two linked lists, sorting by data in nodes
    Returns a new, merged list
    Takes O(n)
    """

    # Create a new linked list that contains nodes from
    # merging left and right
    merge = LinkedList()
    # add a dummy node to be removed later
    merge.add(0)
    current = merge.head

    left_head = left.head
    right_head = right.head

    # iterate over left and right until we reach tail nodes of both
    while left_head or right_head:
        # case where left head is none, we are past the tail
        # add node from right
        if left_head is None:
            current.next_node = right_head
            right_head = right_head.next_node
        # case where right head is none, we are past tail
        # add node from left
        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node
        # case where not at either tail node,
        # need to compare values,
        else:
            # if left data is smaller, set current to left node
            if left_head.data < right_head.data:
                current.next_node = left_head
                left_head = left_head.next_node
            # if right data is smaller than or equal, set current to right node
            else:
                current.next_node = right_head
                right_head = right_head.next_node
        # move current to next node
        current = current.next_node

    # remove dummy head
    merge_head = merge.head
    merge.head = merge_head.next_node

    return merge
