import engine
import util
import time


from items_and_characters import ITEMS, PLAYER_TYPES


TYPES = ['Nerd', 'Laid-back', 'Average'] # = [k for k in PLAYER_TYPES.keys()] 


def display_intro(scroll):
    for row in scroll:
        print(row)
    print()
    

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
        

def meeting_npc(npc):
    if npc["name"] == "best student":
        message = "That's the best student in our group! Would be great if I could get his notes for the exam"
    elif npc["name"] == "perpetual student":
        message = "This dude has been around forever! I'm sure he has the last year's test!"
    else:
        pass
    return message


def finding_items(item):
    if item == "notes":
        message = "Cool! Somebody left their notes here."
    elif item == "Red Bull":
        message == "I was getting a bit sllepy. This energy drink comes right in time!"
    elif item == "instant noodles":
        message = "My favourite instant noodles! Just as I was gettinh hungry!"
    elif item == "beer":
        message == "Someone left a beer in the University dorm! That's crazy! Should I drink it now... Nah, I'll keep it in my backpack. "
    elif item == "nerd's notes":
        message = "Thank's man! With these notes the exam will be a breeze!"
    elif item == "last year's test":
        message = "Dude, you're the best! Now let's hope the professor uses the exact same test this year!"
    else:
        pass


