import os
import pickle


def save_game(p1_boats, p1_attack, cpu_boats, cpu_attack, consecutive_hits, player_ship_count, cpu_ship_count, rounds):
    """
    Save the current state of a game of battleship to a file.

    @param p1_boats: A list representing player 1's boat locations on the game board.
    @type p1_boats: List[List[str, int]]

    @param p1_attack: A list representing player 1's attack locations on the game board.
    @type p1_attack: List[List[str, int]]

    @param cpu_boats: A list representing the CPU's boat locations on the game board.
    @type cpu_boats: List[List[str, int]]

    @param cpu_attack: A list representing the CPU's attack locations on the game board.
    @type cpu_attack: List[List[str, int]]

    @param consecutive_hits: An integer representing the number of consecutive hits the player has made.
    @type consecutive_hits: List[List[int, int]]

    @param player_ship_count: An integer representing the number of ships remaining for player 1.
    @type player_ship_count: int

    @param cpu_ship_count: An integer representing the number of ships remaining for the CPU.
    @type cpu_ship_count: int

    @param rounds: An integer representing the number of rounds played in the game.
    @type rounds: int
    """

    # Build the file path using the os.path.join() function
    file_path = os.path.join('saves', 'game_save.pkl')

    data = {
        'p1_boats': p1_boats,
        'p1_attack': p1_attack,
        'cpu_boats': cpu_boats,
        'cpu_attack': cpu_attack,
        'consecutive_hits': consecutive_hits,
        'player_ship_count': player_ship_count,
        'cpu_ship_count': cpu_ship_count,
        'rounds': rounds
    }

    with open(file_path, 'wb') as f:
        pickle.dump(data, f)


def load_game():
    """
    Load the saved state of a game of battleship from a file.

    @return: the saved state of the game, including player 1's boat locations, player 1's attack locations,
     CPU's boat locations, the CPU's attack locations, the number of consecutive hits made by the player,
     the number of ships remaining for each player, and the number of rounds played in the game.
    @rtype: List[List[str, int]], List[List[str, int]], List[List[str, int]], List[List[str, int]],
    List[List[int, int]], int, int
    """

    # Build the file path using the os.path.join() function
    file_path = os.path.join('saves', 'game_save.pkl')

    # Open the saved game file and load the data using pickle
    with open(file_path, 'rb') as f:
        data = pickle.load(f)

    # Extract the saved game data from the dictionary
    p1_boats = data['p1_boats']
    p1_attack = data['p1_attack']
    cpu_boats = data['cpu_boats']
    cpu_attack = data['cpu_attack']
    consecutive_hits = data['consecutive_hits']
    player_ship_count = data['player_ship_count']
    cpu_ship_count = data['cpu_ship_count']
    rounds = data['rounds']

    # Return the saved game data
    print(p1_boats, p1_attack, cpu_boats, cpu_attack, consecutive_hits, player_ship_count, cpu_ship_count, rounds)
    return p1_boats, p1_attack, cpu_boats, cpu_attack, consecutive_hits, player_ship_count, cpu_ship_count, rounds


def clear_save_data():
    """
    Overwrites the save_game data with -1
    """
    # Use pickle to save the data to a file
    with open('saves/game_save.pkl', 'wb') as file:
        pickle.dump(-1, file)


def check_save_data():
    """
    Reads the data from the 'saves/game_save.pkl' file and checks if it is valid.

    @return: True if the data is valid, False otherwise.
    @rtype: bool
    """
    # Read the data back into the program
    with open('saves/game_save.pkl', 'rb') as file:
        data = pickle.load(file)
        if data != -1:
            return True
