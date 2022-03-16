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
CHARACTERS = [{"name": "best student", "icon": "♥", "attributes": [("nerd's notes", 1)]},
            {"name": "perpetual student", "icon": "‼", "attributes": [("last year's test", 0.5), ("beer", 0.5)]}]

