def arithmetic_arranger(problems, show_answers=False):
    """
    Formats a list of arithmetic problems vertically and side-by-side.

    Args:
        problems (list of str): List of arithmetic problem strings (e.g., "32 + 8").
        show_answers (bool): Whether to include the evaluated results in the final output.

    Returns:
        str: Arranged problems or error message if invalid input.
    """

    # Error if more than 5 problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Lists to hold each line of the formatted problems
    top_line = []
    bottom_line = []
    dash_line = []
    result_line = []

    # Process each problem
    for problem in problems:
        parts = problem.split()

        # Validate problem structure
        if len(parts) != 3:
            return "Error: Invalid problem format."

        left, operator, right = parts

        # Validate operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Validate operands are numbers
        if not left.isdigit() or not right.isdigit():
            return "Error: Numbers must only contain digits."

        # Validate operand length
        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine spacing width (2 extra spaces: one for operator, one for padding)
        width = max(len(left), len(right)) + 2

        # Construct each line
        top_line.append(left.rjust(width))
        bottom_line.append(operator + right.rjust(width - 1))
        dash_line.append('-' * width)

        # Calculate result if requested
        if show_answers:
            result = str(int(left) + int(right)) if operator == '+' else str(int(left) - int(right))
            result_line.append(result.rjust(width))

    # Combine each line with 4 spaces in between
    arranged = '    '.join(top_line) + '\n' + \
               '    '.join(bottom_line) + '\n' + \
               '    '.join(dash_line)

    if show_answers:
        arranged += '\n' + '    '.join(result_line)

    return arranged


# Sample function calls for testing
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])) # Does not show answers
print() # Blank Line
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)) # Shows answers
