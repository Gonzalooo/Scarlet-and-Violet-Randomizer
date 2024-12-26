import os
import json
import copy
import random
import shutil
import Randomizer.shared_Variables as SharedVariables
import Randomizer.helper_function as HelperFunctions
import traceback

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
    # print(key_change)
    # print(file_num)
    if catalog is None:
        print("'Random' Error Caught, currently unsure of the cause")
        print("currently no fix other than to close window and try with a new seed sorry")
        breakpoint()
    if key_change is None:
        print("'Random' Error Caught, currently unsure of the cause")
        print("currently no fix other than to close window and try with a new seed sorry")
        breakpoint()
    if key_change not in catalog:
        print("'Random' Error Caught, currently unsure of the cause")
        print("currently no fix other than to close window and try with a new seed sorry")
        breakpoint()
    new_file_name = catalog[key_change].split('/')
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
                    newfiledir = pokemontextures_animations + "/" + f'{replacedfile}'
                    shutil.copy2(ogfiledir, newfiledir)
        return True
    except Exception as e:
        print(f'Missing folder: {pokemon_file} - the fake entry of {fake_entry}')
        print("Optional pokemon_clean folder not setup or incomplete")
        print("Model may not appear changed/shiny until caught")
        #print(traceback.print_exc())
    return False


def patch_random_catalog(catalog: dict, fake_species_index: int):
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

    for i in range(0, 2):
        for j in range(0, 5):
            match j:
                case 0:
                    scarlet_scene = open(
                        os.getcwd() + "/Randomizer/Scenes/starters_scenes/common_0060_main_0_clean.trsog", "rb")
                    violet_scene = open(
                        os.getcwd() + "/Randomizer/Scenes/starters_scenes/common_0060_main_1_clean.trsog", "rb")
                    scarlet_scene_bytes = scarlet_scene.read()
                    violet_scene_bytes = violet_scene.read()
                    scarlet_scene.close()
                    violet_scene.close()

                    # Sprigatitto_offsets = 0x3B4E
                    # Fuecoco_offsets = 0x2696
                    # Quaxly_offsets = 0x11DA
                    offset = [0x3B4E, 0x2696, 0x11DA]
                    with (open(os.getcwd() + f"/Randomizer/Scenes/starters_scenes/common_0060_main_{str(i)}.trsog",
                               "w+b") as file):
                        if i == 0:
                            file.write(scarlet_scene_bytes)
                        elif i == 1:
                            file.write(violet_scene_bytes)
                        for k in range(0, len(offset)):
                            file.seek(offset[k])
                            file.write(bytearray.fromhex(int(fake_species_list[k]).to_bytes(2,
                                                                                            byteorder='little').hex()))
                    continue
                case 1:
                    scarlet_scene = open(
                        os.getcwd() + "/Randomizer/Scenes/starters_scenes/common_0060_always_0_clean.trsog", "rb")
                    violet_scene = open(
                        os.getcwd() + "/Randomizer/Scenes/starters_scenes/common_0060_always_1_clean.trsog", "rb")
                    scarlet_scene_bytes = scarlet_scene.read()
                    violet_scene_bytes = violet_scene.read()
                    scarlet_scene.close()
                    violet_scene.close()

                    # Sprigatitto_offsets = 0x1328, 1BCA
                    # Fuecoco_offsets = 0x1F78, 281A
                    # Quaxly_offsets = 0x06DC, 0F7E
                    offset = [0x1328, 0x1F78, 0x06DC]
                    offset_2 = [0x1BCA, 0x281A, 0x0F7E]
                    with (open(os.getcwd() + f"/Randomizer/Scenes/starters_scenes/common_0060_always_{str(i)}.trsog",
                               "w+b") as file):
                        if i == 0:
                            file.write(scarlet_scene_bytes)
                        elif i == 1:
                            file.write(violet_scene_bytes)
                        for k in range(0, len(offset)):
                            file.seek(offset[k])
                            file.write(bytearray.fromhex(int(fake_species_list[k]).to_bytes(2,
                                                                                            byteorder='little').hex()))
                        for k in range(0, len(offset_2)):
                            file.seek(offset_2[k])
                            file.write(bytearray.fromhex(int(fake_species_list[k]).to_bytes(2,
                                                                                            byteorder='little').hex()))
                    continue
                case 2:
                    scarlet_scene = open(
                        os.getcwd() + "/Randomizer/Scenes/starters_scenes/common_0070_always_0_clean.trsog", "rb")
                    violet_scene = open(
                        os.getcwd() + "/Randomizer/Scenes/starters_scenes/common_0070_always_1_clean.trsog", "rb")
                    scarlet_scene_bytes = scarlet_scene.read()
                    violet_scene_bytes = violet_scene.read()
                    scarlet_scene.close()
                    violet_scene.close()

                    # sprigattio_offset = 0x3D8A  # 6c 02
                    # fuecoco_offset = 0x158A  # 6d 02
                    # quaxly_offset = 0x2992  # 6e 02
                    offset = [0x3D8A, 0x158A, 0x2992]
                    with (open(os.getcwd() + f"/Randomizer/Scenes/starters_scenes/common_0070_always_{str(i)}.trsog",
                               "w+b") as file):
                        if i == 0:
                            file.write(scarlet_scene_bytes)
                        elif i == 1:
                            file.write(violet_scene_bytes)
                        for k in range(0, len(offset)):
                            file.seek(offset[k])
                            file.write(bytearray.fromhex(int(fake_species_list[k]).to_bytes(2,
                                                                                            byteorder='little').hex()))
                case 3:
                    scarlet_scene = open(
                        os.getcwd() + "/Randomizer/Scenes/starters_scenes/common_0088_always_0_clean.trsog", "rb")
                    violet_scene = open(
                        os.getcwd() + "/Randomizer/Scenes/starters_scenes/common_0088_always_1_clean.trsog", "rb")
                    scarlet_scene_bytes = scarlet_scene.read()
                    violet_scene_bytes = violet_scene.read()
                    scarlet_scene.close()
                    violet_scene.close()

                    # sprigattio_offset = 0x3222  # 6c 02
                    # fuecoco_offset = 0x07EA  # 6d 02
                    # quaxly_offset = 0x1D02  # 6e 02
                    offset = [0x3222, 0x07EA, 0x1D02]
                    with (open(os.getcwd() + f"/Randomizer/Scenes/starters_scenes/common_0088_always_{str(i)}.trsog",
                               "w+b") as file):
                        if i == 0:
                            file.write(scarlet_scene_bytes)
                        elif i == 1:
                            file.write(violet_scene_bytes)
                        for k in range(0, len(offset)):
                            file.seek(offset[k])
                            file.write(bytearray.fromhex(int(fake_species_list[k]).to_bytes(2,
                                                                                            byteorder='little').hex()))
                    continue
                case 4:
                    scarlet_scene = open(
                        os.getcwd() + "/Randomizer/Scenes/starters_scenes/common_0090_main_0_clean.trsog", "rb")
                    violet_scene = open(
                        os.getcwd() + "/Randomizer/Scenes/starters_scenes/common_0090_main_1_clean.trsog", "rb")
                    scarlet_scene_bytes = scarlet_scene.read()
                    violet_scene_bytes = violet_scene.read()
                    scarlet_scene.close()
                    violet_scene.close()

                    # sprigattio_offset = 0x344E  # 6c 02
                    # fuecoco_offset = 0x09FA  # 6d 02
                    # quaxly_offset = 0x1F22  # 6e 02
                    offset = [0x344E, 0x09FA, 0x1F22]
                    with (open(os.getcwd() + f"/Randomizer/Scenes/starters_scenes/common_0090_main_{str(i)}.trsog",
                               "w+b") as file):
                        if i == 0:
                            file.write(scarlet_scene_bytes)
                        elif i == 1:
                            file.write(violet_scene_bytes)
                        for k in range(0, len(offset)):
                            file.seek(offset[k])
                            file.write(bytearray.fromhex(int(fake_species_list[k]).to_bytes(2,
                                                                                            byteorder='little').hex()))
                    continue
                case _:
                    print("YOU SHOULD NEVER REACH HERE")
    print("Patched starters in overworld")
    save_poke_catalog()


