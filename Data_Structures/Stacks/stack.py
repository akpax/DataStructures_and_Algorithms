"""
Stack implemented using array. It can be implemented using linked lists as well
Python has pop() and append() methods which function as pop and push for lists.
"""


class Stack:
    def __init__(self):
        self.array = []

    def is_empty(self):
        return len(self.array) == 0

    def peek(self):
        """
        Views last element of the array
        Takes O(1)
        """
        return self.array[-1]

    def push(self, data):
        """
        Appends data to the top of the stack
        Takes O(1)
        """
        self.array.append(data)
        return

    def pop(self):
        """
        Pops off top element of stack and returns this element
        Takes O(1)
        """
        if self.is_empty():
            print("Stack is empty. Nothing left to pop")
            return
        else:
            return self.array.pop()

    def search(self, data):
        """
        This method searches for the data. Returns True if found and False if not.
        Takes O(n)
        """
        for i in range(len(self.array) - 1, -1, -1):
            if self.array[i] == data:
                return True
        return False

    def print_stack(self):
        """
        This operation prints the stack starting from the top
        Takes O(n)
        """
        for i in range(len(self.array) - 1, -1, -1):
            print(f"[{self.array[i]}]")
        return
