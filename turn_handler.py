from random import randint
from validators import row_to_num, check_integer
from generators import get_adjacent_coordinates
from time import sleep


# function to handle the players turn
def player_turn(cpu_ships, player_attacks, board_size, cpu_ship_count):
    """
    Execute the player's turn in the game.

    @param cpu_ships: The positions of the computer's ships on the board.
    @type cpu_ships: List[List[str]]
    @param player_attacks: The positions that the player has already attacked on the board.
    @type player_attacks: List[List[str]]
    @param board_size: The size of the game board.
    @type board_size: int
    @param cpu_ship_count: The number of ships that the computer has remaining on the board.
    @type cpu_ship_count: int
    @return: The updated player attacks and the updated number of CPU ships remaining on the board.
    @rtype: List[List[str]], int]
    """

    valid = False
    while not valid:
        valid = True
        print("Player's turn")

        # prompt the player for their guess
        x = row_to_num("Enter the x-coordinate: ")
        y = check_integer("Enter the y-coordinate: ")

        # check if the guess is within the valid range of the board
        if x < 0 or x > board_size - 1 or y < 0 or y > board_size - 1:
            print("Invalid coordinates. Please try again.")
            valid = False

        # check if the player has already guessed this spot
        if player_attacks[y][x] == "O":
            print("You have already guessed this spot. Please try again.")
            valid = False

    # check if the guess is a hit or a miss
    if cpu_ships[y][x] == "S":
        # if it is a hit, decrement the count of CPU ships and update the board to reflect the hit
        cpu_ship_count -= 1
        player_attacks[y][x] = "H"
        print("Hit!")
    else:
        # if it is a miss, update the board to reflect the miss
        player_attacks[y][x] = "O"
        print("Miss!")

    return player_attacks, cpu_ship_count


# function to handle the CPU's turn
def cpu_turn(player_ships, cpu_attack, board_size, player_ship_count, consecutive_hits):
    """
    Execute the computer's turn in the game.

    @param player_ships: The positions of the player's ships on the board.
    @type player_ships: List[List[str]]
    @param cpu_attack: The positions that the computer has already attacked on the board.
    @type cpu_attack: List[List[str]]
    @param board_size: The size of the game board.
    @type board_size: int
    @param player_ship_count: The number of ships that the player has remaining on the board.
    @type player_ship_count: int
    @param options: A list of tuples representing coordinates around the last hit location.
    @type options: List[Tuple[int, int]]
    @param consecutive_hits: A list of tuples representing consecutive hit locations.
    @type consecutive_hits: List[Tuple[int, int]]
    @return: The updated computer attacks, the updated number of player ships remaining on the board, the updated list
    of options, and the updated list of consecutive hits.
    @rtype: List[List[str]], int, List[Tuple[int, int]], List[Tuple[int, int]]]
    """
    print("CPU's turn")

    # get a list of adjacent coordinates to the last hit location
    options = get_adjacent_coordinates(consecutive_hits[-1], board_size) if consecutive_hits else []

    valid = False
    while not valid:
        valid = True

        # generate random coordinates for the CPU's guess if there are no consecutive hits
        if not options:
            x = randint(0, board_size - 1)
            y = randint(0, board_size - 1)
        else:
            # select the first item in the options list
            x = options[0][0]
            y = options[0][1]

        # check if the guess is within the bounds of the board and has not been guessed before
        if x < 0 or x > board_size - 1 or y < 0 or y > board_size - 1 or cpu_attack[x][y] in {"O", "H"}:
            valid = False

        # remove the first item from the options list if the guess is not valid and the options list is not empty
        if not valid and options:
            options.pop(0)
        elif not valid and not options:
            consecutive_hits.pop()
            if consecutive_hits:
                options = get_adjacent_coordinates(consecutive_hits[-1], board_size)

    sleep(3)
    print(f"{chr(y+ord('A'))}, {x}")
    sleep(1)

    # check if the guess is a hit
    if player_ships[x][y] == "S":
        # reduce the player's ship count by 1 and update the board to reflect the hit
        player_ship_count -= 1
        cpu_attack[x][y] = "H"
        consecutive_hits.append([x, y])

        print("Hit!")
    else:
        # update the board to reflect the miss
        cpu_attack[x][y] = "O"
        if options:
            options.pop(0)
        elif consecutive_hits:
            consecutive_hits.pop()

        print("Miss!")

    return cpu_attack, player_ship_count, consecutive_hits
