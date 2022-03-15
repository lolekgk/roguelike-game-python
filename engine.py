from util import key_pressed
import random


WALLS = ['░']
PLAYER_ICON = '☺'
PLAYER_START_X = 3
PLAYER_START_Y = 3


def create_board(width, height):
    board = []
    board.append(['░' for i in range(width)])
    for i in range(height - 2):
        row = [' ' for i in range(width - 2)]
        row.insert(0, '░')
        row.append('░')
        board.append(row)
    board.append(['░' for i in range(width)])
    board[random.randint(1, height-2)][-1] = 'B'
    return board


def put_player_on_board(board, player):
    board[PLAYER_START_X][PLAYER_START_Y] = PLAYER_ICON
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''


def put_npc_on_board(board, npc):
    '''randomowe rozmieszczenie postaci npc'''
    while True:
        y = random.randint(0, len(board[0])-1)
        x = random.randint(0, len(board)-1)
        if board[x][y] == ' ':
            board[x][y] = 'n'
            break 


def put_items_on_board(board, item):
    '''randomowe rozmieszczenie przedmiotow'''
    while True:
        y = random.randint(0, len(board[0])-1)
        x = random.randint(0, len(board)-1)
        if board[x][y] == ' ':
            board[x][y] = 'i'
            break 


def is_put_on_board_valid(board, x, y):
    if board[x][y] == ' ':
        return True
    return False


def is_move_valid(board, new_row, new_column):
    if board[new_row][new_column] in WALLS:
        return False
    return True


def player_move(board, key):
    (row, column) = player["field"]
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
        player["field"] = (new_row, new_column)
    

def npc_move():
    pass



board = create_board(30, 20)
put_player_on_board(board, 1)

def display_board(board):
    for row in board:
        print(''.join(row))

# player = {"field":(2,2)}
put_npc_on_board(board, 1)
put_items_on_board(board, 1)
display_board(board)      


