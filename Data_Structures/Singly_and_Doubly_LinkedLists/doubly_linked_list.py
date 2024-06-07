"""
Doubly Linked List Implementation

A doubly linked list is a type of linked list where each node contains a data part and two pointers, 
one pointing to the next node and one pointing to the previous node. This allows traversal of the list 
in both directions.  
This implementation has references to the head and the tail which allows for constant time appending
and prepending.

Key Operations:
- `append(data)`: Adds an element to the end of the list.
- `prepend(data)`: Adds an element to the beginning of the list.
- `insert(position, data)`: Inserts an element at the specified position.
- `delete_by_value(data)`: Deletes the first occurrence of the specified value.
- `delete_by_position(position)`: Deletes the element at the specified position.
- `is_empty()`: Checks if the list is empty.
- `__repr__()`: Returns a string representation of the list.

"""


class Node:
    """
    Object for storing a node of a doubly linked list
    """

    data = None
    next_node = None
    previous_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"<Node data: {self.data}>"


class DoublyLinkedList:
    """
    Singly Linked list
    """

    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def is_empty(self):
        """
        Checks if the list is empty.
        Returns True if the list is empty, otherwise False.
        Takes O(1).
        """
        return self.head == None

    def append(self, data):
        """
        Appends a new node with the given data to the end of the list.
        Takes O(1).
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
            return
        else:
            new_node.previous_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node
            self.length += 1
            return

    def prepend(self, data):
        """
        Prepends a new node with the given data to the beginning of the list.
        Takes O(1).
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
            return
        else:
            new_node.next_node = self.head
            self.head.previous_node = new_node
            self.head = new_node
            self.length += 1
            return

    def insert(self, position, data):
        """
        Inserts a new node with the given data at the specified position.
        If the position is 0, prepends the data.
        If the position is greater than or equal to the length of the list, appends the data.
        Takes O(n).
        """
        if position == 0:
            self.prepend(data)
            return
        if position >= self.length:
            self.append(data)
            return
        else:
            new_node = Node(data)
            current = self.head
            # traverse until insertion position is reached
            for i in range(0, position - 1):
                current = current.next_node
            # Make previous of new node point to current
            new_node.previous_node = current
            # make next of new node point to the next node of current node
            new_node.next_node = current.next_node
            # make current node's next node point to the new node
            current.next_node = new_node
            # make the previous_node of the node ahead of the new node point back to the new node
            new_node.next_node.previous_node = new_node
            self.length += 1
            return

    def delete_by_value(self, data):
        """
        Deletes the first node with the specified data.
        Takes O(n).
        """
        if self.head == None:
            print("head is empty. Nothing to delete")
            return
        current = self.head
        if current.data == data:
            self.head = current.next_node
            if self.head is None or self.head.next_node is None:
                self.tail = self.head
            if self.head != None:
                self.head.previous_node = None
            return
        try:
            # exit while loop when current is the node before the node containing the data
            while current.next_node.data != data:  # and current.next_node != None:
                current = current.next_node
            if current != None:
                # remove next_node
                current.next_node = current.next_node.next_node
                if current.next_node != None:
                    current.next_node.previous_node = current
                else:
                    self.tail = current
                self.length -= 1
            return
        except AttributeError:
            print("Given value not found")
            return

    def delete_by_position(self, position):
        """
        Deletes the node at the specified position.
        Takes O(n).
        """
        if self.head is None:
            print("Linked List empty. Nothing to delete")
            return
        if position == 0:
            self.head = self.head.next_node
            if self.head is None or self.head.next_node is None:
                self.tail = self.head
            if self.head != None:
                self.head.previous_node = None
            return

        if position >= self.length:
            position = self.length - 1

        current = self.head
        # advance to node just before the position
        for _ in range(0, position - 1):
            current = current.next_node
        current.next_node = current.next_node.next_node
        if current.next_node != None:
            current.next_node.previous_node = current
        else:
            self.tail = current
        self.length(-1)

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
            elif current is self.tail:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")

            current = current.next_node

        return "-> <-".join(nodes)


if __name__ == "__main__":
    d = DoublyLinkedList()
    print(d)
    d.prepend(2)
    d.prepend(20)
    d.prepend(222)
    print(d)
    d.delete_by_position(0)
    print(d)
