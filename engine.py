from items_and_characters import ITEMS
import random
from copy import deepcopy


WALLS = ['░']
ROW = 0
COLUMN = 1
ICONS = [item["icon"] for item in ITEMS]
items = ITEMS.deepcopy()


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


def create_stats_scroll(player, height) -> list:
    stats_scroll = ['  _______________________', '=(__    ___      __     _)=', '  |                     |']
    for k in player:
        row = f'  | {k}: {player[k]}'
        while len(row) != len(' _______________________'):
            row += ' '
        row += '|'
        stats_scroll.append(row)
    stats_scroll.append('  |__    ___   __    ___|')
    stats_scroll.append('=(_______________________)=')
    while len(stats_scroll) != height:
        stats_scroll.append('')
    return stats_scroll


def put_player_on_board(board, player):
    row, column = player["position"][ROW], player["position"][COLUMN]
    board[row][column] = player["icon"]
  


def put_npc_on_board(board, npc):
    for i in range(len(npc)):
        row, column = npc[i]["position"][ROW], npc[i]["position"][COLUMN]
        board[row][column] = npc[i]["icon"]
  

def put_items_on_board(board, item):
    for i in range(len(item)):
        for num in range(item[i]['total amount']):
            while True:
                column = random.randint(1, len(board[ROW])-1)
                row = random.randint(1, len(board)-1)
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
  

def is_interaction_with_item(board, player):
    if board(player["field"]) in ICONS:
        return True
    return False


def get_item(board, coords):
    if board[coords[0]][coords[1]] in ICONS:
        for item in items:
            if board[coords[0]][coords[1]] == item["icon"]:
                return item


def interaction_with_item(board, player):
    if is_interaction_with_item(board, player):
        item = get_item(board, player["field"])
        item["total amount"] -= 1
        player["energy"] += item["effect"]["energy"]
        player["knowledge"] += item["effect"]["knowledge"]
         


def get_npc_direction(npc, board):
    dirction = "WASD"
    key = random.choice(dirction)
    #move(npc, board, key)
    return key

