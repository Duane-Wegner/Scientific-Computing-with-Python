def verify_card_number(card_number):
    """
    Validate a card number using the Luhn algorithm.

    Args:
        card_number (str): A string of numeric characters representing the card number.

    Returns:
        bool: True if the card number is valid, False otherwise.
    """
    # Reverse the card number string to process from right to left (per Luhn algorithm)
    card_number_reversed = card_number[::-1]

    # Extract digits in odd positions (0-based index after reversal)
    odd_digits = card_number_reversed[::2]
    sum_of_odd_digits = 0
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    # Extract digits in even positions
    even_digits = card_number_reversed[1::2]
    sum_of_even_digits = 0
    for digit in even_digits:
        number = int(digit) * 2  # Double the digit
        # If the result is two digits, subtract 9 (equivalent to summing the two digits)
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number

    # Total sum of both processed digit groups
    total = sum_of_odd_digits + sum_of_even_digits

    # Return True if total modulo 10 is zero — meaning the number is valid per Luhn
    return total % 10 == 0


def main():
    """
    Sanitize the card number input and check its validity.
    """
    # Example card number with dashes (can also include spaces)
    card_number = '4111-1111-4555-1142'

    # Remove non-numeric characters using str.translate() and str.maketrans()
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    # Validate the cleaned card number and print the result
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')


# Entry point of the script
main()
