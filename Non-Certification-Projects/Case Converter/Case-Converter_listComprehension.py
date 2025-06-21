def convert_to_snake_case(pascal_or_camel_cased_string):
    """
    Convert a PascalCase or camelCase string into snake_case.

    Args:
        pascal_or_camel_cased_string (str): The input string in PascalCase or camelCase format.

    Returns:
        str: The converted snake_case string.
    """

    # Build a list of characters by inserting an underscore before each uppercase letter
    # and converting it to lowercase. Leave all other characters unchanged.
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    # Join the character list into a single string and remove any leading underscores
    return ''.join(snake_cased_char_list).strip('_')


def main():
    # Test the case conversion function with a sample PascalCase string
    print(convert_to_snake_case('IAmAPascalCasedString'))


# Entry point of the script
main()
