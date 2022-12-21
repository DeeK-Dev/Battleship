"""
Terminal-based game of battleship.

@author: K Davis
@version: 1.0
"""

# import functions from other modules
from generators import new_game_data, clear
from text_handler import game_intro, menu
from ship_positions import set_ship_positions
from game_loop import game_loop
from file_handlers import load_game, check_save_data

# constant for the size of the game board
BOARD_SIZE = 10

# constant for the number of ships
GAME_SHIPS = (
    ("Carrier", 5),
    ("Battleship", 4),
    ("Cruiser", 3),
    ("Submarine", 3),
    ("Destroyer", 2)
)
while True:
    ready_player_one = False
    while not ready_player_one:
        # display menu and get user selection
        user_select = int(menu())

        if user_select == 1:
            # display game introduction
            game_intro(BOARD_SIZE)
            # generate initial game data
            player_ships, player_attacks, cpu_ships, cpu_attacks, player_ship_count, cpu_ship_count, consecutive_hits, rounds = new_game_data(
                BOARD_SIZE, GAME_SHIPS)
            # set player ship positions
            set_ship_positions(player_ships, True, GAME_SHIPS)
            # set CPU ship positions
            set_ship_positions(cpu_ships, False, GAME_SHIPS)
            ready_player_one = True
        elif user_select == 2:
            # check if saved game data is available
            if check_save_data():
                # load saved game data
                player_ships, player_attacks, cpu_ships, cpu_attacks, consecutive_hits, player_ship_count, cpu_ship_count, rounds = \
                    load_game()
                ready_player_one = True
            else:
                print("No save found.")
                # Clear the terminal
                clear(2)
        elif user_select == 3:
            print("Not yet implemented")
            clear(2)

        # start game loop
    game_loop(BOARD_SIZE, player_ships, player_attacks, cpu_ships, cpu_attacks,
              player_ship_count, cpu_ship_count, consecutive_hits, rounds)
