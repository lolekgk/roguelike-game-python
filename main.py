from items_and_characters import PLAYER_TYPES
import util
import engine
import ui
from items_and_characters import ITEMS, NPCS, PLAYER_TYPES
from copy import deepcopy
import random
import gamesaves
import time


BOARD_WIDTH = 30
BOARD_HEIGHT = 20
PLAYER_ICON = "☻"
PLAYER_START_COORDS = (1,1)
LEVELS = [1, 2, 3]


def create_player():
    player_type = ui.get_player_type()
    player = deepcopy(PLAYER_TYPES[player_type])
    name = ui.get_player_name()
    player['name'] = name
    player['field'] = PLAYER_START_COORDS
    player['icon'] = PLAYER_ICON
    player['level'] = 1
    return player


def get_npc_direction():
    direction = "WASD"
    key = random.choice(direction)
    return key


def setup_start_boards(boards, player, npcs, items):
    for level in LEVELS:
        items_on_level = [item for item in items if item["level"] == level]
        print(items_on_level)
        npcs_on_level = [npc for npc in npcs if npc["level"] == level]
        print(npcs_on_level)
        engine.put_items_on_board(boards[level - 1], items_on_level)
        engine.put_npcs_on_board(boards[level - 1], npcs_on_level)
        ui.display_board(boards[level - 1], player)
        if level == 1:
            engine.put_player_on_board(boards[level - 1], player)


def main():
    if engine.play_new_game():
        player = create_player()
        npcs = deepcopy(NPCS) 
        items = deepcopy(ITEMS)
        boards = [engine.create_board(BOARD_WIDTH, BOARD_HEIGHT, level) for level in LEVELS]
        for board in boards:
            ui.display_board(board, player)
        setup_start_boards(boards, player, npcs, items)
        for board in boards:
            ui.display_board(board, player)
    else:
        boards, items, npcs, player = gamesaves.load_game()
    #util.clear_screen()
    is_running = True
    while is_running:
        level = player["level"]
        if player["energy"] <= 0:
            print("GAME OVER")
            break
        ui.display_board(boards[level -1], player)
        engine.interaction_with_npc(boards[level -1], player, npcs)
        #util.clear_screen() # uncomment in final version
        ui.display_board(boards[level -1], player)
        key = util.key_pressed().upper()
        if key == 'Q':
            is_running = False
        elif key == 'V':
            gamesaves.save_game(boards, items, npcs, player)
            print("Saving game..")
            time.sleep(2)

        elif key == 'I':
            util.clear_screen()
            ui.display_inventory(player)

        else:
            engine.move(player, boards[level -1], key, player, items)
            # engine.interaction_with_item(board, player, items)
            for npc in npcs:
                if npc["level"] == level:
                    engine.move(npc, boards[level -1], get_npc_direction(), player, items)
        #util.clear_screen()


if __name__ == "__main__":
    main()