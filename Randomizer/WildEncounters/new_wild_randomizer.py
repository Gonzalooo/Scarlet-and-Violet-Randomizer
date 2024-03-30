import json
import random
import os

chosen_biomes = []
recreated_species = []
recreated_altforms = []


def fetch_devname(index: int, csvdata):
    pass # rewrite


# find a way to merge these 3 functions
def get_alt_form_paldea(index: int):
    has_alt = []
    if index in has_alt:
        choice = 0
        match index:
            case 25:
                choice = [1,2,3,4,5,6,7,9]
                # form 8 not in the game (Partner Let's Go Pikachu)
                return choice
            case 52:
                choice = [1,2]
                return choice
            case 80:
                choice = [2]
                # form 1 not in the game (Mega Slowbro)
                return choice
            case 128:
                choice = [0]
                return choice
            case 194:
                choice = [0]
                return choice
            case 386:
                choice = [1,2,3]
                return choice
            case 479:
                choice = [1,2,3,4,5]
                return choice
            case 550:
                choice = [2]
                return choice
            case 646:
                choice = [1,2]
                return choice
            case 774:
                choice = [1,2,3,4,5,6]
                return choice
            case 800:
                choice = [1, 2]
                return choice
            case 869:
                choice = [1,2,3,4,5,6,7,8]
                return choice
            case 898:
                choice = [1,2]
                return choice
            case 952:
                choice = [1,2]
                return choice
            case 960:
                choice = [1,2,3]
                return choice
            case 1011:
                choice = [1,2,3]
                return choice
            case _:
                choice = [1]
                return choice
    else:
        return [0]


def get_alt_form_teal(index: int):
    has_alt = []
    if index in has_alt:
        choice = 0
        match index:
            case 25:
                choice = [1,2,3,4,5,6,7,8,9]
                # form 8 not in the game (Partner Let's Go Pikachu)
                return choice
            case 52:
                choice = [1,2]
                return choice
            case 80:
                choice = [1,2]
                # form 1 not in the game (Mega Slowbro)
                return choice
            case 128:
                choice = [1,2,3]
                return choice
            case 194:
                choice = [1]
                return choice
            case 386:
                choice = [1,2,3]
                return choice
            case 479:
                choice = [1,2,3,4,5]
                return choice
            case 550:
                choice = [0, 1]
                return choice
            case 585:
                choice = [1,2,3]
                return choice
            case 586:
                choice = [1,2,3]
                return choice
            case 646:
                choice = [1,2]
                return choice
            case 669:
                choice = [1,2,3,4]
                return choice
            case 670:
                choice = [1, 2, 3, 4]
                return choice
            case 671:
                choice = [1, 2, 3, 4]
                return choice
            case 774: # includes shield downs form
                choice = [1,2,3,4,5,6]
                return choice
            case 800:
                choice = [1, 2]
                return choice
            case 869:
                choice = [1,2,3,4,5,6,7,8]
                return choice
            case 898:
                choice = [1,2]
                return choice
            case 952:
                choice = [1,2]
                return choice
            case 960:
                choice = [1,2,3]
                return choice
            case 1011:
                choice = [1,2,3]
                return choice
            case _:
                choice = [1]
                return choice
    else:
        return [0]


