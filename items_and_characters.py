PLAYER = {"position": (3, 3), "icon": '☻'}

#the value for "effect" is a tuple containing info about which studen's attribute is affected and how
ITEMS = [{"name": "nerd's notes", "icon": "◘", "total amount": 4, "effect": ("knowledge", +1) },
        {"name": "last year's test", "icon": "T", "total amount": 2, "effect": ("knowledge", +3) },
        {"name": "Red Bull", "icon": "E", "total amount": 8, "effect": ("energy", +4)},
        {"name": "instant noodles", "icon": "§", "total amount": 6, "effect": ("energy", +4)},
        {"name": "beer", "icon": "%", "total amount": 6, "effect": ("energy", +4)}]


# the value for "attributes" is a list of tuples; 
# each tuple cointains item name and probability of getting that item upon interaction
# probabilieties sum up to 1
COMPLEX_ITEM = {"name": "fridge", "icon": "[]", "total amount": 1, "items_list": [("Red Bull", 0.8), ("beer", 0.2)]}


# the value for "attributes" is a list of tuples; 
# each tuple cointains item name and probability of getting that item upon interaction
# probabilieties sum up to 1
NPC = [{"name": "best student", "icon": "♥", "position": (18, 2),
             "attributes": [("nerd's notes", 1)]},
            {"name": "perpetual student", "icon": "‼", "position": (12, 15),
             "attributes": [("last year's test", 0.5), ("beer", 0.5)]}]


# a dictionary of dictionaries with type name as key
# the value is a dictionary with a character's parameters
PLAYER_TYPES = {
        'Nerd': {'class': 'Nerd', 'name': None, 'knowledge': 10, 'smartness': 2, 'energy': 20, 'exams': None}, 
        'Laid-back': {'class': 'Laid-back', 'name': None, 'knowledge': 1, 'smartness': 6, 'energy': 20, 'exams': None},
        'Average': {'class': 'Average', 'name': None, 'knowledge': 5, 'smartness': 4, 'energy': 20, 'exams': None}
        }
