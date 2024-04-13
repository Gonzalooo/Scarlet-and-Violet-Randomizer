import os
import json
import copy
import random
import Randomizer.shared_Variables as SharedVariables
import Randomizer.helper_function as HelperFunctions

sprigattio_offset = 0x3D8A  # 6c 02
fuecoco_offset = 0x158A  # 6d 02
quaxly_offset = 0x2992  # 6e 02


def fetch_devname(index: int, csvdata):
    return str.strip(csvdata[index])


def fetch_devname_index(name: str, csvdata):
    for index, current_name in enumerate(csvdata):
        if str.strip(current_name) == name:
            return index


def patchIndividualScenes():
    # thats ugly but i have no inspiration rn
    scarlet_scene = open(os.getcwd() + "/Randomizer/Scenes/starters_scenes/common_0070_always_0_clean.trsog", "rb")
    violet_scene = open(os.getcwd() + "/Randomizer/Scenes/starters_scenes/common_0070_always_1_clean.trsog", "rb")
    scarlet_scene_bytes = scarlet_scene.read()
    violet_scene_bytes = violet_scene.read()
    scarlet_scene.close()
    violet_scene.close()

    # print(scarlet_scene_bytes)
    # thats even more ugly but f it
    with open(os.getcwd() + "/Randomizer/Scenes/starters_scenes/common_0070_always_0.trsog", "w+b") as file:
        file.write(scarlet_scene_bytes)
        file.seek(sprigattio_offset)
        file.write(b'\x6C\x02')
        file.seek(fuecoco_offset)
        file.write(b'\x6D\x02')
        file.seek(quaxly_offset)
        file.write(b'\x6E\x02')
    with open(os.getcwd() + "/Randomizer/Scenes/starters_scenes/common_0070_always_1.trsog", "w+b") as file:
        file.write(violet_scene_bytes)
        file.seek(sprigattio_offset)
        file.write(b'\x6C\x02')
        file.seek(fuecoco_offset)
        file.write(b'\x6D\x02')
        file.seek(quaxly_offset)
        file.write(b'\x6E\x02')


def retrieve_starter(starters, label):
    for entry in starters['values']:
        if entry['label'] == label:
            return entry


def retrieve_catalog_entry(catalog: dict, species, form, fake_catalog_index):
    for entry in catalog['unk_1']:
        if entry['speciesinfo']['species_number'] == species and entry['speciesinfo']['form_number'] == form:
            # return_entry = entry #probably unnecessary
            return_entry = copy.deepcopy(entry)
            return_entry['speciesinfo']['species_number'] = fake_catalog_index
            if form != 0:
                return_entry['speciesinfo']['form_number'] = 0
                for anim in return_entry['animations']:
                    anim['form_number'] = 0
                for locator in return_entry['locators']:
                    locator['form_number'] = 0
            return return_entry


def patchCatalog(names: list, catalog, starters):
    starter_array_order = ['common_0065_kusa', 'common_0065_hono',
                           'common_0065_mizu']  # prevents me from writing a lot of useless code
    fake_catalog_species = 620
    for current_starter in starter_array_order:
        starter = retrieve_starter(starters, current_starter)
        species_index = fetch_devname_index(starter['pokeData']['devId'], names)
        form_index = starter['pokeData']['formId']
        catalog_entry = retrieve_catalog_entry(catalog, species_index, form_index,
                                               fake_catalog_species)  # replace species index
        catalog['unk_1'].append(catalog_entry)
        fake_catalog_species = fake_catalog_species + 1  # this goes until 622
    pass


def patchScenes():
    # load starters
    starterfile = open(os.getcwd() + "/Randomizer/StartersGifts/" + "eventAddPokemon_array.json",
                       "r")  # 0 is fuecoco, 1 is sprigattio, 2 is quaxly
    starters = json.load(starterfile)
    starterfile.close()

    # load model catalog
    catalogfile = open(os.getcwd() + "/Randomizer/Scenes/poke_resource_table_clean.json", "r")
    catalog = json.load(catalogfile)
    catalogfile.close()

    # load names
    file = open(os.getcwd() + "/Randomizer/StartersGifts/" + "pokemon_to_id.txt", "r")
    names = []
    for name in file:
        names.append(name)
    file.close()

    patchIndividualScenes()
    patchCatalog(names, catalog, starters)

    outdata = json.dumps(catalog, indent=4)
    with open(os.getcwd() + "/Randomizer/Scenes/" + "poke_resource_table.json", 'w') as outfile:
        outfile.write(outdata)
    print("Patched starters in overworld")
    return True


# get pokemon dictionary with hex values
pokemon_dict_json = open(os.getcwd() + "/Randomizer/Scenes/" + "pokemon_dict_info.json", "r")
pokemon_dict = json.load(pokemon_dict_json)
pokemon_dict_json.close()


