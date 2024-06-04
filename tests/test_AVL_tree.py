import pytest

from ..Data_Structures.Balanced_Binary_Search_Trees.AVL_tree import AVL_tree


@pytest.fixture(scope="class")
def avl_tree_fixture():
    t = AVL_tree()
    yield t


class Test_AVL_tree:
    def test_insertion_no_rotation(self, avl_tree_fixture):
        """
        Test insertion before rotations are performed
        Ensures that balance factors, parent and child references, and heights are updated correctly

                    5
                3       7
            1               13
        """

        avl_tree_fixture.insert(avl_tree_fixture.root, 5)
        """
        Current Tree:
                    5          
        """
        assert avl_tree_fixture.root.data == 5

        avl_tree_fixture.insert(avl_tree_fixture.root, 3)
        """
        Current Tree:
                    5
                3                
        """
        assert avl_tree_fixture.root.left.data == 3
        assert avl_tree_fixture.root.left.parent == avl_tree_fixture.root

        avl_tree_fixture.insert(avl_tree_fixture.root, 7)
        """
        Current Tree:
                    5
                3       7         
        """
        assert avl_tree_fixture.root.right.data == 7
        assert avl_tree_fixture.root.right.parent == avl_tree_fixture.root

        avl_tree_fixture.insert(avl_tree_fixture.root, 1)
        """
        Current Tree:
                    5
                3       7
            1                       
        """
        assert avl_tree_fixture.root.left.left.data == 1
        assert avl_tree_fixture.root.left.left.parent == avl_tree_fixture.root.left

        avl_tree_fixture.insert(avl_tree_fixture.root, 13)
        """
        Current Tree:
                    5
                3       7
            1               13           
        """
        assert avl_tree_fixture.root.right.right.data == 13
        assert avl_tree_fixture.root.right.right.parent == avl_tree_fixture.root.right

        # check balance factors of resulting tree
        assert avl_tree_fixture.root.bf == 0
        assert avl_tree_fixture.root.left.bf == -1
        assert avl_tree_fixture.root.left.left.bf == 0
        assert avl_tree_fixture.root.right.bf == 1
        assert avl_tree_fixture.root.right.right.bf == 0

        # check height of resulting tree
        assert avl_tree_fixture.root.height == 2
        assert avl_tree_fixture.root.left.height == 1
        assert avl_tree_fixture.root.left.left.height == 0
        assert avl_tree_fixture.root.right.height == 1
        assert avl_tree_fixture.root.right.right.height == 0

    def test_insertion_w_rotation_rightRightCase(self, avl_tree_fixture):
        # rebuild tree such that it resembles tree below
        avl_tree_fixture.root = None
        data = [5, 3, 7, 1, 13]
        for i in data:
            avl_tree_fixture.insert(avl_tree_fixture.root, i)
        """
        Current Tree:
                    5
                3       7
            1               13           
        """

        avl_tree_fixture.insert(avl_tree_fixture.root, 65)
        """
        Tree Pre-Rebalance:                          Tree Post-Rebalance:
                    5                                      5
                3       7                               3     13
            1               13                      1       7    65
                                65           
        """
        # assert data is correct
        assert avl_tree_fixture.root.data == 5
        assert avl_tree_fixture.root.right.data == 13
        assert avl_tree_fixture.root.right.right.data == 65
        assert avl_tree_fixture.root.right.left.data == 7
        assert avl_tree_fixture.root.left.data == 3
        assert avl_tree_fixture.root.left.left.data == 1

        # assert balancing factors are correct for manipulated nodes
        assert avl_tree_fixture.root.bf == 0
        assert avl_tree_fixture.root.right.bf == 0
        assert avl_tree_fixture.root.right.left.bf == 0
        assert avl_tree_fixture.root.right.right.bf == 0

        # assert heights are correct for manipulated nodes
        assert avl_tree_fixture.root.height == 2
        assert avl_tree_fixture.root.right.height == 1
        assert avl_tree_fixture.root.right.left.height == 0
        assert avl_tree_fixture.root.right.right.height == 0

        # assert parent references are correct
        assert avl_tree_fixture.root.right.right.parent == avl_tree_fixture.root.right
        assert avl_tree_fixture.root.right.left.parent == avl_tree_fixture.root.right
        assert avl_tree_fixture.root.right.parent == avl_tree_fixture.root

    def test_insertion_w_rotation_rightLeftCase(self, avl_tree_fixture):
        # rebuild tree such that it resembles tree below
        avl_tree_fixture.root = None
        data = [5, 3, 7, 1, 13]
        for i in data:
            avl_tree_fixture.insert(avl_tree_fixture.root, i)
        """
        Current Tree:
                    5
                3       7
            1               13           
        """

        avl_tree_fixture.insert(avl_tree_fixture.root, 11)
        """
        Tree Pre-Rebalance:                          Tree Post-Rebalance:
                    5                                      5
                3       7                               3      11
            1               13                      1       7     13
                        11           
        """
        # assert data is correct
        assert avl_tree_fixture.root.data == 5
        assert avl_tree_fixture.root.right.data == 11
        assert avl_tree_fixture.root.right.right.data == 13
        assert avl_tree_fixture.root.right.left.data == 7
        assert avl_tree_fixture.root.left.data == 3
        assert avl_tree_fixture.root.left.left.data == 1

        # assert balancing factors are correct for manipulated nodes
        assert avl_tree_fixture.root.bf == 0
        assert avl_tree_fixture.root.right.bf == 0
        assert avl_tree_fixture.root.right.left.bf == 0
        assert avl_tree_fixture.root.right.right.bf == 0

        # assert heights are correct for manipulated nodes
        assert avl_tree_fixture.root.height == 2
        assert avl_tree_fixture.root.right.height == 1
        assert avl_tree_fixture.root.right.left.height == 0
        assert avl_tree_fixture.root.right.right.height == 0

        # assert parent references are correct
        assert avl_tree_fixture.root.right.right.parent == avl_tree_fixture.root.right
        assert avl_tree_fixture.root.right.left.parent == avl_tree_fixture.root.right
        assert avl_tree_fixture.root.right.parent == avl_tree_fixture.root

    def test_insertion_w_rotation_leftLeftCase(self, avl_tree_fixture):
        # rebuild tree such that it resembles tree below
        avl_tree_fixture.root = None
        data = [5, 4, 7, 3, 13]
        for i in data:
            avl_tree_fixture.insert(avl_tree_fixture.root, i)
        """
        Current Tree:
                    5
                4       7
            3               13           
        """

        avl_tree_fixture.insert(avl_tree_fixture.root, 2)
        """
        Tree Pre-Rebalance:                          Tree Post-Rebalance:
                    5                                       5
                4       7                               3      11
            3               13                       2    4       13
        2                           
        """
        # assert data is correct
        assert avl_tree_fixture.root.data == 5
        assert avl_tree_fixture.root.right.data == 7
        assert avl_tree_fixture.root.right.right.data == 13
        assert avl_tree_fixture.root.left.data == 3
        assert avl_tree_fixture.root.left.left.data == 2
        assert avl_tree_fixture.root.left.right.data == 4

        # assert balancing factors are correct for manipulated nodes
        assert avl_tree_fixture.root.bf == 0
        assert avl_tree_fixture.root.left.bf == 0
        assert avl_tree_fixture.root.left.left.bf == 0
        assert avl_tree_fixture.root.left.right.bf == 0

        # assert heights are correct for manipulated nodes
        assert avl_tree_fixture.root.height == 2
        assert avl_tree_fixture.root.left.height == 1
        assert avl_tree_fixture.root.left.left.height == 0
        assert avl_tree_fixture.root.left.right.height == 0

        # assert parent references are correct
        assert avl_tree_fixture.root.left.left.parent == avl_tree_fixture.root.left
        assert avl_tree_fixture.root.left.right.parent == avl_tree_fixture.root.left
        assert avl_tree_fixture.root.left.parent == avl_tree_fixture.root

    def test_insertion_w_rotation_leftRightCase(self, avl_tree_fixture):
        # rebuild tree such that it resembles tree below
        avl_tree_fixture.root = None
        data = [7, 5, 8, 3, 13]
        for i in data:
            avl_tree_fixture.insert(avl_tree_fixture.root, i)
        """
        Current Tree:
                    7
                5       8
            3               13           
        """

        avl_tree_fixture.insert(avl_tree_fixture.root, 4)
        """
        Tree Pre-Rebalance:                          Tree Post-Rebalance:
                    7                                       7
                5       8                               4      8
            3               13                       3     5       13
                4                       
        """
        # assert data is correct
        assert avl_tree_fixture.root.data == 7
        assert avl_tree_fixture.root.right.data == 8
        assert avl_tree_fixture.root.right.right.data == 13
        assert avl_tree_fixture.root.left.data == 4
        assert avl_tree_fixture.root.left.left.data == 3
        assert avl_tree_fixture.root.left.right.data == 5

        # assert balancing factors are correct for manipulated nodes
        assert avl_tree_fixture.root.bf == 0
        assert avl_tree_fixture.root.left.bf == 0
        assert avl_tree_fixture.root.left.left.bf == 0
        assert avl_tree_fixture.root.left.right.bf == 0

        # assert heights are correct for manipulated nodes
        assert avl_tree_fixture.root.height == 2
        assert avl_tree_fixture.root.left.height == 1
        assert avl_tree_fixture.root.left.left.height == 0
        assert avl_tree_fixture.root.left.right.height == 0

        # assert parent references are correct
        assert avl_tree_fixture.root.left.left.parent == avl_tree_fixture.root.left
        assert avl_tree_fixture.root.left.right.parent == avl_tree_fixture.root.left
        assert avl_tree_fixture.root.left.parent == avl_tree_fixture.root

    def test_removal_left_leaf_node_case_no_rebalance(self, avl_tree_fixture):
        # rebuild tree such that it resembles tree below
        avl_tree_fixture.root = None
        data = [7, 5, 8, 3, 13]
        for i in data:
            avl_tree_fixture.insert(avl_tree_fixture.root, i)
        """
        Current Tree:
                    7
                5       8
            3               13           
        """

        avl_tree_fixture.remove(avl_tree_fixture.root, 3)
        """
        Current Tree:
                    7
                5       8
                           13           
        """
        # check data is correct
        assert avl_tree_fixture.root.left.data == 5

        # check heights are updated
        assert avl_tree_fixture.root.left.height == 0

        # check balance factors are updated
        assert avl_tree_fixture.root.left.bf == 0
        assert avl_tree_fixture.root.bf == 1

        # check references
        assert avl_tree_fixture.root.left.left == None
        assert avl_tree_fixture.root.left.parent == avl_tree_fixture.root

    def test_removal_left_leaf_node_case_w_rebalance(self, avl_tree_fixture):
        # rebuild tree such that it resembles tree below
        avl_tree_fixture.root = None
        data = [7, 5, 8, 13]
        for i in data:
            avl_tree_fixture.insert(avl_tree_fixture.root, i)
        """
        Current Tree:
                    7
                5       8
                            13           
        """
        avl_tree_fixture.remove(avl_tree_fixture.root, 5)
        """
        Post-Removal and Pre-Rebalance Tree:       Rebalanced tree:
                    7                                     8
                        8                             7       13
                           13           
        """
        # check data is correct
        assert avl_tree_fixture.root.left.data == 7
        assert avl_tree_fixture.root.data == 8
        assert avl_tree_fixture.root.right.data == 13

        # check heights are updated
        assert avl_tree_fixture.root.left.height == 0
        assert avl_tree_fixture.root.right.height == 0
        assert avl_tree_fixture.root.height == 1

        # check balance factors are correctly updated
        assert avl_tree_fixture.root.left.bf == 0
        assert avl_tree_fixture.root.right.bf == 0
        assert avl_tree_fixture.root.bf == 0

        # check references
        assert avl_tree_fixture.root.left.parent == avl_tree_fixture.root
        assert avl_tree_fixture.root.right.parent == avl_tree_fixture.root

    def test_removal_right_leaf_node_case_no_rebalance(self, avl_tree_fixture):
        # rebuild tree such that it resembles tree below
        avl_tree_fixture.root = None
        data = [7, 5, 8, 3, 13]
        for i in data:
            avl_tree_fixture.insert(avl_tree_fixture.root, i)
        """
        Current Tree:
                    7
                5       8
            3               13           
        """

        avl_tree_fixture.remove(avl_tree_fixture.root, 13)
        """
        Current Tree:
                    7
                5       8
            3                       
        """
        # check data is correct
        assert avl_tree_fixture.root.right.data == 8

        # check heights are updated
        assert avl_tree_fixture.root.right.height == 0

        # check balance factors are updated
        assert avl_tree_fixture.root.right.bf == 0
        assert avl_tree_fixture.root.bf == -1

        # check references
        assert avl_tree_fixture.root.right.right == None
        assert avl_tree_fixture.root.right.parent == avl_tree_fixture.root

    def test_removal_right_leaf_node_case_w_rebalance(self, avl_tree_fixture):
        # rebuild tree such that it resembles tree below
        avl_tree_fixture.root = None
        data = [7, 5, 8, 3]
        for i in data:
            avl_tree_fixture.insert(avl_tree_fixture.root, i)
        """
        Current Tree:
                    7
                5       8
            3                         
        """

        avl_tree_fixture.remove(avl_tree_fixture.root, 8)
        """
        Post-Removal and Pre-Rebalance Tree:       Rebalanced tree:
                     7                                   5
                 5                                  3        7
             3                        
        """
        # check data is correct
        assert avl_tree_fixture.root.left.data == 3
        assert avl_tree_fixture.root.data == 5
        assert avl_tree_fixture.root.right.data == 7

        # check heights are updated
        assert avl_tree_fixture.root.left.height == 0
        assert avl_tree_fixture.root.right.height == 0
        assert avl_tree_fixture.root.height == 1

        # check balance factors are correctly updated
        assert avl_tree_fixture.root.left.bf == 0
        assert avl_tree_fixture.root.right.bf == 0
        assert avl_tree_fixture.root.bf == 0

        # check references
        assert avl_tree_fixture.root.left.parent == avl_tree_fixture.root
        assert avl_tree_fixture.root.right.parent == avl_tree_fixture.root
