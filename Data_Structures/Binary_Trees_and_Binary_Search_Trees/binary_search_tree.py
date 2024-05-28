"""
Binary search tree implemented using the Node class 
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.node_count = 0
        self.root = None

    def insert(self, data):
        """
        Insert a new node into the tree
        Takes O(log n) for average case and O(n) for worst case
        """
        new_node = Node(data)
        if self.node_count == 0:
            self.root = new_node
            self.node_count += 1
            return
        current = self.root
        while current.left != new_node and current.right != new_node:
            # Ignore duplicate values
            if current.data == new_node.data:
                return
            elif new_node.data < current.data:
                if current.left is None:
                    current.left = new_node
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                else:
                    current = current.right

        self.node_count += 1
        return

    def search(self, data):
        """
        Searches tree for a node with data equal to data.
        Returns True if node found and False if not found.
        Takes O(log n) for average case and O(n) for worst case
        """
        if self.node_count == 0:
            print("Tree is empty")
            return
        else:
            current = self.root
            # while loop exits when None node encountered
            while current:
                if data == current.data:
                    print(f"Found node: {data}")
                    return True
                elif data < current.data:
                    current = current.left
                else:
                    current = current.right
            return False

    def remove(self, data):
        """
        Removes node containing data.
        Takes O(log n) for average case and O(n) for worst case
        """
        if self.node_count == 0:
            print("Tree is empty")
            return
        # while loop exits when None node encountered
        current = self.root
        parent = None

        while current:
            if data < current.data:
                parent = current
                current = current.left
            elif data > current.data:
                parent = current
                current = current.right

            else:
                # case where current is leaf node
                if current.left == None and current.right == None:
                    # current is root node
                    if parent == None:
                        self.root = None
                        self.node_count -= 1
                        return
                    else:
                        # find if current node is left or right node of parent
                        if current.data < parent.data:
                            parent.left = None
                        elif current.data > parent.data:
                            parent.right = None
                        current = None
                        self.node_count -= 1
                        return
                # case where left node has value but right node empty
                elif current.left != None and current.right == None:
                    # current is root node
                    if parent == None:
                        self.root = current.left
                    else:
                        parent.left = current.left
                    current = None
                    self.node_count -= 1
                    return
                # case where left node is empty but right node has value
                elif current.left == None and current.right != None:
                    if parent == None:
                        self.root = current.right
                    else:
                        parent.right = current.right
                    current = None
                    self.node_count -= 1
                    return
                # case where left and right nodes of current have values
                else:
                    del_node, del_parent_node = self.dig_left(current.left)
                    # swap data with current node and left largest node
                    current.data = del_node.data
                    # case when deleted node is child node of parent
                    if del_node.data == del_parent_node.data:
                        current.left = del_node.left
                        self.node_count -= 1
                        return
                    # case when deleted node left child has node
                    elif del_node.left != None:
                        del_parent_node.right = del_node.left
                        self.node_count -= 1
                        return
                    # case when deleted node left is None
                    else:
                        del_parent_node.right = None
                        self.node_count -= 1
                        return
        print("Node not found")

    def dig_left(self, node):
        """
        Finds the largest value in the left subtree.
        Returns largest node and it's parent node
        """
        parent = node
        current = node
        while current.right != None:
            parent = current
            current = current.right
        return current, parent

    def preorder(self, node):
        """
        Performs an pre-order traversal of the tree
        Takes O(n)
        """
        if node == None:
            return
        print(node.data)
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):
        """
        Performs an in-order traversal of the tree
        A unique property of binary trees is that an in-order traversal
        returns nodes in order
        Takes O(n)
        """
        if self.node_count == 0:
            print("Tree is empty. Nothing to traverse")
            return
        if node == None:
            return
        self.inorder(node.left)
        print(node.data)
        self.inorder(node.right)

    def postorder(self, node):
        """
        Performs post-order traversal of the tree
        Takes O(n)
        """
        if node == None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data)


if __name__ == "__main__":
    my_bst = BinarySearchTree()
    my_bst.insert(5)
    my_bst.insert(3)
    my_bst.insert(7)
    my_bst.insert(1)
    my_bst.insert(13)
    my_bst.insert(65)
    my_bst.insert(0)
    my_bst.insert(10)

    """
                5
            3       7
        1               13
    0                10     65
    """
    (my_bst.remove(13))
    """
                5
            3       7
        1               65
    0                10
    """
    my_bst.remove(5)
    """
                7
            3       65
        1        10
    0
    """
    my_bst.remove(3)
    """
                7
            1       65
        0        10
    """
    my_bst.remove(7)
    """
                10
            1       65
        0
    """
    my_bst.remove(1)
    """
                10
            0       65

    """
    my_bst.remove(0)
    """
                10
                    65

    """
    my_bst.remove(10)
    """
            65

    """
    my_bst.remove(65)
    """

    """

    my_bst.insert(10)
    """
            10

    # """

    my_bst.inorder(my_bst.root)
