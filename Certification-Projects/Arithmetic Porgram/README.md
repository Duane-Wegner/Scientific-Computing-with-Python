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

```python
>>> arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----

>>> arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
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

## License
This project was completed as part of the freeCodeCamp curriculum. It is publicly available for educational use and review.