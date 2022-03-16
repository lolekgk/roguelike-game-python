
from items_and_characters import ITEMS
import random


WALLS = ['░']
ICONS = [item["icon"] for item in ITEMS]


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
    pass

#player = {"field":(2,2)}


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


items = ITEMS.deepcopy()


def is_interaction_with_item(player, board):
    if board(player["field"]) in ICONS:
        return True
    return False


def get_item(coords, board):
    if board[coords[0]][coords[1]] in ICONS:
        for item in items:
            if board[coords[0]][coords[1]] == item["icon"]:
                return item


def interaction_with_item(board, item):
    pass 


def npc_move(npc, board):
    dirction = "WASD"
    key = random.choice(dirction)
    move(npc, board, key)

