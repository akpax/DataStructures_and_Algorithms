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
    
class LinkedList():
    """
    Singly Linked list
    """
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def size(self):
        """
        Returns number of nodes in list
        Takes O(n) time
        """
        length = 0
        current = self.head
        while current:
            length +=1
            current = current.next_node
        return length
    
    def add(self,data):
        """
        Adds new node containing data at head of the list
        Takes O(1) time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Returns the first node that has data matching the key
        Rturns
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
    
    def insert(self,data, index):
        """
        Inserts new Node containing data at index, returns False if index not in list
        Insertion takes O(n) time but finding node takes O(n) time
        Therefore, it takes O(n) time
        """
        if index ==0: 
            self.add(data)
        if index>0:
            new = Node(data)
            pos = index
            current = self.head
            while pos>1:
                current = current.next_node
                pos -= 1
                if current is None:
                    return False
            prev_node = current
            next_node = current.next_node
            new.next_node = next_node
            prev_node.next_node = new
    

                    
                    
                    
        
    
    def __repr__(self):
        """
        Returns a string representation of list
        Takes O(n) time
        """
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")

            current = current.next_node
        
        return "->".join(nodes)



