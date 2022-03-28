from items_and_characters import ITEMS
import random
import ui


PLAYER_WALLS = ['░', "♥", "‼"]
NPC_WALLS = ['░', "♥", "‼", "\\", "☻"]
EMPTY = " "
ROW = 0
ICONS = [item["icon"] for item in ITEMS]
NPC_ICONS = ["♥", "‼"]
PLAYER_DATA_TO_DISPLAY = ["name", "class", 'knowledge', 'smartness', 'energy', 'exams']


def create_board(width, height):
    board = []
    board.append(['░' for i in range(width)])
    for i in range(height - 2):
        row = [EMPTY for i in range(width - 2)]
        row.insert(0, '░')
        row.append('░')
        board.append(row)
    board.append(['░' for i in range(width)])
    board[-2][-1] = '\\'
    return board


def create_stats_scroll(player, height) -> list:
    stats_scroll = ['  _______________________', '=(__    ___      __     _)=', '  |                     |']
    for k in PLAYER_DATA_TO_DISPLAY:
        row = f'  | {k}: {player[k]}'
        while len(row) != len(' _______________________'):
            row += EMPTY
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
    if board[row][column] == EMPTY:
        return True
    return False


def is_move_valid(board, new_row, new_column, type_walls):
    if board[new_row][new_column] in type_walls:
        return False
    return True


def get_new_coords(row, column, key):
    if key == "E":
        new_row, new_column = row - 1, column
    elif key == "S":
        new_row, new_column = row, column - 1
    elif key == "X":
        new_row, new_column = row + 1, column
    elif key == "D":
        new_row, new_column = row, column + 1
    else:
        new_row, new_column = row, column
    return new_row, new_column


def move(character, board, key, player, items, npcs):
    row, column = character["field"]
    new_row, new_column = get_new_coords(row, column, key)
    obstacles = PLAYER_WALLS if character == player else NPC_WALLS
    if is_move_valid(board, new_row, new_column, obstacles):
        if board[new_row][new_column] in ICONS and character == player:
            interaction_with_item(board, player, items, new_row, new_column)
        board[row][column] = EMPTY
        character["field"] = (new_row, new_column)
        board[new_row][new_column] = character["icon"]
    if is_interaction_with_npc(player, board):
        interaction_with_npc(board, player, npcs)
        


def get_item(board, row, col, items):
    if board[row][col] in ICONS:
        for item in items:
            if board[row][col] == item["icon"]:
                return item


def interaction_with_item(board, player, items, row, col):
    item = get_item(board, row, col, items)  
    item["total amount"] -= 1 # total amount is used only here
    update_player(player, item)
    

def update_player(player, item):
    player["energy"] += item["effect"]["energy"]
    player["knowledge"] += item["effect"]["knowledge"]
    if item["name"] in player["inventory"]:
        player["inventory"]["name"] += 1

    
def is_interaction_with_npc(player, board):
    row, column = player["field"]
    if board[row - 1][column] in NPC_ICONS or board[row + 1][column] in NPC_ICONS \
        or board[row][column - 1] in NPC_ICONS or board[row][column + 1] in NPC_ICONS:
        return True
    return False


def get_npc(player, npcs):
    row, column = player["field"]
    adjacent_fields = [(row + 1, column), (row, column + 1), (row - 1, column),  (row, column - 1), ]
    for npc in npcs:
        if npc["field"] in adjacent_fields:
            return npc


def will_player_succeed(player, npc, weapon):
    smartness = player["smartness"]
    basic_prob = npc["probability"]
    weapon_amount = weapon[1]
    success_prob = min(1, (smartness + weapon_amount) * 0.25 + basic_prob)
    failure_prob = max(0, 1 - ((smartness + weapon_amount) * 0.25 + basic_prob))
    result = [True, False]
    weights = [success_prob, failure_prob]
    return random.choices(result, weights)


def find_item_by_name(name):
    for item in ITEMS:
        if item["name"] == name:
            return item


def interaction_with_npc(board, player, npcs):
    if is_interaction_with_npc(player, board):
        npc = get_npc(player, npcs)
        # print some dialog window
        # player choose wheapon
        weapon = ui.choose_weapon(player)
        if will_player_succeed(player, npc, weapon):
            name = npc["attribute"]
            item = find_item_by_name(name)
            update_player(player, item)
            row, column = npc["field"] 
            board[row][column] = EMPTY 
            npcs.remove(npc)
        player["energy"] += npc["energy damage"]

        