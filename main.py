from items_and_characters import PLAYER_TYPES
import util
import engine
import ui
<<<<<<< HEAD
from items_and_characters import ITEMS, NPCS, PLAYER_TYPES
from copy import deepcopy
import random

PLAYER_POSITION = {"position": (3, 3), "icon": '☻'}
=======
import items_and_caracters as iac
import copy


PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

>>>>>>> c3ea559219bacf43ee361a099bdb78870e6edfc3
BOARD_WIDTH = 30
BOARD_HEIGHT = 20
PLAYER_ICON = "P"
PLAYER_START_COORDS = (1,1)


def create_player():
<<<<<<< HEAD
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
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    npcs = deepcopy(NPCS) 
    items = deepcopy(ITEMS)
    setup_start_board(board, player, npcs, items)
    util.clear_screen()
    is_running = True
    while is_running:
        if player["energy"] <= 0:
            break
        ui.display_board(board, player)
        key = util.key_pressed().upper()
        if key == 'Q':
            is_running = False
        else:
            engine.move(player, board, key, player, items)
            # engine.interaction_with_item(board, player, items)
            for npc in npcs:
                engine.move(npc, board, get_npc_direction(), player, items)
        util.clear_screen()
=======
    player_types = copy. deepcopy(iac.PLAYER_TYPES)
    player_type = ui.get_player_type()
    player = player_types[player_type]
    player["name"] = ui.get_player_name()
    return player

def create_npc(npc_type):
    all_npcs = copy.deepcopy(iac.NPC)
    npc = all_npcs[npc_type]
    return npc
   

def items_positions():
    items_list = make_item_list()
    for item in items_list:
        column = random.randint(0, len(board[ROW])-1)
        row = random.randint(0, len(board)-1)
        item[1][0] = row
        item[1][1] = column
    return items_list
    

def make_item_list():
    items = iac.ITEMS
    item_info = [None, [None, None]]
    items_list = []
    for item in items:
        for i in range(items["total amount"]):
            item_info[0] = items["name"]
            items_list.append(item_info)
    return items_list


def create_empty_board():
    #creates board and places all characters and items
    pass


def player_movement(player_field, board, key):
    #updates player position
    pass


def npc_movement(field, board):
    #updates the possition of the npc
    pass


def is_colision(player_field, npc_field):
    #returns True or False
    pass


def player_npc_interaction(player_dict, npc_dict):
    #updates player_dict and npc_dict
    pass


def found_item(player_field, all_items):
    #returns True or False
    pass


def player_item_interaction(player_dict, all_items):
    #updates player dict and all items list(item disappears)
    pass


def update_board(board, player_field, npc1_field, npc2_field, all_items):
    put_player_on_board(board)
    put_items_on_board(board)
    put_npcs_on_board(board)
    
    
def main():
    #SETUP PHASE
    player_info = create_player()   
    npc_1 = create_npc("perpetual_student")     
    npc_2 = create_npc("nerd")    
    all_items = items_positions()  
    board = create_empty_board()
    update_board((board, player_info, npc_1, npc_2, all_items))
    
    #PLAYING PHASE
    is_running = (player_info[energy] > 0)
    while is_running:
        while True:
            display_board(board, players_info)
            key = util.key_pressed()
            if key == 'q':
                is_running = False
            else:
                player_position = player_movement(player_info[field], board, key)
                player_info[field] = player_position #player_info dictionary is updated

                npc1_position = npc_movement(npc_1[field], board)
                npc_1[field] = npc1_position #npc_1 dictionary is updated
                if is_colision(player_position, npc1_position):
                    player_npc_interaction(player_info, npc_1) #player_npc_interaction function updates the player_info dictionary
                npc2_position = npc_movement(npc_2[field], board)
                npc_2[field] = npc2_position #npc_2 dictionary is updated
                if is_colision(player_position, npc2_position):
                    player_npc_interaction(player_info, npc_2)

                if found_item(player_info[field], all_items):
                    player_item_interaction(player_info, all_items)

                update_board(board)
                util.clear_screen()
                break

                
#     player_type = ui.get_player_type()
#     name = ui.get_player_name()
#     player = create_player(player_type)
#     player['name'] = name
#     board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
#     stats_scroll = engine.create_stats_scroll(player, BOARD_HEIGHT)
#     util.clear_screen()
#     is_running = True
#     while is_running:
#         engine.put_player_on_board(board, player)
#         ui.display_board(board, stats_scroll)

#         key = util.key_pressed().upper()
#         if key == 'Q':
#             is_running = False
#         else:
#             engine.player_move(board, key)
#         util.clear_screen()
>>>>>>> c3ea559219bacf43ee361a099bdb78870e6edfc3


if __name__ == '__main__':
    main()