def get_alt_form_indigo(index: int):
    has_alt = []
    if index in has_alt:
        choice = 0
        match index:
            case 25:
                choice = [1,2,3,4,5,6,7,8,9]
                # form 8 not in the game (Partner Let's Go Pikachu)
                return choice
            case 27:
                choice = [0]
                return choice
            case 28:
                choice = [0]
                return choice
            case 29:
                choice = [0]
                return choice
            case 30:
                choice = [0]
                return choice
            case 50:
                choice = [0]
                return choice
            case 51:
                choice = [0]
                return choice
            case 52:
                choice = [1,2]
                return choice
            case 74:
                choice = [0]
                return choice
            case 75:
                choice = [0]
                return choice
            case 76:
                choice = [0]
                return choice
            case 79:
                choice = [0]
                return choice
            case 80:
                choice = [0]
                # form 1 not in the game (Mega Slowbro)
                return choice
            case 103:
                choice = [0]
                return choice
            case 128:
                choice = [1,2,3]
                return choice
            case 211:
                choice = [0]
                return choice
            case 386:
                choice = [1,2,3]
                return choice
            case 479:
                choice = [1,2,3,4,5]
                return choice
            case 550:
                choice = [1,2]
                return choice
            case 646:
                choice = [1,2]
                return choice
            case 669:
                choice = [1,2,3,4]
                return choice
            case 670:
                choice = [1, 2, 3, 4]
                return choice
            case 671:
                choice = [1, 2, 3, 4]
                return choice
            case 745:
                choice = [1,2]
                return choice
            case 800:
                choice = [1, 2]
                return choice
            case 869:
                choice = [1,2,3,4,5,6,7,8]
                return choice
            case 898:
                choice = [1,2]
                return choice
            case 952:
                choice = [1,2]
                return choice
            case 960:
                choice = [1,2,3]
                return choice
            case 1011:
                choice = [1,2,3]
                return choice
            case _:
                choice = [1]
                return choice
    else:
        return [0]


def pick_random_biome():
    possible_biomes = ["GRASS", "FOREST", "SWAMP", "LAKE", "TOWN", "MOUNTAIN", "BAMBOO", "MINE", "CAVE", "OLIVE",
                       "UNDERGROUND", "RIVER", "ROCKY", "BEACH", "SNOW", "OSEAN", "RUINS", "FLOWER"]
    choice = possible_biomes[random.randint(0, len(possible_biomes) - 1)]
    while choice in chosen_biomes:
        choice = possible_biomes[random.randint(0, len(possible_biomes) - 1)]
        if len(chosen_biomes) > 4:
            break
    chosen_biomes.append(choice)
    return choice


def generate_lot_value_for_biome():
    return random.randint(1, 50)


def generate_area():
    return random.sample(range(1, 27), 10)


def generate_area_list():
    return(str(generate_area()).replace('[','"').replace(']','"').replace(' ',''))

# fix function to add item for item pokemon
def make_template(new_template, index, csvdata, form=0):
    new_template['devid'] = fetch_devname(index, csvdata)
    new_template['formno'] = form
    new_template['minlevel'] = 2
    new_template['maxlevel'] = 99
    new_template['lotvalue'] = random.randint(1, 50)
    new_template['biome1'] = pick_random_biome()
    new_template['biome2'] = pick_random_biome()
    new_template['biome3'] = pick_random_biome()
    new_template['biome4'] = pick_random_biome()
    new_template['lotvalue1'] = generate_lot_value_for_biome(new_template['biome1'])
    new_template['lotvalue2'] = generate_lot_value_for_biome(new_template['biome2'])
    new_template['lotvalue3'] = generate_lot_value_for_biome(new_template['biome3'])
    new_template['lotvalue4'] = generate_lot_value_for_biome(new_template['biome4'])
    chosen_biomes.clear()
    new_template['area'] = generate_area_list()
    new_template['locationName'] = ""
    new_template['enabletable']['land'] = True
    new_template['enabletable']['up_water'] = True
    new_template['enabletable']['underwater'] = True
    new_template['enabletable']['air1'] = True
    new_template['enabletable']['air2'] = True
    new_template['timetable']['morning'] = True
    new_template['timetable']['noon'] = True
    new_template['timetable']['evening'] = True
    new_template['timetable']['night'] = True
    new_template['flagName'] = ""
    new_template['versiontable']['A'] = True
    new_template['versiontable']['B'] = True
    new_template['bringItem']['itemID'] = "ITEMID_NONE"
    new_template['bringItem']['bringRate'] = 0
    return new_template