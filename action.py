import random
from tkinter import YES
import ui
import main
from items_and_characters import ITEMS, NPCS, BOSS
import util

WALL = f'{ui.bcolors.GRAY}░{ui.bcolors.ENDC}'
EMPTY = " "
ENTRY = f'{ui.bcolors.RED}↑{ui.bcolors.ENDC}'
EXIT = f'{ui.bcolors.GREEN}→{ui.bcolors.ENDC}'
ENTRY_ROW, ENTRY_COLUMN = 0, 15
EXIT_ROW, EXIT_COLUMN = 18, 29
ITEM_ICONS = {item["icon"] for item in ITEMS}
NPC_ICONS = {npc["icon"] for npc in NPCS}
BOSS_ICONS = {char for char in BOSS["icon"]}
PLAYER_OBSTACLES = {WALL} | NPC_ICONS | BOSS_ICONS
NPC_OBSTACLES = {WALL, ENTRY, EXIT, main.PLAYER_ICON} | ITEM_ICONS | NPC_ICONS


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


def get_adjacent_npc(player, npcs):
    row, column = player["field"]
    adjacent_fields = [(row + 1, column), (row, column + 1), (row - 1, column),  (row, column - 1), ]
    for npc in npcs:
        if npc["field"] in adjacent_fields:
            return npc


def get_item_by_name(name):
    for item in ITEMS:
        if item["name"] == name:
            return item


def get_item_by_coords(board, row, col, items):
    if board[row][col] in ITEM_ICONS:
        for item in items:
            if board[row][col] == item["icon"]:
                return item


# MOVEMENT FOR PLAYER AND LEVEL 1-2 NPCS 


def go_through_gate(player):
    player["level"] += 1
    player["field"] = ( ENTRY_ROW + 1, ENTRY_COLUMN)
    

def go_back_through_gate(player):
    player["level"] -= 1
    player["field"] = (EXIT_ROW, EXIT_COLUMN - 1)


def is_move_valid(board, new_row, new_column, obstacles):
    if board[new_row][new_column] in obstacles:
        return False
    return True


def move(character, board, key, player, items):
    row, column = character["field"]
    new_row, new_column = get_new_coords(row, column, key)
    if (new_row, new_column) == (ENTRY_ROW, ENTRY_COLUMN) and player["level"] != 1:
        go_back_through_gate(player)
        return None
    if (new_row, new_column) == (EXIT_ROW, EXIT_COLUMN) \
        and character == player and player["level"] != 3:
        if player["inventory"]["key"] >= player["level"]:
            go_through_gate(player)
        return None
    obstacles = PLAYER_OBSTACLES if character == player else NPC_OBSTACLES
    if is_move_valid(board, new_row, new_column, obstacles):
        if board[new_row][new_column] in ITEM_ICONS and character == player:
            interaction_with_item(board, player, items, new_row, new_column)
        board[row][column] = EMPTY
        character["field"] = (new_row, new_column)
        board[new_row][new_column] = character["icon"]


# INTERACTION LEVEL 1 AND 2


def interaction_with_item(board, player, items, row, col):
    item = get_item_by_coords(board, row, col, items)  
    item["total amount"] -= 1 # total amount is used only here
    update_player_by_item(player, item)
    

def is_interaction_with_npc(player, board):
    row, column = player["field"]
    if board[row - 1][column] in NPC_ICONS or board[row + 1][column] in NPC_ICONS \
        or board[row][column - 1] in NPC_ICONS or board[row][column + 1] in NPC_ICONS:
        return True
    return False


def update_player_by_item(player, item):
    for parameter in item["effect"].keys():
        player[parameter] += item["effect"][parameter]
    if item["name"] in player["inventory"]:
        player["inventory"][item["name"]] += 1


def update_game_if_player_won(board, player, npcs, npc):
    name = npc["attribute"]
    item = get_item_by_name(name)
    update_player_by_item(player, item)
    row, column = npc["field"] 
    board[row][column] = EMPTY 
    npcs.remove(npc)


def get_boolean_with_given_probability(success_prob):
    print("\nThe probability of success was ", success_prob)
    failure_prob = 1 - success_prob
    result = [True, False]
    weights = [success_prob, failure_prob]
    success = random.choices(result, weights)
    ui.display_interaction_effect(success[0])
    return success[0] #success is one-element list that contains the result


def will_player_beat_student(player, npc, weapon):
    smartness = player["smartness"]
    basic_prob = npc["probability"]
    weapon_amount = weapon[1]
    success_prob = min(1, (smartness + weapon_amount) * 0.25 + basic_prob)
    return get_boolean_with_given_probability(success_prob)


