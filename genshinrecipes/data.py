from json import load
from importlib.resources import open_text

__genshinrecipes_data = load(open_text('genshinrecipes', 'recipes.json'))

def return_data():
    return __genshinrecipes_data

def filter_by_rarity(rarity: int):
    matches = dict()

    for key, value in __genshinrecipes_data.items():
        if value['rarity'] == rarity:
            matches[key] = value
    
    return matches
