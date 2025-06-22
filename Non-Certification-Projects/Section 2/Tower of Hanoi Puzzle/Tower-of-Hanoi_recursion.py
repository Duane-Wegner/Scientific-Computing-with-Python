# Define the total number of disks to move in the Tower of Hanoi puzzle
NUMBER_OF_DISKS = 5

# Initialize the three rods: A holds all disks initially; B and C are empty
A = list(range(NUMBER_OF_DISKS, 0, -1))  # Source rod
B = []  # Auxiliary rod
C = []  # Target rod


def move(n, source, auxiliary, target):
    """
    Recursively moves n disks from the source rod to the target rod
    using the auxiliary rod as a helper.

    Parameters:
        n (int): Number of disks to move
        source (list): Rod holding the disks to move
        auxiliary (list): Helper rod used in the process
        target (list): Destination rod where disks should end up
    """
    if n <= 0:
        return  # Base case: no disks left to move

    # Step 1: move top n - 1 disks from source to auxiliary
    move(n - 1, source, target, auxiliary)

    # Step 2: move the nth (largest remaining) disk to target
    target.append(source.pop())

    # Display the current state of the rods after each move
    print(A, B, C, '\n')

    # Step 3: move the n - 1 disks from auxiliary to target
    move(n - 1, auxiliary, source, target)


# Begin solving the puzzle by moving all disks from rod A to rod C
move(NUMBER_OF_DISKS, A, B, C)
