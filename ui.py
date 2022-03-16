TYPES = ['Nerd', 'Laid-back', 'Average']


def display_board(board):
    for row in board:
        print(''.join(row))


def get_player_type() -> str:
    print("Welcome to the game!")
    list_of_types = [f'{i + 1}. - {TYPES[i]}' for i in range(len(TYPES))]
    while True:
        player_type = input(f"Select your student: {list_of_types} > ")
        if player_type not in [str(i + 1) for i in range(len(TYPES))]:
            print("Wrong input!")
            continue
        break
    return TYPES[int(player_type) - 1]

