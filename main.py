import util
import engine
import ui


BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    player_types = {
        'Nerd': {'class': 'Nerd', 'name': None, 'knowledge': 10, 'smartness': 2, 'energy': 20, 'exams': None}, 
        'Laid-back': {'class': 'Laid-back', 'name': None, 'knowledge': 1, 'smartness': 6, 'energy': 20, 'exams': None},
        'Average': {'class': 'Average', 'name': None, 'knowledge': 5, 'smartness': 4, 'energy': 20, 'exams': None}
        }

    player_type = ui.get_player_type()
    player = player_types[player_type]
    player["name"] = ui.get_player_name()
    return player


def main():
    player = create_player()
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board, player)

        key = util.key_pressed().upper()
        if key == 'Q':
            is_running = False
        else:
            engine.player_move(board, key)
        util.clear_screen()


if __name__ == '__main__':
    main()