# Needs Shiny Support
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

    shiny = False
    if gimmighoul['values'][11]['pokeData']['rareType'] == "RARE":
        shiny = True
    patch_poke_catalog(poke_catalog, gimmighoul, 9991, 11, shiny)

    for i in range(0, 2):
        game_scene = open(os.getcwd() + f"/Randomizer/Scenes/gimmighoul_scene/coin_symbol_box_{str(i)}_clean.trsot", "rb")
        game_scene_bytes = game_scene.read()
        game_scene.close()

        # 0 - Gimmighoul-Chest-Form
        fake_pokemon_number = [9991]
        offset = [0x656]

        with open(os.getcwd() + f"/Randomizer/Scenes/gimmighoul_scene/coin_symbol_box_{str(i)}.trsot", "w+b") as file:
            file.write(game_scene_bytes)
            for j in range(0, len(offset)):
                file.seek(offset[j])
                file.write(bytearray.fromhex(int(fake_pokemon_number[j]).to_bytes(2,
                                                                                            byteorder='little').hex()))

    print("Patched Gimmighoul in overworld")
    save_poke_catalog()


# Missing Arven still
def patch_titans_and_arven_titans():
    Titans_Scenes_List = ["Klawf", "Bombirdier", "Orthworm", "GreatIron", "Dondozo", "Tatsugiri"]

    titans_file = open(os.getcwd() + "/Randomizer/StaticFights/" + "eventBattlePokemon_array.json", "r")
    titan = json.load(titans_file)
    titans_file.close()

    fake_pokemon_list = [9990, 9989, 9988, 9987, 9970, 9986, 9969]
    indices =           [43,   41,   35,   45,   47,   33,   37]
    for i in range(0, len(indices)):
        shiny = False
        if titan['values'][indices[i]]['pokeData']['rareType'] == "RARE":
            shiny = True
        patch_poke_catalog(poke_catalog, titan, fake_pokemon_list[i], indices[i], shiny)

    # 18 00 00 00 74 69 5F 46 69 65 6C 64 50 6F 6B 65 6D 6F 6E 43 6F 6D 70 6F 6E 65 6E 74
    for Titans in Titans_Scenes_List:
        for i in range(0, 2):
            titans_files = []
            titans_save_files = []
            offsets = []
            indexes = []
            if Titans == "Klawf":
                titans_files = [
                    f"nushi_iwa_010_pre_start_{i}_clean.trsog",
                    f"nushi_iwa_020_pre_start_{i}_clean.trsog",
                    f"nushi_iwa_fp_1066_{i}_clean.trsot",
                    f"nushi_iwa_fp_1066_020_{i}_clean.trsot",
                    f"sub_037_pre_start_{i}_clean.trsog",
                ]
                titans_save_files = [
                    f"nushi_iwa_010_pre_start_{i}.trsog",
                    f"nushi_iwa_020_pre_start_{i}.trsog",
                    f"nushi_iwa_fp_1066_{i}.trsot",
                    f"nushi_iwa_fp_1066_020_{i}.trsot",
                    f"sub_037_pre_start_{i}.trsog",
                ]
                offsets = [
                    [0x0B1C, 0X0B6E],
                    [0x1700, 0x1762],
                    [0x0B18, 0X0B7A],
                    [0X0FA8, 0X100A],
                    [0X008C, 0X0DBE]
                ]
                indexes = [
                    9990
                ]
            elif Titans == "Bombirdier":
                titans_files = [
                    f"HikoNushi_{i}_clean.trscn",
                    f"nushi_hiko_fp_1063_010_{i}_clean.trsot",
                    f"nushi_hiko_fp_1063_020_{i}_clean.trsot",
                    f"nushi_hikou_010_pre_start_{i}_clean.trsog",
                    f"nushi_hikou_020_pre_start_{i}_clean.trsog",
                    f"nushi_hikou_020_main_{i}_clean.trsog",
                    f"sub_038_pre_start_{i}_clean.trsog",
                ]
                titans_save_files = [
                    f"HikoNushi_{i}.trscn",
                    f"nushi_hiko_fp_1063_010_{i}.trsot",
                    f"nushi_hiko_fp_1063_020_{i}.trsot",
                    f"nushi_hikou_010_pre_start_{i}.trsog",
                    f"nushi_hikou_020_pre_start_{i}.trsog",
                    f"nushi_hikou_020_main_{i}.trsog",
                    f"sub_038_pre_start_{i}.trsog",
                ]
                offsets = [
                    [0x03BC, 0X040E, 0X0C18, 0X1F7A],
                    [0x011C, 0x017E],
                    [0x0484, 0X04E6],
                    [0X05DC, 0X063E],
                    [0X01B6],
                    [0x0C4C, 0x0C9E],
                    [0x008C, 0X0DBE]

                ]
                indexes = [
                    9989
                ]
            elif Titans == "Orthworm":
                titans_files = [
                    f"nushi_hagane_010_pre_start_{i}_clean.trsog",
                    f"nushi_hagane_020_pre_start_{i}_clean.trsog",
                    f"nushi_hagane_fp_1048_010_{i}_clean.trsot",
                    f"nushi_hagane_fp_1048_020_{i}_clean.trsot",
                    f"sub_039_pre_start_{i}_clean.trsog",
                ]
                titans_save_files = [
                    f"nushi_hagane_010_pre_start_{i}.trsog",
                    f"nushi_hagane_020_pre_start_{i}.trsog",
                    f"nushi_hagane_fp_1048_010_{i}.trsot",
                    f"nushi_hagane_fp_1048_020_{i}.trsot",
                    f"sub_039_pre_start_{i}.trsog",
                ]
                offsets = [
                    [0x0384, 0x03E6],
                    [0x0D0C, 0x0D6E],
                    [0x037C, 0X03E6],
                    [0X0634, 0X0696],
                    [0x008C, 0X0DBE]
                ]
                indexes = [
                    9988
                ]
            elif Titans == "GreatIron":
                titans_files = [
                    f"nushi_jimen_010_pre_start_{i}_clean.trsog",
                    f"nushi_jimen_020_pre_start_{i}_clean.trsog",
                    f"nushi_jimen_fp_1082_010_{i}_clean.trsot",
                    f"nushi_jimen_fp_1082_020_{i}_clean.trsot",
                    f"nushi_jimen_fp_1090_010_{i}_clean.trsot",
                    f"nushi_jimen_fp_1090_020_{i}_clean.trsot",
                    f"sub_041_pre_start_{i}_clean.trsog",
                ]
                titans_save_files = [
                    f"nushi_jimen_010_pre_start_{i}.trsog",
                    f"nushi_jimen_020_pre_start_{i}.trsog",
                    f"nushi_jimen_fp_1082_010_{i}.trsot",
                    f"nushi_jimen_fp_1082_020_{i}.trsot",
                    f"nushi_jimen_fp_1090_010_{i}.trsot",
                    f"nushi_jimen_fp_1090_020_{i}.trsot",
                    f"sub_041_pre_start_{i}.trsog",
                ]
                offsets = [
                    [0x0B80, 0x0E32, 0X180C, 0X185E],
                    [0X10B0, 0X1102, 0X1800, 0X1852],
                    [0x0840, 0x0B02],
                    [0X047C, 0X04DE],
                    [0X0774, 0X07D6],
                    [0X0494, 0X04F6],
                    [0X008C, 0X0DBE]
                ]
                match i:
                    case 0:
                        indexes = [
                            9987
                        ]
                    case 1:
                        indexes = [
                            9970
                        ]
                    case _:
                        print("How here")
                        exit(-1)
            elif Titans == "Dondozo":
                titans_files = [
                    f"nushi_dragon_010_always_{i}_clean.trsog",
                    f"nushi_dragon_fp_1035_010_{i}_clean.trsot",
                    f"nushi_dragon_fp_1035_020_{i}_clean.trsot",
                ]
                titans_save_files = [
                    f"nushi_dragon_010_always_{i}.trsog",
                    f"nushi_dragon_fp_1035_010_{i}.trsot",
                    f"nushi_dragon_fp_1035_020_{i}.trsot",
                ]
                offsets = [
                    [0x03F8, 0X0448],
                    [0x03F4, 0X044E],
                    [0X0764, 0X07BC]
                ]
                indexes = [
                    9986
                ]
            elif Titans == "Tatsugiri":
                titans_files = [
                    f"nushi_dragon_010_always_{i}_clean.trsog",
                    f"nushi_dragon_fp_1056_010_{i}_clean.trsot",
                    f"nushi_dragon_fp_1056_020_{i}_clean.trsot",
                    f"sub_040_pre_start_{i}_clean.trsog",
                ]
                titans_save_files = [
                    f"nushi_dragon_010_always_{i}.trsog",
                    f"nushi_dragon_fp_1056_010_{i}.trsot",
                    f"nushi_dragon_fp_1056_020_{i}.trsot",
                    f"sub_040_pre_start_{i}.trsog",
                ]
                offsets = [
                    [0x03F8, 0X0448],
                    [0x11C2, 0X121C],
                    [0X0550, 0X05BA],
                    [0X08D0, 0X0DBE]
                ]
                indexes = [
                    9969
                ]
            elif Titans == "Arven":
                # Get Pokemon from Arven's fight
                titans_files = [
                    f"HaganeRockClashEvent_{i}_clean.trscn",
                    f"HikoRockClashEvent_{i}_clean.trscn",
                    f"JimenRockClashEvent_{i}_clean.trscn",
                    f"DragonRockClashEvent_{i}_clean.trscn",
                    f"RockClashEvent_{i}_clean.trscn",
                    f"nushi_dragon_020_pre_start_{i}_clean.trsog"
                ]
                titans_save_files = [
                    f"HaganeRockClashEvent_{i}.trscn",
                    f"HikoRockClashEvent_{i}.trscn",
                    f"JimenRockClashEvent_{i}.trscn",
                    f"DragonRockClashEvent_{i}.trscn",
                    f"RockClashEvent_{i}.trscn",
                    f"nushi_dragon_020_pre_start_{i}.trsog"
                ]
                offsets = [
                    [],
                    [],
                    [],
                    [],
                    [],
                    []
                ]
                indexes = []

            for files in range(0, len(titans_files)):
                game_scene = open(
                    os.getcwd() + f"/Randomizer/Scenes/Titans/{Titans}/{titans_files[files]}", "rb")
                game_scene_bytes = game_scene.read()
                game_scene.close()

                with open(os.getcwd() + f"/Randomizer/Scenes/Titans/{Titans}/{titans_save_files[files]}",
                          "w+b") as file:
                    file.write(game_scene_bytes)
                    for j in range(0, len(offsets[files])):
                        file.seek(offsets[files][j])
                        file.write(bytearray.fromhex(int(indexes[0]).to_bytes(2, byteorder='little').hex()))
        print(f'Patched Titans {Titans}')
    print("Patched Titans Scenes")
    save_poke_catalog()


