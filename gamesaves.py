import shelve

def save_game(board, items, npcs, player):
    with shelve.open('savegame', 'n') as f:
        f['board'] = board
        f['items'] = items
        f['npcs'] = npcs
        f['player'] = player
        

def load_game():
    with shelve.open('savegame', 'r') as f:
        board = f['board']
        items = f['items']
        npcs = f['npcs']
        player = f['player']
    return board, items, npcs, player

