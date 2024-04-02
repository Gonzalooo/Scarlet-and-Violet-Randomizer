import json
import random
import os
import Randomizer.shared_Variables as SharedVariables
import Randomizer.helper_function as HelperFunctions


def make_static_legendary_available_to_all():
    pass


def randomize_specific_fight(pokedata, allowed_pokemon: list):
    pass


def randomize_static_fights(config):
    make_static_legendary_available_to_all()
    if config['is_enabled'] == "yes":
        file = open('eventBattlePokemon_array_clean.json', 'r')
        file_json = json.load(file)
        file.close()
        # Mappings for later features
        # area0 - 0->10 (1075_multi, 1055_multi_, 1095_multi_, 1180_multi_)
        # gimmighoul - 11->23 (coin_976_01 ... _05 and then inc of 5)
        # lechonk -> 24 (common_0100_)
        # Cave_Houndoom -> 25 (common_0150-)
        # gym_sunfloras -> 26-30 (gym_kusa_020_KIMAWARI_0X)
        # Koraidon -> 31 (lastbattle_AIGUANA)
        # Miraidon -> 32 (lastbattle_BIGUANA)
        # Dondozo_Titan -> 33/34 (nusi_931)
        # Orthworm_Titan -> 35/36 (nusi_944)
        # TATSUGIRI_Titan -> 37 (nusi_952_0X)
        # Tatsugiri_titan_fake -> 38-40 (nusi_952_dummy)
        # Bombardier_Titan -> 41-42 (nusi_959)
        # Klawf_Titan -> 43-44 (nusi_962)
        # Great_Tusk -> 45-46 (nusi_978)
        # Iron Treads -> 47-48 (nusi_986)
        # Ting-Lu -> 49 (semi_legend_994)
        # Chien-Pao -> 50 (semi_legend_995)
        # Wo-Chien -> 51 (semi_legend_996)
        # Chi-Yu -> 52 (semi_legend_997
        # Monkidori (cave-fight) -> 53/54 (sdc01_dokuzaru)
        # Okidogi  -> 55 (SDC01_get_dokuinu)
        # Fezandipiti -> 56 (SDC01_get_dokuinu)
        # Monkidori  -> 57 (SDC01_get_dkuzaru)
        # Ogerpon-fire (Titan) -> 58/59 (SDC01_kamenoni_1)
        # Ogerpon-teal (Titan) -> 60/61 (SDC01_kamenoni_2)
        # Ogerpon-rock (Titan) -> 62/63 (SDC01_kamenoni_3)
        # Ogerpon-water (Titan) -> 64/65 (SDC01_kamenoni_4)
        # Milotic -> 66/67 (SDC01_midoriikenushi)
        # Okidogi (titan) -> 68/69) (SDC01_onitaizi_dokuinu)
        # Fezandipiti (titan) -> 70/71 (SDC01_onitaizi_bird)
        # Monkidori (titan) -> 72/73 (SDC01_onitaizi_monkey)
        # Ariados (Bloodmoon) -> 74 (S1_SIDE02_ariados)
        # Ursaluna (Bloodmoon) -> 75 (S1_SIDE02_himeguma3B)
        # Gouging Fire -> 76 (SDC02_sub_Aentei)
        # Raging Bolt -> 77 (SDC02_sub_Araikou)
        # Area Zero - Garchomp -> 78 (SDC02_area0_gaburiasu)
        # Area Zero - Glimmora -> 79 (SDC02_area0_kirafuroru)
        # Area Zero - Noivern -> 80 (SDC02_area0_onbaan)
        # Area Zero - Garganacl -> 81 (SDC02_area0_sio)
        # Area Zero - Sandy Shocks - > 82 (SDC02_area0_sunanokegawa)
        # Area Zero - Iron Thorns -> 83 (SDC02_area0_tetunoibara)
        # Iron Crown -> 84 (SDC02_sub_Bkobaruon)
        # Iron Boulder -> 85 (SDC02_sub_Bterakion)
        # Pecharunt -> 86 (su2_dokutarou)
        # Terapagos - Kieran -> 87 (SDC02_0310_kodaikame)
        # Terapagos - Stellar -> 88 (SDC02_0330_kodaikame)
        # 90+ Other Legends in the Game.

        allowed_pokemon, allowed_legends = HelperFunctions.check_generation_limiter(config['generation_limiter'])
        if config['randomize_all'] == "yes":
            for i in range(0, len(file_json)):
                randomize_specific_fight(file_json['values'][i], allowed_pokemon)
        else:
            if config['randomize_lechonk'] == "yes":
                randomize_specific_fight(file_json['values'][0], allowed_pokemon)

