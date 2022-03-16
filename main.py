import util
import engine
import ui


BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def create_player(player_type):
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    dict = {
        'Nerd': {'knowledge': 10, 'smartness': 2, 'energy': 20, 'exams': None}, 
        'Laid-back': {'knowledge': 1, 'smartness': 6, 'energy': 20, 'exams': None},
        'Average': {'knowledge': 5, 'smartness': 4, 'energy': 20, 'exams': None}
        }

    return dict[player_type]


def main():

    player_type = ui.get_player_type()
    player = create_player(player_type)
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    print(player)
    # util.clear_screen()

    is_running = True
    while is_running == False:
        engine.put_player_on_board(board, player)
        ui.display_board(board)

        key = util.key_pressed().upper()
        if key == 'Q':
            is_running = False
        else:
            engine.move(player, board, key)
            engine.npc_move(npc, board)
        #util.clear_screen()


if __name__ == '__main__':
    main()
