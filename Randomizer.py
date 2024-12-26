import requests
import Randomizer.FileDescriptor.fileDescriptor as FileDescriptor
import json
import os
import Randomizer.WildEncounters.new_wild_randomizer as WildRandomizer
import Randomizer.Trainers.trainerrando as TrainerRandomizer
import Randomizer.PersonalData.personal_randomizer as PersonalRandomizer
import Randomizer.StartersGifts.randomize_starters as StarterRandomizer
import Randomizer.StartersGifts.gifts_randomizer as GiftsRandomizer
import Randomizer.StaticSpawns.statics as StaticRandomizer
import Randomizer.Scenes.patchscene as PatchScene
import Randomizer.Items.itemrandomizer as ItemRandomizer
import Randomizer.StaticFights.randomize_fights as StaticFightsRandomizer
import Randomizer.TeraRaids.tera_raids_randomizer as TeraRaidsRandomizer
import Randomizer.helper_function as HelperFunctions
import Randomizer.TMs.randomize_tms as TMsRandomizer
import shutil

current_version_txt = '1.1.4a-OndoBranch'

def check_updates():
    print("Checking for Updates")
    print("Current version: " +current_version_txt)
    url = "https://api.github.com/repos/Gonzalooo/Scarlet-and-Violet-Randomizer/releases/latest"
    scrapped_response = requests.get(url)
    formated_response = scrapped_response.json()
    latest = formated_response['tag_name']

    if latest != current_version_txt:
        print(f"Version {latest} is NOW available please download it for best experience.")
    else:
        print("Already have the latest version of the randomizer.")


def open_config():
    if os.path.exists(os.getcwd() + "/config.blob"):
        file = open("config.blob", "r")
        print("!config.blob found, loading fixed seed and config settings from it instead of new_config.json!")
        print("!!!REMOVE config.blob IF YOU WISH TO CREATE A NEW RANDOMIZATION!!!")
    else:
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
    "boss": "world/data/battle/eventBattlePokemon",
    "personal": "avalon/data/",
    "statics": "world/data/field/fixed_symbol/fixed_symbol_table/",
    "itemdata": "world/data/item/itemdata/",
    "hidden_paldea": "world/data/item/hiddenItemDataTable/",
    "hidden_lc": "world/data/item/hiddenItemDataTable_lc/",
    "hidden_kitakami": "world/data/item/hiddenItemDataTable_su1/",
    "hidden_blueberry": "world/data/item/hiddenItemDataTable_su2/",
    "dropitems": "world/data/item/dropitemdata/",
    "pickupitems": "world/data/item/monohiroilItemData/",
    "synchro": "world/data/item/rummagingItemDataTable/",
    "catalog": "pokemon/catalog/catalog/",
    "starters_scenes_00": "world/scene/parts/event/event_scenario/main_scenario/common_0060_/",
    "starters_scenes_01": "world/scene/parts/event/event_scenario/main_scenario/common_0070_/",
    "starters_scenes_02": "world/scene/parts/event/event_scenario/main_scenario/common_0088_/",
    "starters_scenes_03": "world/scene/parts/event/event_scenario/main_scenario/common_0090_/",
    "shiny_scenes": "pokemon/data/",
    "item_fixed": "world/data/raid/raid_fixed_reward_item/",
    "item_lottery": "world/data/raid/raid_lottery_reward_item/",
    "shops": "world/data/ui/shop/friendlyshop/friendlyshop_lineup_data/",
    "tm-machine": "world/data/ui/shop/shop_wazamachine/shop_wazamachine_data/",
    "trpfd": "arc/"
}

