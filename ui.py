import engine
import util
import time
from items_and_characters import bcolors
from intro import END_MESSAGE_WIN, END_MESSAGE_LOSE
from items_and_characters import ITEMS, PLAYER_TYPES, NPCS


TYPES = ['Nerd', 'Average', 'Laid-back'] # = [k for k in PLAYER_TYPES.keys()] 


def display_intro(scroll):
    for row in scroll:
        print(bcolors.BLUE, row, bcolors.ENDC)
    

def display_board(board, player_info):
    stats_scroll = engine.create_stats_scroll(player_info, len(board))
    for row, line in zip(board, stats_scroll):
        print(''.join(row), f'   {line}')


def get_player_type() -> str:
    print(f"{bcolors.YELLOW}> Choose your student type <{bcolors.ENDC}")
    list_of_types = [f'{i + 1}. - {TYPES[i]}' for i in range(len(TYPES))]
    while True:
        player_type = input(f"{bcolors.GREEN}Select your student:{bcolors.ENDC} {list_of_types} > ")
        if player_type not in [str(i + 1) for i in range(len(TYPES))]:
            print(f"{bcolors.RED}Wrong input!{bcolors.ENDC}")
            continue
        break
    return TYPES[int(player_type) - 1]


def get_player_name():
    print(f"{bcolors.YELLOW}> What's your name, student? <{bcolors.ENDC}")
    while True:
        name = input(f'{bcolors.GREEN}Please type your name: {bcolors.ENDC}')
        if len(name) > 13:
            print(f"{bcolors.RED}The name is too long! (max 13 characters){bcolors.ENDC}")
            continue
        elif len(name) < 4:
            print(f"{bcolors.RED}The name is too short! (min 4 characters){bcolors.ENDC}")
            continue
        break
    return name


def choose_beer_amount(player, opponent): 
    # ta funkcja prawdopodobnie zostanie zastąpiona przez get_beer_amount
    # miała być ogólną funkcją do wyboru "broni" do interakcji, ale szanse, że tak się stanie, są niewielkie
    attribute = opponent["attribute"]
    name = opponent["name"]
    max_amount = player["inventory"]["beer"]
    print(f"\nTIP: Use your wits and beer to get {attribute}.")
    while True:
        amount = input(f"You have {max_amount} beers. How many of them will you give the {name}? ")
        if amount not in [str(n) for n in range(0, max_amount + 1)]:
            print(f"{bcolors.RED}Wrong input!{bcolors.ENDC}")
            continue
        break
    return int(amount)


def choose_energy_and_knowledge(player, npc):
    name = npc["name"]
    max_knowledge = npc["exam requirement"]["knowledge"]
    max_energy = npc["exam requirement"]["energy"]
    print(f"\nTime for {name.split()[0]} exam.".upper())
    print("\nHow much study and energy did you spend preparing for the exam?")
    print(f"\nChoosing {max_energy} energy points and {max_knowledge} knowledge points you can be sure you will pass.\n")
    while True:
        energy = input("Energy - ")
        if energy not in [str(n) for n in range(min(max_energy, player["energy"]) + 1)]:
            print(f"{bcolors.RED}Wrong input!{bcolors.ENDC}")
            continue
        break
    while True:
        knowledge = input("Knowledge - ")
        if knowledge not in [str(n) for n in range(min(max_knowledge, player["knowledge"]) + 1)]:
            print(f"{bcolors.RED}Wrong input!{bcolors.ENDC}")
            continue
        break
    return int(energy), int(knowledge)
        

def display_interaction_effect(success):
    if success:
        print("\nYOU DID IT!")
    else:
        print("\nNOT THIS TIME")

def meeting_npc(npc):
    if npc["name"] == "best student":
        message = "\nThat's the best student in our group! Would be great if I could get his notes for the exam"
    elif npc["name"] == "perpetual student":
        message = "\nThis dude has been around forever! I'm sure he has the last year's test!"
    else:
        pass
    return message


def finding_items(item):
    message = ""
    if item["name"] == "notes":
        message = "Cool! Somebody left their notes here."
    elif item["name"] == "Red Bull":
        message = "I was getting a bit sleepy. This energy drink comes right in time!"
    elif item["name"] == "instant noodles":
        message = "My favourite instant noodles! Just as I was getting hungry!"
    elif item["name"] == "beer":
        message = "Someone left a beer in the University dorm! That's crazy! Should I drink it now... Nah, I'll keep it in my backpack. "
    elif item["name"] == "nerd's notes":
        message = "Thank's man! With these notes the exam will be a breeze!"
    elif item["name"] == "last year's test":
        message = "Dude, you're the best! Now let's hope the professor uses the exact same test this year!"
    elif item["name"] == "flowers":
        message = "A nice bouquet of flowers! The lady from the Dean's office might like it."
    elif item["name"] == "chocolates":
        message = "Fancy belgian chocolates. They will help me get some favours!"
    elif item["name"] == "exam":
        message = "This exam is more difficult than I expected..."
    elif item["name"] == "key":
        message = "I found a secret key!!!"
    else:
        pass
    print(f"{bcolors.GREEN}☻{bcolors.ENDC} {bcolors.BOLD}{message}{bcolors.ENDC}")


def select_game_state():
    while True:
        util.clear_screen()
        print("1. New Game")
        print("2. Load Game")
        key = util.key_pressed().upper()
        if key == '1':
            return True
        elif key == '2':
            return False
        else:
            print('Wrong input')
            time.sleep(2)


def display_inventory(player):
    inventory_scroll = [f'{bcolors.YELLOW}   ______________________________{bcolors.ENDC}',
                        f'{bcolors.YELLOW} / \                             \.{bcolors.ENDC}',
            f'{bcolors.YELLOW}|   |{bcolors.ENDC}      {bcolors.BOLD}{bcolors.RED}Player inventory{bcolors.ENDC}      {bcolors.YELLOW}|.{bcolors.ENDC}',
                        f'{bcolors.YELLOW} \_ |                            |.{bcolors.ENDC}'] 
    for k in player['inventory']:
        for item in ITEMS:
            if item['name'] == k:
                icon = item['icon']
        row = f"{bcolors.YELLOW}    |{bcolors.ENDC}  {icon} - {k}: {player['inventory'][k]} "
        while len(row) < len(' \_ |                                     '):
            row += ' '
        row += f'{bcolors.YELLOW}         |.{bcolors.ENDC}'
        inventory_scroll.append(row)
    for line in [f'{bcolors.YELLOW}    |   _________________________|___{bcolors.ENDC}',
                 f'{bcolors.YELLOW}    |  /                            /.{bcolors.ENDC}',
                 f'{bcolors.YELLOW}    \_/____________________________/.{bcolors.ENDC}']:
        inventory_scroll.append(line)
    for row in inventory_scroll:
        print(row)
    secret_code = input("\nPress enter to exit inventory > ")
    if secret_code.upper() == 'PANIZDZIEKANATU':
        win_message(player)
    
    
def lose_message():
    util.clear_screen()
    message = END_MESSAGE_LOSE
    scroll = engine.create_intro_scroll(message)
    display_intro(scroll)
    quit()


def win_message(player):
    util.clear_screen()
    name = player['name']
    message = END_MESSAGE_WIN
    scroll = engine.create_intro_scroll(message)
    display_intro(scroll)
    quit()
