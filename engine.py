from items_and_characters import ITEMS, NPCS
import random
import ui
from os.path import exists


EMPTY = " "
ROW = 0
ICONS = [item["icon"] for item in ITEMS]
NPC_ICONS = [npc["icon"] for npc in NPCS]
PLAYER_OBSTACLES = ['░'] + NPC_ICONS
NPC_OBSTACLES = ['░', "\\", "☻"] + ICONS + NPC_ICONS
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
    add_walls(board, level = 1)    #Dodać wywoływanie odpowiedniego levelu
    return board


def add_walls(board, level):
    if level == 1:
        walls_level_1(board)
    elif level == 2:
        walls_level_2(board)    
    elif level == 3:
        walls_level_3(board)


def walls_level_1(board):
    for i in range(len(board) - 1):
        if i %5 != 0 and i < 17 :
            board[i][8] = "░"
    for i in range(len(board[0]) - 1):
        if i >= 9:
            board[16][i] = "░" 
            board[12][i] = "░"
            board[8][i] = "░"
            if i != 28 and i != 27:
                board[3][i] = "░"
    board[10][22] = "░"
    board[11][22] = "░"


def walls_level_3(board):   
    for i in range(len(board[0])):
        if i < 14 or i > 16:
            board[5][i] = "░"
        if i <= 8 and i >= 2:
            board[14][i] = "░"
    for i in range(len(board)):
        if i > 14:
            board[i][8] = "░"
    

def walls_level_2(board):  
    for i in range(len(board)):
        if i % 4 == 0:
            for j in range(len(board[0]) - 1):
                if j < 13 or j > 16:
                    board[i][j] = "░"
        if i % 4 != 0 and i in range(0,16):
            board[i + 2][12] = "░"
            board[i + 2][17] = "░"
    board[1][12] = "░"
    board[1][17] = "░"


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
    row, column = character["field"]
    new_row, new_column = get_new_coords(row, column, key)
    obstacles = PLAYER_OBSTACLES if character == player else NPC_OBSTACLES
    if is_move_valid(board, new_row, new_column, obstacles):
        if board[new_row][new_column] in ICONS and character == player:
            interaction_with_item(board, player, items, new_row, new_column)
        board[row][column] = EMPTY
        character["field"] = (new_row, new_column)
        board[new_row][new_column] = character["icon"]

        
        


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
        player["inventory"][item["name"]] += 1

    
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
    print("smartness ", smartness)
    basic_prob = npc["probability"]
    weapon_amount = weapon[1]
    print("weapon ", weapon)
    success_prob = min(1, (smartness + weapon_amount) * 0.25 + basic_prob)
    print("probability of success ", success_prob)
    failure_prob = max(0, 1 - ((smartness + weapon_amount) * 0.25 + basic_prob))
    print("probability of failure ", failure_prob)
    result = [True, False]
    weights = [success_prob, failure_prob]
    success = random.choices(result, weights)
    print("success ", success[0])
    return success[0] #success is one-element list that contains the result


def find_item_by_name(name):
    for item in ITEMS:
        if item["name"] == name:
            return item


def interaction_with_npc(board, player, npcs):
    if is_interaction_with_npc(player, board):
        print("player before interaction  ", player)
        npc = get_npc(player, npcs)
        # print some dialog window
        # player choose wheapon
        weapon = ui.choose_weapon(player)
        player["inventory"][weapon[0]] -= weapon[1] # after the "weapon" is choosen it is removed from inventory
        player["energy"] -= npc["energy damage"]
        if will_player_succeed(player, npc, weapon):
            name = npc["attribute"]
            item = find_item_by_name(name)
            print("player before interaction  ", player)
            update_player(player, item)
            # player["inventory"][weapon[0]] -= weapon[1] # uncomment this line (and comment the line before if-block) if we decide that user don't loose his "weapon" in case of failure but looses in case of success
            row, column = npc["field"] 
            board[row][column] = EMPTY 
            npcs.remove(npc)
        print("player after interaction  ", player)

        
def play_new_game():
    if not exists('savegame.db'):   
        return True
    else:
        return ui.select_game_state()

def create_intro_scroll(intro_text):
    line = "  " + "_"*66
    roller ="=(" + "___  ___"*8 + "__)="
    scroll = []
    scroll.append(line)
    scroll.append(roller)
    scroll.append("  |" + " "*64 + '| ')
    for line in intro_text:
        row = "  |" + line.center(64) + '| '
        scroll.append(row)
    scroll.append("  |" + "___  ___"*8 + "|")
    scroll.append('=(' + "_"*66 + ')=')
    return scroll
