from util import key_pressed

def create_board(width, height):
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
    pass


def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    pass

player = {"field":(2,2)}

board = [["0", "0", "0", "0"], ["0", ".", ".", "0"], ["0", ".", ".", "0"], ["0", "0", "0", "0"]]
WALL = ["0"]
#print(board)

def is_move_valid(board, new_row, new_column):
    if board[new_row][new_column] in WALL:
        return False
    return True


def player_move(board):
    direction = key_pressed().upper()
    #print(direction)
    (row, column) = player["field"]
    if direction == "W":
        new_row, new_column = row - 1, column
    elif direction == "A":
        new_row, new_column = row, column - 1
    elif direction == "S":
        new_row, new_column = row + 1, column
    elif direction == "D":
        new_row, new_column = row, column + 1
    else:
        new_row, new_column = row, column
    if is_move_valid(board, new_row, new_column):
        player["field"] = (new_row, new_column)
    #print(player)
    

player_move(board)

    


def npc_move():
    pass