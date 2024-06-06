import pytest

from ..Data_Structures.Indexed_Priority_Queue.indexed_priority_queue import (
    MinIndexedDHeap,
)


@pytest.fixture(scope="function")
def min_indexed_heap_fixture():
    """
    Binary heap fixture with max size 15 for testing
    """
    i = MinIndexedDHeap(2, 15)
    yield i


@pytest.fixture(scope="function")
def min_indexed_ternary_heap_fixture():
    """
    Ternary heap fixture with max size 15 for testing
    """
    i = MinIndexedDHeap(3, 15)
    yield i


class Test_Min_Indexed_Binary_Heap:
    def test_insertion_w_swap(self, min_indexed_heap_fixture):
        """
        Test insertion when swap is required to maintain heap invariant
        """
        min_indexed_heap_fixture.insert(2, 10)
        """
        Current Heap:
                    k:2,v:10
        """
        # check values are correct
        assert min_indexed_heap_fixture._node_value(0) == 10
        # check keys are correct
        assert min_indexed_heap_fixture.im[0] == 2
        # check position map is correct ( key index (ki) -> node index (ni))
        assert min_indexed_heap_fixture.pm[2] == 0

        min_indexed_heap_fixture.insert(4, 100)
        """
        Current Heap:
                    k:2,v:10
            
         k:4,v:100       
        """
        # check values are correct
        assert min_indexed_heap_fixture._node_value(0) == 10
        assert min_indexed_heap_fixture._node_value(1) == 100
        # check keys are correct
        assert min_indexed_heap_fixture.im[0] == 2
        assert min_indexed_heap_fixture.im[1] == 4
        # check position map is correct ( key index (ki) -> node index (ni))
        assert min_indexed_heap_fixture.pm[2] == 0
        assert min_indexed_heap_fixture.pm[4] == 1

        min_indexed_heap_fixture.insert(5, 1)
        """
        Current Heap:
                    k:5,v:1
            
         k:4,v:100           k:2,v:10
        """
        # check values are correct
        assert min_indexed_heap_fixture._node_value(0) == 1
        assert min_indexed_heap_fixture._node_value(1) == 100
        assert min_indexed_heap_fixture._node_value(2) == 10
        # check keys are correct
        assert min_indexed_heap_fixture.im[0] == 5
        assert min_indexed_heap_fixture.im[1] == 4
        assert min_indexed_heap_fixture.im[2] == 2
        # check position map is correct ( key index (ki) -> node index (ni))
        assert min_indexed_heap_fixture.pm[5] == 0
        assert min_indexed_heap_fixture.pm[2] == 2
        assert min_indexed_heap_fixture.pm[4] == 1

    def test_valueOf(self, min_indexed_heap_fixture):
        """
        Test valueOf method of heap
        """
        min_indexed_heap_fixture.insert(2, 10)
        min_indexed_heap_fixture.insert(4, 100)
        min_indexed_heap_fixture.insert(5, 1)
        """
        Current Heap:
                    k:5,v:1
            
         k:4,v:100           k:2,v:10
        """
        assert min_indexed_heap_fixture.valueOf(2) == 10
        assert min_indexed_heap_fixture.valueOf(4) == 100
        assert min_indexed_heap_fixture.valueOf(5) == 1
        assert min_indexed_heap_fixture.valueOf(666) == None

    def test_contains(self, min_indexed_heap_fixture):
        """
        Test contains method of heap
        """
        min_indexed_heap_fixture.insert(2, 10)
        min_indexed_heap_fixture.insert(4, 100)
        min_indexed_heap_fixture.insert(5, 1)
        """
        Current Heap:
                    k:5,v:1
            
         k:4,v:100           k:2,v:,10
        """
        assert min_indexed_heap_fixture.contains(2) == True
        assert min_indexed_heap_fixture.contains(4) == True
        assert min_indexed_heap_fixture.contains(5) == True
        assert min_indexed_heap_fixture.contains(6) == False
        assert min_indexed_heap_fixture.contains(666) == False

    def test_peekMinKeyIndex(self, min_indexed_heap_fixture):
        """
        Test peekMinKeyIndex method of heap
        """
        min_indexed_heap_fixture.insert(2, 10)
        min_indexed_heap_fixture.insert(4, 100)
        min_indexed_heap_fixture.insert(5, 1)
        """
        Current Heap:
                    k:5,v:1
            
         k:4,v:100           k:2,v:10
        """

        assert min_indexed_heap_fixture.peekMinKeyIndex() == 5

    def test_peekMinKeyIndex_empty_heap(self, min_indexed_heap_fixture):
        """
        Test peekMinKeyIndex method of heap when herap is empty
        """
        assert min_indexed_heap_fixture.peekMinKeyIndex() == None

    def test_update(self, min_indexed_heap_fixture):
        """
        Test update method of heap w no swim/sink required
        """
        min_indexed_heap_fixture.insert(2, 10)
        min_indexed_heap_fixture.insert(4, 100)
        min_indexed_heap_fixture.insert(5, 1)
        """
        Current Heap:
                    k:5,v:1
            
         k:4,v:100           k:2,v:10
        """

        min_indexed_heap_fixture.update(4, 30)
        assert min_indexed_heap_fixture.valueOf(4) == 30
        min_indexed_heap_fixture.update(2, 9)
        assert min_indexed_heap_fixture.valueOf(2) == 9
        min_indexed_heap_fixture.update(5, 2)
        assert min_indexed_heap_fixture.valueOf(5) == 2

    def test_update_ki_does_not_exist(self, min_indexed_heap_fixture):
        """
        Test update method of heap when key index (ki) does not exist
        and a new element needs to be inserted into the heap
        """
        min_indexed_heap_fixture.insert(2, 10)
        min_indexed_heap_fixture.insert(4, 100)
        min_indexed_heap_fixture.insert(5, 1)
        """
        Current Heap:
                    k:5,v:1
            
         k:4,v:100           k:2,v:10
        """

        # key index 6 does not exist and a new element must be inserted
        # the element must be swap up into position 1 as well
        min_indexed_heap_fixture.update(6, 30)
        """
        Current Heap:
                            k:5,v:1
                    
                    k:6,v:30           k:2,v:10

            k:4,v:100
        """

        # check values are correct
        assert min_indexed_heap_fixture._node_value(0) == 1
        assert min_indexed_heap_fixture._node_value(1) == 30
        assert min_indexed_heap_fixture._node_value(2) == 10
        assert min_indexed_heap_fixture._node_value(3) == 100

    def test_update_index_error(self, min_indexed_heap_fixture):
        """
        Test update method when the key index (ki) is larger
        than the max_sizer of the heap
        """
        assert min_indexed_heap_fixture.update(16, 30) == None

    def test_smallest_child_ni(self, min_indexed_heap_fixture):
        """
        Test smallest_child_ni method of heap. The method should return
        the node index (ni) of the smallest child node value
        """
        min_indexed_heap_fixture.insert(2, 1)
        min_indexed_heap_fixture.insert(4, 3)
        min_indexed_heap_fixture.insert(5, 4)
        min_indexed_heap_fixture.insert(6, 5)
        min_indexed_heap_fixture.insert(7, 7)
        """
        Current Heap:
                                k:2,v:1

                    k:4,v:3                k:5,v:4

            k:6,v:5         k:7,v:7
        """
        assert min_indexed_heap_fixture._smallest_child_ni(0) == 1
        assert min_indexed_heap_fixture._smallest_child_ni(1) == 3

    def test_smallest_child_no_children(self, min_indexed_heap_fixture):
        """
        Test smallest_child_ni method of heap. The method should return None when
        no child nodes are present.
        """
        min_indexed_heap_fixture.insert(2, 1)
        min_indexed_heap_fixture.insert(4, 3)
        min_indexed_heap_fixture.insert(5, 4)
        """
        Current Heap:
                            k:2,v:1

                 k:4,v:3                k:5,v:4     
        """
        assert min_indexed_heap_fixture._smallest_child_ni(1) == None
        assert min_indexed_heap_fixture._smallest_child_ni(2) == None

    def test_delete_no_swim_or_sink(self, min_indexed_heap_fixture):
        """
        Test delete method of the herap when no sinking or swimming
        is required to maintain the heap invariant
        """
        min_indexed_heap_fixture.insert(2, 1)
        min_indexed_heap_fixture.insert(4, 3)
        min_indexed_heap_fixture.insert(5, 4)
        """
        Current Heap:
                            k:2,v:1

                 k:4,v:3                k:5,v:4     
        """
        # check deleted key, value are returned
        assert min_indexed_heap_fixture.delete(5) == (5, 4)
        """
        Current Heap:
                            k:2,v:1

                 k:4,v:3                 
        """
        assert min_indexed_heap_fixture._node_value(0) == 1
        assert min_indexed_heap_fixture._node_value(1) == 3
        assert min_indexed_heap_fixture._node_value(2) == None

        # check deleted key, value are returned
        assert min_indexed_heap_fixture.delete(4) == (4, 3)
        """
        Current Heap:
                            k:2,v:1
              
        """
        assert min_indexed_heap_fixture._node_value(0) == 1
        assert min_indexed_heap_fixture._node_value(1) == None

        # check deleted key, value are returned
        assert min_indexed_heap_fixture.delete(2) == (2, 1)
        """
        Current Heap:
                            k:2,v:1
              
        """
        assert min_indexed_heap_fixture._node_value(0) == None

    def test_delete_with_sink(self, min_indexed_heap_fixture):
        """
        Test the delete method of heap when sinking is required after the swap.
        """
        min_indexed_heap_fixture.insert(2, 1)
        min_indexed_heap_fixture.insert(4, 3)
        min_indexed_heap_fixture.insert(5, 4)
        min_indexed_heap_fixture.insert(6, 5)
        min_indexed_heap_fixture.insert(7, 7)
        """
        Current Heap:
                                k:2,v:1

                    k:4,v:3                k:5,v:4

            k:6,v:5         k:7,v:7
        """
        # delete ki 4 which will swap ki 7 into that location
        # and require a sink
        # check deleted key, value are returned
        assert min_indexed_heap_fixture.delete(4) == (4, 3)
        """
        Current Heap:
                                k:2,v:1

                    k:6,v:5                k:5,v:4

            k:7,v:7   
        """
        # check node values
        assert min_indexed_heap_fixture._node_value(0) == 1
        assert min_indexed_heap_fixture._node_value(1) == 5
        assert min_indexed_heap_fixture._node_value(2) == 4
        assert min_indexed_heap_fixture._node_value(3) == 7

    def test_delete_with_swim(self, min_indexed_heap_fixture):
        """
        Test delete method of heap when swiming is required after swap.
        """
        min_indexed_heap_fixture.insert(2, 1)
        min_indexed_heap_fixture.insert(4, 3)
        min_indexed_heap_fixture.insert(5, 4)
        min_indexed_heap_fixture.insert(6, 5)
        min_indexed_heap_fixture.insert(7, 7)
        """
        Current Heap:
                                k:2,v:1

                    k:4,v:3                k:5,v:4

            k:6,v:5         k:7,v:7
        """
        # delete ki 4 which will swap ki 7 into that location
        # and require a sink
        # check deleted key, value are returned
        assert min_indexed_heap_fixture.delete(4) == (4, 3)
        """
        Current Heap:
                                k:2,v:1

                    k:6,v:5                k:5,v:4

            k:7,v:7   
        """
        # check node values
        assert min_indexed_heap_fixture._node_value(0) == 1
        assert min_indexed_heap_fixture._node_value(1) == 5
        assert min_indexed_heap_fixture._node_value(2) == 4
        assert min_indexed_heap_fixture._node_value(3) == 7

    def test_delete_ki_does_not_exist(self, min_indexed_heap_fixture):
        """
        Test delete method of heap when key index (ki) does not exist
        """
        assert min_indexed_heap_fixture.delete(10) == None

    def test_poll_min_value(self, min_indexed_heap_fixture):
        """
        Test pollMinValue method of heap. It should return the value
        at the top of the heap.
        """
        min_indexed_heap_fixture.insert(2, 1)
        min_indexed_heap_fixture.insert(4, 3)
        min_indexed_heap_fixture.insert(5, 4)
        """
        Current Heap:
                            k:2,v:1

                 k:4,v:3                k:5,v:4     
        """

        assert min_indexed_heap_fixture.pollMinValue() == 1

    def test_poll_min_value_empty_heap(self, min_indexed_heap_fixture):
        """
        Test pollMinValue method of heap when heap is empty.
        It should return None
        """
        assert min_indexed_heap_fixture.pollMinValue() == None

    def test_poll_min_key_index(self, min_indexed_heap_fixture):
        """
        Test pollMinKeyIndex method of heap. It shoudl return
        the ki associated with the smallest value (top of heap).
        """
        min_indexed_heap_fixture.insert(2, 1)
        min_indexed_heap_fixture.insert(4, 3)
        min_indexed_heap_fixture.insert(5, 4)
        """
        Current Heap:
                            k:2,v:1

                 k:4,v:3                k:5,v:4     
        """

        assert min_indexed_heap_fixture.pollMinKeyIndex() == 2

    def test_poll_min_key_index_empty_heap(self, min_indexed_heap_fixture):
        """
        Test pollMinKeyIndex method of heap when heap is empty.
        It should return none.
        """
        assert min_indexed_heap_fixture.pollMinKeyIndex() == None

    def test_update_with_swim(self, min_indexed_heap_fixture):
        min_indexed_heap_fixture.insert(2, 1)
        min_indexed_heap_fixture.insert(4, 3)
        min_indexed_heap_fixture.insert(5, 4)
        min_indexed_heap_fixture.insert(6, 5)
        min_indexed_heap_fixture.insert(7, 7)
        """
        Current Heap:
                                k:2,v:1

                    k:4,v:3                k:5,v:4

            k:6,v:5         k:7,v:7
        """

        min_indexed_heap_fixture.update(6, 2)
        """
        Current Heap:
                                k:2,v:1

                    k:6,v:2                k:5,v:4

            k:4,v:3         k:7,v:7
        """
        # check node values
        assert min_indexed_heap_fixture._node_value(0) == 1
        assert min_indexed_heap_fixture._node_value(1) == 2
        assert min_indexed_heap_fixture._node_value(2) == 4
        assert min_indexed_heap_fixture._node_value(3) == 3
        assert min_indexed_heap_fixture._node_value(4) == 7

    def test_update_with_sink(self, min_indexed_heap_fixture):
        """
        Test update method of heap when sink is required after update.
        """
        min_indexed_heap_fixture.insert(2, 1)
        min_indexed_heap_fixture.insert(4, 3)
        min_indexed_heap_fixture.insert(5, 4)
        min_indexed_heap_fixture.insert(6, 5)
        min_indexed_heap_fixture.insert(7, 7)
        """
        Current Heap:
                                k:2,v:1

                    k:4,v:3                k:5,v:4

            k:6,v:5         k:7,v:7
        """

        min_indexed_heap_fixture.update(2, 100)
        """
        Current Heap:
                                k:4,v:3

                    k:6,v:5               k:5,v:4

            k:2,v:100        k:7,v:7
        """
        # check node values
        assert min_indexed_heap_fixture._node_value(0) == 3
        assert min_indexed_heap_fixture._node_value(1) == 5
        assert min_indexed_heap_fixture._node_value(2) == 4
        assert min_indexed_heap_fixture._node_value(3) == 100
        assert min_indexed_heap_fixture._node_value(4) == 7

    def test_decrease_key_no_swim(self, min_indexed_heap_fixture):
        """
        Test decreaseKey method of heap when swim is not required after decreasing value.
        """
        min_indexed_heap_fixture.insert(2, 1)
        min_indexed_heap_fixture.insert(4, 3)
        min_indexed_heap_fixture.insert(5, 4)
        """
        Current Heap:
                            k:2,v:1

                 k:4,v:3                k:5,v:4     
        """

        min_indexed_heap_fixture.decreaseKey(4, 2)
        """
        Current Heap:
                            k:2,v:1

                 k:4,v:2                k:5,v:4     
        """
        # check node values
        assert min_indexed_heap_fixture._node_value(1) == 2

    def test_decrease_key_larger_value(self, min_indexed_heap_fixture):
        """
        Test decreaseKey method of heap when value at key index (ki) 4
        is smaller than the proposed value (10).  The key index should
        not be updated because decrease key only updates if the proposed
        value is smaller than the original one.
        """
        min_indexed_heap_fixture.insert(2, 1)
        min_indexed_heap_fixture.insert(4, 3)
        min_indexed_heap_fixture.insert(5, 4)
        """
        Current Heap:
                            k:2,v:1

                 k:4,v:3                k:5,v:4     
        """

        # proposed value 10 is larger than current value and update should n0t occur
        min_indexed_heap_fixture.decreaseKey(4, 10)
        """
        Current Heap:
                            k:2,v:1

                 k:4,v:3                k:5,v:4     
        """
        # check node values
        assert min_indexed_heap_fixture._node_value(1) == 3

    def test_decrease_key_w_swim(self, min_indexed_heap_fixture):
        """
        Test decrease key method of heap when the update requires swimming to
        maintain heap invariant
        """
        min_indexed_heap_fixture.insert(2, 3)
        min_indexed_heap_fixture.insert(4, 5)
        min_indexed_heap_fixture.insert(5, 4)
        """
        Current Heap:
                            k:2,v:3

                 k:4,v:5                k:5,v:4     
        """

        min_indexed_heap_fixture.decreaseKey(5, 2)
        """
        Current Heap:
                            k:5,v:2

                 k:4,v:2                k:2,v:3     
        """
        # check node values
        assert min_indexed_heap_fixture._node_value(0) == 2
        assert min_indexed_heap_fixture._node_value(2) == 3

    def test_decrease_key_w_missing_key(self, min_indexed_heap_fixture):
        """
        Test decrease key method of heap when key index (ki)
        not present in the heap.
        """
        min_indexed_heap_fixture.insert(2, 3)
        min_indexed_heap_fixture.insert(4, 5)
        min_indexed_heap_fixture.insert(5, 4)
        """
        Current Heap:
                            k:2,v:3

                 k:4,v:5                k:5,v:4     
        """

        min_indexed_heap_fixture.decreaseKey(11, 2)

        # check node values
        assert min_indexed_heap_fixture._node_value(0) == 3
        assert min_indexed_heap_fixture._node_value(1) == 5
        assert min_indexed_heap_fixture._node_value(2) == 4

    def test_increase_key_no_sink(self, min_indexed_heap_fixture):
        """
        Test increaseKey mehtod of heap when sink is not required after increasing value.
        """
        min_indexed_heap_fixture.insert(2, 1)
        min_indexed_heap_fixture.insert(4, 3)
        min_indexed_heap_fixture.insert(5, 4)
        """
        Current Heap:
                            k:2,v:1

                 k:4,v:3                k:5,v:4     
        """

        min_indexed_heap_fixture.increaseKey(4, 5)
        """
        Current Heap:
                            k:2,v:1

                 k:4,v:5                k:5,v:4     
        """
        # check node values
        assert min_indexed_heap_fixture._node_value(1) == 5

    def test_increase_key_smaller_value(self, min_indexed_heap_fixture):
        """
        Test increaseKey method of heap when value at key index (ki) 4
        is larger than the proposed value (2).  The key index should
        not be updated because increase key only updates if the proposed
        value is larger than the original one.
        """
        min_indexed_heap_fixture.insert(2, 1)
        min_indexed_heap_fixture.insert(4, 3)
        min_indexed_heap_fixture.insert(5, 4)
        """
        Current Heap:
                            k:2,v:1

                 k:4,v:3                k:5,v:4     
        """

        # proposed value 10 is larger than current value and update should not occur
        min_indexed_heap_fixture.increaseKey(4, 2)
        """
        Current Heap:
                            k:2,v:1

                 k:4,v:3                k:5,v:4     
        """
        # check node values
        assert min_indexed_heap_fixture._node_value(1) == 3

    def test_increase_key_w_sink(self, min_indexed_heap_fixture):
        """
        Test increase key method of heap when the update requires sinking to
        maintain heap invariant.
        """
        min_indexed_heap_fixture.insert(2, 3)
        min_indexed_heap_fixture.insert(4, 5)
        min_indexed_heap_fixture.insert(5, 4)
        """
        Current Heap:
                            k:2,v:3

                 k:4,v:5                k:5,v:4     
        """

        min_indexed_heap_fixture.increaseKey(2, 10)
        """
        Current Heap:
                            k:5,v:4

                 k:4,v:5                k:2,v:10     
        """
        # check node values
        assert min_indexed_heap_fixture._node_value(0) == 4
        assert min_indexed_heap_fixture._node_value(2) == 10


class Test_Min_Indexed_Ternary_Heap:
    def test_smallest_child_ni(self, min_indexed_ternary_heap_fixture):
        """
        Test smallest_child_ni method on a ternary heap.
        """
        min_indexed_ternary_heap_fixture.insert(2, 1)
        min_indexed_ternary_heap_fixture.insert(4, 3)
        min_indexed_ternary_heap_fixture.insert(5, 4)
        min_indexed_ternary_heap_fixture.insert(6, 5)
        """
        Current Heap:
                            k:2,v:1

                 k:4,v:3    k:5,v:4     k:6,v:5
        """
        assert min_indexed_ternary_heap_fixture._smallest_child_ni(0) == 1
