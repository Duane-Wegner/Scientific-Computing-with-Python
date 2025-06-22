# Merge Sort: Recursive Sorting in Python

Welcome to the Merge Sort project! This script demonstrates one of the most efficient and foundational sorting algorithms in computer science. You’ll explore how divide-and-conquer logic, recursion, and in-place memory manipulation work together to sort lists in ascending order.

---

## What This Script Does

- Recursively splits a list into halves using the midpoint  
- Compares and merges sorted sublists back into the original array  
- Uses index tracking to avoid extra space and retain performance  
- Sorts the array in place without creating new structures  

---

## Initial Input

```python
numbers = [4, 10, 6, 14, 2, 1, 8, 5]
```

---

## What I Learned

### Divide-and-Conquer Strategy
- How to split arrays using Python slice notation
- Breaking problems into subproblems until base case (len(array) <= 1)

### Recursive Function Design
- Structuring a clean, termination-safe recursive algorithm
- Keeping parameter logic pure for testability and reuse

### Merge Logic Using Indexes
- Merging two sorted arrays using index counters (left_array_index, right_array_index)
- Tracking the sorted array’s progress with sorted_index
- Appending any leftover items from either half after merging

### In-Place Sorting
- Working within the original array memory space
- Avoiding extra memory allocations for new arrays

---

## How to Use
1. Navigate to the project folder: Non-Certification-Projects/Section 2/Merge Sort Algo/
2. Run the script in any Python 3 environment:

```bash 
   python Merge-and-Sort_dataStructures.py
```

---

## Example Output
```python
Unsorted array:
[4, 10, 6, 14, 2, 1, 8, 5]
Sorted array: [1, 2, 4, 5, 6, 8, 10, 14]
```

---

## Next Steps (Ideas to Explore)
- Add visual step-by-step diagrams of recursive splitting
- Compare merge sort performance vs. Python’s built-in sort()
- Implement a bottom-up (non-recursive) version
- Log the number of comparisons for performance insight
- Add support for descending order sorting with a flag

This project not only sharpens your understanding of recursion and arrays, but also gives you hands-on experience with algorithm optimization techniques.
