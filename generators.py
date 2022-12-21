import subprocess
from random import randint
from time import sleep

from colorama import Fore, Back, Style


def generate_grid(board_size):
    """
    Generate a new game board as a 2D list of size `board_size` x `board_size`,
    where each element is initialized to the value "~".

    @param board_size: The size of the game board.
    @type board_size: int

    @return: The new game board.
    @rtype: List[List[str]]
    """
    # generate and assign "~" to all elements in a new list
    return [["~" for _ in range(board_size)] for _ in range(board_size)]


def display_grid(grid):
    """
    Display the game board represented by the given 2D list `grid`.

    @param grid: The game board to display.
    @type grid: List[List[str]]
    """
    # Print the column labels
    print("     A   B   C   D   E   F   G   H   I   J")

    # Iterate over the rows of the grid
    for i, row in enumerate(grid):
        # Print the row label
        print(f" {i} |", end="")

        # Iterate over the elements of the row
        for j, element in enumerate(row):
            # Print the element, followed by a "|" character
            if element == "H":
                print(f" {Fore.RED}{Back.RED}{element}{Style.RESET_ALL} |", end="")
            else:
                print(f" {element} |", end="")

        # Print a newline to move to the next row
        print()

        # Print a horizontal line to separate the rows
        print("   -----------------------------------------")


def cpu_placement_coordinates(board_size, ship_size):
    """
    Generate random coordinates for the CPU to place a ship of size `ship_size` on the game board of size `board_size`.

    @param board_size: The size of the game board.
    @type board_size: int

    @param ship_size: The size of the ship to place.
    @type ship_size: int

    @return: The coordinates of the start and end points of the ship.
    @rtype: Tuple[int, int, int, int]
    """
    ship_dir = randint(0, 1)  # generate a random number to determine the direction of the ship
    if ship_dir == 0:  # if the ship is horizontal
        x1 = randint(0, board_size - 1 - ship_size)  # generate random x coordinate for the start point
        y1 = randint(0, board_size - 1)  # generate random y coordinate for the start point
        x2 = x1 + ship_size - 1  # calculate x coordinate for the end point
        y2 = y1  # y coordinate for the end point is the same as the start point
    else:  # if the ship is vertical
        x1 = randint(0, board_size - 1)  # generate random x coordinate for the start point
        y1 = randint(0, board_size - 1 - ship_size)  # generate random y coordinate for the start point
        x2 = x1  # x coordinate for the end point is the same as the start point
        y2 = y1 + ship_size - 1  # calculate y coordinate for the end point

    return x1, y1, x2, y2  # return the coordinates of the start and end points


def ship_calc(game_ships):
    """
    Calculate the total number of ship units in the given list of ships.

    @param game_ships: A list of ships, where each ship is a tuple of the form (ship_type, ship_size).
    @type game_ships: List[Tuple[str, int]]

    @return: The total number of ship units.
    @rtype: int
    """
    total = 0  # initialize total to 0
    # iterate over all ships in the list
    for ship in game_ships:
        total += ship[1]  # add the size of the current ship to the total
    return total  # return the total number of ship units


def get_adjacent_coordinates(center, board_size):
    """
    Get the coordinates of all cells adjacent to the given `center` cell on the game board of size `board_size`.

    @param center: The center cell whose adjacent cells are to be returned.
    @type center: Tuple[int, int]

    @param board_size: The size of the game board.
    @type board_size: int

    @return: The coordinates of the adjacent cells.
    @rtype: List[Tuple[int, int]]
    """
    adjacent_coordinates = []  # initialize empty list to store adjacent coordinates
    # iterate over all cells within a range of -1 to 1 from the center cell
    for i in range(-1, 2):
        for j in range(-1, 2):
            x = center[0] + i  # calculate x coordinate of the current cell
            y = center[1] + j  # calculate y coordinate of the current cell
            # if the current cell is within the boundaries of the game board, add it to the list of adjacent coordinates
            if (0 <= x < board_size - 1) and (0 <= y < board_size - 1):
                adjacent_coordinates.append((x, y))
    return adjacent_coordinates  # return the list of adjacent coordinates


def new_game_data(board_size, ships):
    """
    Generates the data for a new game of battleship.

    @param board_size: The size of the board for the game
    @type board_size: int

    @param ships: The number and size of ships for the game
    @type ships: List[int]

    @return: A tuple containing the following data for the game:
        - player_ships: A list representing the player's ships on the board
        - player_attacks: A list representing the player's attacks on the board
        - cpu_ships: A list representing the CPU's ships on the board
        - cpu_attacks: A list representing the CPU's attacks on the board
        - player_ship_count: The number of ships the player has remaining (integer)
        - cpu_ship_count: The number of ships the CPU has remaining (integer)
        - consecutive_hits: A list of consecutive hits made by the player (empty at the start of the game)
        - rounds: The number of rounds played in the game (integer, starts at 0)
    """
    # Generate lists representing the player's and CPU's ships and attacks on the board
    player_ships = list(generate_grid(board_size))
    player_attacks = list(generate_grid(board_size))
    cpu_ships = list(generate_grid(board_size))
    cpu_attacks = list(generate_grid(board_size))

    # Calculate the number of ships the player and CPU have
    player_ship_count = int(ship_calc(ships))
    cpu_ship_count = int(ship_calc(ships))

    # Initialize an empty list to store consecutive hits
    consecutive_hits = []

    # Set the number of rounds played to 0
    rounds = 0

    # Return the generated data as a tuple
    return player_ships, player_attacks, cpu_ships, cpu_attacks, player_ship_count, cpu_ship_count, consecutive_hits, rounds


def clear(sec):
    sleep(sec)
    subprocess.call('clear', shell=True)
