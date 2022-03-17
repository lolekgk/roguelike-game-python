from items_and_characters import ITEMS
import random


PLAYER_WALLS = ['░', "♥", "‼"]
NPC_WALLS = ['░', "♥", "‼", "B", "P"]
ROW = 0
COLUMN = 1
ICONS = [item["icon"] for item in ITEMS]
NPC_ICONS = ["♥", "‼"]


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
    (row, column) = player["field"]
    board[row][column] = player["icon"]
  


def put_npcs_on_board(board, npcs):
    for npc in npcs:
        (row, column) = npc["field"]
        board[row][column] = npc["icon"]
  

def put_items_on_board(board, items):
    for item in items:
        for num in range(item['total amount']):
            while True:
                column = random.randint(1, len(board[ROW])-1)
                row = random.randint(1, len(board)-1)
                if is_put_on_board_valid(board, row, column):
                    board[row][column] = item['icon']
                    break 


def is_put_on_board_valid(board, row, column):
    if board[row][column] == ' ':
        return True
    return False


def is_move_valid(board, new_row, new_column, type_walls):
    if board[new_row][new_column] in type_walls:
        return False
    return True


def get_new_coords(row, column, key):
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
    return new_row, new_column


def move(character, board, key, player, items):
    (row, column) = character["field"]
    new_row, new_column = get_new_coords(row, column, key)
    obstacles = PLAYER_WALLS if character == player else NPC_WALLS
    if is_move_valid(board, new_row, new_column, obstacles):
        if board[new_row][new_column] in ICONS and character == player:
            interaction_with_item(board, player, items, new_row, new_column)
        board[row][column] = " "
        character["field"] = (new_row, new_column)
        board[new_row][new_column] = character["icon"]
    
    
def get_item(board, row, col, items):
    if board[row][col] in ICONS:
        for item in items:
            if board[row][col] == item["icon"]:
                return item


def interaction_with_item(board, player, items, row, col):
    item = get_item(board, row, col, items)
    item["total amount"] -= 1
    player["energy"] += item["effect"]["energy"]
    player["knowledge"] += item["effect"]["knowledge"]
    

def is_interaction_with_npc(player, board):
    (row, column) = player["position"]
    if board(row -1, column) in NPC_ICONS or board(row +1, column) in NPC_ICONS \
        or board(row, column - 1) in NPC_ICONS or board(row, column + 1) in NPC_ICONS:
        return True
    return False


def interaction_with_npc(board, player):
    if is_interaction_with_npc(player):
        pass