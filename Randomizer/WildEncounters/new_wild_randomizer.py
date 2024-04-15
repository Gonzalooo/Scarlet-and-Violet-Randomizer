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


def generate_area():
    return random.sample(range(1, 27), 10)


def generate_area_list():
    return str(generate_area()).replace('[', '"').replace(']', '"').replace(' ', '')


# fix function to add item for item pokemon
def make_template(new_template, index, form=0):
    new_template['formno'] = form
    new_template['lotvalue'] = random.randint(1, 50)
    new_template['biome1'] = pick_random_biome()
    new_template['biome2'] = pick_random_biome()
    new_template['biome3'] = pick_random_biome()
    new_template['biome4'] = pick_random_biome()
    new_template['lotvalue1'] = generate_lot_value_for_biome()
    new_template['lotvalue2'] = generate_lot_value_for_biome()
    new_template['lotvalue3'] = generate_lot_value_for_biome()
    new_template['lotvalue4'] = generate_lot_value_for_biome()
    chosen_biomes.clear()
    new_template['area'] = generate_area_list()
    item_obtained, rate_of_item = HelperFunctions.get_pokemon_item_form(index, form)
    new_template['bringItem']['itemID'] = item_obtained
    new_template['bringItem']['bringRate'] = rate_of_item

    return new_template


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
            'area': generate_area_list(),
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
            new_template = make_template(forms_entry, index, form)

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
            randomize_wild_encounters(config['paldea_settings']['wild_randomizer'], "Paldea", usable_pokemon)
            randomize_wild_encounters(config['paldea_settings']['wild_randomizer'], "Kitakami", usable_pokemon)
            randomize_wild_encounters(config['paldea_settings']['wild_randomizer'], "Blueberry", usable_pokemon)
            return True, True, True
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
