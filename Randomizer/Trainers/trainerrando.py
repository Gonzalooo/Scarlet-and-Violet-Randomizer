import Randomizer.helper_function as HelperFunctions
import json
import random
import os

# trid == rival_01_hono
# ...._kusa
# ...._mizu
# "trid": "raid_assist_NPC_1->52"
# "trid" : botan - penny
#   - "botan_01" penny fight 1
#   - "botan_02" penny ace_tournament Rematch
#   - "botan_multi" penny AZ
#   - "botan_02_01" Epilogue Multi (Max 3 [Try 6])
#   - "botan_schoolwars" Ace Star - Indigo Disk
# - : chairperson - geeta
#   - "chairperson_01" Geeta - League
#   - "chairperson_02" Geeta - Ace Star
#   - "chairperson_03" Getta - Ace Star Rematch
# - : clavel - clavell
#   - "clavel_01" Clavell - ??? (Unsure)
#   - "clavel_01_hono" Clavell - He has Quaxly
#   - "clavel_01_kusa" Clavell - He has Fuecoco
#   - "clavel_01_mizu" Clavell - He has Sprigatito
#   - "clavel_02_hono" Clavell - He has Quaxly Ace Star
#   - "clavel_02_kusa" Clavell - He has Fuecoco Ace Star
#   - "clavel_02_mizu" Clavell - He has Sprigatito Ace Star
# - : dan_aku_ - Dark Team Star
#   - "dan_aku_01" Dark TS - Outside Fight
#   - "dan_aku_boss_01" Dark TS - Boss (Max is 5)
#   - "dan_aku_boss_02" Dark TS - Boss (Max is 6)
# - : dan_doku_ -  Poison
#   - "dan_doku_01" Poison TS - Outside Fight
#   - "dan_doku_boss_01" (Max is 5)
#   - "dan_doku_boss_02" (Max is 6)
# - : dan_fairy_ - Fairy
#   - "dan_fairy_butler_01" Fairy TS - Outside Fight
#   - "dan_fairy_boss_01" (Max is 5)
#   - "dan_fairy_boss_02" (Max is 6)
# - : dan_hono_ - Fire
#   - "dan_hono_01" Fire TS - Outside Fight
#   - "dan_hono_boss_01" (Max is 5)
#   - "dan_hono_boss_02" (Max is 6)
# - : dan_kakutou - Fighting
#   - "dan_kakutou_01" Fire TS - Outside Fight
#   - "dan_kakutou_boss_01" (Max is 5)
#   - "dan_kakutou_boss_02" (Max is 6)
# - : dan_tr - Tutorial TS
#   - "dan_tr_01" Tutorial TS - Fight 1
#   - "dan_tr_02" Tutorial TS - Fight 2
# - : e4_dragon
#   - "e4_dragon_01" E4 - Dragon - First
#   - "e4_dragon_02" E4 - Dragon - Ace Star
# - : e4_hagane
#   - "e4_hagane_01" E4 - Steel - First
# - : e4_hikou
#   - "e4_hikou_01" E4 - Flying - First
# - : e4_jimen
#   - "e4_jimen_01" E4 - Ground - First
# - : gym_denki
#   - "gym_denki_02" - Electric Trainer
#   - "gym_denki_03" - Electric Trainer
#   - "gym_denki_04" - Electric Trainer
#   - "gym_denki_leader_01" - Leader
#   - "gym_denki_leader_02" - Leader Rematch
# - : gym_esper
#   - "gym_esper_01" - Psychic Trainer
#   - "gym_esper_02" - Psychic Trainer
#   - "gym_esper_leader_01" - Leader
#   - "gym_esper_leader_02" - Leader Rematch
# - : gym_ghost
#   - "gym_ghost_01" - Ghost Trainer
#   - "gym_ghost_02" - Ghost Trainer
#   - "gym_ghost_03" - Ghost Trainer
#   - "gym_ghost_leader_01" - Leader
#   - "gym_ghost_leader_02" - Leader Rematch
# - : gym_koori (Ice)
#   - "gym_koori_leader_01" - Leader
#   - "gym_koori_leader_02" - Leader Rematch
# - : gym_kusa (Grass)
#   - "gym_kusa_leader_01" - Leader
#   - "gym_kusa_leader_02" - Leader Rematch
# - : gym_mizu (Water)
#   - "gym_mizu_01" - Water Trainer
#   - "gym_mizu_leader_01" - Leader
#   - "gym_mizu_leader_02" - Leader Rematch
# - : gym_mushi (Bug)
#   - "gym_mushi_01" - Bug Trainer
#   - "gym_mushi_02" - Bug Trainer
#   - "gym_mushi_03" - Bug Trainer
#   - "gym_mushi_leader_01" - Leader
#   - "gym_mushi_leader_02" - Leader Rematch
# - : gym_normal
#   - "gym_normal_01" - Normal Trainer
#   - "gym_normal_02" - Normal Trainer
#   - "gym_normal_03" - Normal Trainer
#   - "gym_normal_leader_01" - Leader
#   - "gym_normal_leader_02" - Leader Rematch
# - : kihada (Dendra)
#   - "kihada_01" - Ace Star
#   - "kihada_02" - Ace Star Rematch
# - : mimoza (Miriam)
#   - "mimoza_01" - Ace Star
# - : pepper - Arven
#   - "pepper_00" - Lighthouse
#   - "pepper_01" - Lighthouse Final
#   - "pepper_02" - Ace Star
#   - "pepper_03" - Ace Star Rematch
#   - "pepper_multi" - AZ
#   - "pepper_nusi_01" - Titan (No Gem Change)
#   - "pepper_nusi_02" - Titan (No Gem Change)
#   - "pepper_nusi_03" - Titan (No Gem Change)
#   - "pepper_nusi_04" - Titan (No Gem Change)
#   - "pepper_nusi_05" - Titan (No Gem Change)
#   - "pepper_02_01" - Epilogue Multi
#   - "pepper_schoolwars" Ace Star - Indigo Disk
# - : professor_A_01 - Sada
#   - "professor_A_01" - Fight
#   - "professor_A_02" - Koraidon Fight
# - : professor_B_01 - Turo
#   - "professor_B_01" - Fight
#   - "professor_B_02" - Miraidon Fight
# - : rehoru (Raifort)
#   - "rehoru_01" - Ace Star Rematch
# - : richf - O'Nare
#   - "richf_01" - Not Fightable Ignore (O'Nare)
# - : rival - Nemona
    # - : rival_01 (Nemona - cutscene)
    # - : rival_02 (Nemona - cutscene)
    # - : rival_03 (Nemona - cutscene)
    # - : rival_05 (Nemona - cutscene)
    # - : rival_06 (Nemona - cutscene)
    # - : rival_0X_hono (Nemona w/Sprigattito) X [1->8; first 6 are gym, then champion, then Ace Tournament Rematch]
    # - : rival_0X_kusa (Nemona w/Quaxly)
    # - : rival_0X_mizu (Nemona w/ Fuecoco)
    # - : rival_multi_hono (Nemona A0 - Sprigatito)
    # - : rival_multi_kusa (Nemona A0 - Quaxly)
    # - : rival_multi_mizu (Nemona A0 - Fuecoco)
    # - : rival_02_01hono (Nemona Epilogue - Sprigatito)
    # - : rival_02_01kusa (Nemona Epilogue - Quaxly)
    # - : rival_02_01mizu (Nemona Epilogue - Fuecoco)
    # - : rival_schoolwars_hono (Nemona Ace - Epilogue - Sprigatito)
    # - : rival_schoolwars_kusa (Nemona Ace - Epilogue - Quaxly)
    # - : rival_schoolwars_mizu (Nemona Ace - Epilogue - Fuecoco)
