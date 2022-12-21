from generators import display_grid, clear
from turn_handler import cpu_turn, player_turn
from file_handlers import save_game, clear_save_data


def game_loop(board_size, player_ships, player_attack, cpu_ships, cpu_attack,
              player_ship_count, cpu_ship_count, consecutive_hits, rounds):
    """
    Run the main game loop for a game of battleship.

    @param board_size: An integer representing the size of the game board.
    @type board_size: int

    @param player_ships: A list representing the locations of the player's ships on the game board.
    @type player_ships: List[List[str, int]]

    @param player_attack: A list representing the locations that the player has attack on the game board.
    @type player_attack: List[List[str, int]]

    @param cpu_ships: A list representing the locations of the CPU's ships on the game board.
    @type cpu_ships: List[List[str, int]]

    @param cpu_attack: A list representing the locations that the CPU has attack on the game board.
    @type cpu_attack: List[List[str, int]]

    @param player_ship_count: An integer representing the number of ships remaining for the player.
    @type player_ship_count: int

    @param cpu_ship_count: An integer representing the number of ships remaining for the CPU.
    @type cpu_ship_count: int

    @param consecutive_hits: An integer representing the number of consecutive hits made by the player.
    @type consecutive_hits: List[List[int, int]]

    @param rounds: An integer representing the number of rounds played in the game.
    @type rounds: int
    """

    options = []
    # print the initial game board
    game_over = False

    # loop until the game is over
    while not game_over:
        # switch the current player
        if rounds % 2 == 1:
            current_player = "cpu"
            display_grid(cpu_attack)
            # handle the CPU's turn
            cpu_attack, player_ship_count, consecutive_hits = cpu_turn(player_ships, cpu_attack,
                                                                       board_size, player_ship_count,
                                                                       consecutive_hits)
        else:
            current_player = "player"
            # handle the player's turn
            display_grid(player_attack)
            player_attack, cpu_ship_count = player_turn(cpu_ships, player_attack, board_size, cpu_ship_count)

        # print the updated game board

        rounds += 1
        game_over = (player_ship_count == 0) or (cpu_ship_count == 0)
        save_game(player_ships, player_attack, cpu_ships, cpu_attack, consecutive_hits, player_ship_count,
                  cpu_ship_count, rounds)
        clear(3)

    # print a message to indicate who won the game
    if current_player == "player":
        print("You won!")
        clear(5)
    else:
        print("The CPU won :(")
        clear(5)
    clear_save_data()