def randomize_based_on_config(config):
    create_modpack()
    config["fixed_seed"] = HelperFunctions.seedgen(config["fixed_seed"])
    HelperFunctions.spoilerindex(config["fixed_seed"], current_version_txt)
    # TMs Randomizer
    tms = TMsRandomizer.randomize_tms(config['items_randomizer'])
    if tms is True:
        HelperFunctions.generate_binary("Randomizer/TMs/itemdata_array.bfbs",
                                        "Randomizer/TMs/itemdata_array.json",
                                        paths["itemdata"])
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

    # Static Randomizer
    static_randomized = StaticRandomizer.randomize_statics(config['static_pokemon_randomizer'])
    if static_randomized is True:
        HelperFunctions.generate_binary("Randomizer/StaticSpawns/fixed_symbol_table_array.bfbs",
                                        "Randomizer/StaticSpawns/fixed_symbol_table_array.json",
                                        paths["statics"])

    # Pokemon Stats Randomizer
    tms_randomize = config['items_randomizer']['randomize_tms']
    pokemon_randomized = PersonalRandomizer.randomize_pokemon_stats(config['pokemon_stats_randomizer'], tms_randomize)
    if pokemon_randomized is True:
        HelperFunctions.generate_binary("Randomizer/PersonalData/personal_array.fbs",
                                        "Randomizer/PersonalData/personal_array.json",
                                        paths["personal"])

    # Item Randomizer
    hidden_bin, pickup_bin, synchro_bin, drops_bin = ItemRandomizer.randomize_items(config['items_randomizer'])
    if hidden_bin is True:
        HelperFunctions.generate_binary("Randomizer/Items/hiddenItemDataTable_array.bfbs",
                                        "Randomizer/Items/hiddenItemDataTable_array.json",
                                        paths["hidden_paldea"])
        HelperFunctions.generate_binary("Randomizer/Items/hiddenItemDataTable_su1_array.bfbs",
                                        "Randomizer/Items/hiddenItemDataTable_su1_array.json",
                                        paths["hidden_kitakami"])
        HelperFunctions.generate_binary("Randomizer/Items/hiddenItemDataTable_su2_array.bfbs",
                                        "Randomizer/Items/hiddenItemDataTable_su2_array.json",
                                        paths["hidden_blueberry"])
        HelperFunctions.generate_binary("Randomizer/Items/hiddenItemDataTable_lc_array.bfbs",
                                        "Randomizer/Items/hiddenItemDataTable_lc_array.json",
                                        paths["hidden_lc"])
    if pickup_bin is True:
        HelperFunctions.generate_binary("Randomizer/Items/monohiroiItemData_array.bfbs",
                                        "Randomizer/Items/monohiroiItemData_array.json",
                                        paths["pickupitems"])
    if synchro_bin is True:
        HelperFunctions.generate_binary("Randomizer/Items/rummagingItemDataTable_array.bfbs",
                                        "Randomizer/Items/rummagingItemDataTable_array.json",
                                        paths["synchro"])
    if drops_bin is True:
        HelperFunctions.generate_binary("Randomizer/Items/dropitemdata_array.bfbs",
                                        "Randomizer/Items/dropitemdata_array.json",
                                        paths["dropitems"])

    # Starter Pokemon
    starters_randomized = StarterRandomizer.randomize_all_starters(config['starter_pokemon_randomizer'])
    if starters_randomized is True:
        HelperFunctions.generate_binary("Randomizer/StartersGifts/eventAddPokemon_array.bfbs",
                                        "Randomizer/StartersGifts/eventAddPokemon_array.json",
                                        paths["gifts"])

    if starters_randomized is True and config['starter_pokemon_randomizer']['show_starters_in_overworld'] == "yes":  # Updated for 3.0.1
        PatchScene.patch_starter_selection_scenes()

        for i in range(0, 4):
            HelperFunctions.create_folder_hierarchy('output/romfs/' + paths[f'starters_scenes_0{i}'])
        HelperFunctions.create_folder_hierarchy('output/romfs/' + paths['catalog'])

        HelperFunctions.generate_binary("Randomizer/Scenes/poke_resource_table.fbs",
                                        "Randomizer/Scenes/poke_resource_table.json",
                                        paths['catalog'])

        shutil.copyfile("Randomizer/Scenes/starters_scenes/common_0060_always_0.trsog",
                        "output/romfs/" + paths['starters_scenes_00'] + 'common_0060_always_0.trsog')
        shutil.copyfile("Randomizer/Scenes/starters_scenes/common_0060_always_1.trsog",
                        "output/romfs/" + paths['starters_scenes_00'] + 'common_0060_always_1.trsog')

        shutil.copyfile("Randomizer/Scenes/starters_scenes/common_0060_main_0.trsog",
                        "output/romfs/" + paths['starters_scenes_00'] + 'common_0060_main_0.trsog')
        shutil.copyfile("Randomizer/Scenes/starters_scenes/common_0060_main_1.trsog",
                        "output/romfs/" + paths['starters_scenes_00'] + 'common_0060_main_1.trsog')

        shutil.copyfile("Randomizer/Scenes/starters_scenes/common_0070_always_0.trsog",
                        "output/romfs/" + paths['starters_scenes_01'] + 'common_0070_always_0.trsog')
        shutil.copyfile("Randomizer/Scenes/starters_scenes/common_0070_always_1.trsog",
                        "output/romfs/" + paths['starters_scenes_01'] + 'common_0070_always_1.trsog')

        shutil.copyfile("Randomizer/Scenes/starters_scenes/common_0088_always_0.trsog",
                        "output/romfs/" + paths['starters_scenes_02'] + 'common_0088_always_0.trsog')
        shutil.copyfile("Randomizer/Scenes/starters_scenes/common_0088_always_1.trsog",
                        "output/romfs/" + paths['starters_scenes_02'] + 'common_0088_always_1.trsog')

        shutil.copyfile("Randomizer/Scenes/starters_scenes/common_0090_main_0.trsog",
                        "output/romfs/" + paths['starters_scenes_03'] + 'common_0090_main_0.trsog')
        shutil.copyfile("Randomizer/Scenes/starters_scenes/common_0090_main_1.trsog",
                        "output/romfs/" + paths['starters_scenes_03'] + 'common_0090_main_1.trsog')

    # Trainer Fight
    paldea_fight, kita_fight, blue_fight = TrainerRandomizer.randomize_trainers(config)
    if paldea_fight is True or kita_fight is True or blue_fight is True:
        HelperFunctions.generate_binary("Randomizer/Trainers/trdata_array.bfbs",
                                        "Randomizer/Trainers/trdata_array.json",
                                        paths["trainers"])

    # Gift Pokemon
    gifts_randomized = GiftsRandomizer.randomize_gifts(config['gift_pokemon_randomizer'])
    if gifts_randomized is True:
        HelperFunctions.generate_binary("Randomizer/StartersGifts/eventAddPokemon_array.bfbs",
                                        "Randomizer/StartersGifts/eventAddPokemon_array.json",
                                        paths["gifts"])

    # Static Fights Pokemon
    static_fights = StaticFightsRandomizer.randomize_static_fights(config['boss_pokemon_randomizer'])
    if static_fights is True:
        HelperFunctions.generate_binary("Randomizer/StaticFights/eventBattlePokemon_array.bfbs",
                                        "Randomizer/StaticFights/eventBattlePokemon_array.json",
                                        paths["boss"])
        HelperFunctions.generate_binary("Randomizer/Scenes/poke_resource_table.fbs",
                                        "Randomizer/Scenes/poke_resource_table.json",
                                        paths['catalog'])

    # Tera Raid Pokemon
    paldea_raid, kitakami_raid, blueberry_raid = TeraRaidsRandomizer.randomize_tera_raids(config)
    if paldea_raid is True:
        for i in range(1,7):
            HelperFunctions.generate_binary(f"Randomizer/TeraRaids/raid_enemy_0{str(i)}_array.bfbs",
                                            f"Randomizer/TeraRaids/raid_enemy_0{str(i)}_array.json",
                                            f"world/data/raid/raid_enemy_0{str(i)}")
    if kitakami_raid is True:
        for i in range(1,7):
            HelperFunctions.generate_binary(f"Randomizer/TeraRaids/su1_raid_enemy_0{str(i)}_array.bfbs",
                                            f"Randomizer/TeraRaids/su1_raid_enemy_0{str(i)}_array.json",
                                            f"world/data/raid/su1_raid_enemy_0{str(i)}")
    if blueberry_raid is True:
        for i in range(1,7):
            HelperFunctions.generate_binary(f"Randomizer/TeraRaids/su2_raid_enemy_0{str(i)}_array.bfbs",
                                            f"Randomizer/TeraRaids/su2_raid_enemy_0{str(i)}_array.json",
                                            f"world/data/raid/su2_raid_enemy_0{str(i)}")

    if paldea_raid is True or kitakami_raid is True or blueberry_raid is True:
        HelperFunctions.generate_binary(f"Randomizer/TeraRaids/raid_fixed_reward_item_array.bfbs",
                       f"Randomizer/TeraRaids/raid_fixed_reward_item_array.json",
                       paths["item_fixed"])
        HelperFunctions.generate_binary(f"Randomizer/paldeaTeraRaids/raid_lottery_reward_item_array.bfbs",
                       f"Randomizer/TeraRaids/raid_lottery_reward_item_array.json",
                       paths["item_lottery"])

    if os.path.exists(os.getcwd() + "/Randomizer/StartersGifts/" + f'output') is True:
        shutil.copytree(os.getcwd() + "/Randomizer/StartersGifts/output/romfs/pokemon/data", os.getcwd() +
                        "/output/romfs/" + paths['shiny_scenes'])


