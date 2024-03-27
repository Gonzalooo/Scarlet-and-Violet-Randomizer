import json
import os
import Randomizer.WildEncounters.wildrando as WildRandomizer
import Randomizer.Trainers.trainerrando as TrainerRandomizer
import Randomizer.PersonalData.personal_randomizer as PersonalRandomizer
import Randomizer.Starters.randomize_starters as StarterRandomizer
import Randomizer.StaticSpawns.statics as StaticRandomizer
import Randomizer.Scenes.patchscene as PatchScene
import Randomizer.generationLimiter.generationrando as GenerationLimiter
import Randomizer.Items.itemrandomizer as ItemRandomizer
import Randomizer.paldeaTeraRaids.teraRandomizePaldea as PaldeaRaids
import Randomizer.kitakamiTeraRaids.teraRandomizerTeal as KitakamiRaids
import Randomizer.blueberryTeraRaids.teraRandomizerIndigo as BlueberryRaids
import shutil
import subprocess
import platform
import requests


def check_updates():
    url = "https://api.github.com/repos/Gonzalooo/Scarlet-and-Violet-Randomizer/releases/latest"
    scrapped_response = requests.get(url)
    formated_response = scrapped_response.json()
    latest = formated_response['tag_name']

    if latest != '1.0.7-Release':
        print(f"Version {latest} is NOW available please download it for best experience.")


