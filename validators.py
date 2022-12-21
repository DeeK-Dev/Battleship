from time import sleep
from generators import clear


def get_coordinates(board, boat_size):
    """
    Prompt the user to enter coordinates for a ship and validate the input.

    @param board: the game board
    @type board: list of lists of str
    @param boat_size: the size of the ship
    @type boat_size: int
    @return: the coordinates of the two ends of the ship
    @rtype: tuple of int
    """
    valid = False
    while not valid:
        try:
            # prompt user to enter x-coordinate of first end of ship
            x1 = row_to_num("Enter the x-coordinate of the first end of the ship: ")
            # prompt user to enter y-coordinate of first end of ship
            y1 = check_integer("Enter the y-coordinate of the first end of the ship: ")
            # prompt user to enter x-coordinate of second end of ship
            x2 = row_to_num("Enter the x-coordinate of the second end of the ship: ")
            # prompt user to enter y-coordinate of second end of ship
            y2 = check_integer("Enter the y-coordinate of the second end of the ship: ")

            # check if any of the coordinates are empty
            if any(val == "" for val in (x1, y1, x2, y2)):
                valid = False
                raise ValueError()
            # check if the coordinates are valid
            valid = check_coordinates(board, x1, y1, x2, y2, boat_size)

        except ValueError as e:
            print(e)
            print("Enter coordinates again")

    # return the coordinates
    return x1, y1, x2, y2


def check_coordinates(board, x1, y1, x2, y2, size):
    """
    Check if the given coordinates are valid for placing a ship on the board.

    @param board: the game board
    @type board: List[List[str, int]]
    @param x1: the x-coordinate of the first end of the ship
    @type x1: int
    @param y1: the y-coordinate of the first end of the ship
    @type y1: int
    @param x2: the x-coordinate of the second end of the ship
    @type x2: int
    @param y2: the y-coordinate of the second end of the ship
    @type y2: int
    @param size: the size of the ship
    @type size: int
    @return: True if the coordinates are valid, False otherwise
    @rtype: bool
    @raise ValueError: if the ship overlaps with any existing ships
    """
    valid = True
    # Check if coordinates are valid
    if any(val < 0 or val >= len(board) for val in (x1, y1, x2, y2)):
        print("Invalid coordinates!")
        valid = False

    # Calculate the difference between the coordinates
    dx, dy = abs(x1 - x2), abs(y1 - y2)

    # Check if ship fits on board
    if dx == 0 and dy + 1 == size:
        # Ship is vertical
        pass
    elif dy == 0 and dx + 1 == size:
        # Ship is horizontal
        pass
    else:
        print("Invalid ship placement!")
        valid = False

    # Check if ship overlaps with any existing ships
    for i in range(min(x1, x2), max(x1, x2) + 1):
        for j in range(min(y1, y2), max(y1, y2) + 1):
            if board[j][i] != "~":
                raise ValueError("Invalid ship placement! Ship already occupies a space")
                valid = False
    return valid


def check_integer(msg):
    """
    Prompt the user to enter a single integer and validate the input.

    @param msg: the prompt message to display to the user
    @type msg: str
    @return: the user-entered integer
    @rtype: int
    """
    while True:
        try:
            value = int(input(msg))
        except ValueError:
            print("Invalid input: input must be an integer")
            continue
        if isinstance(value, int) and len(str(value)) == 1:
            return value
        else:
            print("Invalid input: input must be a single integer")


def row_to_num(msg):
    """
    Prompt the user to enter a letter representing a row on the game board and convert it to a number.

    @param msg: the prompt message to display to the user
    @type msg: str
    @return: the numeric representation of the row
    @rtype: int
    """
    while True:
        row = input(msg)
        # Convert the row string to uppercase
        try:
            row = row.upper()
        except AttributeError:
            print("Invalid input: Please enter a single letter")
            continue
        if len(row) == 1 and "A" <= row <= "J":
            # Convert the row string to a number (A is 0, B is 1, etc.)
            return ord(row) - ord("A")
        else:
            print("Invalid input. Must be between A and J (inclusive)")
