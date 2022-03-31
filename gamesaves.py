import shelve



def save_game(board, items, npcs, player, boss):
    with shelve.open('savegame', 'n') as f:
        f['board'] = board
        f['items'] = items
        f['npcs'] = npcs
        f['player'] = player
        f['boss'] = boss
        

def load_game():
    with shelve.open('savegame', 'r') as f:
        board = f['board']
        items = f['items']
        npcs = f['npcs']
        player = f['player']
        boss = f['boss']
    return board, items, npcs, player, boss

