# Pascal/Camel Case to Snake Case Converter (Python)

This project converts strings written in `PascalCase` or `camelCase` into `snake_case`. It's a clean, expressive example of how to use **list comprehension**, **conditional expressions**, and **string manipulation** in Python to build practical tools that align with naming conventions in Python and beyond.

---

## What It Does

Given an input like:

```python
'IAmAPascalCasedString'
```
This is helpful for transforming variable names, parsing identifiers, or converting code formats between programming styles.

## Example
```
def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper() else char
        for char in pascal_or_camel_cased_string
    ]
    return ''.join(snake_cased_char_list).strip('_')

print(convert_to_snake_case('IAmAPascalCasedString'))
```
### Output: i_am_a_pascal_cased_string

## How to Use

1. Clone or download the script.
2. Run it using Python 3:
    ```bash
   Case-Converter_listComprehension.py
3. The main() function will call the converter with a sample string and print the result.
4. You can replace the test string in main() to try out your own input.

# What I Learned
## String Techniques
.isupper() for detecting uppercase characters

.lower() for case conversion

.join() for assembling a final string

.strip('_') to remove leading or trailing underscores

## Code Style
Clean, readable list comprehensions

Inline ternary expressions for conditional logic

Writing pure, testable functions with clear inputs and outputs

## Structure & Style
Modular code design with a main() entry point

Clear inline comments and docstrings

Use of descriptive naming and consistent formatting

## Future Ideas
Accept user input via input() for dynamic string conversion

Add batch conversion support for multiple variables or files

Create a command-line utility or VS Code extension

Improve acronym handling (e.g. getHTTPResponse → get_http_response)

## Why This Project Matters
Transforming strings like this reflects real-world needs in software engineering, especially when working 
across different coding styles, languages, or data pipelines. This project helps you practice logic, 
Python expression fluency, and professional code documentation all in one shot.