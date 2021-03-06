class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    GRAY = "\033[100m"
    ENDC = '\033[0m'
    PURPLE = "\033[35m"
    BROWN = "\033[97m" #nie jest brązowy :(


# the value for "effect" is a tuple containing info about which studen's attribute is affected and how
# please don't add a new item with a name longer than 16 characters, as it will mess up the inventory! ~~Sebastian
ITEMS = [
        {"name": "notes",               "level": 1, "icon": "█",                                "total amount": 4, "effect": {"knowledge": 1} },
        {"name": "Red Bull",            "level": 1, "icon": f"{bcolors.BLUE}E{bcolors.ENDC}",   "total amount": 8, "effect": {"energy": 2, "knowledge": 0} },
        {"name": "instant noodles",     "level": 1, "icon": "§",                                "total amount": 6, "effect": {"energy": 1} },
        {"name": "beer",                "level": 1, "icon": f"{bcolors.YELLOW}%{bcolors.ENDC}", "total amount": 6, "effect": {} },
        {"name": "nerd's notes",        "level": 1, "icon": "◘",                                "total amount": 0, "effect": {"energy": 1, "knowledge": 4} },
        {"name": "last year's test",    "level": 1, "icon": "T",                                "total amount": 0, "effect": {"energy": 2, "knowledge": 7} }, 
        {"name": "flowers",             "level": 2, "icon": f"{bcolors.PURPLE}*{bcolors.ENDC}", "total amount": 4, "effect": {} },
        {"name": "chocolates",          "level": 2, "icon": f"{bcolors.BROWN}#{bcolors.ENDC}",  "total amount": 4, "effect": {} },
        {"name": "Red Bull",            "level": 2, "icon": f"{bcolors.BLUE}E{bcolors.ENDC}",   "total amount": 3, "effect": {"energy": 3} },
        {"name": "exam",                "level": 2, "icon": "X",                                "total amount": 0, "effect": {"energy": 2, "exam": 1 } },
        {"name": "key",                 "level": 1, "icon": f"{bcolors.CYAN}¬{bcolors.ENDC}",   "total amount": 0, "effect": {} }
        ]


# the value for "attributes" is a list of tuples; 
# each tuple cointains item name and probability of getting that item upon interaction
# probabilieties sum up to 1
COMPLEX_ITEM = {"name": "fridge", "icon": "[]", "total amount": 1, "items_list": [("Red Bull", 0.8), ("beer", 0.2)]}

  
# the value for "attributes" is a list of tuples; 
# each tuple cointains item name and probability of getting that item upon interaction of player with smartness 0 without any wheapon in inventory
# the probability increase with smartness and "wheapon"
NPCS = [ 
        {"name": "best student",        "level": 1, "icon": f"{bcolors.RED}♥{bcolors.ENDC}",     "field": ( 2,20), "attribute": "nerd's notes",        "probability": 0.5, "energy damage": 5},
        {"name": "perpetual student",   "level": 1, "icon": f"{bcolors.RED}‼{bcolors.ENDC}",     "field": (15,14), "attribute": "last year's test",    "probability": 0,   "energy damage": 10},
        {"name": "math professor",      "level": 2, "icon": f"{bcolors.RED}π{bcolors.ENDC}",     "field": (14,21), "attribute": "exam",                "probability": 0,   "exam requirement" : {"knowledge": 12, "energy": 18}},
        {"name": "english professor",   "level": 2, "icon": f"{bcolors.RED}\u00E6{bcolors.ENDC}","field": (15, 6), "attribute": "exam",                "probability": 0.2,"exam requirement" : {"knowledge": 8, "energy": 12}},
        {"name": "philosophy professor","level": 2, "icon": f"{bcolors.RED}?{bcolors.ENDC}",     "field": (11, 7), "attribute": "exam",                "probability": 0.5, "exam requirement" : {"knowledge": 4, "energy": 6}}
        ]


BOSS = {"name": "Boss", "icon": '^|-O=', "face": ['^^^^^', '|O-O|', '| ^ |', '|===|', '-----'],  "field": (14, 14), "attribute": None, "probability": 0, "energy damage": 3, "content": 0}


# a dictionary of dictionaries with type name as key
# the value is a dictionary with a character's parameters
PLAYER_TYPES = {
        'Nerd':         {'class': 'Nerd',       'knowledge': 10, 'smartness': 0, 'energy': 20, 'exam': 0, "inventory": {"beer": 0, "key": 0, "flowers": 0, "chocolates": 1}}, 
        'Average':      {'class': 'Average',    'knowledge': 5,  'smartness': 1, 'energy': 20, 'exam': 0, "inventory": {"beer": 0, "key": 0, "flowers": 0, "chocolates": 0}},
        'Laid-back':    {'class': 'Laid-back',  'knowledge': 1,  'smartness': 2, 'energy': 20, 'exam': 0, "inventory": {"beer": 1, "key": 0, "flowers": 0, "chocolates": 0}}
        }


