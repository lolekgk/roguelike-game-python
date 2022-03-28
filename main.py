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


def create_player():
    player_type = ui.get_player_type()
    player = deepcopy(PLAYER_TYPES[player_type])
    name = ui.get_player_name()
    player['name'] = name
    player['field'] = PLAYER_START_COORDS
    player['icon'] = PLAYER_ICON
    return player


def get_npc_direction():
    direction = "WASD"
    key = random.choice(direction)
    return key


def setup_start_board(board, player, npcs, items):
    engine.put_player_on_board(board, player)
    engine.put_items_on_board(board, items)
    engine.put_npcs_on_board(board, npcs)


def main():
    if engine.play_new_game():
        player = create_player()
        board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
        npcs = deepcopy(NPCS) 
        items = deepcopy(ITEMS)
        setup_start_board(board, player, npcs, items)
    else:
        board, items, npcs, player = gamesaves.load_game()
    util.clear_screen()
    is_running = True
    while is_running:
        if player["energy"] <= 0:
            print("GAME OVER")
            break
        ui.display_board(board, player)
        engine.interaction_with_npc(board, player, npcs)
        #util.clear_screen() # uncomment in final version
        ui.display_board(board, player)
        key = util.key_pressed().upper()
        if key == 'Q':
            is_running = False
        elif key == 'V':
            gamesaves.save_game(board, items, npcs, player)
            print("Saving game..")
            time.sleep(2)

        elif key == 'I':
            util.clear_screen()
            ui.display_inventory(player)

        else:
            engine.move(player, board, key, player, items)
            # engine.interaction_with_item(board, player, items)
            for npc in npcs:
                engine.move(npc, board, get_npc_direction(), player, items)
        util.clear_screen()


if __name__ == "__main__":
    main()