def patch_treasure_of_ruins():
    treasure_file = open(os.getcwd() + "/Randomizer/StaticFights/" + "eventBattlePokemon_array.json", "r")
    treasure = json.load(treasure_file)
    treasure_file.close()
    # Chien-Pao - 0x00F8, 0x087E
    # Chi-Yu - 0x00F8, 0X087E
    # Ting-Lu - 0x0822
    # Wo-Chien - 0x0822
    fake_pokemon_list = [9985, 9984, 9983, 9982]
    ruin_numbers = [49, 50, 51, 52]
    for number in range(0, 4):
        shiny = False
        if treasure['values'][ruin_numbers[number]]['pokeData']['rareType'] == "RARE":
            shiny = True
        patch_poke_catalog(poke_catalog, treasure, fake_pokemon_list[number], ruin_numbers[number], shiny)

    for i in range(14, 18):
        for j in range(0, 2):
            game_scene = open(os.getcwd() + f"/Randomizer/Scenes/Treasures-Ruin/sub_0{str(i)}_main_{str(j)}_clean.trsog", "rb")
            game_scene_bytes = game_scene.read()
            game_scene.close()
            offset = []
            fight_num = 0

            match i:
                case 14:
                    offset = [0x0822]
                    fight_num = 9985
                case 15:
                    offset = [0x00F8, 0X087E]
                    fight_num = 9984
                case 16:
                    offset = [0x0822]
                    fight_num = 9983
                case 17:
                    offset = [0x00F8, 0X087E]
                    fight_num = 9982
                case _:
                    break

            with open(os.getcwd() + f"/Randomizer/Scenes/Treasures-Ruin/sub_0{str(i)}_main_{str(j)}.trsog", "w+b") as file:
                file.write(game_scene_bytes)
                for k in range(0, len(offset)):
                    file.seek(offset[k])
                    file.write(bytearray.fromhex(int(fight_num).to_bytes(2, byteorder='little').hex()))
    print("Patched All Treasures of Ruin")
    save_poke_catalog()


