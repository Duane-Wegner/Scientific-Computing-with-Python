# Password Lab: Python Secure Password Generator

Welcome to Password Lab! This project puts regular expressions and secure randomness to work by generating customizable passwords with specific character constraints. You'll explore how to combine cryptography and validation logic to create robust, criteria-based outputs.

---

## What This Script Does

- Uses `secrets` for cryptographically strong random password generation  
- Ensures inclusion of:
  - Digits (`0–9`)
  - Lowercase letters (`a–z`)
  - Uppercase letters (`A–Z`)
  - Special characters (e.g. `!@#$%^&*`)
- Validates password content using regular expressions  
- Allows customization of password length and character type requirements

---

## What I Learned

### String Construction
- Concatenating randomized characters from multiple character pools  
- Building a single string from secure random choices

### Regex and Validation
- Using `re.findall()` to match character types in a string  
- Constructing dynamic patterns like `fr"[{symbols}]"` to validate special characters  
- Validating all criteria using a single list comprehension with `all()`

### Control Flow and Security
- Using `while True` loops with validation to ensure constraints are met  
- Protecting random generation logic with the `secrets` module  
- Writing reusable, well-scoped functions

---

## How to Use

1. Clone or download this repository.  
2. Open the script in a Python 3 environment.  
3. Run the file directly to generate a default 16-character password.  
4. Customize parameters inside `generate_password()` for:
   - `length` (total number of characters)
   - `nums` (minimum number of digits)
   - `special_chars` (minimum special characters)
   - `uppercase` (minimum uppercase letters)
   - `lowercase` (minimum lowercase letters)

---

## Example Output

```python
Generated password: &MO3lO(Qt)_5~P3A
```

## Next Steps (Ideas to Explore)
- Add a CLI interface for runtime argument input (argparse)
- Let users exclude ambiguous characters (like l and 1)
- Export generated passwords to a secure vault or file
- Build a web UI for interacting with the generator online

Whether you're strengthening your Python regex muscles or building practical password tools, this project offers a valuable hands-on lesson in validation, randomness, and customization. Try it out and stay secure!