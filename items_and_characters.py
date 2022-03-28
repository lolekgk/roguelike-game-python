
#the value for "effect" is a tuple containing info about which studen's attribute is affected and how
ITEMS = [
        {"name": "notes",               "icon": "█", "total amount": 4, "effect": {"energy": 0, "knowledge": 1} },
        {"name": "Red Bull",            "icon": "E", "total amount": 8, "effect": {"energy": 4, "knowledge": 1} },
        {"name": "instant noodles",     "icon": "§", "total amount": 6, "effect": {"energy": 2, 'knowledge': 0} },
        {"name": "beer",                "icon": "%", "total amount": 6, "effect": {"energy": 0, "knowledge": 0} },
        {"name": "nerd's notes",        "icon": "◘", "total amount": 0, "effect": {'energy': 1, "knowledge": 3} },
        {"name": "last year's test",    "icon": "T", "total amount": 0, "effect": {'energy': 2, "knowledge": 6} }
        ]


# the value for "attributes" is a list of tuples; 
# each tuple cointains item name and probability of getting that item upon interaction
# probabilieties sum up to 1
COMPLEX_ITEM = {"name": "fridge", "icon": "[]", "total amount": 1, "items_list": [("Red Bull", 0.8), ("beer", 0.2)]}

  
# the value for "attributes" is a list of tuples; 
# each tuple cointains item name and probability of getting that item upon interaction of player with smartness 0 without any wheapon in inventory
# the probability increase with smartness and "wheapon"
NPCS = [ 
        {"name": "best student",       "icon": "♥", "field": ( 3, 2), "attribute": "nerd's notes", "probability": 0.5, "energy damage": -5},
        {"name": "perpetual student",  "icon": "‼", "field": (18,14), "attribute": "last year's test", "probability": 0, "energy damage": -10}
        ]


# a dictionary of dictionaries with type name as key
# the value is a dictionary with a character's parameters
PLAYER_TYPES = {
        'Nerd':         {'class': 'Nerd',       'knowledge': 10, 'smartness': 0, 'energy': 20, 'exams': 0, "inventory": {"beer": 0}}, 
        'Average':      {'class': 'Average',    'knowledge': 5,  'smartness': 1, 'energy': 20, 'exams': 0, "inventory": {"beer": 0}},
        'Laid-back':    {'class': 'Laid-back',  'knowledge': 1,  'smartness': 2, 'energy': 20, 'exams': 0, "inventory": {"beer": 1}}
        }
