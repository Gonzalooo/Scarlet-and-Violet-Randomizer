import json
import random
import os
import Randomizer.helper_function as HelperFunctions
import Randomizer.shared_Variables as SharedVariables

chosen_biomes = []
wilderness_paths = {
    "wilds": "world/data/encount/pokedata/pokedata/",
    "wilds_su1": "world/data/encount/pokedata/pokedata_su1/",
    "wilds_su2": "world/data/encount/pokedata/pokedata_su2/",
}


def get_alt_form_list(index: int):
    if index in SharedVariables.has_alternate_form:
        match index:
            case 25:
                return [1, 2, 3, 4, 5, 6, 7, 9]
            case 52:
                return [1, 2]
            case 80:
                return [2]
            case 128:
                return [1, 2, 3]
            case 386:
                return [1, 2, 3]
            case 479:
                return [1, 2, 3, 4, 5]
            case 493:
                return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
            case 585:
                return [1, 2, 3]
            case 586:
                return [1, 2, 3]
            case 646:
                return [1, 2]
            case 664:
                return [1]
            case 665:
                return [1]
            case 666:
                return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
            case 669:
                return [1, 2, 3, 4]
            case 670:
                return [1, 2, 3, 4]
            case 671:
                return [1, 2, 3, 4]
            case 741:
                return [1, 2, 3]
            case 745:
                return [1, 2]
            case 774:
                return [1, 2, 3, 4, 5, 6]
            case 778:
                return []
            case 800:
                return [1, 2]
            case 845:
                return []
            case 869:
                return [1, 2, 3, 4, 5, 6, 7, 8]
            case 875:
                return []
            case 877:
                return []
            case 898:
                return [1, 2]
            case 978:
                return [1, 2]
            case 931:
                return [1, 2, 3]
            case 1017:
                return [1, 2, 3]
            case _:
                return [1]
    else:
        return []


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


def generate_area(region: str):
    if region == "Paldea":
        return random.sample(range(1, 27), 6)
    elif region == "Kitakami":
        return random.sample(range(1, 11), 5)
    elif region == "Blueberry":
        return random.sample(range(1, 4), 2)


def generate_area_list(region: str):
    return str(generate_area(region)).replace('[', '"').replace(']', '"').replace(' ', '')


# fix function to add item for item pokemon
def make_template(new_template, index, region: str, form=0):
    new_template['formno'] = form
    new_template['lotvalue'] = random.randint(1, 50)
    arealist = generate_area_list(region)
    new_template['area'] = arealist
    new_template['biome1'] = pick_random_biome()
    new_template['biome2'] = pick_random_biome()
    new_template['biome3'] = pick_random_biome()
    new_template['biome4'] = pick_random_biome()
    new_template['lotvalue1'] = generate_lot_value_for_biome()
    new_template['lotvalue2'] = generate_lot_value_for_biome()
    new_template['lotvalue3'] = generate_lot_value_for_biome()
    new_template['lotvalue4'] = generate_lot_value_for_biome()
    chosen_biomes.clear()
    item_obtained, rate_of_item = HelperFunctions.get_pokemon_item_form(index, form)
    new_template['bringItem']['itemID'] = item_obtained
    new_template['bringItem']['bringRate'] = rate_of_item

    return new_template


def balance_spawns(region: str, areas: str, entry: dict):
    if region == "Paldea":

        list_of_areas = ((areas.replace("\"", "")).replace(" ", "")).split(',')
        location_areas = ""
        if '23' in list_of_areas:
            list_of_areas.remove('23')
            choice = random.randint(0, 6)
            if len(location_areas) == 0:
                location_areas = SharedVariables.area_zero_locations[choice]
            else:
                location_areas = location_areas + SharedVariables.area_zero_locations[choice]
            choice_second = random.randint(0, 6)
            while choice_second == choice:
                choice_second = random.randint(0, 6)
            location_areas = location_areas + SharedVariables.area_zero_locations[choice_second]
        entry['locationName'] = location_areas

        return entry
    pass