def patch_area_zero_first():
    files = [1055, 1075, 1095, 1170]

    para_file = open(os.getcwd() + "/Randomizer/StaticFights/" + "eventBattlePokemon_array.json", "r")
    paradoxes = json.load(para_file)
    para_file.close()

    fake_pokemon_list = [9981, 9980, 9979, 9978, 9977, 9976, 9975, 9974, 9973, 9972, 9971]
    ruin_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for number in range(0, len(fake_pokemon_list)):
        shiny = False
        if paradoxes['values'][ruin_numbers[number]]['pokeData']['rareType'] == "RARE":
            shiny = True
        patch_poke_catalog(poke_catalog, paradoxes, fake_pokemon_list[number], ruin_numbers[number], shiny)

    for scene in files:
        for i in range(0, 2):
            file = ""
            if scene != 1170:
                game_scene = open(os.getcwd() + f"/Randomizer/Scenes/Area_Zero_Way_Home/common_{scene}_main_{i}_clean.trsog", "rb")
                game_scene_bytes = game_scene.read()
                game_scene.close()
            else:
                game_scene = open(os.getcwd() + f"/Randomizer/Scenes/Area_Zero_Way_Home/common_{scene}_always_{i}_clean.trsog", "rb")
                game_scene_bytes = game_scene.read()
                game_scene.close()

            offsets = []
            indexs = []
            match scene:
                case 1055:
                    # Glimmora
                    offsets = [0x025C, 0x09E2]
                    indexs = [9981, 9981]
                case 1075:
                    # Iron Bundle, Scream Tails
                    offsets = [0x0832, 0x1DAA]
                    match i:
                        case 0:
                            indexs = [9980, 9980]
                        case 1:
                            indexs = [9979, 9979]
                        case _:
                            print("How here")
                            exit(-1)
                    pass
                case 1095:
                    # Iron Treads, Great Tusk
                    offsets = [0x083A, 0x1DBE]
                    match i:
                        case 0:
                            indexs = [9978, 9978]
                        case 1:
                            indexs = [9977, 9977]
                        case _:
                            print("How here")
                            exit(-1)
                    pass
                case 1170:
                    # Brute Bonnet, Brute Bonnet, Great Tusks, Brute Bonnet, Brute Bonnet, Flutter Mane,
                    # Brute Bonnet, Great Tusks
                    # Iron Hands, Iron Hands, Iron Treads, Iron Hands, Iron Hands, Iron Jugulis, Iron Hands, Iron Treads
                    offsets = [0x07DA, 0x1C7A, 0x3116, 0x45B6, 0x5A52, 0X6F5A, 0X8406, 0x98B2]
                    match i:
                        case 0:
                            indexs = [9975, 9975, 9976, 9975, 9975, 9974, 9975, 9976]
                        case 1:
                            indexs = [9972, 9972, 9973, 9972, 9972, 9971, 9972, 9973]
                        case _:
                            print("How here")
                            exit(-1)
                    pass
                case _:
                    print("How we get here")
                    exit(-1)

            if scene != 1170:
                with open(os.getcwd() + f"/Randomizer/Scenes/Area_Zero_Way_Home/common_{scene}_main_{i}.trsog",
                          "w+b") as file:
                    file.write(game_scene_bytes)
                    for j in range(0, len(offsets)):
                        file.seek(offsets[j])
                        file.write(bytearray.fromhex(int(indexs[j]).to_bytes(2, byteorder='little').hex()))
            else:
                with open(os.getcwd() + f"/Randomizer/Scenes/Area_Zero_Way_Home/common_{scene}_always_{i}.trsog",
                          "w+b") as file:
                    file.write(game_scene_bytes)
                    for j in range(0, len(offsets)):
                        file.seek(offsets[j])
                        file.write(bytearray.fromhex(int(indexs[j]).to_bytes(2, byteorder='little').hex()))
    print("Patched Area Zero Way Home overworld pokemon")
    save_poke_catalog()


