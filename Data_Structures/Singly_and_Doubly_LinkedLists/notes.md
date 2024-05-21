# Data Structure: a data storage format

It is the collection of va

lues and the format they are stored in, the relationships between the values
in the collection as well as the opertions applied on the data stored in the structure.

contiguous data structure: values stored in blocks of memory  that are next to each other
non-contiguous dsata structure: structure stores vlaue as well as reference (pointer) to where next value is

Array: collection of values that can be indexed,contiguous data structure
    -analogy: train
    - heterogenous in python (can store different types of values [int, str, int])
    - homogenous in java (can store different types of values [int, int, int])

## Linked List

linear data structure where each element is contained in sperate object called a node

![i](/Users/austinpaxton/Documents/dev/DSA/Data_Structures/Singly_and_Doubly_LinkedLists/img/1.png)

![i](/Users/austinpaxton/Documents/dev/DSA/Data_Structures/Singly_and_Doubly_LinkedLists/img/2.png)

![2](/Users/austinpaxton/Documents/dev/DSA/Data_Structures/Singly_and_Doubly_LinkedLists/img/3.png)

![im](/Users/austinpaxton/Documents/dev/DSA/Data_Structures/Singly_and_Doubly_LinkedLists/img/4.png)

![img](/Users/austinpaxton/Documents/dev/DSA/Data_Structures/Singly_and_Doubly_LinkedLists/img/5.png)

![img](/Users/austinpaxton/Documents/dev/DSA/Data_Structures/Singly_and_Doubly_LinkedLists/img/6.png)

    - analogy: treasure map
    - node contains element as well as reference to next node in the list (self-referential object)
        *first node called head and last node called tail
            - list only maintins reference to head; maintains reference to tail in some implementations
    - singlely linked list: only stores reference to next node
    - doubly linked list: stores reference to previous and next node

Operations on Data Structures:
    * Access and read values
    * Search for an arbitrary value
    * Insert values at any point into the structure
    * Delete value in structure
