def merge_sort(array):
    """
    Recursively sorts an array using the Merge Sort algorithm.

    Parameters:
        array (list): The list of numbers to sort

    Returns:
        None: The input list is sorted in place
    """
    # Base case: a list of 0 or 1 elements is already sorted
    if len(array) <= 1:
        return

    # Find the midpoint to divide the array into two halves
    middle_point = len(array) // 2
    left_part = array[:middle_point]  # Left half
    right_part = array[middle_point:]  # Right half

    # Recursively sort both halves
    merge_sort(left_part)
    merge_sort(right_part)

    # Initialize indices for merging
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    # Merge the two halves into the original array
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        # If current element in left_part is smaller, place it in the array
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    # Copy any remaining elements from left_part
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1

    # Copy any remaining elements from right_part
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1


if __name__ == '__main__':
    # Sample unsorted array
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]

    print('Unsorted array: ')
    print(numbers)

    # Perform merge sort
    merge_sort(numbers)

    # Output the sorted array
    print('Sorted array: ' + str(numbers))