def patch_kitakami_nonlegends():
    kitakami_fights = open(os.getcwd() + "/Randomizer/StaticFights/" + "eventBattlePokemon_array.json", "r")
    kitakami = json.load(kitakami_fights)
    kitakami_fights.close()

    fake_pokemon_number = [9968, 9967, 9966]
    indexes = [66, 74, 75]

    for number in range(0, len(fake_pokemon_number)):
        shiny = False
        if kitakami['values'][indexes[number]]['pokeData']['rareType'] == "RARE":
            shiny = True
        patch_poke_catalog(poke_catalog, kitakami, fake_pokemon_number[number], indexes[number], shiny)

    pokemons = ["Milotic", "Ariados", "Ursaluna"]

    for fights in pokemons:
        for i in range(0, 2):
            kitakami_scenes = []
            kitakami_saves = []
            offsets = []
            index = []
            if fights == "Milotic":
                kitakami_scenes = [
                    f"sdc01_0300_main_{i}_clean.trsog",
                ]
                kitakami_saves = [
                    f"sdc01_0300_main_{i}.trsog",
                ]
                offsets = [0X07C6]
                index = [9968]
            elif fights == "Ariados":
                kitakami_scenes = [
                    f"s1_side02_0030_main_{i}_clean.trsog",
                ]
                kitakami_saves = [
                    f"s1_side02_0030_main_{i}.trsog",
                ]
                offsets = [0X07C2]
                index = [9967]
            elif fights == "Ursaluna":
                kitakami_scenes = [
                    f"s1_side02_0050_main_{i}_clean.trsog",
                ]
                kitakami_saves = [
                    f"s1_side02_0050_main_{i}.trsog",
                ]
                offsets = [0x07D8]
                index = [9966]

            game_scene = open(os.getcwd() + f"/Randomizer/Scenes/Kitakami/{fights}/{kitakami_scenes[0]}", "rb")
            game_scene_bytes = game_scene.read()
            game_scene.close()

            with open(os.getcwd() + f"/Randomizer/Scenes/Kitakami/{fights}/{kitakami_saves[0]}", "w+b") as file:
                file.write(game_scene_bytes)
                for j in range(0, len(offsets)):
                    file.seek(offsets[j])
                    lenght = 2
                    if fights == "Ursaluna":
                        lenght = 3
                    file.write(bytearray.fromhex(int(index[0]).to_bytes(lenght, byteorder='little').hex()))

    print("Patched Milotic, Ariados and Ursaluna in overworld")
    save_poke_catalog()


def patch_area_zero_treasure():
    treasure_fights = open(os.getcwd() + "/Randomizer/StaticFights/" + "eventBattlePokemon_array.json", "r")
    treasure = json.load(treasure_fights)
    treasure_fights.close()

    fake_pokemon_number = [9965, 9964, 9963, 9962, 9961, 9960, 9959, 9958, 9957, 9956]
    indexes =             [76,   77,   78,   79,   80,   81,   82,   83,   84,   85]

    for number in range(0, len(fake_pokemon_number)):
        shiny = False
        if treasure['values'][indexes[number]]['pokeData']['rareType'] == "RARE":
            shiny = True
        patch_poke_catalog(poke_catalog, treasure, fake_pokemon_number[number], indexes[number], shiny)

    pokemons = ["Garchomp", "Garganacl", "Glimmora", "Gouging Fire", "Noivern", "Raging Bolt", "Sandy Shocks"]

    for fights in pokemons:
        for i in range(0, 2):
            treasure_scenes = []
            treasure_saves = []
            offsets = []
            index = []
            if fights == "Garchomp":
                treasure_scenes = [
                    f"s2_sub_005_pre_start_{i}_clean.trsog",
                ]
                treasure_saves = [
                    f"s2_sub_005_pre_start_{i}.trsog",
                ]
                offsets = [0x08C4, 0x1076]
                index = [9963]
            elif fights == "Garganacl":
                treasure_scenes = [
                    f"sdc02_0267_pre_start_{i}_clean.trsog",
                ]
                treasure_saves = [
                    f"sdc02_0267_pre_start_{i}.trsog",
                ]
                offsets = [0x609C, 0X684E]
                index = [9960]
            elif fights == "Glimmora":
                treasure_scenes = [
                    f"sdc02_0262_main_{i}_clean.trsog",
                ]
                treasure_saves = [
                    f"sdc02_0262_main_{i}.trsog",
                ]
                offsets = [0x5DEC, 0x6596]
                index = [9962]
            elif fights == "Gouging Fire":
                treasure_scenes = [
                    f"s2_side02_0010_pre_start_{i}_clean.trsog",
                ]
                treasure_saves = [
                    f"s2_side02_0010_pre_start_{i}.trsog",
                ]
                offsets = [0x0882]
                match i:
                    case 0:
                        index = [9965]
                    case 1:
                        index = [9957]
                    case _:
                        print('How here')
                        exit(0)
            elif fights == "Noivern":
                treasure_scenes = [
                    f"sdc02_0263_pre_start_{i}_clean.trsog",
                ]
                treasure_saves = [
                    f"sdc02_0263_pre_start_{i}.trsog",
                ]
                offsets = [0x0BB0, 0x1362]
                index = [9961]
            elif fights == "Raging Bolt":
                treasure_scenes = [
                    f"s2_side02_0020_pre_start_{i}_clean.trsog",
                ]
                treasure_saves = [
                    f"s2_side02_0020_pre_start_{i}.trsog",
                ]
                offsets = [0x0882]
                match i:
                    case 0:
                        index = [9964]
                    case 1:
                        index = [9956]
                    case _:
                        print('How here')
                        exit(0)
            elif fights == "Sandy Shocks":
                treasure_scenes = [
                    f"sdc02_0265_pre_start_{i}_clean.trsog",
                ]
                treasure_saves = [
                    f"sdc02_0265_pre_start_{i}.trsog",
                ]
                offsets = [0x609C, 0X684E]
                match i:
                    case 0:
                        index = [9959]
                    case 1:
                        index = [9958]
                    case _:
                        print('How here')
                        exit(0)

            game_scene = open(os.getcwd() + f"/Randomizer/Scenes/Area_Zero_Hidden_Treasure/{fights}/{treasure_scenes[0]}", "rb")
            game_scene_bytes = game_scene.read()
            game_scene.close()

            with open(os.getcwd() + f"/Randomizer/Scenes/Area_Zero_Hidden_Treasure/{fights}/{treasure_saves[0]}", "w+b") as file:
                file.write(game_scene_bytes)
                for j in range(0, len(offsets)):
                    file.seek(offsets[j])
                    file.write(bytearray.fromhex(int(index[0]).to_bytes(2, byteorder='little').hex()))

    print("Patched Area Zero from DLC2")
    save_poke_catalog()


