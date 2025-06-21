# ========================
# Cipher Lab: Python Encryption Learning Module
# ========================

# This file explores two classical encryption methods:
# - Caesar Cipher (rotational shift)
# - Vigenère Cipher (keyword-based shifting)
# along with core string manipulation concepts

# ---------------------------------------------
# PART 1: Variable Types and String Methods
# ---------------------------------------------

number = 5                      # integer
text = 'Hello World'            # string
shift = 3                       # Caesar cipher shift amount
alphabet = 'abcdefghijklmnopqrstuvwxyz'  # reference alphabet

# Indexing & Inspection
print(text[0])                  # first character
print(len(text))                # number of characters
print(type(text))               # check the data type
print(text.lower())             # convert to lowercase

# ---------------------------------------------
# Python Notes: Variables & Strings

# - Variable names must begin with a letter or underscore (not a number).
# - Reserved keywords (like for, while, True) can't be used as variable names.
# - Variables are case-sensitive: MY_VAR ≠ my_var.
# - Use snake_case for readability (e.g. encrypted_text).
# - Strings are immutable—they cannot be changed directly.
# ---------------------------------------------


# ---------------------------------------------
# PART 2: Caesar Cipher — Simple Rotational Encryption
# ---------------------------------------------

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]

    return encrypted_text

# ===> Caesar Demos
print('\n=== Caesar Cipher Demos ===')
text = 'Hello Zaira'
print('Original message:', text)
print('Shift 3:', caesar(text, 3))        # encrypted
print('Shift 13:', caesar(text, 13))

# ---------------------------------------------
# PART 3: Vigenère Cipher — Keyword-Based Shifting
# ---------------------------------------------

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else:
            key_char = key[key_index % len(key)]
            key_index += 1

            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message

# Helper functions
def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)

# ===> Vigenère Demo
print('\n=== Vigenère Cipher Demo ===')
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

print('Encrypted text:', text)
print('Key:', custom_key)
decryption = decrypt(text, custom_key)
print('Decrypted text:', decryption)