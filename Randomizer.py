import json
import os
import Randomizer.WildEncounters.new_wild_randomizer as WildRandomizer
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
import Randomizer.helper_function as HelperFunctions
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
def open_config():
    file = open("new_config.json", "r")
    config = json.load(file)
    file.close()
    return config


def create_modpack():
    if os.path.exists(os.getcwd() + "/randomizer-patched-shiny"):
        shutil.rmtree(os.getcwd() + "/randomizer-patched-shiny")

    if os.path.exists(os.getcwd() + "/randomizer-patched"):
        shutil.rmtree(os.getcwd() + "/randomizer-patched")

    if os.access("output/", mode=777) is True:
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
    # Wild Pokemon Randomizer
    paldea_wild, kitakami_wild, blueberry_wild = WildRandomizer.randomize_wilderness(config)
    if paldea_wild is True:
        HelperFunctions.generate_binary("Randomizer/WildEncounters/pokedata_array.bfbs",
                                        "Randomizer/WildEncounters/pokedata_array.json",
                                        paths["wilds"])
    if kitakami_wild is True:
        HelperFunctions.generate_binary("Randomizer/WildEncounters/pokedata_su1_array.bfbs",
                                        "Randomizer/WildEncounters/pokedata_su1_array.json",
                                        paths["wilds_su1"])
    if blueberry_wild is True:
        HelperFunctions.generate_binary("Randomizer/WildEncounters/pokedata_su2_array.bfbs",
                                        "Randomizer/WildEncounters/pokedata_su2_array.json",
                                        paths["wilds_su2"])

    # Pokemon Stats Randomizer
    pokemon_randomized = PersonalRandomizer.randomize_pokemon_stats(config['pokemon_stats_randomizer'])
    if pokemon_randomized is True:
        HelperFunctions.generate_binary("Randomizer/PersonalData/personal_array.bfbs",
                                        "Randomizer/PersonalData/personal_array.json",
                                        paths["personal"])
    exit(0)
    if config['starter_randomizer']['is_enabled'] == "yes" and config['starter_randomizer']['show_starters_in_overworld'] == "yes":  # Updated for 3.0.1
        PatchScene.patchScenes()
        HelperFunctions.generate_binary("Randomizer/Scenes/poke_resource_table.fbs", "Randomizer/Scenes/poke_resource_table.json",
                       paths['catalog'])

        HelperFunctions.create_folder_hierarchy('output/romfs/'+paths["scenes"])

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
            HelperFunctions.generate_binary("Randomizer/FileDescriptor/data.fbs", "Randomizer/FileDescriptor/data.json", paths['trpfd'])
            if os.path.exists(os.getcwd() + "/randomizer-patched"):
                shutil.rmtree(os.getcwd() + "/randomizer-patched")
            shutil.copytree('output/', 'randomizer-patched/')
            shutil.make_archive("randomizer-patched/randomizer", "zip", "output/")
            if config['starter_randomizer']['is_enabled'] == "yes" and config['starter_randomizer']['shiny_overworld'] == "yes":
                if os.path.exists(os.getcwd() + "/Randomizer/Starters/" + f'output'):
                    shutil.copytree(os.getcwd() + "/Randomizer/Starters/output/romfs/pokemon/data",
                                    "output/romfs/" + paths['shiny_scenes'])
                    FileDescriptor.patchFileDescriptor()
                    HelperFunctions.generate_binary("Randomizer/FileDescriptor/data.fbs", "Randomizer/FileDescriptor/data.json",
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
                HelperFunctions.generate_binary("Randomizer/FileDescriptor/data.fbs", "Randomizer/FileDescriptor/data.json", paths['trpfd'])
                if os.path.exists(os.getcwd() + "/randomizer-patched"):
                    shutil.rmtree(os.getcwd() + "/randomizer-patched")
                shutil.copytree('output/', 'randomizer-patched/')
                shutil.make_archive("randomizer-patched/randomizer", "zip", "output/")
                if config['starter_randomizer']['is_enabled'] == "yes" and config['starter_randomizer']['shiny_overworld'] == "yes":
                    if os.path.exists(os.getcwd() + "/Randomizer/Starters/" + f'output'):
                        shutil.copytree(os.getcwd() + "/Randomizer/Starters/output/romfs/pokemon/data",
                                        "output/romfs/" + paths['shiny_scenes'])
                        FileDescriptor.patchFileDescriptor()
                        HelperFunctions.generate_binary("Randomizer/FileDescriptor/data.fbs", "Randomizer/FileDescriptor/data.json",
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


if __name__ == "__main__":
    randomize()