def patch_all_legendaries():
    legends_fights = open(os.getcwd() + "/Randomizer/StaticFights/" + "eventBattlePokemon_array.json", "r")
    legendaries = json.load(legends_fights)
    legends_fights.close()

    fake_pokemon_number = [9955, 9954, 9953, 9952, 9951, 9950, 9949, 9948, 9947, 9946, 9945, 9944, 9943,
                           9942, 9941, 9940, 9939, 9938, 9937, 9936, 9935, 9934, 9933, 9932,
                           9931, 9930, 9929]
    indexes =             [92,   89,   91,   93,   94,   95,   90,   96,   97,   98,   99,  100,  101,
                           114,  102,  103,  86,   104,  105,  106,  107,  108,  109,  110,
                           111,  112,  113]

    for number in range(0, len(indexes)):
        shiny = False
        if legendaries['values'][indexes[number]]['pokeData']['rareType'] == "RARE":
            shiny = True
        patch_poke_catalog(poke_catalog, legendaries, fake_pokemon_number[number], indexes[number], shiny)

    pokemons = ["Articuno", "Cobalion", "Entei", "Glastier", "Groundon", "Ho-oH", "Kubfu", "Kyogre", "Kyurem",
                "Latias", "Latios", "Lugia", "Lunala", "Meloetta", "Moltres", "Necrozma", "Pecharunt", "Raikou",
                "Rayquaza", "Reshiram", "Solgaleo", "Spectier", "Suicune", "Terrakion", "Virizion", "Zapdos",
                "Zekrom"]

    for fights in pokemons:
        for i in range(0, 2):
            legends_scenes = []
            legends_saves = []
            offsets = []
            index = []

            if fights == "Articuno": # 92
                legends_scenes = [
                    f"s2_sub_013_pre_start_{i}_clean.trsog",
                ]
                legends_saves = [
                    f"s2_sub_013_pre_start_{i}.trsog",
                ]
                offsets = [0x0A0A]
                index = [9955]
            elif fights == "Cobalion": # 89
                legends_scenes = [
                    f"s2_sub_026_pre_start_{i}_clean.trsog",
                ]
                legends_saves = [
                    f"s2_sub_026_pre_start_{i}.trsog",
                ]
                offsets = [0x0A0A]
                index = [9954]
            elif fights == "Entei": #91
                legends_scenes = [
                    f"s2_sub_017_pre_start_{i}_clean.trsog",
                ]
                legends_saves = [
                    f"s2_sub_017_pre_start_{i}.trsog",
                ]
                offsets = [0x0A0A]
                index = [9953]
            elif fights == "Glastier": # 93
                legends_scenes = [
                    f"s2_sub_036_pre_start_{i}_clean.trsog",
                ]
                legends_saves = [
                    f"s2_sub_036_pre_start_{i}.trsog",
                ]
                offsets = [0x0A0A]
                index = [9952]
            elif fights == "Groundon": # 94
                legends_scenes = [
                    f"s2_sub_024_pre_start_{i}_clean.trsog",
                ]
                legends_saves = [
                    f"s2_sub_024_pre_start_{i}.trsog",
                ]
                offsets = [0x0A0A]
                index = [9951]
            elif fights == "Ho-oH": # 95
                legends_scenes = [
                    f"s2_sub_020_pre_start_{i}_clean.trsog",
                ]
                legends_saves = [
                    f"s2_sub_020_pre_start_{i}.trsog",
                ]
                offsets = [0x0A0A]
                index = [9950]
            elif fights == "Kubfu": # 90
                legends_scenes = [
                    f"s2_sub_035_pre_start_{i}_clean.trsog",
                ]
                legends_saves = [
                    f"s2_sub_035_pre_start_{i}.trsog",
                ]
                offsets = [0x0A0A]
                index = [9949]
            elif fights == "Kyogre": # 96
                legends_scenes = [
                    f"s2_sub_023_pre_start_{i}_clean.trsog",
                ]
                legends_saves = [
                    f"s2_sub_023_pre_start_{i}.trsog",
                ]
                offsets = [0x0A0A]
                index = [9948]
            elif fights == "Kyurem": # 97
                legends_scenes = [
                    f"s2_sub_031_pre_start_{i}_clean.trsog",
                ]
                legends_saves = [
                    f"s2_sub_031_pre_start_{i}.trsog",
                ]
                offsets = [0x0A0A]
                index = [9947]
            elif fights == "Latias": # 98
                legends_scenes = [
                    f"s2_sub_021_pre_start_{i}_clean.trsog",
                ]
                legends_saves = [
                    f"s2_sub_021_pre_start_{i}.trsog",
                ]
                offsets = [0x0A0A]
                index = [9946]
            elif fights == "Latios": # 99
                legends_scenes = [
                    f"s2_sub_022_pre_start_{i}_clean.trsog",
                ]
                legends_saves = [
                    f"s2_sub_022_pre_start_{i}.trsog",
                ]
                offsets = [0x0A0A]
                index = [9945]
            elif fights == "Lugia": # 100
                legends_scenes = [
                    f"s2_sub_019_pre_start_{i}_clean.trsog",
                ]
                legends_saves = [
                    f"s2_sub_019_pre_start_{i}.trsog",
                ]
                offsets = [0x0A0A]
                index = [9944]
            elif fights == "Lunala": # 101
                legends_scenes = [
                    f"s2_sub_033_pre_start_{i}_clean.trsog",
                ]
                legends_saves = [
                    f"s2_sub_033_pre_start_{i}.trsog",
                ]
                offsets = [0x0A0A]
                index = [9943]
            elif fights == "Meloetta": # 114
                legends_scenes = [
                    f"s2_sub_003_pop_{i}_clean.trscn"
                ]
                legends_saves = [
                    f"s2_sub_003_pop_{i}.trscn"
                ]
                offsets = [0x0DF6]
                index = [9942]
            elif fights == "Moltres": # 102
                legends_scenes = [
                    f"s2_sub_015_pre_start_{i}_clean.trsog",
                ]
                legends_saves = [
                    f"s2_sub_015_pre_start_{i}.trsog",
                ]
                offsets = [0x0A0A]
                index = [9941]
            elif fights == "Necrozma": # 103
                legends_scenes = [
                    f"s2_sub_034_pre_start_{i}_clean.trsog",
                ]
                legends_saves = [
                    f"s2_sub_034_pre_start_{i}.trsog",
                ]
                offsets = [0x0A0A]
                index = [9940]
            elif fights == "Pecharunt": # 86
                legends_scenes = [
                    f"s2_side01_0160_always_{i}_clean.trsog",
                    f"s2_side01_0180_always_{i}_clean.trsog"
                ]
                legends_saves = [
                    f"s2_side01_0160_always_{i}.trsog",
                    f"s2_side01_0180_always_{i}.trsog"
                ]
                offsets = [
                    [0X5D6E],
                    [0X0001B836]
                ]
                index = [9939]
            elif fights == "Raikou": # 104
                legends_scenes = [
                    f"s2_sub_016_pre_start_{i}_clean.trsog",
                ]
                legends_saves = [
                    f"s2_sub_016_pre_start_{i}.trsog",
                ]
                offsets = [0x0A0A]
                index = [9938]
            elif fights == "Rayquaza": # 105
                legends_scenes = [
                    f"s2_sub_025_pre_start_{i}_clean.trsog",
                ]
                legends_saves = [
                    f"s2_sub_025_pre_start_{i}.trsog",
                ]
                offsets = [0x0A0A]
                index = [9937]
            elif fights == "Reshiram": # 106
                legends_scenes = [
                    f"s2_sub_029_pre_start_{i}_clean.trsog",
                ]
                legends_saves = [
                    f"s2_sub_029_pre_start_{i}.trsog",
                ]
                offsets = [0x0A0A]
                index = [9936]
            elif fights == "Solgaleo": # 107
                legends_scenes = [
                    f"s2_sub_032_pre_start_{i}_clean.trsog",
                ]
                legends_saves = [
                    f"s2_sub_032_pre_start_{i}.trsog",
                ]
                offsets = [0x0A0A]
                index = [9935]
            elif fights == "Spectier": # 108
                legends_scenes = [
                    f"s2_sub_037_pre_start_{i}_clean.trsog",
                ]
                legends_saves = [
                    f"s2_sub_037_pre_start_{i}.trsog",
                ]
                offsets = [0x0A0A]
                index = [9934]
            elif fights == "Suicune": # 109
                legends_scenes = [
                    f"s2_sub_018_pre_start_{i}_clean.trsog",
                ]
                legends_saves = [
                    f"s2_sub_018_pre_start_{i}.trsog",
                ]
                offsets = [0x0A0A]
                index = [9933]
            elif fights == "Terrakion": #110
                legends_scenes = [
                    f"s2_sub_027_pre_start_{i}_clean.trsog",
                ]
                legends_saves = [
                    f"s2_sub_027_pre_start_{i}.trsog",
                ]
                offsets = [0x0A0A]
                index = [9932]
            elif fights == "Virizion": # 111
                legends_scenes = [
                    f"s2_sub_028_pre_start_{i}_clean.trsog",
                ]
                legends_saves = [
                    f"s2_sub_028_pre_start_{i}.trsog",
                ]
                offsets = [0x0A0A]
                index = [9931]
            elif fights == "Zapdos": # 112
                legends_scenes = [
                    f"s2_sub_014_pre_start_{i}_clean.trsog",
                ]
                legends_saves = [
                    f"s2_sub_014_pre_start_{i}.trsog",
                ]
                offsets = [0x0A0A]
                index = [9930]
            elif fights == "Zekrom": # 113
                legends_scenes = [
                    f"s2_sub_030_pre_start_{i}_clean.trsog",
                ]
                legends_saves = [
                    f"s2_sub_030_pre_start_{i}.trsog",
                ]
                offsets = [0x0A0A]
                index = [9929]

            if fights != "Pecharunt":
                game_scene = open(os.getcwd() + f"/Randomizer/Scenes/Legendaries/{fights}/{legends_scenes[0]}", "rb")
                game_scene_bytes = game_scene.read()
                game_scene.close()

                with open(os.getcwd() + f"/Randomizer/Scenes/Legendaries/{fights}/{legends_saves[0]}", "w+b") as file:
                    file.write(game_scene_bytes)
                    for j in range(0, len(offsets)):
                        file.seek(offsets[j])
                        file.write(bytearray.fromhex(int(index[0]).to_bytes(2, byteorder='little').hex()))
            else:
                for files in range(0, len(legends_scenes)):
                    game_scene = open(
                        os.getcwd() + f"/Randomizer/Scenes/Legendaries/{fights}/{legends_scenes[files]}", "rb")
                    game_scene_bytes = game_scene.read()
                    game_scene.close()

                    with open(os.getcwd() + f"/Randomizer/Scenes/Legendaries/{fights}/{legends_saves[files]}",
                              "w+b") as file:
                        file.write(game_scene_bytes)
                        for j in range(0, len(offsets[files])):
                            file.seek(offsets[files][j])
                            file.write(bytearray.fromhex(int(index[0]).to_bytes(2, byteorder='little').hex()))

    print("All Legendaries")
    save_poke_catalog()


