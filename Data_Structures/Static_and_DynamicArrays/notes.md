# Static Array:

- Fixed Length container containing n elements indexable from the range [0,n-1]

  Q: What does indexable mean?
  A: This means that each slot/index in the array can be referenced with a number

  #### Use cases:


  - Storing and accessing sequential data
  - Temporarily storing objects
  - Used by IO routines aas buffers (Read small chunks of large file into buffer)
  - Lookup tables and inverse lookup tables
  - Can be used to return multiple values from a function
  - Used in dynamic programming to cache answers to subproblems
- Complexity

  | Complexity | Static Array | Dynamic Array |
  | ---------- | ------------ | ------------- |
  | Access     | O(1)         | O(1)          |
  | Search     | O(n)         | O(n)          |
  | Insertion  | N/A          | O(n)          |
  | Appending  | N/A          | O(1)          |
  | Deletion   | N/A          | O(n)          |

## Dynamic Array

Q: How can we implement a dynamic array?

A: One way is to use a static array.

1. Create a static array with an initial capacity
2. Add elements to the underlying static array keeping track of the number of elements
3. If adding another element will exceed the capacity, then create a new static array with
   twice the capcity and copy the original elements into it