# thanks zadenowen for the function
def generateBinary(schema: str, json: str, path: str):
    iswindows = platform.system() == "Windows"
    flatc = os.path.abspath("flatc/flatc.exe") if iswindows else "flatc"
    outpath = os.path.abspath("output/romfs/" + path + "/")
    # print(outpath)
    outpath = outpath.replace("\\", '/')
    folders = outpath.split('/')
    index_value = 0
    #print(outpath)
    for i in range(0, len(folders)):
        index_value = index_value + 1
        if folders[i] == "output":
            break

    test = folders[index_value:]
    foldertogetperms = "/"
    for i in range(1, index_value):
        foldertogetperms = foldertogetperms+f"{folders[i]}/"
    #print(foldertogetperms)

    for i in range(0, len(test)):
        foldertogetperms = foldertogetperms + f"{test[i]}/"
        #print(foldertogetperms)
        os.makedirs(foldertogetperms, mode=0o777, exist_ok=True)

    proc = subprocess.run(
        [flatc,
        "-b",
        "-o",
        outpath,
        os.path.abspath(schema),
        os.path.abspath(json)
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    # print(proc.args)
    # print(proc.stdout + "Here")
    # print(proc.stderr)
    return proc


def open_config():
    file = open("config.json", "r")
    config = json.load(file)
    file.close()
    return config


def create_modpack():
    if os.path.exists(os.getcwd() + "/randomizer-patched-shiny"):
        shutil.rmtree(os.getcwd() + "/randomizer-patched-shiny")

    if os.path.exists(os.getcwd() + "/randomizer-patched"):
        shutil.rmtree(os.getcwd() + "/randomizer-patched")

    if os.access("output/", mode=777) == True: #exists
        shutil.rmtree("output/")
    os.makedirs("output/", mode=0o777, exist_ok=True)


paths = {
    "wilds": "world/data/encount/pokedata/pokedata/",
    "wilds_su1": "world/data/encount/pokedata/pokedata_su1/",
    "wilds_su2": "world/data/encount/pokedata/pokedata_su2/",
    "trainers": "world/data/trainer/trdata/",
    "gifts": "world/data/event/event_add_pokemon/eventAddPokemon/",
    "personal": "avalon/data/",
    "statics": "world/data/field/fixed_symbol/fixed_symbol_table/",
    "itemdata": "world/data/item/itemdata/",
    "hidden_paldea": "world/data/item/hiddenItemDataTable/",
    "hidden_lc": "world/data/item/hiddenItemDataTable_lc/",
    "hidden_kitakami": "world/data/item/hiddenItemDataTable_su1/",
    "hidden_blueberry": "world/data/item/hiddenItemDataTable_su2/",
    "dropitems": "world/data/item/dropitemdata/",
    "pickupitems": "world/data/item/monohiroilItemData/",
    "letsgo": "world/data/item/rummagingItemDataTable/",
    "catalog": "pokemon/catalog/catalog/",
    "scenes": "world/scene/parts/event/event_scenario/main_scenario/common_0070_/",
    "shiny_scenes": "pokemon/data/",
    "item_fixed": "world/data/raid/raid_fixed_reward_item/",
    "item_lottery": "world/data/raid/raid_lottery_reward_item/",
    "trpfd": "arc/"
}


def randomize_based_on_config(config):
    create_modpack()
    if config['limit_generation']['is_enabled'] == "yes":
        GenerationLimiter.randomize(config['limit_generation'], config)
        if config['limit_generation']['evolution_limiter'] == "yes":
            generateBinary("Randomizer/PersonalData/personal_array.fbs",
                           "Randomizer/PersonalData/personal_array.json", paths["personal"])

        if config['limit_generation']['starter_limiter'] == "yes":
            generateBinary("Randomizer/Starters/eventAddPokemon_array.bfbs",
                           "Randomizer/Starters/eventAddPokemon_array.json", paths["gifts"])

        if config['limit_generation']['static_limiter'] == "yes":
            generateBinary("Randomizer/StaticSpawns/fixed_symbol_table_array.bfbs",
                           "Randomizer/StaticSpawns/fixed_symbol_table_array.json", paths["statics"])

        if config['limit_generation']['trainer_limiter'] == "yes":
            generateBinary("Randomizer/Trainers/trdata_array.bfbs", "Randomizer/Trainers/trdata_array.json",
                           paths["trainers"])

        if config['limit_generation']['wild_limiter'] == "yes":
            generateBinary("Randomizer/WildEncounters/pokedata_array.bfbs",
                           "Randomizer/WildEncounters/pokedata_array.json", paths["wilds"])
            generateBinary("Randomizer/WildEncounters/pokedata_su1_array.bfbs",
                           "Randomizer/WildEncounters/pokedata_su1_array.json",
                           paths["wilds_su1"])
            generateBinary("Randomizer/WildEncounters/pokedata_su2_array.bfbs",
                           "Randomizer/WildEncounters/pokedata_su2_array.json",
                           paths["wilds_su2"])
    if config['wild_randomizer']['is_enabled'] == "yes":  # Updated for 3.0.1
        if config['limit_generation']['wild_limiter'] == "no" or config['limit_generation']['is_enabled'] == "no":
            WildRandomizer.randomize(config['wild_randomizer'])
            WildRandomizer.randomize_teal(config['wild_randomizer'])
            WildRandomizer.randomize_indigo(config['wild_randomizer'])
            generateBinary("Randomizer/WildEncounters/pokedata_array.bfbs",
                           "Randomizer/WildEncounters/pokedata_array.json", paths["wilds"])
            generateBinary("Randomizer/WildEncounters/pokedata_su1_array.bfbs",
                           "Randomizer/WildEncounters/pokedata_su1_array.json",
                           paths["wilds_su1"])
            generateBinary("Randomizer/WildEncounters/pokedata_su2_array.bfbs",
                           "Randomizer/WildEncounters/pokedata_su2_array.json",
                           paths["wilds_su2"])
    if config['trainer_randomizer']['is_enabled'] == "yes":  # Updated for 3.0.1
        if config['limit_generation']['trainer_limiter'] == "no" or config['limit_generation']['is_enabled'] == "no":
            TrainerRandomizer.randomize(config['trainer_randomizer'])
            generateBinary("Randomizer/Trainers/trdata_array.bfbs", "Randomizer/Trainers/trdata_array.json",
                           paths["trainers"])
    if config['personal_data_randomizer']['is_enabled'] == "yes":  # Updated to 3.0.1
        PersonalRandomizer.randomize(config['personal_data_randomizer'], config)
        if config['limit_generation']['evolution_limiter'] == "no" or config['limit_generation'][
            'is_enabled'] == "no":
            generateBinary("Randomizer/PersonalData/personal_array.fbs",
                           "Randomizer/PersonalData/personal_array.json", paths["personal"])
    if config['starter_randomizer']['is_enabled'] == "yes":  # Updated to 3.0.1
        if config['limit_generation']['starter_limiter'] == "no" or config['limit_generation']['is_enabled'] == "no":
            StarterRandomizer.randomize(config['starter_randomizer'])
            generateBinary("Randomizer/Starters/eventAddPokemon_array.bfbs",
                           "Randomizer/Starters/eventAddPokemon_array.json", paths["gifts"])
    if config['static_randomizer']['is_enabled'] == "yes":  # Updated to 3.0.1
        if config['limit_generation']['static_limiter'] == "no" or config['limit_generation']['is_enabled'] == "no":
            StaticRandomizer.randomize(config['static_randomizer'])
            generateBinary("Randomizer/StaticSpawns/fixed_symbol_table_array.bfbs",
                           "Randomizer/StaticSpawns/fixed_symbol_table_array.json", paths["statics"])
    if config['item_randomizer']['is_enabled'] == "yes":
        ItemRandomizer.randomize(config['item_randomizer'])
        if config['item_randomizer']['randomize_hidden_items'] == "yes":
            generateBinary("Randomizer/Items/hiddenItemDataTable_array.bfbs",
                           "Randomizer/Items/hiddenItemDataTable_array.json", paths["hidden_paldea"])
            generateBinary("Randomizer/Items/hiddenItemDataTable_lc_array.bfbs",
                           "Randomizer/Items/hiddenItemDataTable_lc_array.json", paths["hidden_lc"])
            generateBinary("Randomizer/Items/hiddenItemDataTable_su1_array.bfbs",
                           "Randomizer/Items/hiddenItemDataTable_su1_array.json", paths["hidden_kitakami"])
            generateBinary("Randomizer/Items/hiddenItemDataTable_su2_array.bfbs",
                           "Randomizer/Items/hiddenItemDataTable_su2_array.json", paths["hidden_blueberry"])
        if config['item_randomizer']['randomize_items_from_pickup_ability'] == "yes":
            generateBinary("Randomizer/Items/monohiroiItemData_array.bfbs",
                           "Randomizer/Items/monohiroiItemData_array.json", paths["pickupitems"])
        if config['item_randomizer']['randomize_synchro_items'] == "yes":
            generateBinary("Randomizer/Items/rummagingItemDataTable_array.bfbs",
                           "Randomizer/Items/rummagingItemDataTable_array.json", paths["letsgo"])
        if config['item_randomizer']['randomize_pokemon_drops'] == "yes":
            generateBinary("Randomizer/Items/dropitemdata_array.bfbs",
                           "Randomizer/Items/dropitemdata_array.json", paths["dropitems"])
    if config['tera_raids_randomizer']['is_enabled'] == "yes":
        PaldeaRaids.randomize(config['tera_raids_randomizer'], config)
        for i in range(1, 7):
            generateBinary(f"Randomizer/paldeaTeraRaids/raid_enemy_0{str(i)}_array.bfbs",
                           f"Randomizer/paldeaTeraRaids/raid_enemy_0{str(i)}_array.json",
                           f"world/data/raid/raid_enemy_0{str(i)}")
        generateBinary(f"Randomizer/paldeaTeraRaids/raid_fixed_reward_item_array.bfbs",
                        f"Randomizer/paldeaTeraRaids/raid_fixed_reward_item_array.json",
                        paths["item_fixed"])
        generateBinary(f"Randomizer/paldeaTeraRaids/raid_lottery_reward_item_array.bfbs",
                        f"Randomizer/paldeaTeraRaids/raid_lottery_reward_item_array.json",
                        paths["item_lottery"])

        KitakamiRaids.randomize(config['tera_raids_randomizer'], config)
        for i in range(1, 7):
            generateBinary(f"Randomizer/kitakamiTeraRaids/su1_raid_enemy_0{str(i)}_array.bfbs",
                           f"Randomizer/kitakamiTeraRaids/su1_raid_enemy_0{str(i)}_array.json",
                           f"world/data/raid/su1_raid_enemy_0{str(i)}")

        BlueberryRaids.randomize(config['tera_raids_randomizer'], config)
        for i in range(1, 7):
            generateBinary(f"Randomizer/blueberryTeraRaids/su2_raid_enemy_0{str(i)}_array.bfbs",
                           f"Randomizer/blueberryTeraRaids/su2_raid_enemy_0{str(i)}_array.json",
                           f"world/data/raid/su2_raid_enemy_0{str(i)}")
    if config['starter_randomizer']['is_enabled'] == "yes" and config['starter_randomizer']['show_starters_in_overworld'] == "yes":  # Updated for 3.0.1
        PatchScene.patchScenes()
        generateBinary("Randomizer/Scenes/poke_resource_table.fbs", "Randomizer/Scenes/poke_resource_table.json",
                       paths['catalog'])
        test = os.path.abspath("output/romfs/" + paths['scenes'])
        test = test.replace("\\", '/')
        folders = test.split('/')
        index_value = 0
        for i in range(0, len(folders)):
            index_value = index_value + 1
            if folders[i] == "output":
                break

        test = folders[index_value:]

        foldertogetperms = "/"
        for i in range(1, index_value):
            foldertogetperms = foldertogetperms + f"{folders[i]}/"
        # print(foldertogetperms)

        for i in range(0, len(test)):
            foldertogetperms = foldertogetperms + f"{test[i]}/"
            # print(foldertogetperms)
            os.makedirs(foldertogetperms, mode=0o777, exist_ok=True)

        shutil.copyfile("Randomizer/Scenes/common_0070_always_0.trsog",
                        "output/romfs/" + paths['scenes'] + 'common_0070_always_0.trsog')
        shutil.copyfile("Randomizer/Scenes/common_0070_always_1.trsog",
                        "output/romfs/" + paths['scenes'] + 'common_0070_always_1.trsog')


def randomize():
    check_updates()
    if os.path.exists(os.getcwd() + "/all-created-randomizer"):
        shutil.rmtree(os.getcwd() + "/all-created-randomizer")
    config = open_config()
    if (config['bulk_creation']['is_enabled'] == "no" or
            config['bulk_creation']["number_of_unique_randomizers_to_create"] <= 1):
        print("Only creating one Randomizer")
        if os.path.exists(os.getcwd() + "/all-created-randomizer"):
            shutil.rmtree(os.getcwd() + "/all-created-randomizer")
        randomize_based_on_config(config)
        if config['patch_trpfd'] == "yes":
            import Randomizer.FileDescriptor.fileDescriptor as FileDescriptor
            FileDescriptor.patchFileDescriptor()
            generateBinary("Randomizer/FileDescriptor/data.fbs", "Randomizer/FileDescriptor/data.json", paths['trpfd'])
            if os.path.exists(os.getcwd() + "/randomizer-patched"):
                shutil.rmtree(os.getcwd() + "/randomizer-patched")
            shutil.copytree('output/', 'randomizer-patched/')
            shutil.make_archive("randomizer-patched/randomizer", "zip", "output/")
            if config['starter_randomizer']['is_enabled'] == "yes" and config['starter_randomizer']['shiny_overworld'] == "yes":
                if os.path.exists(os.getcwd() + "/Randomizer/Starters/" + f'output'):
                    shutil.copytree(os.getcwd() + "/Randomizer/Starters/output/romfs/pokemon/data",
                                    "output/romfs/" + paths['shiny_scenes'])
                    FileDescriptor.patchFileDescriptor()
                    generateBinary("Randomizer/FileDescriptor/data.fbs", "Randomizer/FileDescriptor/data.json",
                                   paths['trpfd'])
                    if os.path.exists(os.getcwd() + "/randomizer-patched-shiny"):
                        shutil.rmtree(os.getcwd() + "/randomizer-patched-shiny")
                    shutil.copytree('output/', 'randomizer-patched-shiny/')
                    shutil.make_archive("randomizer-patched-shiny/randomizer-shiny-overworld", "zip", "output/")
        else:
            shutil.make_archive("output/randomizer", "zip", "output/romfs/")

            if config['starter_randomizer']['shiny_overworld'] == "yes":
                if os.path.exists(os.getcwd() + "/Randomizer/Starters/" + f'output'):
                    shutil.copytree(os.getcwd() + "/Randomizer/Starters/output/romfs/pokemon/data",
                                    "output/romfs/" + paths['shiny_scenes'])
                    shutil.make_archive("output/randomizer-shiny-overworld", "zip", "output/romfs/")
                else:
                    print('No Shiny starter')
    elif (config['bulk_creation']['is_enabled'] == "yes" and
            config['bulk_creation']["number_of_unique_randomizers_to_create"] > 1):
        print("Creating Multiple Randomizers")
        for i in range(0, config['bulk_creation']["number_of_unique_randomizers_to_create"]):
            randomize_based_on_config(config)
            if config['patch_trpfd'] == "yes":
                import Randomizer.FileDescriptor.fileDescriptor as FileDescriptor
                shinyFile = False
                FileDescriptor.patchFileDescriptor()
                generateBinary("Randomizer/FileDescriptor/data.fbs", "Randomizer/FileDescriptor/data.json", paths['trpfd'])
                if os.path.exists(os.getcwd() + "/randomizer-patched"):
                    shutil.rmtree(os.getcwd() + "/randomizer-patched")
                shutil.copytree('output/', 'randomizer-patched/')
                shutil.make_archive("randomizer-patched/randomizer", "zip", "output/")
                if config['starter_randomizer']['is_enabled'] == "yes" and config['starter_randomizer']['shiny_overworld'] == "yes":
                    if os.path.exists(os.getcwd() + "/Randomizer/Starters/" + f'output'):
                        shutil.copytree(os.getcwd() + "/Randomizer/Starters/output/romfs/pokemon/data",
                                        "output/romfs/" + paths['shiny_scenes'])
                        FileDescriptor.patchFileDescriptor()
                        generateBinary("Randomizer/FileDescriptor/data.fbs", "Randomizer/FileDescriptor/data.json",
                                       paths['trpfd'])
                        shinyFile = True
                        if os.path.exists(os.getcwd() + "/randomizer-patched-shiny"):
                            shutil.rmtree(os.getcwd() + "/randomizer-patched-shiny")
                        shutil.copytree('output/', 'randomizer-patched-shiny/')
                        shutil.make_archive("randomizer-patched-shiny/randomizer-shiny-overworld", "zip", "output/")
                if i == 0:
                    if os.path.exists(os.getcwd() + f"/all-created-randomizer"):
                        shutil.rmtree(os.getcwd() + f"/all-created-randomizer")
                    os.makedirs("all-created-randomizer/randomizer_0")
                    shutil.copytree('randomizer-patched/',
                                    'all-created-randomizer/randomizer_0/randomizer-patched')
                    if shinyFile is True:
                        shutil.copytree('randomizer-patched-shiny/',
                                        'all-created-randomizer/randomizer_0/randomizer-patched-shiny')
                else:
                    os.makedirs(f"all-created-randomizer/randomizer_{i}")
                    shutil.copytree('randomizer-patched/',
                                    f'all-created-randomizer/randomizer_{i}/randomizer-patched')
                    if shinyFile is True:
                        shutil.copytree('randomizer-patched-shiny/',
                                        f'all-created-randomizer/randomizer_{i}/randomizer-patched-shiny')
            else:
                shutil.make_archive("output/randomizer", "zip", "output/romfs/")

                shinyFile = False
                if config['starter_randomizer']['shiny_overworld'] == "yes":
                    if os.path.exists(os.getcwd() + "/Randomizer/Starters/" + f'output'):
                        shutil.copytree(os.getcwd() + "/Randomizer/Starters/output/romfs/pokemon/data",
                                        "output/romfs/" + paths['shiny_scenes'])
                        shutil.make_archive("output/randomizer-shiny-overworld", "zip", "output/romfs/")
                        shinyFile = True
                    else:
                        print('No Shiny starter')

                if i == 0:
                    if os.path.exists(os.getcwd() + f"/all-created-randomizer"):
                        shutil.rmtree(os.getcwd() + f"/all-created-randomizer")
                    os.makedirs("all-created-randomizer/randomizer_0")
                    shutil.copy2('output/randomizer.zip',
                                    'all-created-randomizer/randomizer_0/randomizer.zip')
                    if shinyFile is True:
                        shutil.copy2('output/randomizer-shiny-overworld.zip/',
                                        'all-created-randomizer/randomizer_0/randomizer-shiny-overworld.zip')
                else:
                    os.makedirs(f"all-created-randomizer/randomizer_{i}")
                    shutil.copy2('output/randomizer.zip',
                                    f'all-created-randomizer/randomizer_{i}/randomizer.zip')
                    if shinyFile is True:
                        shutil.copy2('output/randomizer-shiny-overworld.zip/',
                                        f'all-created-randomizer/randomizer_{i}/randomizer-shiny-overworld.zip')
    check_updates()

def test():
    create_modpack()


def main():
    randomize()


if __name__ == "__main__":
    main()