def patch_starter_selection_scenes():
    # load starters - 0 is fuecoco, 1 is sprigattio, 2 is quaxly
    starterfile = open(os.getcwd() + "/Randomizer/StartersGifts/" + "eventAddPokemon_array.json", "r")
    starters = json.load(starterfile)
    starterfile.close()

    scarlet_scene = open(os.getcwd() + "/Randomizer/Scenes/starters_scenes/common_0070_always_0_clean.trsog", "rb")
    violet_scene = open(os.getcwd() + "/Randomizer/Scenes/starters_scenes/common_0070_always_1_clean.trsog", "rb")
    scarlet_scene_bytes = scarlet_scene.read()
    violet_scene_bytes = violet_scene.read()
    scarlet_scene.close()
    violet_scene.close()

    hex_checks = [pokemon_dict['pokemons'][starters['values'][0]['pokeData']['devId']]['hex'],
                  pokemon_dict['pokemons'][starters['values'][1]['pokeData']['devId']]['hex'],
                  pokemon_dict['pokemons'][starters['values'][2]['pokeData']['devId']]['hex']]

    # sprigattio_offset = 0x3D8A  # 6c 02
    # fuecoco_offset = 0x158A  # 6d 02
    # quaxly_offset = 0x2992  # 6e 02
    offset = [0x158A, 0x3D8A, 0x2992]

    for i in range(0, 2):
        with open(os.getcwd() + f"/Randomizer/Scenes/starters_scenes/common_0070_always_{str(i)}.trsog", "w+b") as file:
            if i == 0:
                file.write(scarlet_scene_bytes)
            elif i == 1:
                file.write(violet_scene_bytes)
            for j in range(0, len(offset)):
                file.seek(offset[j])
                file.write(bytearray.fromhex(hex_checks[j]))

    print("Patched starters in overworld")


def patch_lechonk_starting_scene():
    scarlet_scene = open(os.getcwd() + "/Randomizer/Scenes/lechonk_scenes/common_0100_main_0_clean.trsog", "rb")
    violet_scene = open(os.getcwd() + "/Randomizer/Scenes/lechonk_scenes/common_0100_main_1_clean.trsog", "rb")
    scarlet_scene_bytes = scarlet_scene.read()
    violet_scene_bytes = violet_scene.read()
    scarlet_scene.close()
    violet_scene.close()

    lechonk_file = open(os.getcwd() + "/Randomizer/StaticFights/" + "eventBattlePokemon_array.json", "r")
    lechonk = json.load(lechonk_file)
    lechonk_file.close()

    # 0 - fletching
    # 1 - flecthing (2) [map out which exactly better later]
    # 2 - Pawmi
    # 3->6 - tarountula
    # 7->11 - Lechonk
    offset = [0xAB6, 0x1FE2, 0x350E, 0x4A3A, 0x5F62, 0x748A, 0x89B2, 0x9EDA, 0xB402, 0xC92A, 0xDE52, 0xF37A]

    for i in range(0, 2):
        with open(os.getcwd() + f"/Randomizer/Scenes/lechonk_scenes/common_0100_main_{str(i)}.trsog", "w+b") as file:
            if i == 0:
                file.write(scarlet_scene_bytes)
            elif i == 1:
                file.write(violet_scene_bytes)
            for j in range(0, len(offset)):
                file.seek(offset[j])
                if j >= 7:
                    hex_values_to_use = pokemon_dict['pokemons'][lechonk['values'][24]['pokeData']['devId']]['hex']
                    file.write(bytearray.fromhex(hex_values_to_use))
                else:
                    # For now all other pokemon random until we find a way to map the areas and spawnpoints
                    choice = random.randint(1, 1025)
                    while choice in SharedVariables.banned_pokemon:
                        choice = random.randint(1, 1025)
                    hex_values_to_use = pokemon_dict['pokemons'][HelperFunctions.fetch_developer_name(choice)]['hex']
                    file.write(bytearray.fromhex(hex_values_to_use))

    print("Patched Lechonk in overworld")


def patch_gimmighoul_scene():
    for i in range(0, 2):
        game_scene = open(os.getcwd() + f"/Randomizer/Scenes/gimmighoul_scene/coin_symbol_box_{str(i)}_clean.trsot", "rb")
        game_scene_bytes = game_scene.read()
        game_scene.close()

        ghoul_file = open(os.getcwd() + "/Randomizer/StaticFights/" + "eventBattlePokemon_array.json", "r")
        gimmighoul = json.load(ghoul_file)
        ghoul_file.close()

        # 0 - Gimmighoul
        offset = [0x656]

        with open(os.getcwd() + f"/Randomizer/Scenes/gimmighoul_scene/coin_symbol_box_{str(i)}.trsot", "w+b") as file:
            file.write(game_scene_bytes)
            for j in range(0, len(offset)):
                file.seek(offset[j])
                hex_values_to_use = pokemon_dict['pokemons'][gimmighoul['values'][9]['pokeData']['devId']]['hex']
                file.write(bytearray.fromhex(hex_values_to_use))

    print("Patched Gimmighoul in overworld")