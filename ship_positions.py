from validators import get_coordinates
from generators import display_grid, cpu_placement_coordinates


def set_ship_positions(board, player, ships):
    """
    Set positions for ships on the board.

    @param board: The game board.
    @type board: List[List[int]]
    @param player: Boolean value indicating whether the player or the computer is setting ship positions.
    @type player: bool
    @param ships: List of ships with their names and sizes.
    @type ships: List[Tuple[str, int]]
    """

    # Create a list of ship sizes
    ship_sizes = []
    for i in range(len(ships)):
        ship_sizes.append(ships[i][1])

    # Set positions for ships
    for ship in range(len(ship_sizes)):
        if not player:
            # Get coordinates for computer placement
            x1, y1, x2, y2 = cpu_placement_coordinates(len(board) - 1, ship_sizes[ship])
        else:
            # Get coordinates for player placement
            print(f"Coordinate entry for {ships[ship][0]}")
            x1, y1, x2, y2 = get_coordinates(board, ship_sizes[ship])
        # Place the ship on the board
        place_ship(board, x1, y1, x2, y2)
        # Display the updated board
        display_grid(board)


def place_ship(board, x1, y1, x2, y2):
    """
    Place a ship on the board, starting at (x1, y1) and ending at (x2, y2).

    @param board: The game board.
    @type board: List[List[int]]
    @param x1: The x-coordinate of the starting position of the ship.
    @type x1: int
    @param y1: The y-coordinate of the starting position of the ship.
    @type y1: int
    @param x2: The x-coordinate of the ending position of the ship.
    @type x2: int
    @param y2: The y-coordinate of the ending position of the ship.
    @type y2: int
    """

    # Place ship on board
    if x1 == x2:
        # Ship is vertical
        for y in range(y1, y2 + 1):
            board[y][x1] = "S"
    else:
        # Ship is horizontal
        for x in range(x1, x2 + 1):
            board[y1][x] = "S"
