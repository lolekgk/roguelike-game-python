from items_and_characters import BOSS, PLAYER_TYPES
import util
import engine
import action
import ui
from items_and_characters import ITEMS, NPCS, PLAYER_TYPES, BOSS
from copy import deepcopy
import random
import gamesaves
import time


BOARD_WIDTH = 30
BOARD_HEIGHT = 20
PLAYER_ICON = f"{ui.bcolors.GREEN}☻{ui.bcolors.ENDC}"
PLAYER_START_COORDS = (1,1)
LEVELS = [1, 2, 3]
KNOWLEDGE_TO_GET_KEY = 10     #Zmienić na 15
EXAMS_TO_GET_KEY = 0          #Zmienić na 3

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


def setup_start_boards(boards, player, npcs, items, boss):
    for level in LEVELS:
        items_on_level = [item for item in items if item["level"] == level]
        npcs_on_level = [npc for npc in npcs if npc["level"] == level]
        engine.put_items_on_board(boards[level - 1], items_on_level)
        engine.put_npcs_on_board(boards[level - 1], npcs_on_level)
        ui.display_board(boards[level - 1], player)
        if level == 3:
            engine.put_boss_on_board(boards[level - 1], boss)


def initialize_game():
    if engine.play_new_game():
        player = create_player()
        npcs = deepcopy(NPCS) 
        items = deepcopy(ITEMS)
        boss = deepcopy(BOSS)
        boards = [engine.create_board(BOARD_WIDTH, BOARD_HEIGHT, level) for level in LEVELS]
        setup_start_boards(boards, player, npcs, items, boss)
    else:
        boards, player, items, npcs, boss = gamesaves.load_game()
    return boards, player, items, npcs, boss


def interaction_with_bot(boards, player, npcs, boss, level):
    if level == 1:
        action.interaction_with_student(boards[level - 1], player, npcs)
    elif level == 2:
        action.interaction_with_professor(boards[level - 1], player, npcs)
    else:
        action.interaction_with_boss(boards[level - 1], player, boss)


def react_on_key(boards, player, items, npcs, boss, level, key):
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
        action.move(player, boards[level -1], key, player, items)
        for npc in npcs:
            if npc["level"] == level:
                action.move(npc, boards[level -1], get_npc_direction(), player, items)
            if level == 3:
                action.move_boss(boards[level - 1], boss)
        return True


def add_next_level_key_if_possible(boards, player, level, items):
    if level == 1 and player["knowledge"] >= KNOWLEDGE_TO_GET_KEY \
       or level == 2 and player["exams"] >= EXAMS_TO_GET_KEY:
            engine.put_item(boards[level - 1], items[10]['icon'])
            return True
    else:
        return False


def main():
    boards, player, items, npcs, boss = initialize_game()
    is_running = True
    is_key_on_board = [False for level in LEVELS]
    while is_running:
        level = player["level"]
        engine.put_player_on_board(boards[level - 1], player) # ta funkcja jest koniecza przy zmianie poziomu, poza ty nie, ale nie przeszkadza 
        util.clear_screen() 
        ui.display_board(boards[level - 1], player)
        interaction_with_bot(boards, player, npcs, boss, level)
        if player["energy"] <= 0:
            print("GAME OVER")
            is_running = False
            break
        if not is_key_on_board[level - 1]:
            is_key_on_board[level - 1] = add_next_level_key_if_possible(boards, player, level, items)
        key = util.key_pressed().upper()
        is_running = react_on_key(boards, player, items, npcs, boss, level, key)


if __name__ == "__main__":
    main()