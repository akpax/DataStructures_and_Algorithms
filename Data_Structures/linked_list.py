class Node():
    """
    Object for storing a node of a singly linked list
    """
    data = None
    next_node = None

    def __init__(self,data):
        self.data = data

    def __repr__(self):
        return f"<Node data: {self.data}>"