import engine

TYPES = ['Nerd', 'Laid-back', 'Average']


def display_board(board, player_info):
    stats_scroll = engine.create_stats_scroll(player_info, len(board))
    for row, line in zip(board, stats_scroll):
        print(''.join(row), f'   {line}')


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
    while True:
        weapon_no = input("Choose wheapon number ")
        if weapon_no == "1":     # hardcoded for test of level 1
            weapon_kind = "beer"
            break
    while True:
        amount = int(input("Choose amount "))
        if amount in range(0, player["inventory"][weapon_kind] + 1):
            return (weapon_kind, amount)
        
