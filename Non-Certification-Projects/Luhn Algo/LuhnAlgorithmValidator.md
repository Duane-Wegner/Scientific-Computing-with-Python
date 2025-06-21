# Luhn Algorithm Validator

This Python script checks whether a given credit card number is **valid** using the Luhn algorithm—a checksum formula used to validate identification numbers such as credit card numbers.

---

## What This Script Does

- Cleans up a formatted card number by removing spaces and dashes
- Reverses the card number and separates digits into odd and even positions
- Sums the digits according to the Luhn algorithm:
  - Odd-positioned digits are added directly
  - Even-positioned digits are doubled, and their individual digits are summed if the result is two digits (e.g., 8 → 16 → 1 + 6)
- Returns `VALID!` if the final total is divisible by 10, otherwise returns `INVALID!`

---

## What I Learned

### String Manipulation
- Reversing a string using slicing: `[::-1]`
- Extracting every other character using slicing: `[::2]` and `[1::2]`
- Translating strings with `str.maketrans()` and `.translate()` to strip unwanted characters

### Loops & Logic
- Using `for` loops to iterate over digits
- Understanding conditionals (`if`) to apply rules to different cases
- Performing digit transformation and checksum calculation

### Functions & Modularity
- Writing reusable functions (`verify_card_number`)
- Returning boolean values and using them in `if/else` statements
- Separating validation logic from the program’s entry point using `main()`

---

## How to Use

1. Open the script in any Python 3 environment
2. Set your `card_number` variable inside the `main()` function
3. Run the script and see whether the card number is `VALID!` or `INVALID!`

---

## Example Output

VALID!

---

## Next Steps (Stretch Goals)

- Accept card numbers via `input()` for dynamic testing
- Process a list of numbers from a file or user interface
- Include support for other checksum systems or formatting output

---
