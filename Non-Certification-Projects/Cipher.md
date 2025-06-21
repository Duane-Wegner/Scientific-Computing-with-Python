# Cipher Lab: Python Encryption Learning Module

Welcome to Cipher Lab! This project walks through the fundamentals of encryption using Python. It introduces two classical cipher systems, **Caesar Cipher** and **Vigenère Cipher**, alongside a practical exploration of string manipulation, control flow, and functional programming.

---

## What This Script Does

- Demonstrates how to manipulate and inspect strings using indexing, slicing, and case conversion.
- Explains and implements the Caesar Cipher (single-letter shift encryption).
- Implements the Vigenère Cipher (keyword-based encryption and decryption).
- Provides hands-on examples of modular arithmetic, loops, conditionals, and helper functions.

---

## What I Learned

### String Manipulation
- Slicing and indexing (`text[0]`, `text[::-1]`, etc.)
- Converting to lowercase (`.lower()`)
- Using `.find()` and `.index()` to locate characters
- Immutable properties of strings

### Control Flow
- `for` loops to iterate over characters in a message
- `if/else` conditions for branching logic
- Modular arithmetic with `%` for wrapping character shifts

### Functions and Modularity
- Writing reusable functions like `caesar()`, `encrypt()`, and `decrypt()`
- Using parameters and return values effectively
- Structuring code with readability and reusability in mind

---

## How to Use

1. Clone or download this repository.
2. Open the file in a Python 3 environment.
3. Run the script to see both ciphers in action:
   - Caesar Cipher encrypts "Hello Zaira" with shifts of 3 and 13.
   - Vigenère Cipher decrypts an encoded message with the key `"happycoding"`.
4. Modify the `text`, `key`, or `shift` variables to experiment with your own messages.

---

## Example Output

=== Caesar Cipher Demos === Original message: Hello Zaira Shift 3: khoor cdlud Shift 13: uryyb mnven

=== Vigenère Cipher Demo === Encrypted text: mrttaqrhknsw ih puggrur Key: happycoding Decrypted text: protectthecode at allcost


---

## Next Steps (Ideas to Explore)

- Build an interactive menu for choosing a cipher type and entering custom text
- Add support for uppercase letters and punctuation in both ciphers
- Create a combined encrypt/decrypt toolkit as a Python module or CLI app

---

 Whether you're learning Python fundamentals or diving deeper into classical cryptography, this project gives you hands-on practice wrapped in practical logic and creativity. Enjoy exploring!