# - : sawaro (Saguaro)
#   - "sawaro_01" - Ace Star Rematch
# - : seizi (Salvatore)
#   - "seizi_01" - Ace Star Rematch
# - : strong_01 (Garchomp - Ignore)
# ---------------DLC 1 Starts here---------------
# - : Brother (Kieran - SU1)
#   - "brother_01_01" - First Battle - Not Complete
#   - "brother_01_01_strong" - First Battle - Complete
#   - "brother_01_02" - Second Battle - Not Complete
#   - "brother_01_02_strong" - Second Battle - Complete
#   - "brother_01_03" - Third Battle - Not Complete
#   - "brother_01_03_strong" - Third Battle - Complete
#   - "brother_01_04" - Fourth Battle - Not Complete - Loyalty Plaza
#   - "brother_01_04_strong" - Fourth Battle - Complete - Loyalty Plaza
#   - "brother_01_05" - Fourth Battle - Not Complete - Fight For Ogerpon
#   - "brother_01_05_strong" - Fourth Battle - Complete - Fight For Ogerpon
#   - "brother_02_01" - DLC Champion Fight
#   - "brother_02_02" - Terapagos Fight (Ignore)
#   - "brother_kodaigame" - Multi Terapagos
#   - "s2_side_brother" - Multi Epilogue
# - : Camera (Perrin)
#   - "camera_01_01" - Fight
# - : serebu (O'Nare)
#   - "serebu_01" - First Fight
#   - "serebu_01" - Second Fight
# - : O'Nare Wife
#   - "serevy_03" - First Fight
# - : sister (Carmine)
#   - "sister_01_01" - First Fight - Not Complete
#   - "sister_01_01_strong" - First Fight - Complete
#   - "sister_01_02" - Second Fight - Not Complete
#   - "sister_01_02_strong" - Second Fight - Complete
#   - "sister_01_03" - Third Fight - Not Complete
#   - "sister_01_03_strong" - Third Fight - Complete
#   - "sister_muruchi_01" - Multi (Milotic) - Not Complete
#   - "sister_muruchi_01_strong" - Multi (Milotic) - Complete
#   - "sister_onitaizi" - Multi (Titan Legend) - Not Complete
#   - "sister_onitaizi_strong" - Multi (Titan Legend) - Complete
#   - "sister_02_01" - Aquarium Fight
#   - "sister_02_02" - Terapagos Multi
# - : sp_trainer (Ogre Clan)
#   - "sp_trainer_0X" - Ogre Member (X = 1->7)
#   - "sp_trainer_boss" - Ogre Boss
# ---------------DLC 2 Starts here---------------
# - : dragon4 (BB4)
#   - "dragon4_02_01" - BB Dragon Fight
# - : dragonchallenge
#   - "dragonchallenge_01" - BB Dragon Challenge
#   - "dragonchallenge_02" - BB Dragon Challenge
#   - "dragonchallenge_03" - BB Dragon Challenge
# - : fairy4
#   - "fairy4_02_01" - School Yard Fight
#   - "fairy4_02_01" - BB Fairy Fight
# - : fairychallenge
#   - "fairychallenge_0X" - BB Fairy Challenge [X = 1->5]
# - : s2_side_grandfather - Epilogue
# - : s2_side_grandmother - Epilogue
# - : hagane4
#   - "hagane4_02_01" - BB Steel Fight
# - : hono4
#   - "hono4_02_01" - BB Fire Fight
# - : honochallenge
#   - "honochallenge_01" - BB Fire Challenge
#   - "honochallenge_02" - BB Fire Challenge
#   - "honochallenge_03" - BB Fire Challenge
# - : shiano (Citrano)
#   - "shiano" - BBLeauge Fight
# - : su2_bukatu (bbleauge)
#   - "su2_bukatu_akamatu" - Crispin
#   - "su2_bukatu_botan" - Penny (Also Ace Star)
#   - "su2_bukatu_claver_honoo" - Clavell with Quaxly
#   - "su2_bukatu_claver_kusa" - Clavell with Fuecoco
#   - "su2_bukatu_claver_mizu" - Clavell with Sprigatito
#   - "su2_bukatu_denki" - Electric Leader
#   - "su2_bukatu_doragon" - Dragon E4
#   - "su2_bukatu_esper" - Psychic Leader
#   - "su2_bukatu_ghost" - Ghost Leader
#   - "su2_bukatu_hagane" - Steel E4
#   - "su2_bukatu_hikou" - Normal Leader
#   - "su2_bukatu_kakitubata" - Dragon BBE4
#   - "su2_bukatu_kihada" - Dendra
#   - "su2_bukatu_Koori" - Grusha
#   - "su2_bukatu_kusa" - Braissius
#   - "su2_bukatu_mimoza" - Miriam
#   - "su2_bukatu_mizu" - Kofu
#   - "su2_bukatu_mushi" - Katy
#   - "su2_bukatu_nemo_honoo" - Nemona w/Sprigatito
#   - "su2_bukatu_nemo_kusa"  - Nemona w/Quaxly
#   - "su2_bukatu_nemo_mizu"  - Nemona w/Fuecoco
#   - "su2_bukatu_nerine" - Steel BBE4
#   - "su2_bukatu_omodaka" - Geeta
#   - "su2_bukatu_pepa" - Arven
#   - "su2_bukatu_rehool" - Raifort
#   - "su2_bukatu_sawaro" - Saguaro
#   - "su2_bukatu_seizi" - Salvatore
#   - "su2_bukatu_suguri" - Kieran
#   - "su2_bukatu_taro" - Lacey
#   - "su2_bukatu_time" - Tyme
#   - "su2_bukatu_zeiyu" - Carmine
#   - "su2_bukatu_zimen" - Rika
#   - "su2_bukatu_zinia" - Jacq
# - : s2_side_villager01
# - : s2_side_villager02
# - : taimu (Ryme)
#   - "taimu_01" - Star Ace Rematch
# - : zinia (Bio Teacher)
#   - "zinia_01" - Star Ace
#   - "zinia_02" - Star Ace Rematch
# botan_01 has index [356]
# botan_02 has index [357]
# botan_multi has index [358]
# botan_02_01 has index [677]
# botan_schoolwars has index [678]
# chairperson_01 has index [359]
# chairperson_02 has index [360]
# chairperson_03 has index [361]
# clavel_01 has index [362]
# clavel_01_hono has index [363]
# clavel_01_kusa has index [364]
# clavel_01_mizu has index [365]
# clavel_02_hono has index [366]
# clavel_02_kusa has index [367]
# clavel_02_mizu has index [368]
# dan_aku_01 has index [369]
# dan_aku_boss_01 has index [370]
# dan_aku_boss_02 has index [371]
# dan_doku_01 has index [372]
# dan_doku_boss_01 has index [373]
# dan_doku_boss_02 has index [374]
# dan_fairy_butler_01 has index [377]
# dan_fairy_boss_01 has index [375]
# dan_fairy_boss_02 has index [376]
# dan_hono_01 has index [378]
# dan_hono_boss_01 has index [379]
# dan_hono_boss_02 has index [380]
# dan_kakutou_01 has index [381]
# dan_kakutou_boss_01 has index [382]
# dan_kakutou_boss_02 has index [383]
# dan_tr_01 has index [384]
# dan_tr_02 has index [385]
# e4_dragon_01 has index [386]
# e4_dragon_02 has index [387]
# e4_hagane_01 has index [388]
# e4_hikou_01 has index [389]
# e4_jimen_01 has index [390]
# gym_denki_01 has index [391]
# gym_denki_02 has index [392]
# gym_denki_03 has index [393]
# gym_denki_04 has index [394]
# gym_denki_leader_01 has index [395]
# gym_denki_leader_02 has index [396]
# gym_esper_01 has index [397]
# gym_esper_02 has index [398]
# gym_esper_leader_01 has index [399]
# gym_esper_leader_02 has index [400]
# gym_ghost_01 has index [401]
# gym_ghost_02 has index [402]
# gym_ghost_03 has index [403]
# gym_ghost_leader_01 has index [404]
# gym_ghost_leader_02 has index [405]
# gym_koori_leader_01 has index [406]
# gym_koori_leader_02 has index [407]
# gym_kusa_leader_01 has index [408]
# gym_kusa_leader_02 has index [409]
# gym_mizu_01 has index [410]
# gym_mizu_leader_01 has index [411]
# gym_mizu_leader_02 has index [412]
# gym_mushi_01 has index [413]
# gym_mushi_02 has index [414]
# gym_mushi_03 has index [415]
# gym_mushi_leader_01 has index [416]
# gym_mushi_leader_02 has index [417]
# gym_normal_01 has index [418]
# gym_normal_02 has index [419]
# gym_normal_03 has index [420]
# gym_normal_leader_01 has index [421]
# gym_normal_leader_02 has index [422]
# kihada_01 has index [423] - Not randomized
# kihada_02 has index [424] - Not randomized
# mimoza_01 has index [425] - Not randomized
# pepper_00 has index [426]
# pepper_01 has index [427]
# pepper_02 has index [428]
# pepper_03 has index [429]
# pepper_multi has index [430]
# pepper_nusi_01 has index [431] - Not randomized
# pepper_nusi_02 has index [432] - Not randomized
# pepper_nusi_03 has index [433] - Not randomized
# pepper_nusi_04 has index [434] - Not randomized
# pepper_nusi_05 has index [435] - Not randomized
# pepper_02_01 has index [701]
# pepper_schoolwars has index [702]
# professor_A_01 has index [436]
# professor_A_02 has index [437] - Not randomized
# professor_B_01 has index [438]
# professor_B_02 has index [439] - Not randomized
# rehoru_01 has index [492] - Not randomized
# richf_01 has index [493] - Not randomized
# rival_01 has index [494]
# rival_02 has index [498]
# rival_03 has index [502]
# rival_05 has index [509]
# rival_06 has index [513]
# rival_01_hono has index [495]
# rival_02_hono has index [499]
# rival_03_hono has index [503]
# rival_04_hono has index [506]
# rival_05_hono has index [510]
# rival_06_hono has index [514]
# rival_07_hono has index [517]
# rival_08_hono has index [520]
# rival_01_kusa has index [496]
# rival_02_kusa has index [500]
# rival_03_kusa has index [504]
# rival_04_kusa has index [507]
# rival_05_kusa has index [511]
# rival_06_kusa has index [515]
# rival_07_kusa has index [518]
# rival_08_kusa has index [521]
# rival_01_mizu has index [497]
# rival_02_mizu has index [501]
# rival_03_mizu has index [505]
# rival_04_mizu has index [508]
# rival_05_mizu has index [512]
# rival_06_mizu has index [516]
# rival_07_mizu has index [519]
# rival_08_mizu has index [522]
# rival_multi_hono has index [523]
# rival_multi_kusa has index [524]
# rival_multi_mizu has index [525]
# rival_02_01hono has index [703]
# rival_02_01kusa has index [704]
# rival_02_01mizu has index [705]
# rival_schoolwars_hono has index [706]
# rival_schoolwars_kusa has index [707]
# rival_schoolwars_mizu has index [708]
# sawaro_01 has index [526]  - Not randomized
# seizi_01 has index [527] - Not randomized
# strong_01 has index [528] - Not randomized
# brother_01_01 has index [585]
# brother_01_02 has index [587]
# brother_01_03 has index [589]
# brother_01_04 has index [591]
# brother_01_05 has index [593]
# brother_01_01_strong has index [586]
# brother_01_02_strong has index [588]
# brother_01_03_strong has index [590]
# brother_01_04_strong has index [592]
# brother_01_05_strong has index [594]
# brother_02_01 has index [679]
# brother_02_02 has index [680] - Not Randomized
# brother_kodaigame has index [681]
# s2_side_brother has index [682]
# camera_01_01 has index [595] - Not Randomized
# serebu_01 has index [596] - Not Randomized
# serebu_01 has index [596] - Not Randomized
# serevy_03 has index [598] - Not Randomized
# sister_01_01 has index [599]
# sister_01_02 has index [601]
# sister_01_03 has index [603]
# sister_01_01_strong has index [600]
# sister_01_02_strong has index [602]
# sister_01_03_strong has index [604]
# sister_muruchi_01 has index [605]
# sister_muruchi_01_strong has index [606]
# sister_onitaizi has index [607]
# sister_onitaizi_strong has index [608]
# sister_02_01 has index [710]
# sister_02_02 has index [711]
# sp_trainer_01 has index [609]
# sp_trainer_02 has index [610]
# sp_trainer_03 has index [611]
# sp_trainer_04 has index [612]
# sp_trainer_05 has index [613]
# sp_trainer_06 has index [614]
# sp_trainer_07 has index [615]
# sp_trainer_boss has index [616]
# dragon4_02_01 has index [683]
# dragonchallenge_01 has index [684]
# dragonchallenge_02 has index [685]
# dragonchallenge_03 has index [686]
# fairy4_02_01 has index [687]
# fairy4_02_02 has index [688]
# fairychallenge_01 has index [689]
# fairychallenge_02 has index [690]
# fairychallenge_03 has index [691]
# fairychallenge_04 has index [692]
# fairychallenge_05 has index [693]
# s2_side_grandfather has index [694]
# s2_side_grandmother has index [695]
# hagane4_02_01 has index [696]
# hono4_02_01 has index [697]
# honochallenge_01 has index [698]
# honochallenge_02 has index [699]
# honochallenge_03 has index [700]
# shiano has index [709]
# su2_bukatu_akamatu has index [712]
# su2_bukatu_botan has index [713]
# su2_bukatu_claver_honoo has index [714]
# su2_bukatu_claver_kusa has index [715]
# su2_bukatu_claver_mizu has index [716]
# su2_bukatu_denki has index [717]
# su2_bukatu_doragon has index [718]
# su2_bukatu_esper has index [719]
# su2_bukatu_ghost has index [720]
# su2_bukatu_hagane has index [721]
# su2_bukatu_hikou has index [722]
# su2_bukatu_kakitubata has index [723]
# su2_bukatu_kihada has index [724]
# su2_bukatu_Koori has index [725]
# su2_bukatu_kusa has index [726]
# su2_bukatu_mimoza has index [727]
# su2_bukatu_mizu has index [728]
# su2_bukatu_mushi has index [729]
# su2_bukatu_nemo_honoo has index [730]
# su2_bukatu_nemo_kusa has index [731]
# su2_bukatu_nemo_mizu has index [732]
# su2_bukatu_nerine has index [733]
# su2_bukatu_omodaka has index [734]
# su2_bukatu_pepa has index [735]
# su2_bukatu_rehool has index [736]
# su2_bukatu_sawaro has index [737]
# su2_bukatu_seizi has index [738]
# su2_bukatu_suguri has index [739]
# su2_bukatu_taro has index [740]
# su2_bukatu_time has index [741]
# su2_bukatu_zeiyu has index [742]
# su2_bukatu_zimen has index [743]
# su2_bukatu_zinia has index [744]
# s2_side_villager01 has index [745]
# s2_side_villager02 has index [746]
# taimu_01 has index [747]
# zinia_01 has index [754]
# zinia_02 has index [755]
# NOTE: Ace Tournament and BBLeague Share Pokemon Teams


