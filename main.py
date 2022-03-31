import util
import engine
import action
import ui
from items_and_characters import ITEMS, NPCS, PLAYER_TYPES, BOSS
import random
import gamesaves
import time
import copy
from intro import LEVEL_1,LEVEL_2,LEVEL_3


BOARD_WIDTH = 30
BOARD_HEIGHT = 20
PLAYER_ICON = f"{ui.bcolors.GREEN}☻{ui.bcolors.ENDC}"
PLAYER_START_COORDS = (1,1)
LEVELS = [1, 2, 3]
KNOWLEDGE_TO_GET_KEY = 10     #Zmienić na 15
EXAMS_TO_GET_KEY = 0          #Zmienić na 3
text_dict = {1: copy.copy(LEVEL_1), 2: copy.copy(LEVEL_2), 3: copy.copy(LEVEL_3)}


def create_player():
    player_type = ui.get_player_type()
    player = copy.deepcopy(PLAYER_TYPES[player_type])
    name = ui.get_player_name()
    player['name'] = name
    player['field'] = PLAYER_START_COORDS
    player['icon'] = PLAYER_ICON
    player['level'] = 3
    return player


def get_npc_direction():
    direction = "WASD"
    key = random.choice(direction)
    return key


def setup_start_boards(boards, player, npcs, items, boss):
    for level in LEVELS:
        items_on_level = [item for item in items if item["level"] == level]
        npcs_on_level = [npc for npc in npcs if npc["level"] == level]
        engine.put_items_on_board(boards[level - 1], items_on_level)
        engine.put_npcs_on_board(boards[level - 1], npcs_on_level)
        if level == 3:
            engine.put_boss_on_board(boards[level - 1], boss)


def initialize_game():
    if engine.play_new_game():
        player = create_player()
        npcs = copy.deepcopy(NPCS) 
        items = copy.deepcopy(ITEMS)
        boss = copy.deepcopy(BOSS)
        boards = [engine.create_board(BOARD_WIDTH, BOARD_HEIGHT, level) for level in LEVELS]
        setup_start_boards(boards, player, npcs, items, boss)
    else:
        boards, player, items, npcs, boss = gamesaves.load_game()
    return boards, player, items, npcs, boss


def interaction_with_bot(boards, player, npcs, boss, level):
    if action.is_interaction_with_npc(player, boards[level - 1]):
        if level == 1:
            action.interaction_with_student(boards[level - 1], player, npcs)
        elif level == 2:
            action.interaction_with_professor(boards[level - 1], player, npcs)
    elif level == 3:
            action.interaction_with_boss(boards[level - 1], player, boss)


def react_on_key(boards, player, items, npcs, boss, level, key):
    if key == 'Q':
        return False
    elif key == 'V':
        gamesaves.save_game(boards, items, npcs, player, boss)
        print("Saving game..")
        time.sleep(2)
        return False
    elif key == 'I':
        util.clear_screen()
        ui.display_inventory(player)
        return True
    else:
        action.move(player, boards[level -1], key, player, items)
        for npc in npcs:
            if npc["level"] == level:
                action.move(npc, boards[level -1], get_npc_direction(), player, items)
            if level == 3:
                action.move_boss(boards[level - 1], boss)
        return True


def add_next_level_key_if_possible(boards, player, level, items):
    if level == 1 and player["knowledge"] >= KNOWLEDGE_TO_GET_KEY \
       or level == 2 and player["exam"] >= EXAMS_TO_GET_KEY:
            engine.put_item(boards[level - 1], items[10]['icon'])
            return True
    else:
        return False


def intro(level):
    try:
        text_dict[level]
        text_list = text_dict[level]
        del text_dict[level]
        scroll = engine.create_intro_scroll(text_list)
        ui.display_intro(scroll)
        input()
        util.clear_screen()
    except KeyError:
        pass


def main():
    boards, player, items, npcs, boss = initialize_game()
    util.clear_screen() 
    intro(player["level"])
    is_running = True
    is_key_on_board = [False for level in LEVELS]
    while is_running:
        level = player["level"]
        util.clear_screen()
        intro(level)
        engine.put_player_on_board(boards[level - 1], player) # ta funkcja jest koniecza przy zmianie poziomu, poza ty nie, ale nie przeszkadza 
        util.clear_screen() 
        ui.display_board(boards[level - 1], player)
        interaction_with_bot(boards, player, npcs, boss, level)
        if player["energy"] <= 0:
            ui.lose_message()
            is_running = False
            break
        if not is_key_on_board[level - 1]:
            is_key_on_board[level - 1] = add_next_level_key_if_possible(boards, player, level, items)
        key = util.key_pressed().upper()
        is_running = react_on_key(boards, player, items, npcs, boss, level, key)


if __name__ == "__main__":
    main()
