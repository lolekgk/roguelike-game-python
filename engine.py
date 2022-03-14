import random


WALLS = ['░']


def create_board(width, height):
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
    board = []
    board.append(['░' for i in range(width)])
    for i in range(height - 2):
        row = [' ' for i in range(width - 2)]
        row.insert(0, '░')
        row.append('░')
        board.append(row)
    board.append(['░' for i in range(width)])
    board[random.randint(1, height-2)][-1] = 'B'
    for row in board:
        print(''.join(row))


create_board(30, 20)


def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    pass
