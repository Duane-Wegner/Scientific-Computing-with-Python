# Tower of Hanoi Solver: Recursive Disk Transfer in Python
Welcome to the Tower of Hanoi Solver! This program implements the classic recursive algorithm to solve the Tower of Hanoi puzzle using Python. You'll explore recursion, stack manipulation, and problem decomposition while visually tracking disk transfers across three rods.

--- 

## What This Script Does
- Solves the Tower of Hanoi problem for any number of disks using recursion
- Simulates and displays each step of the puzzle's solution
- Demonstrates base case handling and elegant recursion patterns
- Provides a clean visualization of rod states throughout the process

--- 

## Initial Configuration
```python
NUMBER_OF_DISKS = 5
A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []
```
This setup reflects the starting condition: all disks are stacked on rod A in descending order.

--- 

## What I Learned

### Recursive Thinking
- Solving complex problems by breaking them into smaller subproblems
- Identifying a clear base case (n <= 0) to prevent infinite recursion
- Visually tracing the recursive call stack by printing after each disk move

### List Handling & Stack Logic

- Using .pop() to remove the top disk from the source
- Using .append() to add the disk to the destination rod
- Simulating rod behavior using Python lists for LIFO operations

### Debugging & Progress Display

- Printing rod states after each move to track the algorithm’s progress
- Using function arguments instead of dictionary keys for simplicity
- Structuring clean, readable recursive functions with helpful comments and docstrings

--- 

## How to Use

1. Clone or download this repository
2. Open the script in a Python 3 environment
3. Run the script using:

```bash
python Tower-of-Hanoi_recursion.py
```
Watch the rod lists update after every move until the entire stack transfers from rod A to rod C

--- 

## Example Output

```python
[5, 4, 3, 2] [] [1]  
[5, 4, 3] [2] [1]  
[5, 4, 3] [2, 1] []  
...
[] [] [5, 4, 3, 2, 1]
```

--- 

## Next Steps (Ideas to Explore)

- Add ASCII art or visual output to show tower states graphically
- Animate the process using time.sleep() for better pacing
- Extend to an iterative version of the algorithm
- Allow user input for disk count and rod names

Whether you're honing your skills in recursion or just love classic puzzles, this project is a great way to build both problem-solving intuition and Python fluency.