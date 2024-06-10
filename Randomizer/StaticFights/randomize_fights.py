import json
import random
import os
import shutil
import Randomizer.shared_Variables as SharedVariables
import Randomizer.helper_function as HelperFunctions
import Randomizer.Scenes.patchscene as ChangeScenes

paths = {
    "lechonk_scenes": "world/scene/parts/event/event_scenario/main_scenario/common_0100_/",
    "coins_roaming": "world/obj_template/parts/coin_symbol/coin_symbol_walk_/",
    "coins_chest": "world/obj_template/parts/coin_symbol/coin_symbol_box_/",
    "glimmora_base": "world/scene/parts/event/event_scenario/main_scenario/common_1055_/",
    "scream_bundle": "world/scene/parts/event/event_scenario/main_scenario/common_1075_/",
    "tusk_treads": "world/scene/parts/event/event_scenario/main_scenario/common_1095_/",
    "big_fight_before_tm": "world/scene/parts/event/event_scenario/main_scenario/common_1170_/",
    "kora_mirai_titan_1": "world/scene/parts/event/event_scenario/main_scenario/legend_0020_/",
    "ting-lu": "world/scene/parts/event/event_scenario/sub_scenario/sub_014_/",
    "chien-pao": "world/scene/parts/event/event_scenario/sub_scenario/sub_015_/",
    "wo-chien": "world/scene/parts/event/event_scenario/sub_scenario/sub_016_/",
    "chi-yu": "world/scene/parts/event/event_scenario/sub_scenario/sub_017_/",
    "koraidon-miraidon": "world/scene/parts/event/event_scenario/sub_scenario/sub_018_/",
    'houndoom': "world/scene/parts/event/event_scenario/main_scenario/common_0150_/",
    'sunflora': "world/scene/parts/event/event_scenario/main_scenario/gym_kusa_poke_finding_/"
}

titans_fights = {
    'klawf_nushi': "world/obj_template/parts/nushi/iwa/nushi_iwa_fp_1066_/",
    'klawf_nushi_2': "world/obj_template/parts/nushi/iwa/nushi_iwa_fp_1066_020_/",
    'klawf_sub': "world/scene/parts/event/event_scenario/sub_scenario/sub_037_/",
    'klawf_main': "world/scene/parts/event/event_scenario/main_scenario/nushi_iwa_010_/",
    'klawf_main_2': "world/scene/parts/event/event_scenario/main_scenario/nushi_iwa_020_/",
    'greatiron_nushi': "world/obj_template/parts/nushi/jimen/nushi_jimen_fp_1082_010_/",
    'greatiron_nushi_2': "world/obj_template/parts/nushi/jimen/nushi_jimen_fp_1082_020_/",
    'greatiron_nushi_3': "world/obj_template/parts/nushi/jimen/nushi_jimen_fp_1090_010_/",
    'greatiron_nushi_4': "world/obj_template/parts/nushi/jimen/nushi_jimen_fp_1090_020_/",
    'greatiron_sub': "world/scene/parts/event/event_scenario/sub_scenario/sub_041_/",
    'greatiron_main': "world/scene/parts/event/event_scenario/main_scenario/nushi_jimen_010_/",
    'greatiron_main_2': "world/scene/parts/event/event_scenario/main_scenario/nushi_jimen_020_/",
    'orthworm_nushi': "world/obj_template/parts/nushi/hagane/nushi_hagane_fp_1048_010_/",
    'orthworm_nushi_2': "world/obj_template/parts/nushi/hagane/nushi_hagane_fp_1048_020_/",
    'orthworm_sub': "world/scene/parts/event/event_scenario/sub_scenario/sub_039_/",
    'orthworm_main': "world/scene/parts/event/event_scenario/main_scenario/nushi_hagane_010_/",
    'orthworm_main_2': "world/scene/parts/event/event_scenario/main_scenario/nushi_hagane_020_/",
    'dondozo_nushi': "world/obj_template/parts/nushi/dragon/nushi_dragon_fp_1035_010_/",
    'dondozo_nushi_2': "world/obj_template/parts/nushi/dragon/nushi_dragon_fp_1035_020_/",
    'dondozo_main': "world/scene/parts/event/event_scenario/main_scenario/nushi_dragon_010_/",
    'tatsugiri_nushi': "world/obj_template/parts/nushi/dragon/nushi_dragon_fp_1056_010_/",
    "tatsugiri_nushi_2": "world/obj_template/parts/nushi/dragon/nushi_dragon_fp_1056_020_/",
    'tatsugiri_sub': "world/scene/parts/event/event_scenario/sub_scenario/sub_040_/",
    'tatsugiri_main': "world/scene/parts/event/event_scenario/main_scenario/nushi_dragon_010_/",
    'bombirdier_nushi': "world/obj_template/parts/nushi/hiko/nushi_hiko_fp_1063_010_/",
    'bombirdier_nushi_2': "world/obj_template/parts/nushi/hiko/nushi_hiko_fp_1063_020_/",
    'bombirdier_sub': "world/scene/parts/event/event_scenario/sub_scenario/sub_038_/",
    'bombirdier_main': "world/scene/parts/event/event_scenario/main_scenario/nushi_hikou_010_/",
    'bombirdier_main_2': "world/scene/parts/event/event_scenario/main_scenario/nushi_hikou_020_/",
    'bombirdier_field': "world/scene/parts/field/field_contents/nushi/hiko/HikoNushi_/",
    "arven_toad": "world/scene/parts/field/field_contents/nushi/hagane/HaganeRockClashEvent_/",
    "arven_nacli": "world/scene/parts/field/field_contents/nushi/hiko/HikoRockClashEvent_/",
    "arven_villan": "world/scene/parts/field/field_contents/nushi/jimen/JimenRockClashEvent_/",
    "arven_greedent": "world/scene/parts/field/field_contents/nushi/dragon/DragonRockClashEvent_/",
    "arven_shellder": "world/scene/parts/field/field_contents/nushi/common/RockClashEvent_/",
    "arven_greedent_2": "world/scene/parts/event/event_scenario/main_scenario/nushi_dragon_020_/"
}