def generate_pokemon_entry(pokemon_index: int, region: str):
    '''
            template_entry = {
            "devid": HelperFunctions.fetch_developer_name(index),
            "sex": "DEFAULT",
            "formno": 0,
            "minlevel": 2,
            "maxlevel": 99,
            "lotvalue": random.randint(1, 50),
            "biome1": pick_random_biome(),
            'lotvalue1': generate_lot_value_for_biome(),
            "biome2": pick_random_biome(),
            'lotvalue2': generate_lot_value_for_biome(),
            "biome3": pick_random_biome(),
            'lotvalue3': generate_lot_value_for_biome(),
            "biome4": pick_random_biome(),
            'lotvalue4': generate_lot_value_for_biome(),
            'area': generate_area_list(region),
            'locationName': "",
            "minheight": 0,
            "maxheight": 0,
            "enabletable": {
                "land": True,
                "up_water": True,
                "underwater": True,
                "air1": True,
                "air2": True
            },
            "timetable": {
                "morning": True,
                "noon": True,
                "evening": True,
                "night": True
            },
            "flagName": "",
            "bandrate": 0,
            "bandtype": "NONE",
            "bandpoke": "DEV_NULL",
            "bandSex": "DEFAULT",
            "bandFormno": 0,
            "outbreakLotvalue": 10,
            "pokeVoiceClassification": "ANIMAL_LITTLE",
            "versiontable": {
                "A": True,
                "B": True
            },
            "bringItem": {
                "itemID": "ITEMID_NONE",
                "bringRate": 0
            }
        }
    '''

    pokemon_entry = {
        "devid": HelperFunctions.fetch_developer_name(pokemon_index),
        'sex': "DEFAULT",
        'formno': 0
    }
    areas = generate_area_list(region)
    pokemon_entry = balance_spawns(region, areas, pokemon_entry)
    print(pokemon_entry)
    exit(0)

    return 0


def balanced_wild_encounters(config, region: str, allowed_pokemon: list):
    for pokemon in range(0, 1026):
        if pokemon in SharedVariables.banned_pokemon:
            continue

        if pokemon not in allowed_pokemon:
            continue

        randomized_pokemon = generate_pokemon_entry(pokemon, region)


def create_wilderness_file(region: str):
    if region == "Paldea":
        return "pokedata_array.json"
    if region == "Kitakami":
        return "pokedata_su1_array.json"
    if region == "Blueberry":
        return "pokedata_su2_array.json"

    print("No Valid Region")
    exit(0)


def randomize_wild_encounters(config, region: str, allowed_pokemon: list):
    poke_dict: dict[str, list] = {'values': []}

    # Recreate whole json file to manually add every pokemon not banned.
    for index in range(1, 1026):
        if index in SharedVariables.banned_pokemon:
            continue

        if index not in allowed_pokemon:
            continue

        if config['exclude_legendaries'] == "yes":
            if index in SharedVariables.legends:
                continue

        elif config['only_legendary_pokemon'] == "yes":
            if index not in SharedVariables.legends:
                continue

        elif config['only_paradox_pokemon'] == "yes":
            if index not in SharedVariables.paradox:
                continue

        elif config['only_legends_and_paradox'] == "yes":
            if index not in SharedVariables.legends_and_paradox:
                continue
        template_entry = {
            "devid": HelperFunctions.fetch_developer_name(index),
            "sex": "DEFAULT",
            "formno": 0,
            "minlevel": 2,
            "maxlevel": 99,
            "lotvalue": random.randint(1, 50),
            "biome1": pick_random_biome(),
            'lotvalue1': generate_lot_value_for_biome(),
            "biome2": pick_random_biome(),
            'lotvalue2': generate_lot_value_for_biome(),
            "biome3": pick_random_biome(),
            'lotvalue3': generate_lot_value_for_biome(),
            "biome4": pick_random_biome(),
            'lotvalue4': generate_lot_value_for_biome(),
            'area': generate_area_list(region),
            'locationName': "",
            "minheight": 0,
            "maxheight": 0,
            "enabletable": {
                "land": True,
                "up_water": True,
                "underwater": True,
                "air1": True,
                "air2": True
            },
            "timetable": {
                "morning": True,
                "noon": True,
                "evening": True,
                "night": True
            },
            "flagName": "",
            "bandrate": 0,
            "bandtype": "NONE",
            "bandpoke": "DEV_NULL",
            "bandSex": "DEFAULT",
            "bandFormno": 0,
            "outbreakLotvalue": 10,
            "pokeVoiceClassification": "ANIMAL_LITTLE",
            "versiontable": {
                "A": True,
                "B": True
            },
            "bringItem": {
                "itemID": "ITEMID_NONE",
                "bringRate": 0
            }
        }

        forms_entry = template_entry.copy()
        new_template = template_entry.copy()

        poke_dict['values'].append(new_template)
        chosen_biomes.clear()

        forms = get_alt_form_list(index)
        for form in forms:
            new_template = make_template(forms_entry, index, region, form)

            poke_dict['values'].append(new_template)

    outdata = json.dumps(poke_dict, indent=2)
    with open(os.getcwd() + "/Randomizer/WildEncounters/" + create_wilderness_file(region), 'w') as outfile:
        outfile.write(outdata)
    print(f"Randomization - {region} Wilderness Done!")


