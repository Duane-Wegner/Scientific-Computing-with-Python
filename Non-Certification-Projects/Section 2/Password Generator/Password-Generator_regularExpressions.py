import re  # For regular expression matching to validate character constraints
import secrets  # For generating cryptographically secure random choices
import string  # For accessing pre-defined sets of characters (letters, digits, punctuation)


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    """
    Generate a secure random password that satisfies specific character-type requirements.

    Args:
        length (int): Total length of the generated password.
        nums (int): Minimum number of digits required.
        special_chars (int): Minimum number of special characters required.
        uppercase (int): Minimum number of uppercase letters required.
        lowercase (int): Minimum number of lowercase letters required.

    Returns:
        str: A valid password meeting all specified constraints.
    """

    # Define available character pools
    letters = string.ascii_letters  # Includes both lowercase and uppercase letters
    digits = string.digits  # '0123456789'
    symbols = string.punctuation  # e.g. '!@#$%^&*()'

    # Combine all character categories into one pool for random selection
    all_characters = letters + digits + symbols

    while True:
        password = ''

        # Generate a random password of the specified length
        for _ in range(length):
            password += secrets.choice(all_characters)

        # Define constraints: each tuple holds (required_count, regex_pattern)
        constraints = [
            (nums, r'\d'),  # At least `nums` digits
            (special_chars, fr'[{symbols}]'),  # At least `special_chars` from symbols
            (uppercase, r'[A-Z]'),  # At least `uppercase` uppercase letters
            (lowercase, r'[a-z]')  # At least `lowercase` lowercase letters
        ]

        # Check if all constraints are met using regex match count
        if all(
                constraint <= len(re.findall(pattern, password))
                for constraint, pattern in constraints
        ):
            break  # Exit the loop when a valid password is generated

    return password


# Run the password generator only if this script is executed directly
if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)