def will_player_pass_exam(player, npc, energy, knowledge):
    sum = npc["exam requirement"]["energy"] + npc["exam requirement"]["knowledge"]
    success_prob = (energy + knowledge) / sum 
    return get_boolean_with_given_probability(success_prob)


def interaction_with_student(board, player, npcs):
    student = get_adjacent_npc(player, npcs)
    print(ui.meeting_npc(student))
    weapon = ui.choose_weapon(player, student)
    player["inventory"][weapon[0]] -= weapon[1] # after the "weapon" is choosen it is removed from inventory
    player["energy"] -= student["energy damage"]
    if will_player_beat_student(player, student, weapon):
        update_game_if_player_won(board, player, npcs, student)


def interaction_with_professor(board, player, npcs):
    professor = get_adjacent_npc(player, npcs)
    energy, knowledge = ui.choose_energy_and_knowledge(player, professor)
    print("choosen energy ", energy, " knowledge ", knowledge)
    player["energy"] -= energy
    player["knowledge"] -= knowledge
    if will_player_pass_exam(player, professor, energy, knowledge):
        update_game_if_player_won(board, player, npcs, professor)


# BOSS MOVEMENT AND INTERACTION


def interaction_with_boss(board, player, boss):
    if check_for_boss(player, board):
        print("You are facing the final boss - lady from the dean's office\nShe's on a coffee break right now, and cannot help you\n\nWhat do you want to do? (Type Q to leave)")
        option = None
        while option not in [str(i) for i in range(1, len(player['inventory']) + 1)] + ['Q']:
            option = input(f'\nGive her {[(i + 1, k) for i, k in enumerate(player["inventory"])]} (Type Q to leave) > ')
        while boss["content"] < 5:
            boss_options(player, boss, option)
            if option.upper() == 'Q':
                print('You decide to leave, and try some other time.')
                board[player['field'][0]][player['field'][1]] = EMPTY
                player["field"] = (2, 15) # ensures no interaction right after exiting
                break
            if boss["content"] < 5:
                option = input(f'Give her {[(i + 1, k) for i, k in enumerate(player["inventory"])]} (Type Q to leave) > ')
        if boss['content'] >= 5:
            # win_message()
            print('Wygranko') # placeholder


def boss_options(player, boss, option):
    if option == '1':
        print("Lady from the dean's office doesn't want your beer, and yells at you for bringing it here. (-%s energy)" %(boss['energy damage']*2))
        player['energy'] -= boss['energy damage']
    if option == '2':
        print("Lady from the dean's office has no use for this item. (-%s energy)" %boss['energy damage'])
        player["energy"] -= boss['energy damage']
    if option == '3':
        if player["inventory"]["flowers"] > 0:
            print('The lady likes your flowers, but says she is really busy right now')
            player["inventory"]["flowers"] -= 1
            boss["content"] += 1
        else:
            print("You don't have any flowers!")
    if option == '4':
        if player["inventory"]["chocolates"] > 0:
            print("The lady likes your chocolates, but says she'so na a diet")
            boss["content"] += 1
            player["inventory"]["chocolates"] -= 1
        else:
            print("You don't have any chocolates!")


def check_for_boss(player, board):
    row, column = player["field"]
    if board[row - 1][column] in BOSS_ICONS or board[row + 1][column] in BOSS_ICONS \
        or board[row][column - 1] in BOSS_ICONS or board[row][column + 1] in BOSS_ICONS:
        return True
    return False


def put_boss_on_board(board, boss):
    row, column = boss['field']
    for x in range(5):
        for y in range(5):
            board[row + x][column + y] = boss["face"][x][y]


def move_boss(board, boss):
    direction = main.get_npc_direction()
    row, col = boss['field']
    new_row, new_col = get_new_coords(row, col, direction)
    if new_row > len(board) - 6 or new_col > len(board[0]) - 6: # This ensures no index error, len(board[0]) is the board's width
        move_boss(board, boss)
    else:
        if check_valid_boss_move(board, new_row, new_col):
            for x in range(len(board)):
                for y in range(len(board[0])):
                    if board[x][y] in boss['icon']:
                        board[x][y] = EMPTY
            for x in range(0, 5):
                for y in range(0, 5):
                    board[new_row + x][new_col + y] = boss["face"][x][y]
            boss['field'] = (new_row, new_col)
        else:
            move_boss(board, boss)


def check_valid_boss_move(board, new_row, new_col):
    for x in range(5):
        for y in range(5):
            if board[new_row + x][new_col + y] in NPC_OBSTACLES:
                return False
    return True
