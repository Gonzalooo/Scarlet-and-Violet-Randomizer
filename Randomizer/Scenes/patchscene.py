import os
import json
import copy
import random
import shutil
import Randomizer.shared_Variables as SharedVariables
import Randomizer.helper_function as HelperFunctions

# get pokemon dictionary with hex values
pokemon_dict_json = open(os.getcwd() + "/Randomizer/Scenes/" + "pokemon_dict_info.json", "r")
pokemon_dict = json.load(pokemon_dict_json)
pokemon_dict_json.close()

catalogfile = open(os.getcwd() + "/Randomizer/Scenes/poke_resource_table_clean.json", "r")
poke_catalog = json.load(catalogfile)
catalogfile.close()


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


def create_new_file_for_shiny(catalog: dict, key_change: str, file_num: int):
    new_file_name = catalog[f'{key_change}'].split('/')
    new_file_name[0] = f'pm{file_num}'
    new_file_name = '/'.join(new_file_name)
    return new_file_name


def patch_poke_catalog(catalog: dict, poke_data: dict, fake_species_index: int, index_to_use: int, shiny=False):
    pokemon_to_add = poke_data['values'][index_to_use]
    species_index = pokemon_dict['pokemons'][pokemon_to_add['pokeData']['devId']]['id']
    form_index = pokemon_to_add['pokeData']['formId']
    catalog_entry = retrieve_catalog_entry(catalog, species_index, form_index,
                                           fake_species_index)
    if shiny is True:
        file_exists = flip_starter_texture(pokemon_dict['pokemons'][pokemon_to_add['pokeData']['devId']]['natdex'],
                             fake_species_index)
        if file_exists is True:
            catalog_entry['model'] = create_new_file_for_shiny(catalog_entry, 'model', fake_species_index)
            catalog_entry['material'] = create_new_file_for_shiny(catalog_entry, 'material', fake_species_index)
            catalog_entry['config'] = create_new_file_for_shiny(catalog_entry, 'config', fake_species_index)
            catalog_entry['animations'][0]['anim_path'] = create_new_file_for_shiny(catalog_entry['animations'][0],
                                                                                    'anim_path', fake_species_index)
            catalog_entry['locators'][0]['loc_path'] = create_new_file_for_shiny(catalog_entry['locators'][0],
                                                                                    'loc_path', fake_species_index)
            catalog_entry['iconname'] = create_new_file_for_shiny(catalog_entry, 'iconname', fake_species_index)

    catalog['unk_1'].append(catalog_entry)


def flip_starter_texture(starter_num: int, fake_entry: int):
    pokemon_file = HelperFunctions.fetch_animation_file(starter_num)
    try:
        shutil.copytree(os.getcwd() + "/Randomizer/StartersGifts/" + f'pokemon_clean/{pokemon_file}',
                        os.getcwd() + "/Randomizer/StartersGifts/" + f'output/romfs/pokemon/data/pm{fake_entry}')

        current_check = os.getcwd() + "/Randomizer/StartersGifts/" + f'output/romfs/pokemon/data/pm{fake_entry}'

        for pokemonfolder in os.listdir(current_check):
            pokemontextures_animations = current_check + "/" + pokemonfolder

            for files in os.listdir(pokemontextures_animations):
                if "rare" in files:
                    replacedfile = files.replace("_rare", '')
                    ogfiledir = pokemontextures_animations + "/" + f'{files}'
                    newfiledir =pokemontextures_animations + "/" + f'{replacedfile}'
                    shutil.copy2(ogfiledir, newfiledir)
        return True
    except Exception:
        print("ERROR - NO FILES IN POKEMON_CLEAN - SHINY STARTER WILL USE REGULAR TEXTURE - FIX FOR NEXT TIME.")
    return False


def patch_random_catalog(catalog: dict, fake_species_index: int, shiny=False):
    pokemon_to_add = random.randint(1, 1025)
    while pokemon_to_add in SharedVariables.banned_pokemon:
        pokemon_to_add = random.randint(1, 1025)
    pokemon_dev_name = HelperFunctions.fetch_developer_name(pokemon_to_add)
    species_index = pokemon_dict['pokemons'][pokemon_dev_name]['id']
    form_index = HelperFunctions.get_alternate_form(pokemon_to_add)
    catalog_entry = retrieve_catalog_entry(catalog, species_index, form_index,
                                           fake_species_index)
    catalog['unk_1'].append(catalog_entry)


