# Time Calculator (Certification Project)

This project calculates what time it will be after adding a given duration to a starting time. It’s one of the required projects for the [Scientific Computing with Python Certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/#build-a-time-calculator-project) by freeCodeCamp.

---

## What It Does

Given:
- A start time in 12-hour AM/PM format (e.g. `"3:00 PM"`)
- A duration in hours and minutes (e.g. `"3:10"`)
- Optionally, a weekday (e.g. `"Monday"`)

The function will:
- Compute the new time
- Optionally include the day
- Indicate if the result is the next day or several days later

---

## Core Concepts Practiced

- String parsing and time formatting
- Modular arithmetic (handling time rollovers)
- Case-insensitive day handling and index rotation
- Defensive logic for time unit boundaries
- Clean formatting of results using conditional logic

---

## Rules
The function assumes properly formatted input:
- Start time must be in HH:MM AM/PM format
- Duration must be in H:MM format
- If a weekday is given, it must be a valid weekday (case-insensitive)

Notes:
- The minutes in the duration will always be less than 60
- The start time is always valid; no external library is used
- Time rolls over after 24 hours and accounts for AM/PM transition

---

## Input Rules
The function assumes properly formatted input:
- Start time must be in HH:MM AM/PM format
- Duration must be in H:MM format
- If a weekday is given, it must be a valid weekday (case-insensitive)

Notes:
- The minutes in the duration will always be less than 60
- The start time is always valid; no external library is used
- Time rolls over after 24 hours and accounts for AM/PM transition

---

## How to Use
1. Save the script as time_calculator.py
2. Call the add_time() function with appropriate arguments:

```python
from time_calculator import add_time

print(add_time("8:16 PM", "466:02", "tuesday"))
# Output: "6:18 AM, Monday (20 days later)"
```

---

## Tech Stack
Language: Python 3.x No external libraries required

---

## Given project parameters

Build a Time Calculator Project
Write a function named add_time that takes in two required parameters and one optional parameter:

- a start time in the 12-hour clock format (ending in AM or PM)
- a duration time that indicates the number of hours and minutes
- (optional) a starting day of the week, case insensitive

The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.

Example Code:

Function Call:
```python
add_time("3:00 PM", "3:10")
```
Return:
```python
"6:10 PM"
```
Function Call:
```python
add_time("11:30 AM", "2:32", "Monday")
```
Return:
```python
"2:02 PM, Monday"
```
Function Call:
```python
add_time("11:43 PM", "24:20", "tueSday")
```
Return:
```python
"12:03 AM, Thursday (2 days later)"
```
Function Call:
```python
add_time("6:30 PM", "205:12")
```
Return:
```python
"7:42 AM (9 days later)"
```
Do not import any Python libraries. Assume that the start times are valid times. The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.

---

## License
This project was completed as part of the freeCodeCamp curriculum. It is publicly available for educational use and review.




