from items_and_characters import BOSS, PLAYER_TYPES
import util
import engine
import ui
from items_and_characters import ITEMS, NPCS, PLAYER_TYPES
from copy import deepcopy
import random
import gamesaves
import time


BOARD_WIDTH = 30
BOARD_HEIGHT = 20
PLAYER_ICON = "☻"
PLAYER_START_COORDS = (1,1)
LEVELS = [1, 2, 3]

intro_level1 = ["You are a young, more or less brilliant student",
                "who is about to finish their first year of studies.",
                "You have spend the whole year studying / partying",
                "and enjoying the student's life.",
                "Unfortunately all good things come to an end...",
                "Ahead of you is the most dreadful period for any student...",
                "THE EXAMS!" ,
                "Your first task is to prepare for them the best you can.",
                "Increase your knowledge or use less honorable ways",
                "to increase your chances of passing all final exams."]

intro_level2 = ["You have done the best you can",
                "to prepare yourself for the final exams",
                "in the little time you had.",
                "Your next challange is to defeat the 3 professors",
                "and actually pass the exams",
                "This task won't be easy, having good knowledge helps",
                "but as all students know there are other ways",
                "to get what you need from the noble members of Academia..."]

intro_level3 = ["Congratulations!",
                "You have passed the final exams and you are getting",
                "ready for some well-deserved vacation.",
                "Little do you know that your fight is far from over!",
                "Your ultimate enemy is the lady from the Dean's office",
                "the only person who can give you your Grade Transcript.",
                "Only young, naive freshmen believe it's an easy task!",
                "Catch the lady, be nice and if today is your lucky day",
                "she might give you the Holy Graal of every student."]


def create_player():
    player_type = ui.get_player_type()
    player = deepcopy(PLAYER_TYPES[player_type])
    name = ui.get_player_name()
    player['name'] = name
    player['field'] = PLAYER_START_COORDS
    player['icon'] = PLAYER_ICON
    player['level'] = 1
    return player


def get_npc_direction():
    direction = "WASD"
    key = random.choice(direction)
    return key


def setup_start_boards(boards, player, npcs, items):
    for level in LEVELS:
        items_on_level = [item for item in items if item["level"] == level]
        print(items_on_level)
        npcs_on_level = [npc for npc in npcs if npc["level"] == level]
        print(npcs_on_level)
        engine.put_items_on_board(boards[level - 1], items_on_level)
        engine.put_npcs_on_board(boards[level - 1], npcs_on_level)
        ui.display_board(boards[level - 1], player)
        if level == 1:
            engine.put_player_on_board(boards[level - 1], player)
        if level == 3:
            engine.put_boss_on_board(boards[level - 1])


def initialize_game():
    if engine.play_new_game():
        player = create_player()
        npcs = deepcopy(NPCS) 
        items = deepcopy(ITEMS)
        boards = [engine.create_board(BOARD_WIDTH, BOARD_HEIGHT, level) for level in LEVELS]
        setup_start_boards(boards, player, npcs, items)
    else:
        boards, items, npcs, player = gamesaves.load_game()
    return boards, items, npcs, player


def react_on_key(boards, items, npcs, player, level, key):
    if key == 'Q':
        return False
    elif key == 'V':
        gamesaves.save_game(boards, items, npcs, player)
        print("Saving game..")
        time.sleep(2)
        return False
    elif key == 'I':
        util.clear_screen()
        ui.display_inventory(player)
        return True
    else:
        engine.move(player, boards[level -1], key, player, items)
        for npc in npcs:
            if npc["level"] == level:
                engine.move(npc, boards[level -1], get_npc_direction(), player, items)
        return True


def main():
    boards, items, npcs, player = initialize_game()
    #util.clear_screen()
    is_running = True
    while is_running:
        level = player["level"]
        ui.display_board(boards[level - 1], player)
        engine.interaction_with_npc(boards[level -1], player, npcs)
        engine.move_boss(boards[2], BOSS)
        if player["energy"] <= 0:
            print("GAME OVER")
            is_running = False
            break
        #util.clear_screen() # uncomment in final version
        ui.display_board(boards[level - 1], player)
        key = util.key_pressed().upper()
        is_running = react_on_key(boards, items, npcs, player, level, key)
        #util.clear_screen()


if __name__ == "__main__":
    main()