from generators import display_grid, generate_grid


def title():
    print("██████╗  █████╗ ████████╗████████╗██╗     ███████╗██████╗  ██████╗  █████╗ ████████╗███████╗██╗")
    print("██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝██║")
    print("██████╔╝███████║   ██║      ██║   ██║     █████╗  ██████╔╝██║   ██║███████║   ██║   ███████╗██║")
    print("██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝  ██╔══██╗██║   ██║██╔══██║   ██║   ╚════██║╚═╝")
    print("██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗██████╔╝╚██████╔╝██║  ██║   ██║   ███████║██╗")
    print("╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝")


def game_intro(board_size):
    title()
    print()
    print("Welcome to the game of battleships!")
    print(f"In this game, you and your opponent will each have a grid of squares"
          f" on which you will place your battleships.")
    display_grid(generate_grid(board_size))
    print(f"The objective of the game is to sink all of your "
          f"opponent's battleships before they sink all of yours.")
    print(f"Each turn, you and your opponent will take turns "
          f"guessing the coordinates of the other player's battleships.")
    print(f"If you guess correctly, you will score a hit "
          f"and one of your opponent's battleships will be marked as sunk.")
    print(f"The first player to sink all of their opponent's battleships wins the game.")
    print(f"Are you ready to play? Let's get started!\n\n---------------")


def menu():
    """
    Display the main menu for the game and handle user input.
    """
    print("Welcome to Battleships!")
    # Display the menu options
    print("--- Main Menu ---")
    print("1. New game")
    print("2. Load game")
    print("3. Options")
    print("4. Exit")

    valid_option = False
    while not valid_option:
        # Get user input for the menu option
        option = input("Enter the number for your selection: ")

        # Handle the user's menu selection
        if option in {"1", "2", "3"}:
            return option
        elif option == "4":
            # Exit the game
            print("Exiting game...")
            exit()
        else:
            # Invalid selection, display an error message and display the menu again
            print("Invalid selection. Please try again.")

