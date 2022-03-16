import util
import engine
import ui
from items_and_characters import ITEMS, NPCS
from copy import deepcopy
import random


BOARD_WIDTH = 30
BOARD_HEIGHT = 20

PLAYER_START_COORDS = (1,1)


def create_player(player_type):
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    player_types = {
        'Nerd': {'class': 'Nerd', 'name': None, 'knowledge': 10, 'smartness': 2, 'energy': 20, 'exams': 0}, 
        'Laid-back': {'class': 'Laid-back', 'name': None, 'knowledge': 2, 'smartness': 6, 'energy': 20, 'exams': 0},
        'Average': {'class': 'Average', 'name': None, 'knowledge': 5, 'smartness': 4, 'energy': 20, 'exams': 0}
        }

    return player_types[player_type]


def get_npc_direction():
    direction = "WASD"
    key = random.choice(direction)
    return key


def main():
    player_type = ui.get_player_type()
    name = ui.get_player_name()
    player = create_player(player_type)
    player['name'] = name
    player['field'] = PLAYER_START_COORDS
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    stats_scroll = engine.create_stats_scroll(player, BOARD_HEIGHT)
    engine.put_player_on_board(board, player)
    npcs = NPCS.deepcopy() 
    engine.put_npcs_on_board(board, npcs)
    items = ITEMS.deepcopy()
    engine.put_items_on_board(board, items)
    util.clear_screen()

    is_running = True
    while is_running:
        if player["energy"] <= 0:
            break
        ui.display_board(board, stats_scroll)
        key = util.key_pressed().upper()
        if key == 'Q':
            is_running = False
        else:
            engine.move(player, board, key)
            for npc in npcs:
                engine.move(npc, board, get_npc_direction())
            
        util.clear_screen()


if __name__ == '__main__':
    main()
