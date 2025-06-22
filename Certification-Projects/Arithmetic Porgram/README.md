# Arithmetic Formatter (Certification Project)

This project formats arithmetic problems vertically and side-by-side, just like students would write them in primary school. It’s one of the required projects for the [Scientific Computing with Python Certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/#build-an-arithmetic-formatter-project) by freeCodeCamp.

---

## What It Does

Given a list of arithmetic problems (e.g. `"32 + 698"`, `"3801 - 2"`), this function will:
- Validate the format of each problem
- Align them vertically and side-by-side with consistent spacing
- Optionally display the result of each operation

---

## Core Concepts Practiced

- String alignment using `rjust()`
- Parsing and validating string input
- Conditional logic and clean formatting
- Handling optional parameters
- Defensive programming with informative error messages

---

## Example Output

Function Call:

```python
>>> arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```

Output:

```python
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

Function Call:

```python
>>> arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```

Output:

```python
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

---

## Input Rules
The function will return an error if:

- More than 5 problems are given → 'Error: Too many problems.'
- An operator other than + or - is used → 'Error: Operator must be "+" or "-".'
- Operands contain characters other than digits → 'Error: Numbers must only contain digits.'
- Any operand is more than four digits long → 'Error: Numbers cannot be more than four digits.'

---

## How to Use
1. Save the script as arithmetic_arranger.py
2. Import the function or run test calls directly in the script
    ```
    from arithmetic_arranger import arithmetic_arranger

    print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
    ```
   
---

## Tech Stack
Language: Python 3.x

No external libraries required

---
## Given project perameters

Build an Arithmetic Formatter Project

Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:

```python
  235
+  52
-----
```

Finish the arithmetic_arranger function that receives a list of strings which are arithmetic problems, and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

Example

Function Call:

```python
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```

Output:

```python
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

Function Call:

```python
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```

Output:

```python
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```
Rules

The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

Situations that will return an error:

If there are too many problems supplied to the function. The limit is five, anything more will return: 'Error: Too many problems.'
The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: "Error: Operator must be '+' or '-'."
Each number (operand) should only contain digits. Otherwise, the function will return: 'Error: Numbers must only contain digits.'
Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: 'Error: Numbers cannot be more than four digits.'
If the user supplied the correct format of problems, the conversion you return will follow these rules:
There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).

Numbers should be right-aligned.

There should be four spaces between each problem.

There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)

---

## License

This project was completed as part of the freeCodeCamp curriculum. It is publicly available for educational use and review.