def patch_kitakami_legends():
    kitakami_legends = ["Fenzadipiti", "Monkidori", "Okidogi", "Shared_Kita"]

    kita_legends = open(os.getcwd() + "/Randomizer/StaticFights/" + "eventBattlePokemon_array.json", "r")
    kita_legendaries = json.load(kita_legends)
    kita_legends.close()

    fake_pokemon_list = [9928, 9927, 9926]
    indices = [53, 55, 56]
    for i in range(0, len(indices)):
        shiny = False
        if kita_legendaries['values'][indices[i]]['pokeData']['rareType'] == "RARE":
            shiny = True
        patch_poke_catalog(poke_catalog, kita_legendaries, fake_pokemon_list[i], indices[i], shiny)

    # 18 00 00 00 74 69 5F 46 69 65 6C 64 50 6F 6B 65 6D 6F 6E 43 6F 6D 70 6F 6E 65 6E 74
    for Legends in kitakami_legends:
        for i in range(0, 2):
            legends_files = []
            legends_save_files = []
            offsets = []
            indexes = []
            if Legends == "Fenzadipiti":
                legends_files = [
                    f"sdc01_3gods_c_pre_start_{i}_clean.trsog",
                    f"sdc01_3gods_c_before_pre_start_{i}_clean.trsog",
                    f"s1_sub_016_pre_start_{i}_clean.trsog"
                ]
                legends_save_files = [
                    f"sdc01_3gods_c_pre_start_{i}.trsog",
                    f"sdc01_3gods_c_before_pre_start_{i}.trsog",
                    f"s1_sub_016_pre_start_{i}.trsog"
                ]
                offsets = [
                    [0x0150, 0x08E6],
                    [0X0618, 0X0DCA],
                    [0X014C, 0X08E2]
                ]
                indexes = [
                    9926
                ]
            elif Legends == "Monkidori":
                legends_files = [
                    f"sdc01_3gods_b_pre_start_{i}_clean.trsog",
                    f"s1_sub_012_pre_start_{i}_clean.trsog"
                ]
                legends_save_files = [
                    f"sdc01_3gods_b_pre_start_{i}.trsog",
                    f"s1_sub_012_pre_start_{i}.trsog"
                ]
                offsets = [
                    [0X06EC, 0X0E82],
                    [0X014C, 0X08E2]
                ]
                indexes = [
                    9927
                ]
            elif Legends == "Okidogi":
                legends_files = [
                    f"sdc01_3gods_a_pre_start_{i}_clean.trsog",
                    f"s1_sub_011_pre_start_{i}_clean.trsog"
                ]
                legends_save_files = [
                    f"sdc01_3gods_a_pre_start_{i}.trsog",
                    f"s1_sub_011_pre_start_{i}.trsog"
                ]
                offsets = [
                    [0X06EC, 0X0E82],
                    [0X014C, 0X08E2]
                ]
                indexes = [
                    9928
                ]
            elif Legends == "Shared_Kita":
                legends_files = [
                    f"sdc01_0330_always_{i}_clean.trsog",
                    f"sdc01_0360_pre_start_{i}_clean.trsog",
                    f"sdc01_0400_main_{i}_clean.trsog",
                    f"sdc01_0410_main_{i}_clean.trsog",
                    f"sdc01_0420_main_{i}_clean.trsog",
                ]
                legends_save_files = [
                    f"sdc01_0330_always_{i}.trsog",
                    f"sdc01_0360_pre_start_{i}.trsog",
                    f"sdc01_0400_main_{i}.trsog",
                    f"sdc01_0410_main_{i}.trsog",
                    f"sdc01_0420_main_{i}.trsog",
                ]
                # Fezan - F803 Munki - F703 Oki - F603
                offsets = [
                    [0x07D6, 0X1D02, 0X3236],
                    [0X0D7E, 0X22AA, 0X37D6],  # 4D0A - OGERPON
                    [0X321A, 0X1CFE, 0x07E2],  # 4D16
                    [0X321A, 0X1CFE, 0X07E2],  # 4D16
                    [0X36A6, 0X218A, 0X0C6E]   # 6DD6
                ]
                indexes = [9926, 9927, 9928]

            for files in range(0, len(legends_files)):
                game_scene = open(
                    os.getcwd() + f"/Randomizer/Scenes/Kitakami/{Legends}/{legends_files[files]}", "rb")
                game_scene_bytes = game_scene.read()
                game_scene.close()

                with open(os.getcwd() + f"/Randomizer/Scenes/Kitakami/{Legends}/{legends_save_files[files]}",
                          "w+b") as file:
                    file.write(game_scene_bytes)
                    for j in range(0, len(offsets[files])):
                        file.seek(offsets[files][j])
                        if Legends != "Shared_Kita":
                            file.write(bytearray.fromhex(int(indexes[0]).to_bytes(2, byteorder='little').hex()))
                        else:
                            file.write(bytearray.fromhex(int(indexes[j]).to_bytes(2, byteorder='little').hex()))
    print("Patched Loyal Three")
    save_poke_catalog()


