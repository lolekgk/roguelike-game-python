from items_and_characters import ITEMS
import random
import items_and_characters


WALLS = ['░']
ROW = 0
COLUMN = 1


def create_board(width, height):
    board = []
    board.append(['░' for i in range(width)])
    for i in range(height - 2):
        row = [' ' for i in range(width - 2)]
        row.insert(0, '░')
        row.append('░')
        board.append(row)
    board.append(['░' for i in range(width)])
    board[-2][-1] = 'B'
    return board


def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    board[PLAYER_START_X][PLAYER_START_Y] = PLAYER_ICON
  


def put_npc_on_board(board, npc):
    '''
    Modifies the game board by placing the NPC icons at their coordinates.

    Args:
    list: The game board
    list of dictionaries: The NPC information containing the icons and coordinates

    Returns:
    Nothing
    '''
    for i in range(len(npc)):
        row, column = npc[i]["position"][ROW], npc[i]["position"][COLUMN]
        board[row][column] = npc[i]["icon"]
  

def put_items_on_board(board, item):
    '''
    Modifies the game board by placing the items icons at their coordinates.

    Args:
    list: The game board
    list of dictionaries: The items information containing the icons and coordinates

    Returns:
    Nothing
    '''
    for i in range(len(item)):
        for num in range(item[i]['total amount']):
            while True:
                column = random.randint(0, len(board[ROW])-1)
                row = random.randint(0, len(board)-1)
                if is_put_on_board_valid(board, row, column):
                    board[row][column] = item[i]['icon']
                    break 


def is_put_on_board_valid(board, row, column):
    if board[row][column] == ' ':
        return True
    return False


def is_move_valid(board, new_row, new_column):
    if board[new_row][new_column] in WALLS:
        return False
    return True


def move(character, board, key):
    (row, column) = character["field"]
    if key == "W":
        new_row, new_column = row - 1, column
    elif key == "A":
        new_row, new_column = row, column - 1
    elif key == "S":
        new_row, new_column = row + 1, column
    elif key == "D":
        new_row, new_column = row, column + 1
    else:
        new_row, new_column = row, column
    if is_move_valid(board, new_row, new_column):
        character["field"] = (new_row, new_column)

    

def npc_move():
    pass
 

def is_interaction_with_item(player, board):
    icons = [item["icon"] for item in ITEMS]
    if board(player["field"]) in icons:
        return True
    return False


def interaction_with_item(board):
    pass


def npc_move(npc, board):
    dirction = "WASD"
    key = random.choice(dirction)
    move(npc, board, key)