kitakami_files = {
    'milotic': "world/scene/parts/event/event_scenario/main_scenario/sdc01_0300_/",
    'ariados': "world/scene/parts/event/event_scenario/sub_scenario/s1_side02_0030_/",
    'bloodmon': "world/scene/parts/event/event_scenario/sub_scenario/s1_side02_0050_/",
    'shared_1': "world/scene/parts/event/event_scenario/main_scenario/sdc01_0330_/",
    'shared_2': "world/scene/parts/event/event_scenario/main_scenario/sdc01_0360_/",
    'shared_3': "world/scene/parts/event/event_scenario/main_scenario/sdc01_0400_/",
    'shared_4': "world/scene/parts/event/event_scenario/main_scenario/sdc01_0410_/",
    'shared_5': "world/scene/parts/event/event_scenario/main_scenario/sdc01_0420_/",
    'okidogi_1': "world/scene/parts/event/event_scenario/main_scenario/sdc01_3gods_a_/",
    'okidogi_2': "world/scene/parts/event/event_scenario/sub_scenario/s1_sub_011_/",
    'monkidori_1': "world/scene/parts/event/event_scenario/main_scenario/sdc01_3gods_b_/",
    'monkidori_2': "world/scene/parts/event/event_scenario/sub_scenario/s1_sub_012_/",
    'Fezandipiti_1': "world/scene/parts/event/event_scenario/main_scenario/sdc01_3gods_c_/",
    'Fezandipiti_2': "world/scene/parts/event/event_scenario/main_scenario/sdc01_3gods_c_before_/",
    'Fezandipiti_3': "world/scene/parts/event/event_scenario/sub_scenario/s1_sub_016_/",
}


hidden_paths = {
    'glimmora': "world/scene/parts/event/event_scenario/main_scenario/sdc02_0262_/",
    'garchomp': "world/scene/parts/event/event_scenario/sub_scenario/s2_sub_005_/",
    'garganacl': "world/scene/parts/event/event_scenario/main_scenario/sdc02_0267_/",
    'gougingcrown': "world/scene/parts/event/event_scenario/sub_scenario/s2_side01_0160_/",
    'noivern': "world/scene/parts/event/event_scenario/main_scenario/sdc02_0263_/",
    'ragingboulder': "world/scene/parts/event/event_scenario/sub_scenario/s2_side01_0180_/",
    'sandythorns': "world/scene/parts/event/event_scenario/main_scenario/sdc02_0265_/"
}

special_legends = {
    'pecharunt_1': "world/scene/parts/event/event_scenario/sub_scenario/s2_side01_0160_/",
    'pecharunt_2': "world/scene/parts/event/event_scenario/sub_scenario/s2_side01_0180_/",
    'meloetta': "world/scene/parts/event/event_scenario/sub_scenario/s2_sub_003_pop_/"
}

def randomize_specific_fight(pokedata, allowed_pokemon: list):
    choice = random.randint(1, 1025)
    while choice in SharedVariables.banned_pokemon or choice not in allowed_pokemon:
        choice = random.randint(1, 1025)
    pokedata['pokeData']['devId'] = HelperFunctions.fetch_developer_name(choice)
    form_id = HelperFunctions.get_alternate_form(choice)
    pokedata['pokeData']['formId'] = form_id
    pokedata['pokeData']['sex'] = "DEFAULT"
    pokedata['pokeData']['item'] = HelperFunctions.get_pokemon_item_form(choice, form_id)[0]
    pokedata['pokeData']['wazaType'] = "DEFAULT"
    shiny_change = random.randint(1, 10)
    shiny_change = 7
    if shiny_change == 7:
        pokedata['pokeData']['rareType'] = "RARE"
    for i in range(1, 5):
        pokedata['pokeData'][f'waza{str(i)}']['wazaId'] = "WAZA_NULL"
    return pokedata


