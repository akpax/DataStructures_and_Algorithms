"""
Stack Implementation

This stack is implemented using a dynamic array. Stacks can also be implemented using linked lists. 
In Python, the built-in list methods `pop()` and `append()` function as the pop and push operations for stacks, respectively.
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
        Appends data to the top of the stack (self.array[-1])
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
        This method prints the stack starting from the top
        Takes O(n)
        """
        for i in range(len(self.array) - 1, -1, -1):
            print(f"[{self.array[i]}]")
        return