def make_poke():
    pass


def randomize_penny():
    return [356, 357, 358, 677, 678]


def randomize_geeta():
    return [359, 360, 361]


def randomize_clavell():
    return [362, 363, 364, 365, 366, 367, 368]


def randomize_team_star():
    return [369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385]


def randomize_e4_paldea():
    return [386, 387, 388, 389, 390, 392]


def randomize_gym():
    return [391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411,
            412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422]


def randomize_professors():
    return [436, 438]


def randomize_arven():
    return [426, 427, 428, 429, 430, 701, 702]


def randomize_nemona():
    return [
        494, 498, 502, 509, 513,  # rival_01 to rival_06
        495, 499, 503, 506, 510, 514, 517, 520,  # rival_01_hono to rival_08_hono
        496, 500, 504, 507, 511, 515, 518, 521,  # rival_01_kusa to rival_08_kusa
        497, 501, 505, 508, 512, 516, 519, 522,  # rival_01_mizu to rival_08_mizu
        523, 524, 525,  # rival_multi_hono to rival_multi_mizu
        703, 704, 705,  # rival_02_01hono to rival_02_01mizu
        706, 707, 708  # rival_schoolwars_hono to rival_schoolwars_mizu
    ]


def randomize_kieran_su1():
    return [585, 587, 589, 591, 593, 586, 588, 590, 592, 594]


