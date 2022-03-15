import util
import engine
import ui


PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    pass


def main():
    player = {"field":(2,2)}  #create_player()
    npc = {"field":(3,3)}
    print(f"player to-----: {player}")
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)

    #util.clear_screen()
    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)

        key = util.key_pressed().upper()
        if key == 'Q':
            is_running = False
        else:
            engine.icon_move(player, board, key)
            engine.npc_move(npc, board)
        #util.clear_screen()


if __name__ == '__main__':
    main()
