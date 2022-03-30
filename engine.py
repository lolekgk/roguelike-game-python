from socketserver import ThreadingUDPServer
import random
from os.path import exists
import os
import time
import util
import ui
from items_and_characters import ITEMS, NPCS, BOSS


ROW = 0
WALL = f'{ui.bcolors.GRAY}░{ui.bcolors.ENDC}'
EMPTY = " "
ENTRY = f'{ui.bcolors.RED}↑{ui.bcolors.ENDC}'
EXIT = f'{ui.bcolors.GREEN}→{ui.bcolors.ENDC}'
ENTRY_ROW, ENTRY_COLUMN = 0, 15
EXIT_ROW, EXIT_COLUMN = 18, 29
PLAYER_DATA_TO_DISPLAY = ["name", "class", 'knowledge', 'smartness', 'energy', 'exams']


def select_game_state():
    while True:
        util.clear_screen()
        print("1. New Game")
        print("2. Load Game")
        key = util.key_pressed().upper()
        if key == '1':
            return True
        elif key == '2':
            return False
        else:
            print('Wrong input')
            time.sleep(2)
            
            
def create_board(width, height, level):
    board = []
    board.append([WALL for i in range(width)])
    for i in range(height - 2):
        row = [EMPTY for i in range(width - 2)]
        row.insert(0, WALL)
        row.append(WALL)
        board.append(row)
    board.append([WALL for i in range(width)])
    add_walls(board, level)
    add_entry(board, level)  
    add_exit(board, level)
    return board


def add_entry(board, level):
    if level in [2, 3]:
        board[ENTRY_ROW][ENTRY_COLUMN] = ENTRY


def add_exit(board, level):
    if level in [1, 2]:
        board[EXIT_ROW][EXIT_COLUMN] = EXIT 


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
            board[i][8] = WALL
    for i in range(len(board[0]) - 1):
        if i >= 9:
            board[16][i] = WALL 
            board[12][i] = WALL
            board[8][i] = WALL
            if i != 28 and i != 27:
                board[3][i] = WALL
    board[10][22] = WALL
    board[11][22] = WALL


def walls_level_3(board):   
    for i in range(len(board[0])):
        if i < 14 or i > 16:
            board[5][i] = WALL
        if i <= 8 and i >= 2:
            board[14][i] = WALL
    for i in range(len(board)):
        if i > 14:
            board[i][8] = WALL
    

def walls_level_2(board):  
    for i in range(len(board)):
        if i % 4 == 0:
            for j in range(len(board[0]) - 1):
                if j < 13 or j > 16:
                    board[i][j] = WALL
        if i % 4 != 0 and i in range(0,16):
            board[i + 2][12] = WALL
            board[i + 2][17] = WALL
    board[1][12] = WALL
    board[1][17] = WALL


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
            item_to_put = item['icon']
            put_item(board, item_to_put)


def put_item(board, item):
    while True:
        column = random.randint(1, len(board[ROW])-1)
        row = random.randint(1, len(board)-1)
        if is_put_on_board_valid(board, row, column):
            board[row][column] = item
            break 


def is_put_on_board_valid(board, row, column):
    if board[row][column] == EMPTY:
        return True
    return False


def put_boss_on_board(board, boss):
    row, column = boss['field']
    for x in range(5):
        for y in range(5):
            board[row + x][column + y] = boss["face"][x][y]


def play_new_game():
    if os.name == "nt":
        file = 'savegame.dat'
    else:
        file = 'savegame.db'
    if not exists(file):   
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