def randomize_kieran_su2():
    return [679, 681, 682]


def randomize_carmine_su1():
    return [599, 601, 603, 600, 602, 604, 605, 606, 607, 608]


def randomize_carmine_su2():
    return [710, 711]


def randomize_ogre_clan():
    return [609, 610, 611, 612, 613, 614, 615, 616]


def randomize_trainers(config):
    if config['trainers_randomizer']['is_enabled'] == "yes" and config['use_paldea_settings_for_all'] == "yes":
        file = open(os.getcwd() + "/Randomizer/Trainers/" +"trdata_array_clean.json", "r")
        data = json.load(file)
        allowed_pokemon, allowed_legends, bpl = HelperFunctions.check_generation_limiter(
                                                config['all_trainers_settings']['generation_limiter'])

        # for entry in data['values']:
        #     if config['only_randomize_important_trainers'] == "yes":
        #         if checkTrainerImportance(entry) is False:
        #             continue
        #
        #     if entry['trainerType'] == "su2_brother_kodaigame":
        #         continue
        #     elif entry['trid'] == "professor_A_02":
        #         continue
        #     elif entry['trid'] == "professor_B_02":
        #         continue
        #     # Counter to see how many pokemon there are to randomize originally
        #     counter = 0
        #     for j in range(0, 6):
        #         t = j+1
        #         if entry['poke' + str(t)]['devId'] != "DEV_NULL":
        #             counter = counter + 1
        #     pokemon_to_randomize = counter
        #
        #     if config['give_trainers_extra_mons'] == "yes":
        #         new_counter = 1
        #         # Counter to see how many free slots there are
        #         for j in range(2, 6):
        #             if entry['poke' + str(j)]['devId'] == "DEV_NULL":
        #                 new_counter = new_counter + 1
        #         # If none then just randomize all 6
        #         if new_counter == 0:
        #             pokemon_to_randomize = 6
        #         else:
        #             # if some then choose a random number between 1 and itself
        #             pokemon_to_randomize = random.randint(1, new_counter)
        #             pokemon_to_randomize = pokemon_to_randomize + counter
        #             if pokemon_to_randomize > 6:
        #                 pokemon_to_randomize = 6
        #     if config['force_6_pokemons_on_trainers'] == "yes":
        #         # If user wants all 6 then set to all 6
        #         pokemon_to_randomize = 6
        #
        #     # a way to prevent any errors
        #     beginner = False
        #     if pokemon_to_randomize > 6:
        #         pokemon_to_randomize = 6
        #     elif pokemon_to_randomize < 1:
        #         # get exact number if its less than 1 (should never happen)
        #         counter = 1
        #         for j in range(0, 6):
        #             t = j + 1
        #             if entry['poke' + str(t)]['devId'] != "DEV_NULL":
        #                 counter = counter + 1
        #         pokemon_to_randomize = counter
        #     temp_legends = config['only_legends']
        #     temp_paradox = config['only_paradox']
        #     temp_both = config['only_legends_and_paradoxes']
        #     if checkTrainerImportance(entry) == "raid":
        #         if config['tera_raid_trainers_only_legends'] == "yes":
        #             config['only_legends'] = "yes"
        #         if config['tera_raid_trainers_only_paradox'] == "yes":
        #             config['only_paradox'] = "yes"
        #         if config['tera_raid_trainers_only_both'] == "yes":
        #             config['only_legends_and_paradoxes'] = "yes"
        #     elif checkTrainerImportance(entry) is True:
        #         if config["force_important_trainers_to6_pokemon"] == "yes":
        #             pokemon_to_randomize = 6
        #         if config['impo_trainers_only_legends'] == "yes":
        #             config['only_legends'] = "yes"
        #         if config['impo_trainers_only_paradox'] == "yes":
        #             config['only_paradox'] = "yes"
        #         if config['impo_trainers_only_both'] == "yes":
        #             config['only_legends_and_paradoxes'] = "yes"
        #     if entry['trid'] == "rival_01_hono" or entry['trid'] == "rival_01_kusa" or entry['trid'] == "rival_01_mizu":
        #         pokemon_to_randomize = 1
        #         beginner = True
        #
        #     i = 1
        #     while i <= pokemon_to_randomize:
        #         make_poke(entry, str(i), csvdata, config, beginner)
        #         i = i + 1
        #     config['only_legends'] = temp_legends
        #     config['only_paradox'] = temp_paradox
        #     config['only_legends_and_paradoxes'] = temp_both
        #
        #     if config['make_ai_smart_for_all_trainers'] == "yes" and beginner is False:
        #         entry['aiBasic'] = True
        #         entry['aiHigh'] = True
        #         entry['aiExpert'] = True
        #         entry['aiChange'] = True
        #     if config['allow_all_trainers_to_terastalize'] == "yes" and beginner is False:
        #         entry['changeGem'] = True
        #     if "raid_assist_NPC" not in entry['trid']:
        #         if config['randomnly_choose_single_or_double'] == "yes" and beginner is False:
        #             battleformat = random.randint(1, 2)
        #             if battleformat == 2 and pokemon_to_randomize < 2:
        #                 make_poke(entry, str(2), csvdata, config, beginner)
        #             if battleformat == 2:
        #                 entry['aiDouble'] = True
        #             type_of_battle = f"_{battleformat}vs{battleformat}"
        #             entry['battleType'] = type_of_battle
        #         if config['only_double'] == "yes" and beginner is False:
        #             entry['battleType'] = "_2vs2"
        #             entry['aiDouble'] = True
        #             if pokemon_to_randomize < 2:
        #                 make_poke(entry, str(2), csvdata, config, beginner)

        outdata = json.dumps(data, indent=4)
        with open(os.getcwd() + "/Randomizer/Trainers/" +"trdata_array.json", 'w') as outfile:
            outfile.write(outdata)
        print("Randomization of Trainers done !")
        return True
    return False