def randomize():
    check_updates()
    if os.path.exists(os.getcwd() + "/all-created-randomizer"):
        shutil.rmtree(os.getcwd() + "/all-created-randomizer")
    if os.path.exists(os.getcwd() + "/output"):
        shutil.rmtree(os.getcwd() + "/output")
    if os.path.exists(os.getcwd() + "/spoilers.log"):
        os.remove("spoilers.log")
    config = open_config()
    config = HelperFunctions.fix_config(config)
    HelperFunctions.gen_all_lookups()
    HelperFunctions.update_shiny_rate(config)
    if (config['bulk_creation']['is_enabled'] == "no" or
            config['bulk_creation']["number_of_unique_randomizers_to_create"] <= 1):
        print("Only creating one Randomizer")
        if os.path.exists(os.getcwd() + "/all-created-randomizer"):
            shutil.rmtree(os.getcwd() + "/all-created-randomizer")
        randomize_based_on_config(config)
        if config['auto-patch-romfs'] == "yes":
            FileDescriptor.patchFileDescriptor()
            HelperFunctions.generate_binary("Randomizer/FileDescriptor/data.fbs", "Randomizer/FileDescriptor/data.json", paths['trpfd'])
            if os.path.exists(os.getcwd() + "/randomizer-patched"):
                shutil.rmtree(os.getcwd() + "/randomizer-patched")
            shutil.copytree('output/', 'randomizer-patched/')
            shutil.make_archive("randomizer-patched/randomizer", "zip", "output/")
            shutil.copyfile("spoilers.log", "randomizer-patched/spoilers.log")
            with open("randomizer-patched/config.blob", 'w', encoding='utf-8') as f:
                json.dump(config, f, ensure_ascii=False, indent=2)
                f.close()

        else:
            shutil.make_archive("output/randomizer", "zip", "output/romfs/")
            shutil.copyfile("spoilers.log", "output/spoilers.log")
            with open("output/config.blob", 'w', encoding='utf-8') as f:
                json.dump(config, f, ensure_ascii=False, indent=2)
                f.close()

            if config['starter_pokemon_randomizer']['show_shiny_starters_in_overworld'] == "yes":
                if os.path.exists(os.getcwd() + "/Randomizer/StartersGifts/" + f'output'):
                    shutil.copytree(os.getcwd() + "/Randomizer/StartersGifts/output/romfs/pokemon/data",
                                    "output/romfs/" + paths['shiny_scenes'])
                    shutil.make_archive("output/randomizer-shiny-overworld", "zip", "output/romfs/")
                else:
                    print('No Shiny starter')
    elif (config['bulk_creation']['is_enabled'] == "yes" and
            config['bulk_creation']["number_of_unique_randomizers_to_create"] > 1):
        print("Creating Multiple Randomizers")
        for i in range(0, config['bulk_creation']["number_of_unique_randomizers_to_create"]):
            if os.path.exists(os.getcwd() + "/spoilers.log"):
                os.remove("spoilers.log")
            if os.path.exists(os.getcwd() + "/config.dump"):
                os.remove("config.dump")
            if os.path.exists(os.getcwd() + "/output"):
                shutil.rmtree(os.getcwd() + "/output")
            randomize_based_on_config(config)
            with open("config.dump", 'w', encoding='utf-8') as f:
                        json.dump(config, f, ensure_ascii=False, indent=2)
                        f.close()
            if config['auto-patch-romfs'] == "yes":
                shinyFile = False
                FileDescriptor.patchFileDescriptor()
                HelperFunctions.generate_binary("Randomizer/FileDescriptor/data.fbs", "Randomizer/FileDescriptor/data.json", paths['trpfd'])
                if os.path.exists(os.getcwd() + "/randomizer-patched"):
                    shutil.rmtree(os.getcwd() + "/randomizer-patched")
                shutil.copytree('output/', 'randomizer-patched/')
                shutil.make_archive("randomizer-patched/randomizer", "zip", "output/")
                if i == 0:
                    config["fixed_seed"] = 0#continue from first seed not repeat
                    if os.path.exists(os.getcwd() + f"/all-created-randomizer"):
                        shutil.rmtree(os.getcwd() + f"/all-created-randomizer")
                    os.makedirs("all-created-randomizer/randomizer_0")
                    shutil.copytree('randomizer-patched/',
                                    'all-created-randomizer/randomizer_0/randomizer-patched')
                    shutil.copyfile("spoilers.log", 'all-created-randomizer/spoilers_0.log')
                else:
                    os.makedirs(f"all-created-randomizer/randomizer_{i}")
                    shutil.copytree('randomizer-patched/',
                                    f'all-created-randomizer/randomizer_{i}/randomizer-patched') 
                    shutil.copyfile("spoilers.log", f'all-created-randomizer/spoilers_{i}.log')
            else:
                shutil.make_archive("output/randomizer", "zip", "output/romfs/")
                if i == 0:
                    config["fixed_seed"] = 0#continue from first seed not repeat
                    if os.path.exists(os.getcwd() + f"/all-created-randomizer"):
                        shutil.rmtree(os.getcwd() + f"/all-created-randomizer")
                    os.makedirs("all-created-randomizer/randomizer_0")
                    shutil.copy2('output/randomizer.zip',
                                    'all-created-randomizer/randomizer_0/randomizer.zip')
                    shutil.copyfile("spoilers.log", 'all-created-randomizer/spoilers_0.log')
                else:
                    os.makedirs(f"all-created-randomizer/randomizer_{i}")
                    shutil.copy2('output/randomizer.zip',
                                    f'all-created-randomizer/randomizer_{i}/randomizer.zip')
                    shutil.copyfile("spoilers.log", f'all-created-randomizer/spoilers_{i}.log')
            shutil.copyfile("config.dump", 'all-created-randomizer/config.blob')
            if os.path.exists(os.getcwd() + "/config.dump"):
                os.remove("config.dump")
    check_updates()


if __name__ == "__main__":
    randomize()