def patch_kora_miraidon():
    legend_file = open(os.getcwd() + "/Randomizer/StaticFights/" + "eventBattlePokemon_array.json", "r")
    legends = json.load(legend_file)
    legend_file.close()

    fake_pokemon_number = [9925, 9924]
    indexes = [115, 116]
    for i in range(0, 2):
        shiny = False
        if legends['values'][indexes[i]]['pokeData']['rareType'] == "RARE":
            shiny = True
        patch_poke_catalog(poke_catalog, legends, fake_pokemon_number[i], indexes[i], shiny)

    for i in range(0, 2):
        game_scene = open(os.getcwd() + f"/Randomizer/Scenes/Koraidon-Miraidon-Catch/sub_018_pre_start_{str(i)}_clean.trsog", "rb")
        game_scene_bytes = game_scene.read()
        game_scene.close()

        offset = [0x0098, 0x08E2]

        with open(os.getcwd() + f"/Randomizer/Scenes/Koraidon-Miraidon-Catch/sub_018_pre_start_{str(i)}.trsog", "w+b") as file:
            file.write(game_scene_bytes)
            for j in range(0, len(offset)):
                file.seek(offset[j])
                file.write(bytearray.fromhex(int(fake_pokemon_number[i]).to_bytes(2,
                                                                                            byteorder='little').hex()))

    print("Patched Koraidon and Miraidon in overworld")
    save_poke_catalog()


def patch_misc_pokemon():
    legend_file = open(os.getcwd() + "/Randomizer/StaticFights/" + "eventBattlePokemon_array.json", "r")
    legends = json.load(legend_file)
    legend_file.close()

    fake_pokemon_number = [9923, 9922]
    indexes = [25, 26]
    for i in range(0, 2):
        shiny = False
        if legends['values'][indexes[i]]['pokeData']['rareType'] == "RARE":
            shiny = True
        patch_poke_catalog(poke_catalog, legends, fake_pokemon_number[i], indexes[i], shiny)

    misc_pokemon = ["Houndoom", "Sunflora"]
    for pokemon in misc_pokemon:
        for i in range(0, 2):
            files = []
            files_save = []
            offset = []
            indexes = []
            if pokemon == "Houndoom":
                files = [f"common_0150_main_{i}_clean.trsog"]
                files_save = [f"common_0150_main_{i}.trsog"]
                offset = [0x0996]
                indexes = [9923]
            elif pokemon == "Sunflora":
                files = [f"pokes_{i}_clean.trsog"]
                files_save = [f"pokes_{i}.trsog"]
                offset = [0x04D2, 0x162E, 0X278A, 0X38EA, 0X4A4A, 0X5BAA, 0X6D0A, 0X7E66, 0X8FC6,
                          0XA126, 0XB282, 0XC3E2, 0XD53E, 0XE69E, 0XF7FE, 0X0001095E, 0X00011ABE,
                          0X00012C1A, 0X00013D7A, 0X00014EDA, 0X0001603A, 0X0001719A, 0X000182FE,
                          0X00019462, 0X0001A5C2, 0X0001B7E2, 0X0001C946, 0X0001DAA2, 0X0001EBFE,
                          0X0001FD5A]
                indexes = [9922]
            for k in range(0, len(files)):
                game_scene = open(os.getcwd() + f"/Randomizer/Scenes/Misc/{pokemon}/{files[k]}", "rb")
                game_scene_bytes = game_scene.read()
                game_scene.close()

                with open(os.getcwd() + f"/Randomizer/Scenes/Misc/{pokemon}/{files_save[k]}", "w+b") as file:
                    file.write(game_scene_bytes)
                    for j in range(0, len(offset)):
                        file.seek(offset[j])
                        file.write(bytearray.fromhex(int(indexes[0]).to_bytes(2, byteorder='little').hex()))

    print("Patched Misc Pokemon in overworld")
    save_poke_catalog()