def save_poke_catalog():
    outdata = json.dumps(poke_catalog, indent=4)
    with open(os.getcwd() + "/Randomizer/Scenes/" + "poke_resource_table.json", 'w') as outfile:
        outfile.write(outdata)


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

    shiny = False
    fake_species_list = [9996, 9997, 9998]
    # Sprigatito - Patch
    if starters['values'][1]['pokeData']['rareType'] == "RARE":
        shiny = True
    patch_poke_catalog(poke_catalog, starters, 9996, 1, shiny)
    shiny = False

    # Fuecoco - Patch
    if starters['values'][0]['pokeData']['rareType'] == "RARE":
        shiny = True
    patch_poke_catalog(poke_catalog, starters, 9997, 0, shiny)
    shiny = False

    # Quaxly - Patch
    if starters['values'][2]['pokeData']['rareType'] == "RARE":
        shiny = True
    patch_poke_catalog(poke_catalog, starters, 9998, 2, shiny)

    # sprigattio_offset = 0x3D8A  # 6c 02
    # fuecoco_offset = 0x158A  # 6d 02
    # quaxly_offset = 0x2992  # 6e 02
    offset = [0x3D8A, 0x158A, 0x2992]

    for i in range(0, 2):
        with open(os.getcwd() + f"/Randomizer/Scenes/starters_scenes/common_0070_always_{str(i)}.trsog", "w+b") as file:
            if i == 0:
                file.write(scarlet_scene_bytes)
            elif i == 1:
                file.write(violet_scene_bytes)
            for j in range(0, len(offset)):
                file.seek(offset[j])
                file.write(bytearray.fromhex(int(fake_species_list[j]).to_bytes(2, byteorder='little').hex()))

    print("Patched starters in overworld")
    save_poke_catalog()


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

    # 0 ->1 - fletching
    # 2 - Pawmi
    # 3->6 - tarountula
    # 7->11 - Lechonk
    fake_species_list = [9992, 9993, 9994, 9995]
    patch_random_catalog(poke_catalog, 9992)
    patch_random_catalog(poke_catalog, 9993)
    patch_random_catalog(poke_catalog, 9994)
    patch_poke_catalog(poke_catalog, lechonk, 9995, 24)
    offset = [0xAB6, 0x1FE2, 0x350E, 0x4A3A, 0x5F62, 0x748A, 0x89B2, 0x9EDA, 0xB402, 0xC92A, 0xDE52, 0xF37A]

    for i in range(0, 2):
        with open(os.getcwd() + f"/Randomizer/Scenes/lechonk_scenes/common_0100_main_{str(i)}.trsog", "w+b") as file:
            if i == 0:
                file.write(scarlet_scene_bytes)
            elif i == 1:
                file.write(violet_scene_bytes)
            for j in range(0, len(offset)):
                file.seek(offset[j])
                if 0 <= j <= 1:
                    file.write(bytearray.fromhex(fake_species_list[0].to_bytes(2, byteorder='little').hex()))
                if j == 2:
                    file.write(bytearray.fromhex(fake_species_list[1].to_bytes(2, byteorder='little').hex()))
                if 3 <= j <= 6:
                    file.write(bytearray.fromhex(fake_species_list[2].to_bytes(2, byteorder='little').hex()))
                if j >= 7:
                    file.write(bytearray.fromhex(fake_species_list[3].to_bytes(2, byteorder='little').hex()))

    print("Patched Lechonk in overworld")
    save_poke_catalog()


def patch_gimmighoul_scene():
    ghoul_file = open(os.getcwd() + "/Randomizer/StaticFights/" + "eventBattlePokemon_array.json", "r")
    gimmighoul = json.load(ghoul_file)
    ghoul_file.close()

    for i in range(0, 2):
        game_scene = open(os.getcwd() + f"/Randomizer/Scenes/gimmighoul_scene/coin_symbol_box_{str(i)}_clean.trsot", "rb")
        game_scene_bytes = game_scene.read()
        game_scene.close()

        # 0 - Gimmighoul-Chest-Form
        offset = [0x656]

        with open(os.getcwd() + f"/Randomizer/Scenes/gimmighoul_scene/coin_symbol_box_{str(i)}.trsot", "w+b") as file:
            file.write(game_scene_bytes)
            for j in range(0, len(offset)):
                file.seek(offset[j])
                hex_values_to_use = pokemon_dict['pokemons'][gimmighoul['values'][9]['pokeData']['devId']]['hex']
                file.write(bytearray.fromhex(hex_values_to_use))

    print("Patched Gimmighoul in overworld")
    save_poke_catalog()
