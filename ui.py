import engine
import util
import time


from items_and_characters import ITEMS, PLAYER_TYPES


TYPES = ['Nerd', 'Laid-back', 'Average'] # = [k for k in PLAYER_TYPES.keys()] 


def display_board(board, player_info):
    stats_scroll = engine.create_stats_scroll(player_info, len(board))
    for row, line in zip(board, stats_scroll):
        print(''.join(row), f'   {line}')


def display_inventory(player):
    inventory_scroll = ['   ______________________________',' / \                             \.','|   |      Player inventory      |.',' \_ |                            |.'] 
    for k in player['inventory']:
        for item in ITEMS:
            if item['name'] == k:
                icon = item['icon']
        row = f"    |  {icon} - {k}: {player['inventory'][k]} "
        while len(row) < len(' \_ |                            '):
            row += ' '
        row += '|.'
        inventory_scroll.append(row)
    for line in ['    |   _________________________|___','    |  /                            /.','    \_/____________________________/.']:
        inventory_scroll.append(line)
    for row in inventory_scroll:
        print(row)
    input("\nPress enter to exit inventory > ")
    

def get_player_type() -> str:
    print("> Choose your student type <")
    list_of_types = [f'{i + 1}. - {TYPES[i]}' for i in range(len(TYPES))]
    while True:
        player_type = input(f"Select your student: {list_of_types} > ")
        if player_type not in [str(i + 1) for i in range(len(TYPES))]:
            print("Wrong input!")
            continue
        break
    return TYPES[int(player_type) - 1]


def get_player_name():
    print("> What's your name, student? <")
    while True:
        name = input('Please type your name: ')
        if len(name) > 13:
            print("The name is too long! (max 13 characters)")
            continue
        break
    return name


def choose_weapon(player):
    #display_inventory(player)
    print("players inventory" , player["inventory"])
    while True:
        weapon_no = input("Choose weapon number ")
        if weapon_no == "1":     # hardcoded for test of level 1
            weapon_kind = "beer"
            break
    while True:
        amount = int(input("Choose amount "))
        if amount in range(0, player["inventory"][weapon_kind] + 1):
            return (weapon_kind, amount)


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
    
