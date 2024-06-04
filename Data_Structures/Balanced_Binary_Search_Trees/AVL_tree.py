class Node:
    """
    Doubly linked node.
    """

    def __init__(self, data):
        self.data = data
        self.height = 0
        # balance factor
        self.bf = 0
        self.left = None
        self.right = None
        self.parent = None


class AVL_tree:
    def __init__(self):
        self.root = None

    def insert(self, node, data):
        """"""
        # case when tree is empty
        if self.root == None:
            self.root = Node(data)
            return

        if node == None:
            return Node(data)

        cmp = self._compare(node, data)

        if cmp == -1:
            node.left = self.insert(node.left, data)
            node.left.parent = node
        elif cmp == 1:
            node.right = self.insert(node.right, data)
            node.right.parent = node
        # case when data already exists in tree
        elif cmp == 0:
            print(f"Data: {data} already exists and will not be added")
            return

        self._update(node)
        return self._balance(node)

    def _update(self, node):
        """
        Updates node height and balance factor..

        Note:
        - node height is the number of edges between
            the node and its furthest leaf.
        - balance factor (bf) is the difference between
            the heights of the left and right subtrees
        """
        # Initialize with -1 for case when node is leaf node
        lh = -1
        rh = -1

        if node.left != None:
            lh = node.left.height
        if node.right != None:
            rh = node.right.height
        node.height = 1 + max(lh, rh)
        node.bf = rh - lh

    def _balance(self, node):
        if node.bf == -2:
            if node.left.bf == -1:
                return self._leftLeftCase(node)
            else:
                return self._leftRightCase(node)
        elif node.bf == 2:
            if node.right.bf == 1:
                return self._rightRightCase(node)
            else:
                return self._rightLeftCase(node)
        return node

    def _leftLeftCase(self, node):
        """
        This case occurs when node has a balance factor of -2
        and the left child node has a balance factor of -1.
        """
        return self._right_rotation(node)

    def _leftRightCase(self, node):
        """
        This case occurs when node has a balance factor of -2
        and the left child node has a balance factor of +1.
        Two operations are performed:
            1. Left rotation is performed which converts the
                left child node's balance factor to -1.
            2. After operation 1, we now have a leftLeftCase, so
                the function is called.
        """
        self._left_rotation(node.left)
        return self._leftLeftCase(node)

    def _rightRightCase(self, node):
        """
        This case occurs when node has a balance factor of +2
        and the left child node has a balance factor of +1.
        """
        return self._left_rotation(node)

    def _rightLeftCase(self, node):
        """
        This case occurs when node has a balance factor of +2
        and the left child node has a balance factor of -1.
        Two operations are performed:
            1. Right rotation is performed which converts the
                left child node's balance factor to +1.
            2. After operation 1, we now have a rightRightCase, so
                the function is called.
        """
        self._right_rotation(node.right)
        return self._rightRightCase(node)

    def _right_rotation(self, node):
        """
        Performs a right rotation.
        The left child is swapped with the
        node and the references are updated accordingly.
        Called right rotation since tree effectively rotates clockwise.
        """
        print("Performing Right Rotation")
        parent = node.parent
        swap_node = node.left

        node.left = swap_node.right
        if swap_node.right != None:
            swap_node.right.parent = node

        node.parent = swap_node
        swap_node.right = node

        swap_node.parent = parent
        if parent != None:
            if parent.left == node:
                parent.left = swap_node
            else:
                parent.right = swap_node

        if node == self.root:
            self.root == swap_node

        self._update(node)
        self._update(swap_node)
        return swap_node

    def _left_rotation(self, node):
        print("Performing Left Rotation")
        parent = node.parent
        swap_node = node.right

        node.right = swap_node.left

        if swap_node.left != None:
            swap_node.left.parent = node

        node.parent = swap_node
        swap_node.left = node

        swap_node.parent = parent
        if parent != None:
            if parent.left == node:
                parent.left = swap_node
            else:
                parent.right = swap_node

        if node == self.root:
            self.root == swap_node

        self._update(node)
        self._update(swap_node)
        return swap_node

    def _compare(self, node, value):
        """
        Comparison function to compare new value to existing nodes.
        """
        if value < node.data:
            return -1
        elif value > node.data:
            return 1
        else:
            return 0

    def preorder(self, node):
        """
        Performs an pre-order traversal of the tree
        Takes O(n)
        """
        if self.root == None:
            print("Tree is empty. Nothing to traverse")
            return
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
        if self.root == None:
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
        if self.root == None:
            print("Tree is empty. Nothing to traverse")
            return
        if node == None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data)


if __name__ == "__main__":
    t = AVL_tree()
    data = [5, 3, 7, 1, 13]
    for i in data:
        t.insert(t.root, i)
    t.insert(t.root, 11)
    """
    Current Tree:
                5
            3       7
        1               13           
    """
    # t.insert(t.root, 5)
    # t.insert(t.root, 3)
    # t.insert(t.root, 7)
    # t.insert(t.root, 1)
    # t.insert(t.root, 13)
    # t.insert(t.root, 65)
    # t.insert(t.root, 0)
    # t.insert(t.root, 10)
    # t.inorder(t.root)

    """
                5
            3       7
        1               13
    0                10     65
    """