def randomize_static_fights(config):
    if config['is_enabled'] == "yes":
        file = open(os.getcwd() + "/Randomizer/StaticFights/" + 'eventBattlePokemon_array_clean.json', 'r')
        file_json = json.load(file)
        file.close()
        # Mappings for later features
        # area0 - 0->10 (1075_multi, 1055_multi_, 1095_multi_, 1180_multi_) - Done
        # gimmighoul - 11->23 (coin_976_01 ... _05 and then inc of 5) - Done
        # lechonk -> 24 (common_0100_) - Done
        # Cave_Houndoom -> 25 (common_0150-) - Can't find (Ignore for now)
        # gym_sunfloras -> 26-30 (gym_kusa_020_KIMAWARI_0X)
        # Koraidon -> 31 (lastbattle_AIGUANA) (Figure out later) - Done
        # Miraidon -> 32 (lastbattle_BIGUANA) (Figure out later) - Done
        # Dondozo_Titan -> 33/34 (nusi_931) - Done
        # Orthworm_Titan -> 35/36 (nusi_944) - Done
        # TATSUGIRI_Titan -> 37 (nusi_952_0X) - Done
        # Tatsugiri_titan_fake -> 38-40 (nusi_952_dummy) - Done
        # Bombardier_Titan -> 41-42 (nusi_959) - Done
        # Klawf_Titan -> 43-44 (nusi_962) - Done
        # Great_Tusk Titan -> 45-46 (nusi_978) - Done
        # Iron Treads Titan -> 47-48 (nusi_986) - Done
        # Ting-Lu -> 49 (semi_legend_994) - Done
        # Chien-Pao -> 50 (semi_legend_995) - Done
        # Wo-Chien -> 51 (semi_legend_996) - Done
        # Chi-Yu -> 52 (semi_legend_997) - Done
        # Monkidori (cave-fight) -> 53/54 (sdc01_dokuzaru)
        # Okidogi  -> 55 (SDC01_get_dokuinu) - Done
        # Fezandipiti -> 56 (SDC01_get_dokuinu) - Done
        # Monkidori  -> 57 (SDC01_get_dkuzaru) - Done
        # Ogerpon-fire (Titan) -> 58/59 (SDC01_kamenoni_1)
        # Ogerpon-teal (Titan) -> 60/61 (SDC01_kamenoni_2)
        # Ogerpon-rock (Titan) -> 62/63 (SDC01_kamenoni_3)
        # Ogerpon-water (Titan) -> 64/65 (SDC01_kamenoni_4)
        # Milotic -> 66/67 (SDC01_midoriikenushi) - Done
        # Okidogi (titan) -> 68/69) (SDC01_onitaizi_dokuinu) - Done
        # Fezandipiti (titan) -> 70/71 (SDC01_onitaizi_bird) - Done
        # Monkidori (titan) -> 72/73 (SDC01_onitaizi_monkey) - Done
        # Ariados (Bloodmoon) -> 74 (S1_SIDE02_ariados) - Done
        # Ursaluna (Bloodmoon) -> 75 (S1_SIDE02_himeguma3B) - Done
        # Gouging Fire -> 76 (SDC02_sub_Aentei) - Done
        # Raging Bolt -> 77 (SDC02_sub_Araikou) - Done
        # Area Zero - Garchomp -> 78 (SDC02_area0_gaburiasu) - Done
        # Area Zero - Glimmora -> 79 (SDC02_area0_kirafuroru) - Done
        # Area Zero - Noivern -> 80 (SDC02_area0_onbaan) - Done
        # Area Zero - Garganacl -> 81 (SDC02_area0_sio) - Done
        # Area Zero - Sandy Shocks - > 82 (SDC02_area0_sunanokegawa) - Done
        # Area Zero - Iron Thorns -> 83 (SDC02_area0_tetunoibara) - Done
        # Iron Crown -> 84 (SDC02_sub_Bkobaruon) - Done
        # Iron Boulder -> 85 (SDC02_sub_Bterakion) - Done
        # Pecharunt -> 86 (su2_dokutarou) - Done
        # Terapagos - Kieran -> 87 (SDC02_0310_kodaikame)
        # Terapagos - Stellar -> 88 (SDC02_0330_kodaikame)
        # 90+ Other Legends in the Game. - Koraidon/Miraidon (Obtained) - Done

        allowed_pokemon, allowed_legends, bpl = HelperFunctions.check_generation_limiter(config['generation_limiter'])
        if config['randomize_all'] == "yes":
            for i in range(0, len(file_json['values'])):
                # Also all DLC Fights
                if i == 31 or i == 32:
                    continue
                if 58 <= i <= 65:
                    continue
                if i == 87 or i == 88:
                    continue
                if 12 <= i <= 23:
                    file_json['values'][i]['pokeData']['devId'] = file_json['values'][11]['pokeData']['devId']
                    file_json['values'][i]['pokeData']['formId'] = file_json['values'][11]['pokeData']['formId']
                    file_json['values'][i]['pokeData']['sex'] = "DEFAULT"
                    file_json['values'][i]['pokeData']['item'] = file_json['values'][11]['pokeData']['item']
                    file_json['values'][i]['pokeData']['wazaType'] = "DEFAULT"
                    file_json['values'][i]['pokeData']['rareType'] = file_json['values'][11]['pokeData']['rareType']
                    for k in range(1, 5):
                        file_json['values'][i]['pokeData'][f'waza{str(k)}']['wazaId'] = "WAZA_NULL"
                elif 27 <= i <= 30:
                    file_json['values'][i]['pokeData']['devId'] = file_json['values'][26]['pokeData']['devId']
                    file_json['values'][i]['pokeData']['formId'] = file_json['values'][26]['pokeData']['formId']
                    file_json['values'][i]['pokeData']['sex'] = "DEFAULT"
                    file_json['values'][i]['pokeData']['item'] = file_json['values'][26]['pokeData']['item']
                    file_json['values'][i]['pokeData']['wazaType'] = "DEFAULT"
                    file_json['values'][i]['pokeData']['rareType'] = file_json['values'][26]['pokeData']['rareType']
                    for k in range(1, 5):
                        file_json['values'][i]['pokeData'][f'waza{str(k)}']['wazaId'] = "WAZA_NULL"
                elif 33 <= i <= 48:
                    match i:
                        case 34:
                            file_json['values'][i]['pokeData']['devId'] = file_json['values'][33]['pokeData']['devId']
                            file_json['values'][i]['pokeData']['formId'] = file_json['values'][33]['pokeData']['formId']
                            file_json['values'][i]['pokeData']['sex'] = "DEFAULT"
                            file_json['values'][i]['pokeData']['item'] = file_json['values'][33]['pokeData']['item']
                            file_json['values'][i]['pokeData']['wazaType'] = "DEFAULT"
                            file_json['values'][i]['pokeData']['rareType'] = file_json['values'][33]['pokeData'][
                                'rareType']
                            for k in range(1, 5):
                                file_json['values'][i]['pokeData'][f'waza{str(k)}']['wazaId'] = "WAZA_NULL"
                        case 36:
                            file_json['values'][i]['pokeData']['devId'] = file_json['values'][35]['pokeData']['devId']
                            file_json['values'][i]['pokeData']['formId'] = file_json['values'][35]['pokeData']['formId']
                            file_json['values'][i]['pokeData']['sex'] = "DEFAULT"
                            file_json['values'][i]['pokeData']['item'] = file_json['values'][35]['pokeData']['item']
                            file_json['values'][i]['pokeData']['wazaType'] = "DEFAULT"
                            file_json['values'][i]['pokeData']['rareType'] = file_json['values'][35]['pokeData'][
                                'rareType']
                            for k in range(1, 5):
                                file_json['values'][i]['pokeData'][f'waza{str(k)}']['wazaId'] = "WAZA_NULL"
                        case 42:
                            file_json['values'][i]['pokeData']['devId'] = file_json['values'][41]['pokeData']['devId']
                            file_json['values'][i]['pokeData']['formId'] = file_json['values'][41]['pokeData']['formId']
                            file_json['values'][i]['pokeData']['sex'] = "DEFAULT"
                            file_json['values'][i]['pokeData']['item'] = file_json['values'][41]['pokeData']['item']
                            file_json['values'][i]['pokeData']['wazaType'] = "DEFAULT"
                            file_json['values'][i]['pokeData']['rareType'] = file_json['values'][41]['pokeData'][
                                'rareType']
                            for k in range(1, 5):
                                file_json['values'][i]['pokeData'][f'waza{str(k)}']['wazaId'] = "WAZA_NULL"
                        case 44:
                            file_json['values'][i]['pokeData']['devId'] = file_json['values'][43]['pokeData']['devId']
                            file_json['values'][i]['pokeData']['formId'] = file_json['values'][43]['pokeData']['formId']
                            file_json['values'][i]['pokeData']['sex'] = "DEFAULT"
                            file_json['values'][i]['pokeData']['item'] = file_json['values'][43]['pokeData']['item']
                            file_json['values'][i]['pokeData']['wazaType'] = "DEFAULT"
                            file_json['values'][i]['pokeData']['rareType'] = file_json['values'][43]['pokeData'][
                                'rareType']
                            for k in range(1, 5):
                                file_json['values'][i]['pokeData'][f'waza{str(k)}']['wazaId'] = "WAZA_NULL"
                        case 46:
                            file_json['values'][i]['pokeData']['devId'] = file_json['values'][45]['pokeData']['devId']
                            file_json['values'][i]['pokeData']['formId'] = file_json['values'][45]['pokeData']['formId']
                            file_json['values'][i]['pokeData']['sex'] = "DEFAULT"
                            file_json['values'][i]['pokeData']['item'] = file_json['values'][45]['pokeData']['item']
                            file_json['values'][i]['pokeData']['wazaType'] = "DEFAULT"
                            file_json['values'][i]['pokeData']['rareType'] = file_json['values'][45]['pokeData'][
                                'rareType']
                            for k in range(1, 5):
                                file_json['values'][i]['pokeData'][f'waza{str(k)}']['wazaId'] = "WAZA_NULL"
                        case 48:
                            file_json['values'][i]['pokeData']['devId'] = file_json['values'][47]['pokeData']['devId']
                            file_json['values'][i]['pokeData']['formId'] = file_json['values'][47]['pokeData']['formId']
                            file_json['values'][i]['pokeData']['sex'] = "DEFAULT"
                            file_json['values'][i]['pokeData']['item'] = file_json['values'][47]['pokeData']['item']
                            file_json['values'][i]['pokeData']['wazaType'] = "DEFAULT"
                            file_json['values'][i]['pokeData']['rareType'] = file_json['values'][47]['pokeData']['rareType']
                            for k in range(1, 5):
                                file_json['values'][i]['pokeData'][f'waza{str(k)}']['wazaId'] = "WAZA_NULL"
                        case _:
                            randomize_specific_fight(file_json['values'][i], allowed_pokemon)
                elif i == 67:
                    file_json['values'][i]['pokeData']['devId'] = file_json['values'][66]['pokeData']['devId']
                    file_json['values'][i]['pokeData']['formId'] = file_json['values'][66]['pokeData']['formId']
                    file_json['values'][i]['pokeData']['sex'] = "DEFAULT"
                    file_json['values'][i]['pokeData']['item'] = file_json['values'][66]['pokeData']['item']
                    file_json['values'][i]['pokeData']['wazaType'] = "DEFAULT"
                    file_json['values'][i]['pokeData']['rareType'] = file_json['values'][66]['pokeData']['rareType']
                    for k in range(1, 5):
                        file_json['values'][i]['pokeData'][f'waza{str(k)}']['wazaId'] = "WAZA_NULL"
                # elif i == 115:
                #     file_json['values'][i]['pokeData']['devId'] = file_json['values'][31]['pokeData']['devId']
                #     file_json['values'][i]['pokeData']['formId'] = file_json['values'][31]['pokeData']['formId']
                #     file_json['values'][i]['pokeData']['sex'] = "DEFAULT"
                #     file_json['values'][i]['pokeData']['item'] = file_json['values'][31]['pokeData']['item']
                #     file_json['values'][i]['pokeData']['wazaType'] = "DEFAULT"
                #     file_json['values'][i]['pokeData']['rareType'] = file_json['values'][31]['pokeData']['rareType']
                #     for k in range(1, 5):
                #         file_json['values'][i]['pokeData'][f'waza{str(k)}']['wazaId'] = "WAZA_NULL"
                # elif i == 116:
                #     file_json['values'][i]['pokeData']['devId'] = file_json['values'][32]['pokeData']['devId']
                #     file_json['values'][i]['pokeData']['formId'] = file_json['values'][32]['pokeData']['formId']
                #     file_json['values'][i]['pokeData']['sex'] = "DEFAULT"
                #     file_json['values'][i]['pokeData']['item'] = file_json['values'][32]['pokeData']['item']
                #     file_json['values'][i]['pokeData']['wazaType'] = "DEFAULT"
                #     file_json['values'][i]['pokeData']['rareType'] = file_json['values'][32]['pokeData']['rareType']
                #     for k in range(1, 5):
                #         file_json['values'][i]['pokeData'][f'waza{str(k)}']['wazaId'] = "WAZA_NULL"
                else:
                    randomize_specific_fight(file_json['values'][i], allowed_pokemon)

            outdata = json.dumps(file_json, indent=2)
            with open(os.getcwd() + "/Randomizer/StaticFights/" + "eventBattlePokemon_array.json", 'w') as outfile:
                outfile.write(outdata)

            ChangeScenes.patch_gimmighoul_scene()
            HelperFunctions.create_folder_hierarchy(os.getcwd() + '/output/romfs/' + paths['coins_chest'])

            shutil.copyfile(os.getcwd() + "/Randomizer/Scenes/gimmighoul_scene/coin_symbol_box_0.trsot",
                            os.getcwd() + "/output/romfs/" + paths['coins_chest'] + 'coin_symbol_box_0.trsot')
            shutil.copyfile(os.getcwd() + "/Randomizer/Scenes/gimmighoul_scene/coin_symbol_box_1.trsot",
                            os.getcwd() + "/output/romfs/" + paths['coins_chest'] + 'coin_symbol_box_1.trsot')

            ChangeScenes.patch_lechonk_starting_scene()
            HelperFunctions.create_folder_hierarchy(os.getcwd() + '/output/romfs/' + paths['lechonk_scenes'])
            shutil.copyfile(os.getcwd() + "/Randomizer/Scenes/lechonk_scenes/common_0100_main_0.trsog",
                            os.getcwd() + "/output/romfs/" + paths['lechonk_scenes'] + 'common_0100_main_0.trsog')
            shutil.copyfile(os.getcwd() + "/Randomizer/Scenes/lechonk_scenes/common_0100_main_1.trsog",
                            os.getcwd() + "/output/romfs/" + paths['lechonk_scenes'] + 'common_0100_main_1.trsog')

            ChangeScenes.patch_treasure_of_ruins()
            HelperFunctions.create_folder_hierarchy(os.getcwd() + '/output/romfs/' + paths['ting-lu'])
            shutil.copyfile(os.getcwd() + "/Randomizer/Scenes/Treasures-Ruin/sub_014_main_0.trsog",
                            os.getcwd() + "/output/romfs/" + paths['ting-lu'] + 'sub_014_main_0.trsog')
            shutil.copyfile(os.getcwd() + "/Randomizer/Scenes/Treasures-Ruin/sub_014_main_1.trsog",
                            os.getcwd() + "/output/romfs/" + paths['ting-lu'] + 'sub_014_main_1.trsog')

            HelperFunctions.create_folder_hierarchy(os.getcwd() + '/output/romfs/' + paths['chien-pao'])
            shutil.copyfile(os.getcwd() + "/Randomizer/Scenes/Treasures-Ruin/sub_015_main_0.trsog",
                            os.getcwd() + "/output/romfs/" + paths['chien-pao'] + 'sub_015_main_0.trsog')
            shutil.copyfile(os.getcwd() + "/Randomizer/Scenes/Treasures-Ruin/sub_015_main_1.trsog",
                            os.getcwd() + "/output/romfs/" + paths['chien-pao'] + 'sub_015_main_1.trsog')

            HelperFunctions.create_folder_hierarchy(os.getcwd() + '/output/romfs/' + paths['wo-chien'])
            shutil.copyfile(os.getcwd() + "/Randomizer/Scenes/Treasures-Ruin/sub_016_main_0.trsog",
                            os.getcwd() + "/output/romfs/" + paths['wo-chien'] + 'sub_016_main_0.trsog')
            shutil.copyfile(os.getcwd() + "/Randomizer/Scenes/Treasures-Ruin/sub_016_main_1.trsog",
                            os.getcwd() + "/output/romfs/" + paths['wo-chien'] + 'sub_016_main_1.trsog')

            HelperFunctions.create_folder_hierarchy(os.getcwd() + '/output/romfs/' + paths['chi-yu'])
            shutil.copyfile(os.getcwd() + "/Randomizer/Scenes/Treasures-Ruin/sub_017_main_0.trsog",
                            os.getcwd() + "/output/romfs/" + paths['chi-yu'] + 'sub_017_main_0.trsog')
            shutil.copyfile(os.getcwd() + "/Randomizer/Scenes/Treasures-Ruin/sub_017_main_1.trsog",
                            os.getcwd() + "/output/romfs/" + paths['chi-yu'] + 'sub_017_main_1.trsog')

            ChangeScenes.patch_area_zero_first()
            HelperFunctions.create_folder_hierarchy(os.getcwd() + '/output/romfs/' + paths['glimmora_base'])
            shutil.copyfile(os.getcwd() + "/Randomizer/Scenes/Area_Zero_Way_Home/common_1055_main_0.trsog",
                            os.getcwd() + "/output/romfs/" + paths['glimmora_base'] + 'common_1055_main_0.trsog')
            shutil.copyfile(os.getcwd() + "/Randomizer/Scenes/Area_Zero_Way_Home/common_1055_main_1.trsog",
                            os.getcwd() + "/output/romfs/" + paths['glimmora_base'] + 'common_1055_main_1.trsog')

            HelperFunctions.create_folder_hierarchy(os.getcwd() + '/output/romfs/' + paths['scream_bundle'])
            shutil.copyfile(os.getcwd() + "/Randomizer/Scenes/Area_Zero_Way_Home/common_1075_main_0.trsog",
                            os.getcwd() + "/output/romfs/" + paths['scream_bundle'] + 'common_1075_main_0.trsog')
            shutil.copyfile(os.getcwd() + "/Randomizer/Scenes/Area_Zero_Way_Home/common_1075_main_1.trsog",
                            os.getcwd() + "/output/romfs/" + paths['scream_bundle'] + 'common_1075_main_1.trsog')

            HelperFunctions.create_folder_hierarchy(os.getcwd() + '/output/romfs/' + paths['tusk_treads'])
            shutil.copyfile(os.getcwd() + "/Randomizer/Scenes/Area_Zero_Way_Home/common_1095_main_0.trsog",
                            os.getcwd() + "/output/romfs/" + paths['tusk_treads'] + 'common_1095_main_0.trsog')
            shutil.copyfile(os.getcwd() + "/Randomizer/Scenes/Area_Zero_Way_Home/common_1095_main_1.trsog",
                            os.getcwd() + "/output/romfs/" + paths['tusk_treads'] + 'common_1095_main_1.trsog')

            HelperFunctions.create_folder_hierarchy(os.getcwd() + '/output/romfs/' + paths['big_fight_before_tm'])
            shutil.copyfile(os.getcwd() + "/Randomizer/Scenes/Area_Zero_Way_Home/common_1170_always_0.trsog",
                            os.getcwd() + "/output/romfs/" + paths['big_fight_before_tm'] + 'common_1170_always_0.trsog')
            shutil.copyfile(os.getcwd() + "/Randomizer/Scenes/Area_Zero_Way_Home/common_1170_always_1.trsog",
                            os.getcwd() + "/output/romfs/" + paths['big_fight_before_tm'] + 'common_1170_always_1.trsog')

            ChangeScenes.patch_titans_and_arven_titans()
            for files in titans_fights:
                HelperFunctions.create_folder_hierarchy(os.getcwd() + '/output/romfs/' + titans_fights[files])
            Titans_Folders_List = ["Klawf", "Bombirdier", "Orthworm", "GreatIron", "Dondozo", "Tatsugiri"]

            for Titans in Titans_Folders_List:
                for i in range(0, 2):
                    titans_save_files = []
                    paths_for_saving = []
                    if Titans == "Klawf":
                        titans_save_files = [
                            f"nushi_iwa_010_pre_start_{i}.trsog",
                            f"nushi_iwa_020_pre_start_{i}.trsog",
                            f"nushi_iwa_fp_1066_{i}.trsot",
                            f"nushi_iwa_fp_1066_020_{i}.trsot",
                            f"sub_037_pre_start_{i}.trsog",
                        ]
                        paths_for_saving = [
                            f"{titans_fights['klawf_main']}",
                            f"{titans_fights['klawf_main_2']}",
                            f"{titans_fights['klawf_nushi']}",
                            f"{titans_fights['klawf_nushi_2']}",
                            f"{titans_fights['klawf_sub']}",
                        ]
                    elif Titans == "Bombirdier":
                        titans_save_files = [
                            f"HikoNushi_{i}.trscn",
                            f"nushi_hiko_fp_1063_010_{i}.trsot",
                            f"nushi_hiko_fp_1063_020_{i}.trsot",
                            f"nushi_hikou_010_pre_start_{i}.trsog",
                            f"nushi_hikou_020_pre_start_{i}.trsog",
                            f"nushi_hikou_020_main_{i}.trsog",
                            f"sub_038_pre_start_{i}.trsog",
                        ]
                        paths_for_saving = [
                            f"{titans_fights['bombirdier_field']}",
                            f"{titans_fights['bombirdier_nushi']}",
                            f"{titans_fights['bombirdier_nushi_2']}",
                            f"{titans_fights['bombirdier_main']}",
                            f"{titans_fights['bombirdier_main_2']}",
                            f"{titans_fights['bombirdier_main_2']}",
                            f"{titans_fights['bombirdier_sub']}",
                        ]
                    elif Titans == "Orthworm":
                        titans_save_files = [
                            f"nushi_hagane_010_pre_start_{i}.trsog",
                            f"nushi_hagane_020_pre_start_{i}.trsog",
                            f"nushi_hagane_fp_1048_010_{i}.trsot",
                            f"nushi_hagane_fp_1048_020_{i}.trsot",
                            f"sub_039_pre_start_{i}.trsog",
                        ]
                        paths_for_saving = [
                            f"{titans_fights['orthworm_main']}",
                            f"{titans_fights['orthworm_main_2']}",
                            f"{titans_fights['orthworm_nushi']}",
                            f"{titans_fights['orthworm_nushi_2']}",
                            f"{titans_fights['orthworm_sub']}",
                        ]
                    elif Titans == "GreatIron":
                        titans_save_files = [
                            f"nushi_jimen_010_pre_start_{i}.trsog",
                            f"nushi_jimen_020_pre_start_{i}.trsog",
                            f"nushi_jimen_fp_1082_010_{i}.trsot",
                            f"nushi_jimen_fp_1082_020_{i}.trsot",
                            f"nushi_jimen_fp_1090_010_{i}.trsot",
                            f"nushi_jimen_fp_1090_020_{i}.trsot",
                            f"sub_041_pre_start_{i}.trsog",
                        ]
                        paths_for_saving = [
                            f"{titans_fights['greatiron_main']}",
                            f"{titans_fights['greatiron_main_2']}",
                            f"{titans_fights['greatiron_nushi']}",
                            f"{titans_fights['greatiron_nushi_2']}",
                            f"{titans_fights['greatiron_nushi_3']}",
                            f"{titans_fights['greatiron_nushi_4']}",
                            f"{titans_fights['greatiron_sub']}",
                        ]
                    elif Titans == "Dondozo":
                        titans_save_files = [
                            f"nushi_dragon_010_always_{i}.trsog",
                            f"nushi_dragon_fp_1035_010_{i}.trsot",
                            f"nushi_dragon_fp_1035_020_{i}.trsot",
                        ]
                        paths_for_saving = [
                            f"{titans_fights['dondozo_main']}",
                            f"{titans_fights['dondozo_nushi']}",
                            f"{titans_fights['dondozo_nushi_2']}",
                        ]
                    elif Titans == "Tatsugiri":
                        titans_save_files = [
                            f"nushi_dragon_010_always_{i}.trsog",
                            f"nushi_dragon_fp_1056_010_{i}.trsot",
                            f"nushi_dragon_fp_1056_020_{i}.trsot",
                            f"sub_040_pre_start_{i}.trsog",
                        ]
                        paths_for_saving = [
                            f"{titans_fights['tatsugiri_main']}",
                            f"{titans_fights['tatsugiri_nushi']}",
                            f"{titans_fights['tatsugiri_nushi_2']}",
                            f"{titans_fights['tatsugiri_sub']}",
                        ]
                    for j in range(0, len(titans_save_files)):
                        shutil.copyfile(os.getcwd() + f"/Randomizer/Scenes/Titans/{Titans}/{titans_save_files[j]}",
                                        os.getcwd() + "/output/romfs/" + paths_for_saving[j] + titans_save_files[j])

            ChangeScenes.patch_kitakami_nonlegends()
            ChangeScenes.patch_kitakami_legends()
            for kita in kitakami_files:
                HelperFunctions.create_folder_hierarchy(os.getcwd() + '/output/romfs/' + kitakami_files[kita])

            kitakami_scenes = ["Ariados", "Fenzadipiti", "Milotic", "Monkidori", "Okidogi", "Ursaluna", "Shared_Kita"]

            for pokemons in kitakami_scenes:
                for i in range(0, 2):
                    k_files = []
                    k_paths = []
                    if pokemons == "Ariados":
                        k_files = [
                            f"s1_side02_0030_main_{i}.trsog",
                        ]
                        k_paths = [
                            kitakami_files['ariados']
                        ]
                    elif pokemons == "Fenzadipiti":
                        k_files = [
                            f"sdc01_3gods_c_pre_start_{i}.trsog",
                            f"sdc01_3gods_c_before_pre_start_{i}.trsog",
                            f"s1_sub_016_pre_start_{i}.trsog"
                        ]
                        k_paths = [
                            kitakami_files['Fezandipiti_1'],
                            kitakami_files['Fezandipiti_2'],
                            kitakami_files['Fezandipiti_3'],
                        ]
                    elif pokemons == "Milotic":
                        k_files = [
                            f"sdc01_0300_main_{i}.trsog",
                        ]
                        k_paths = [
                            kitakami_files['milotic']
                        ]
                    elif pokemons == "Monkidori":
                        k_files = [
                            f"sdc01_3gods_b_pre_start_{i}.trsog",
                            f"s1_sub_012_pre_start_{i}.trsog"
                        ]
                        k_paths = [
                            kitakami_files['monkidori_1'],
                            kitakami_files['monkidori_2'],
                        ]
                    elif pokemons == "Okidogi":
                        k_files = [
                            f"sdc01_3gods_a_pre_start_{i}.trsog",
                            f"s1_sub_011_pre_start_{i}.trsog"
                        ]
                        k_paths = [
                            kitakami_files['okidogi_1'],
                            kitakami_files['okidogi_2'],
                        ]
                    elif pokemons == "Ursaluna":
                        k_files = [
                            f"s1_side02_0050_main_{i}.trsog",
                        ]
                        k_paths = [
                            kitakami_files['bloodmon']
                        ]
                    elif pokemons == "Shared_Kita":
                        k_files = [
                            f"sdc01_0330_always_{i}.trsog",
                            f"sdc01_0360_pre_start_{i}.trsog",
                            f"sdc01_0400_main_{i}.trsog",
                            f"sdc01_0410_main_{i}.trsog",
                            f"sdc01_0420_main_{i}.trsog",
                        ]
                        k_paths = [
                            kitakami_files['shared_1'],
                            kitakami_files['shared_2'],
                            kitakami_files['shared_3'],
                            kitakami_files['shared_4'],
                            kitakami_files['shared_5']
                        ]

                    for j in range(0, len(k_files)):
                        shutil.copyfile(os.getcwd() + f"/Randomizer/Scenes/Kitakami/{pokemons}/{k_files[j]}",
                                        os.getcwd() + "/output/romfs/" + k_paths[j] + k_files[j])

            ChangeScenes.patch_area_zero_treasure()
            for treasures in hidden_paths:
                HelperFunctions.create_folder_hierarchy(os.getcwd() + '/output/romfs/' + hidden_paths[treasures])

            treasure_scenes = ["Garchomp", "Garganacl", "Glimmora", "Gouging Fire", "Noivern", "Raging Bolt", "Sandy Shocks"]

            for pokemons in treasure_scenes:
                for i in range(0, 2):
                    treasure_files = [

                    ]
                    treasure_paths = [

                    ]
                    if pokemons == "Garchomp":
                        treasure_files = [
                            f"s2_sub_005_pre_start_{i}.trsog",
                        ]
                        treasure_paths = [
                            hidden_paths['garchomp']
                        ]
                    elif pokemons == "Garganacl":
                        treasure_files = [
                            f"sdc02_0267_pre_start_{i}.trsog",
                        ]
                        treasure_paths = [
                            hidden_paths['garganacl']
                        ]
                    elif pokemons == "Glimmora":
                        treasure_files = [
                            f"sdc02_0262_main_{i}.trsog",
                        ]
                        treasure_paths = [
                            hidden_paths['glimmora']
                        ]
                    elif pokemons == "Gouging Fire":
                        treasure_files = [
                            f"s2_side02_0010_pre_start_{i}.trsog",
                        ]
                        treasure_paths = [
                            hidden_paths['gougingcrown']
                        ]
                    elif pokemons == "Noivern":
                        treasure_files = [
                            f"sdc02_0263_pre_start_{i}.trsog",
                        ]
                        treasure_paths = [
                            hidden_paths['noivern']
                        ]
                    elif pokemons == "Raging Bolt":
                        treasure_files = [
                            f"s2_side02_0020_pre_start_{i}.trsog",
                        ]
                        treasure_paths = [
                            hidden_paths['ragingboulder']
                        ]
                    elif pokemons == "Sandy Shocks":
                        treasure_files = [
                            f"sdc02_0265_pre_start_{i}.trsog",
                        ]
                        treasure_paths = [
                            hidden_paths['sandythorns']
                        ]

                    for j in range(0, len(treasure_files)):
                        shutil.copyfile(os.getcwd() + f"/Randomizer/Scenes/Area_Zero_Hidden_Treasure/{pokemons}/{treasure_files[j]}",
                                        os.getcwd() + "/output/romfs/" + treasure_paths[j] + treasure_files[j])

            ChangeScenes.patch_all_legendaries()
            for i in range(13, 38):
                legend_path = {
                    'legend': f"world/scene/parts/event/event_scenario/sub_scenario/s2_sub_0{i}_/"
                }
                HelperFunctions.create_folder_hierarchy(os.getcwd() + '/output/romfs/' + legend_path['legend'])

            legends_scenes = ["Articuno", "Zapdos", "Moltres", "Raikou", "Entei", "Suicune", "Lugia", "Ho-oH",
                              "Latias", "Latios", "Kyogre", "Groundon", "Rayquaza", "Cobalion", "Terrakion",
                              "Virizion", "Reshiram", "Zekrom", "Kyurem", "Solgaleo", "Lunala", "Necrozma",
                              "Kubfu", "Glastier", "Spectier"]
            index = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]

            for legend in range(0, len(legends_scenes)):
                for i in range(0, 1):
                    legend_path = {
                        'legend': f"world/scene/parts/event/event_scenario/sub_scenario/s2_sub_0{index[legend]}_/"
                    }
                    shutil.copyfile(os.getcwd() + f"/Randomizer/Scenes/Legendaries/{legends_scenes[legend]}/s2_sub_0{index[legend]}_pre_start_{i}.trsog",
                                    os.getcwd() + "/output/romfs/" + legend_path['legend'] + f"s2_sub_0{index[legend]}_pre_start_{i}.trsog")

            for treasures in special_legends:
                HelperFunctions.create_folder_hierarchy(os.getcwd() + '/output/romfs/' + special_legends[treasures])
            special_leg = ["Pecharunt", "Meloetta"]

            for specialleg in special_leg:
                leg_files = []
                leg_paths = []
                if specialleg == "Pecharunt":
                    leg_files = [
                        f"s2_side01_0160_always_{i}.trsog",
                        f"s2_side01_0180_always_{i}.trsog"
                    ]
                    leg_paths = [
                        special_legends['pecharunt_1'],
                        special_legends['pecharunt_2']
                    ]
                if specialleg == "Meloetta":
                    leg_files = [
                        f"s2_sub_003_pop_{i}.trscn"
                    ]
                    leg_paths = [
                        special_legends['meloetta'],
                    ]
                for j in range(0, len(leg_files)):
                    shutil.copyfile(
                        os.getcwd() + f"/Randomizer/Scenes/Legendaries/{specialleg}/{leg_files[j]}",
                        os.getcwd() + "/output/romfs/" + leg_paths[j] + leg_files[j])

            ChangeScenes.patch_kora_miraidon()
            HelperFunctions.create_folder_hierarchy(os.getcwd() + '/output/romfs/' + paths['koraidon-miraidon'])
            shutil.copyfile(os.getcwd() + "/Randomizer/Scenes/Koraidon-Miraidon-Catch/sub_018_pre_start_0.trsog",
                            os.getcwd() + "/output/romfs/" + paths['koraidon-miraidon'] + 'sub_018_pre_start_0.trsog')
            shutil.copyfile(os.getcwd() + "/Randomizer/Scenes/Koraidon-Miraidon-Catch/sub_018_pre_start_1.trsog",
                            os.getcwd() + "/output/romfs/" + paths['koraidon-miraidon'] + 'sub_018_pre_start_1.trsog')

            ChangeScenes.patch_misc_pokemon()
            HelperFunctions.create_folder_hierarchy(os.getcwd() + '/output/romfs/' + paths['houndoom'])
            shutil.copyfile(os.getcwd() + "/Randomizer/Scenes/Misc/Houndoom/common_0150_main_0.trsog",
                            os.getcwd() + "/output/romfs/" + paths['houndoom'] + 'common_0150_main_0.trsog')
            shutil.copyfile(os.getcwd() + "/Randomizer/Scenes/Misc/Houndoom/common_0150_main_1.trsog",
                            os.getcwd() + "/output/romfs/" + paths['houndoom'] + 'common_0150_main_1.trsog')

            HelperFunctions.create_folder_hierarchy(os.getcwd() + '/output/romfs/' + paths['sunflora'])
            shutil.copyfile(os.getcwd() + "/Randomizer/Scenes/Misc/Sunflora/pokes_0.trsog",
                            os.getcwd() + "/output/romfs/" + paths['sunflora'] + 'pokes_0.trsog')
            shutil.copyfile(os.getcwd() + "/Randomizer/Scenes/Misc/Sunflora/pokes_1.trsog",
                            os.getcwd() + "/output/romfs/" + paths['sunflora'] + 'pokes_1.trsog')


        print("Randomization Of Static Fights Pokemon Done!")
        return True
    return False