def randomize_wilderness(config):
    if config['use_paldea_settings_for_all'] == "yes":
        if config['paldea_settings']['wild_randomizer']['is_enabled'] == "yes":
            usable_pokemon, useless, bpl = HelperFunctions.check_generation_limiter(config['paldea_settings']['wild_randomizer']
                                                                      ['generation_limiter'])
            balanced = False
            if config['paldea_settings']['wild_randomizer']['balance_bst_per_area'] == "yes":
                balanced = True
            if balanced is not True:
                randomize_wild_encounters(config['paldea_settings']['wild_randomizer'], "Paldea", usable_pokemon)
                randomize_wild_encounters(config['paldea_settings']['wild_randomizer'], "Kitakami", usable_pokemon)
                randomize_wild_encounters(config['paldea_settings']['wild_randomizer'], "Blueberry", usable_pokemon)
            else:
                print('Still a work in progress')
                exit(0)

        return False, False, False
    else:
        paldea_binary = False
        kitakami_binary = False
        blueberry_binary = False

        if config['paldea_settings']['wild_randomizer']['is_enabled'] == "yes":
            usable_pokemon, useless, bpl  = HelperFunctions.check_generation_limiter(config['paldea_settings']['wild_randomizer']
                                                                      ['generation_limiter'])
            randomize_wild_encounters(config['paldea_settings']['wild_randomizer'], "Paldea", usable_pokemon)

            paldea_binary = True
        if config['kitakami_settings']['wild_randomizer']['is_enabled'] == "yes":
            usable_pokemon, useless = HelperFunctions.check_generation_limiter(config['kitakami_settings']['wild_randomizer']
                                                                      ['generation_limiter'])
            randomize_wild_encounters(config['kitakami_settings']['wild_randomizer'], "Kitakami", usable_pokemon)

            kitakami_binary = True
        if config['blueberry_settings']['wild_randomizer']['is_enabled'] == "yes":
            usable_pokemon, useless = HelperFunctions.check_generation_limiter(config['blueberry_settings']['wild_randomizer']
                                                                      ['generation_limiter'])
            randomize_wild_encounters(config['blueberry_settings']['wild_randomizer'], "Kitakami", usable_pokemon)
            blueberry_binary = True

        return paldea_binary, kitakami_binary, blueberry_binary


# Areas maping - Paldea
# 1 - Los Platos / South Province (Area One)
# 2 - Unused Area (MAYBE DLC2 ?????)
# 3 - Pokemon League
# 4 - South Province (Area Two)
# 5 - South Province (Area Four)
# 6 - South Province (Area Six)
# 7 - South Province (Area Five)
# 8 - South Province (Area Three)
# 9 - West Province (Area One)
#10 - Asado Desert
#11 - West Province (Area Two)
#12 - West Province (Area Three)
#13 - Tagtree Thicket
#14 - East Province (Area Three)
#15 - East Province (Area One)
#16 - East Province (Area Two)
#17 - Dalizapa Passage
#18 - Casseroya Lake
#19 - Glaseado Mountain
#20 - North Province (Area Three)
#21 - North Province (Area One)
#22 - North Province (Area Two)
#23 - Area Zero
#24 - South Paldean Sea
#25 - West Paldean Sea
#26 - East Paldean Sea
#27 - North Paldean Sea

# Area mapping - Kitakami
# 1 - Kitakami Road
# 2 - Apple Hills
# 3 - Reveler's Road
# 4 - Oni Mountain
# 5 - Infernal Passage
# 6 - Crystal Pool
# 7 - Wistful Fields
# 8 - Mossfell Confluence
# 9 - Fellhorn Gorge
#10 - Paradize Barrens
#11 - kitakami wilds/timeless wood

# Area Mapping - Blueberry
# 1 - Savannah
# 2 - Coastal
# 3 - Polar
# 4 - Canyon

# paths to spawners info: world\data\encount\point_data\point_data\
# paths to tera_raid info: world\data\encount\point_data\outbreak_point_data\
# main path to field info: \world\data\field\area\....
