import Randomizer.helper_function as HelperFunctions
import Randomizer.shared_Variables as SharedVariables
import json
import random
import os
import math

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
#   - "serebu_02" - Second Fight
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
# kihada_01 has index [423]
# kihada_02 has index [424]
# mimoza_01 has index [425]
# pepper_00 has index [426]
# pepper_01 has index [427]
# pepper_02 has index [428]
# pepper_03 has index [429]
# pepper_multi has index [430]
# pepper_nusi_01 has index [431]
# pepper_nusi_02 has index [432]
# pepper_nusi_03 has index [433]
# pepper_nusi_04 has index [434]
# pepper_nusi_05 has index [435]
# pepper_02_01 has index [701]
# pepper_schoolwars has index [702]
# professor_A_01 has index [436]
# professor_A_02 has index [437]
# professor_B_01 has index [438]
# professor_B_02 has index [439]
# rehoru_01 has index [492]
# richf_01 has index [493] - Not fightable
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
# sawaro_01 has index [526]
# seizi_01 has index [527]
# strong_01 has index [528] - Not fightable
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
# brother_02_02 has index [680]
# brother_kodaigame has index [681]
# s2_side_brother has index [682]
# camera_01_01 has index [595]
# serebu_01 has index [596]
# serebu_02 has index [597]
# serevy_03 has index [598]
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


def randomize_penny():
    return [356, 357, 358, 677, 678]


def randomize_geeta():
    return [359, 360, 361]


def randomize_clavell():
    return [362, 363, 364, 365, 366, 367, 368]


def randomize_team_star():
    return [369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385]


def randomize_e4_paldea():
    return [386, 387, 388, 389, 390]


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


def randomize_bb_e4():
    return [683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700]


def randomize_bb_league():
    return [709, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731,
            732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746]


def randomize_school_professors():
    return [423, 424, 425, 492, 526, 527, 747, 754, 755]


def randomize_professor_dragon():
    return [437, 439]


def randomize_arven_titan():
    return [431, 432, 433, 434, 435]


def randomize_kieran_terapagos():
    return [680]


def randomize_perrin():
    return [595]


def randomize_billy_onare():
    return [596, 597, 598]


def count_missing_pokemon(trainer_to_check):
    missing = 0
    not_missing = 1
    for i in range(1, 7):
        if trainer_to_check[f"poke{str(i)}"]["devId"] == "DEV_NULL":
            missing += 1
        else:
            not_missing += 1
    return not_missing, missing


def get_pokemon_based_on_starter(starter: dict, trainer_name: str):
    if trainer_name == "Nemona":
        if "hono" in starter['trid']:
            # Gets sprigatito
            pokemon = SharedVariables.current_starters_selected["kusa"]['id']
            form = SharedVariables.current_starters_selected["kusa"]['form']
            item = HelperFunctions.get_pokemon_item_form(pokemon, form)[0]
            return pokemon, form, item
        if "kusa" in starter['trid']:
            # Gets Quaxly
            pokemon = SharedVariables.current_starters_selected["mizu"]['id']
            form = SharedVariables.current_starters_selected["mizu"]['form']
            item = HelperFunctions.get_pokemon_item_form(pokemon, form)[0]
            return pokemon, form, item
        if "mizu" in starter['trid']:
            # Gets Fuecoco
            pokemon = SharedVariables.current_starters_selected["hono"]['id']
            form = SharedVariables.current_starters_selected["hono"]['form']
            item = HelperFunctions.get_pokemon_item_form(pokemon, form)[0]
            return pokemon, form, item
    if trainer_name == "Clavell":
        if "hono" in starter['trid']:
            # Gets Quaxly
            pokemon = SharedVariables.current_starters_selected["mizu"]['id']
            form = SharedVariables.current_starters_selected["mizu"]['form']
            item = HelperFunctions.get_pokemon_item_form(pokemon, form)[0]
            return pokemon, form, item
        if "kusa" in starter['trid']:
            # Gets Fuecoco
            pokemon = SharedVariables.current_starters_selected["hono"]['id']
            form = SharedVariables.current_starters_selected["hono"]['form']
            item = HelperFunctions.get_pokemon_item_form(pokemon, form)[0]
            return pokemon, form, item
        if "mizu" in starter['trid']:
            # Gets Sprigatito
            pokemon = SharedVariables.current_starters_selected["kusa"]['id']
            form = SharedVariables.current_starters_selected["kusa"]['form']
            item = HelperFunctions.get_pokemon_item_form(pokemon, form)[0]
            return pokemon, form, item

    pokemon = random.randint(1, 1025)
    while pokemon in SharedVariables.banned_pokemon:
        pokemon = random.randint(1, 1025)
    form = 0
    item = "ITEMID_NONE"
    return pokemon, form, item

#allowed_pokemon, banned_pokes,list_to_check, data['values'])
def make_poke(config, trainer_config, allowed_pokemon, banned_stages, trainer_list, trainers, spoiler=None):
    for i in trainer_list:
        # Change Tera
        try:
            if trainer_config['all_trainers_settings']['allow_terastalize_to_all'] == "yes":
                trainers[i]["changeGem"] = True
            elif config['allow_terastalization'] == "yes":
                trainers[i]["changeGem"] = True
        except KeyError:
            if trainer_config['all_trainers_settings']['allow_terastalize_to_all'] == "yes":
                trainers[i]["changeGem"] = True
        # Change Fight Type
        doubles = False
        if (trainer_config['all_trainers_settings']['randomnly_choose_single_or_doubles'] == "yes" and
                i not in SharedVariables.raid_npc_index and
            i not in SharedVariables.multi_battles_index):
            fight_choice = random.randint(1, 2)
            trainers[i]["battleType"] = f"_{fight_choice}vs{fight_choice}"
            if fight_choice == 2:
                trainers[i]['aiDouble'] = True
                doubles = True
        elif (trainer_config['all_trainers_settings']['only_double_battles'] == "yes" and
              i not in SharedVariables.raid_npc_index and i not in SharedVariables.raid_npc_index and
            i not in SharedVariables.multi_battles_index):
            trainers[i]["battleType"] = f"_2vs2"
            trainers[i]['aiDouble'] = True
            doubles = True
        # Checks for amount of pokemon to randomize
        max_amount, ignore = count_missing_pokemon(trainers[i])
        try:
            if config['force_6_pokemon'] == "yes":
                max_amount = 7
            elif config['add_extra_pokemon'] == "yes":
                present, not_present = count_missing_pokemon(trainers[i])
                if not_present == 0:
                    max_amount = 7
                else:
                    trainers_selection = random.randint(1, not_present)
                    max_amount = present + trainers_selection + 1
                    if max_amount > 7:
                        max_amount = 7
        except KeyError:
            pass

        if doubles is True and max_amount < 3:
            max_amount = 3

        # Hard Code Rival Fight to always only have 1 pokemon - Single and No Tera
        if (trainers[i]['trid'] == "rival_01_hono" or trainers[i]['trid'] == "rival_01_kusa"
                or trainers[i]['trid'] == "rival_01_mizu"):
            max_amount = 2
            trainers[i]["battleType"] = f"_1vs1"
            trainers[i]["changeGem"] = False
            trainers[i]['aiDouble'] = False

        if spoiler:
            spoiler.write('\n\n--------------------\n'+trainers[i]['trid']+'\n--------------------\n')
            spoiler.write('Mon Count: '+str(max_amount-1))
            spoiler.write(' Can tera: '+str(trainers[i]["changeGem"]))
            spoiler.write(' Doubles: '+str(doubles)+'\n')
        highest_lvl = 1
        for j in range(1, max_amount):

            pokemon_choice = random.randint(1, 1025)
            while (pokemon_choice in SharedVariables.banned_pokemon or pokemon_choice not in allowed_pokemon
                    or pokemon_choice in banned_stages):
                pokemon_choice = random.randint(1, 1025)
            form_choice = HelperFunctions.get_alternate_form(pokemon_choice)
            item_choice = HelperFunctions.get_pokemon_item_form(pokemon_choice, form_choice)[0]
            if j == max_amount-1 and i in randomize_nemona():
                pokemon_choice, form_choice, item_choice = get_pokemon_based_on_starter(trainers[i], "Nemona")
                trainers[i][f"poke{str(j)}"]["devId"] = HelperFunctions.fetch_developer_name(pokemon_choice)
                trainers[i][f"poke{str(j)}"]["formId"] = form_choice
                trainers[i][f"poke{str(j)}"]["item"] = item_choice
            elif j == max_amount-1 and i in randomize_clavell():
                pokemon_choice, form_choice, item_choice = get_pokemon_based_on_starter(trainers[i], "Clavell")
                trainers[i][f"poke{str(j)}"]["devId"] = HelperFunctions.fetch_developer_name(pokemon_choice)
                trainers[i][f"poke{str(j)}"]["formId"] = form_choice
                trainers[i][f"poke{str(j)}"]["item"] = item_choice
            else:
                trainers[i][f"poke{str(j)}"]["devId"] = HelperFunctions.fetch_developer_name(pokemon_choice)
                trainers[i][f"poke{str(j)}"]["formId"] = form_choice
                trainers[i][f"poke{str(j)}"]["item"] = item_choice

            if trainers[i][f"poke{str(j)}"]["level"] == 0:
                trainers[i][f"poke{str(j)}"]["level"] = highest_lvl
            else:
                if trainer_config['all_trainers_settings']['boostlevels'] == "yes":
                    trainers[i][f"poke{str(j)}"]["level"] = get_boosted_level(trainers[i][f"poke{str(j)}"]["level"], trainer_config['all_trainers_settings'])
            #store highest lvl mon trainer has to use for extras added
            if trainers[i][f"poke{str(j)}"]["level"] > highest_lvl:
                highest_lvl = trainers[i][f"poke{str(j)}"]["level"]
            trainers[i][f"poke{str(j)}"]["wazaType"] = "DEFAULT"

            for k in range(1, 5):
                trainers[i][f"poke{str(j)}"][f"waza{str(k)}"]['wazaId'] = "WAZA_NULL"

            if trainer_config['all_trainers_settings']['randomize_tera_types'] == "yes":
                trainers[i][f"poke{str(j)}"]["gemType"] = HelperFunctions.choose_tera_type(pokemon_choice, form_choice)

            trainers[i][f"poke{str(j)}"]["tokusei"] = "RANDOM_12"

            # Changes to IV
            if config['force_perfect_ivs']:
                trainers[i][f"poke{str(j)}"]["talentType"] = "VALUE"
                IVs = {
                    "hp": 31,
                    "atk": 31,
                    "def": 31,
                    "spAtk": 31,
                    "spDef": 31,
                    "agi": 31
                }
                trainers[i][f"poke{str(j)}"]["talentValue"] = IVs

            # Changes to shinyness
            shiny = 0
            if trainer_config['all_trainers_settings']['allow_shiny_pokemon'] == "yes":
                shiny = random.randint(1, SharedVariables.boostedshiny)
                if shiny == 1:
                    trainers[i][f"poke{str(j)}"]["rareType"] = "RARE"
                    
            if spoiler:
                spoiler.write('\n'+str(j)+". Lvl: "+str(trainers[i][f"poke{str(j)}"]["level"]))
                if shiny == 1:
                    spoiler.write(' **Shiny!**')
                spoiler.write(' '+HelperFunctions.get_monname(pokemon_choice))
                if form_choice != 0:
                    spoiler.write(HelperFunctions.get_form_txt(form_choice))
                if item_choice != "ITEMID_NONE":
                    spoiler.write('\n---Holding: '+HelperFunctions.get_itemname(HelperFunctions.get_itemid(item_choice)))
                
        if config['make_ai_smart'] == "yes":
            trainers[i]["isStrong"] = True
            trainers[i]['aiBasic'] = True
            trainers[i]['aiHigh'] = True
            trainers[i]['aiExpert'] = True
            trainers[i]['aiItem'] = True
            trainers[i]['aiChange'] = True


def set_allowed_pokemon(config, randomizer_check: str, og=1):
    if config[f'{randomizer_check}']['only_legendary_and_paradox'] == "yes":
        return SharedVariables.legends_and_paradox
    elif config[f'{randomizer_check}']['only_legendary_pokemon'] == "yes":
        return SharedVariables.legends
    elif config[f'{randomizer_check}']['only_paradox_pokemon'] == "yes":
        return SharedVariables.paradox
    return og


def set_banned_stages(config, banned_check: str):
    list_of_banned = []
    if config[f'{banned_check}']['ban_stage1_pokemon'] == "yes":
        list_of_banned.extend(SharedVariables.gen9Stage1)
    elif config[f'{banned_check}']['ban_stage2_pokemon'] == "yes":
        list_of_banned.extend(SharedVariables.gen9Stage2)
    elif config[f'{banned_check}']['ban_single_stage_pokemon'] == "yes":
        list_of_banned.extend(SharedVariables.no_evolution)
    return list_of_banned

def calc_boosted_vars(config):
    if config["useondomathforboost"] == "yes":
        print("Soz cant actually enable 'useondomathforboost' in the config atm, setting is just a placeholder... for now")
    return
    min_i = config["boost_min"]
    if min_i < 0.1:
        min_i = 0.1
    if min_i > 99:
        min_i = 99
    max_i = config["boost_max"]
    if max_i < 0.1:
        max_i = 0.1
    if max_i > 99:
        max_i = 99
    print("setting boosted lvl range: "+str(min_i)+" - "+str(max_i))
    SharedVariables.boosted_lvl_b = pow(max_i, (1/(100-max_i)))
    SharedVariables.boosted_lvl_a = min_i/ SharedVariables.boosted_lvl_b
    SharedVariables.boosted_lvl_b = round( SharedVariables.boosted_lvl_b, 4)
    SharedVariables.boosted_lvl_a = round( SharedVariables.boosted_lvl_a, 4)
    print(SharedVariables.boosted_lvl_a)
    print(SharedVariables.boosted_lvl_b)
    
def get_boosted_level(orig_lvl, config):
    extralvls = (orig_lvl/100)*config['boostpercent']
    #leaving this code here for now, disabled till i debug it properly
    #extralvls = SharedVariables.boosted_lvl_a*pow(SharedVariables.boosted_lvl_b, orig_lvl)
    new_lvl = orig_lvl+math.ceil(extralvls)
    if new_lvl > 100:
        new_lvl = 100
    return new_lvl
    
def boosted_lvls_checker(config):
    get_setmin = config["boost_min"]
    get_setmax = config["boost_max"]
    lvllist0 = []
    lvllist0to10 = []
    lvllist1to10 = []
    lvllist10to10 = []
    lvllist4to17 = []
    config["boost_min"] = 0
    config["boost_max"] = 0
    calc_boosted_vars(config)
    i = 1;
    while i < 100:
        lvllist0.append(str(get_boosted_level(i, config)))
        i = i + 1
        
    config["boost_min"] = 0
    config["boost_max"] = 10
    calc_boosted_vars(config)
    i = 1;
    while i < 100:
        lvllist0to10.append(str(get_boosted_level(i, config)))
        i = i + 1
        
    config["boost_min"] = 1
    config["boost_max"] = 10
    calc_boosted_vars(config)
    i = 1;
    while i < 100:
        lvllist1to10.append(str(get_boosted_level(i, config)))
        i = i + 1
        
    config["boost_min"] = 10
    config["boost_max"] = 11
    calc_boosted_vars(config)
    i = 1;
    while i < 100:
        lvllist10to10.append(str(get_boosted_level(i, config)))
        i = i + 1
        
    config["boost_min"] = 4
    config["boost_max"] = 17
    calc_boosted_vars(config)
    i = 1;
    while i < 100:
        lvllist4to17.append(str(get_boosted_level(i, config)))
        i = i + 1
    i = 0
    print("base lvl(+15%) - 0min to 0max - 0min to 10max - 1min to 10max - 10min to 10max - 4min to 17max")
    while i < 99:
        print(str(i+1)+"("+str((i+1)+((i+1)/10))+"). "+lvllist0[i]+" - "+lvllist0to10[i]+" - "+lvllist1to10[i]+" - "+lvllist10to10[i]+" - "+lvllist4to17[i])
        i = i + 1
    config["boost_min"] = get_setmin
    config["boost_max"] = get_setmax
    calc_boosted_vars(config)
    
def randomize_trainers(config):
    
    if config['use_paldea_settings_for_all'] == "yes":
        #boosted_lvls_checker(config['paldea_settings']['trainers_randomizer']["all_trainers_settings"])
        calc_boosted_vars(config['paldea_settings']['trainers_randomizer']["all_trainers_settings"])
        
        if config['paldea_settings']['trainers_randomizer']['is_enabled'] == "yes":
            spoilers = HelperFunctions.spoilerlog("Trainers")
            file = open(os.getcwd() + "/Randomizer/Trainers/" +"trdata_array_clean.json", "r")
            data = json.load(file)
            allowed_pokemon, allowed_legends, bpl = HelperFunctions.check_generation_limiter(
                                                    config['paldea_settings']['trainers_randomizer']
                                                    ['all_trainers_settings']['generation_limiter'])

            allowed_pokemon = set_allowed_pokemon(config['paldea_settings']['trainers_randomizer'],
                                                  'rival_randomizer', allowed_pokemon)
            banned_pokes = set_banned_stages(config['paldea_settings']['trainers_randomizer'], 'rival_randomizer')

            if config['paldea_settings']['trainers_randomizer']['rival_randomizer']['is_enabled'] == "yes":
                list_to_check = randomize_nemona()
                list_to_check.extend(randomize_arven())
                list_to_check.extend(randomize_penny())
                list_to_check.extend(randomize_clavell())
                list_to_check.extend(randomize_team_star())
                list_to_check.extend(randomize_kieran_su1())
                list_to_check.extend(randomize_kieran_su2())
                list_to_check.extend(randomize_carmine_su1())
                list_to_check.extend(randomize_carmine_su2())
                list_to_check.extend(randomize_perrin())
                list_to_check.extend(randomize_billy_onare())
                list_to_check.extend(randomize_school_professors())
                spoilers.write("\n-----------------\nRival Fights\n-----------------\n")
                make_poke(config['paldea_settings']['trainers_randomizer']['rival_randomizer'],
                          config['paldea_settings']['trainers_randomizer'], allowed_pokemon, banned_pokes,
                          list_to_check, data['values'], spoilers)

            if config['paldea_settings']['trainers_randomizer']['route_trainers_randomizer']['is_enabled'] == "yes":
                list_to_check = SharedVariables.wild_trainer_index

                if config['paldea_settings']['trainers_randomizer']['all_trainers_settings']['use_rival_randomizer_forall'] == "no":
                    allowed_pokemon = set_allowed_pokemon(config['paldea_settings']['trainers_randomizer'],
                                                          'route_trainers_randomizer', allowed_pokemon)
                    banned_pokes = set_banned_stages(config['paldea_settings']['trainers_randomizer'], 'route_trainers_randomizer')

                spoilers.write("\n-----------------\nRoute Trainers\n-----------------\n")
                make_poke(config['paldea_settings']['trainers_randomizer']['route_trainers_randomizer'],
                          config['paldea_settings']['trainers_randomizer'], allowed_pokemon, banned_pokes,
                          list_to_check, data['values'], spoilers)

            if config['paldea_settings']['trainers_randomizer']['gym_randomizer']['is_enabled'] == "yes":
                list_to_check = randomize_gym()

                if config['paldea_settings']['trainers_randomizer']['all_trainers_settings']['use_rival_randomizer_forall'] == "no":
                    allowed_pokemon = set_allowed_pokemon(config['paldea_settings']['trainers_randomizer'],
                                                          'gym_randomizer', allowed_pokemon)
                    banned_pokes = set_banned_stages(config['paldea_settings']['trainers_randomizer'], 'gym_randomizer')

                spoilers.write("\n-----------------\nGyms\n-----------------\n")
                make_poke(config['paldea_settings']['trainers_randomizer']['gym_randomizer'],
                          config['paldea_settings']['trainers_randomizer'], allowed_pokemon, banned_pokes,
                          list_to_check, data['values'], spoilers)

            if config['paldea_settings']['trainers_randomizer']['elite4_randomizer']['is_enabled'] == "yes":
                list_to_check = randomize_bb_e4()
                list_to_check.extend(randomize_e4_paldea())
                list_to_check.extend(randomize_ogre_clan())

                if config['paldea_settings']['trainers_randomizer']['all_trainers_settings']['use_rival_randomizer_forall'] == "no":
                    allowed_pokemon = set_allowed_pokemon(config['paldea_settings']['trainers_randomizer'],
                                                          'elite4_randomizer', allowed_pokemon)
                    banned_pokes = set_banned_stages(config['paldea_settings']['trainers_randomizer'], 'elite4_randomizer')

                spoilers.write("\n-----------------\nElite 4 | BB Elite 4 | Ogre Clan\n-----------------\n")
                make_poke(config['paldea_settings']['trainers_randomizer']['rival_randomizer'],
                          config['paldea_settings']['trainers_randomizer'], allowed_pokemon, banned_pokes,
                          list_to_check, data['values'], spoilers)

            if config['paldea_settings']['trainers_randomizer']['champion_randomizer']['is_enabled'] == "yes":
                list_to_check = randomize_geeta()
                list_to_check.extend(randomize_professors())
                list_to_check.extend(randomize_bb_league())

                if config['paldea_settings']['trainers_randomizer']['all_trainers_settings']['use_rival_randomizer_forall'] == "no":
                    allowed_pokemon = set_allowed_pokemon(config['paldea_settings']['trainers_randomizer'],
                                                          'champion_randomizer', allowed_pokemon)
                    banned_pokes = set_banned_stages(config['paldea_settings']['trainers_randomizer'], 'champion_randomizer')

                spoilers.write("\n-----------------\nChampions\n-----------------\n")
                make_poke(config['paldea_settings']['trainers_randomizer']['champion_randomizer'],
                          config['paldea_settings']['trainers_randomizer'], allowed_pokemon, banned_pokes,
                          list_to_check, data['values'], spoilers)

            if config['paldea_settings']['trainers_randomizer']['raid_npc_randomizer']['is_enabled'] == "yes":
                list_to_check = SharedVariables.raid_npc_index

                if config['paldea_settings']['trainers_randomizer']['all_trainers_settings']['use_rival_randomizer_forall'] == "no":
                    allowed_pokemon = set_allowed_pokemon(config['paldea_settings']['trainers_randomizer'],
                                                          'raid_npc_randomizer', allowed_pokemon)
                    banned_pokes = set_banned_stages(config['paldea_settings']['trainers_randomizer'], 'raid_npc_randomizer')

                spoilers.write("\n-----------------\nRaid NPCs\n-----------------\n")
                make_poke(config['paldea_settings']['trainers_randomizer']['raid_npc_randomizer'],
                          config['paldea_settings']['trainers_randomizer'], allowed_pokemon, banned_pokes,
                          list_to_check, data['values'], spoilers)

            outdata = json.dumps(data, indent=4)
            with open(os.getcwd() + "/Randomizer/Trainers/" +"trdata_array.json", 'w') as outfile:
                outfile.write(outdata)
            print("Randomization of Trainers done !")
            spoilers.close()
            return True, True, True
        return False, False, False
    else:
        paldea, kitakami, bluberry = False, False, False
        file = open(os.getcwd() + "/Randomizer/Trainers/" + "trdata_array_clean.json", "r")
        data = json.load(file)
        spoilers = HelperFunctions.spoilerlog("Trainers")
        if config['paldea_settings']['trainers_randomizer']['is_enabled'] == "yes":
            allowed_pokemon, allowed_legends, bpl = HelperFunctions.check_generation_limiter(
                config['paldea_settings']['trainers_randomizer']
                ['all_trainers_settings']['generation_limiter'])

            calc_boosted_vars(config['paldea_settings']['trainers_randomizer']["all_trainers_settings"])
            if config['paldea_settings']['trainers_randomizer']['rival_randomizer']['is_enabled'] == "yes":
                allowed_pokemon = set_allowed_pokemon(config['paldea_settings']['trainers_randomizer'],
                                                      'rival_randomizer', allowed_pokemon)
                banned_pokes = set_banned_stages(config['paldea_settings']['trainers_randomizer'], 'rival_randomizer')
                list_to_check = randomize_nemona()
                list_to_check.extend(randomize_arven())
                list_to_check.extend(randomize_penny())
                list_to_check.extend(randomize_clavell())
                list_to_check.extend(randomize_team_star())
                list_to_check.extend(randomize_school_professors())
                spoilers.write("\n-----------------\nRival Fights\n-----------------\n")
                make_poke(config['paldea_settings']['trainers_randomizer']['rival_randomizer'],
                          config['paldea_settings']['trainers_randomizer'], allowed_pokemon, banned_pokes,
                          list_to_check, data['values'], spoilers)

            if config['paldea_settings']['trainers_randomizer']['route_trainers_randomizer']['is_enabled'] == "yes":
                list_to_check = SharedVariables.wild_trainer_index

                allowed_pokemon = set_allowed_pokemon(config['paldea_settings']['trainers_randomizer'],
                                                      'route_trainers_randomizer', allowed_pokemon)
                banned_pokes = set_banned_stages(config['paldea_settings']['trainers_randomizer'], 'route_trainers_randomizer')

                spoilers.write("\n-----------------\nRoute Trainers\n-----------------\n")
                make_poke(config['paldea_settings']['trainers_randomizer']['route_trainers_randomizer'],
                          config['paldea_settings']['trainers_randomizer'], allowed_pokemon, banned_pokes,
                          list_to_check, data['values'], spoilers)

            if config['paldea_settings']['trainers_randomizer']['gym_randomizer']['is_enabled'] == "yes":
                list_to_check = randomize_gym()

                allowed_pokemon = set_allowed_pokemon(config['paldea_settings']['trainers_randomizer'],
                                                      'gym_randomizer', allowed_pokemon)
                banned_pokes = set_banned_stages(config['paldea_settings']['trainers_randomizer'], 'gym_randomizer')

                spoilers.write("\n-----------------\nGyms\n-----------------\n")
                make_poke(config['paldea_settings']['trainers_randomizer']['gym_randomizer'],
                          config['paldea_settings']['trainers_randomizer'], allowed_pokemon, banned_pokes,
                          list_to_check, data['values'], spoilers)

            if config['paldea_settings']['trainers_randomizer']['elite4_randomizer']['is_enabled'] == "yes":
                list_to_check = randomize_e4_paldea()

                allowed_pokemon = set_allowed_pokemon(config['paldea_settings']['trainers_randomizer'],
                                                      'elite4_randomizer', allowed_pokemon)
                banned_pokes = set_banned_stages(config['paldea_settings']['trainers_randomizer'], 'elite4_randomizer')

                spoilers.write("\n-----------------\nElite 4\n-----------------\n")
                make_poke(config['paldea_settings']['trainers_randomizer']['elite4_randomizer'],
                          config['paldea_settings']['trainers_randomizer'], allowed_pokemon, banned_pokes,
                          list_to_check, data['values'], spoilers)

            if config['paldea_settings']['trainers_randomizer']['champion_randomizer']['is_enabled'] == "yes":
                list_to_check = randomize_geeta()
                list_to_check.extend(randomize_professors())

                allowed_pokemon = set_allowed_pokemon(config['paldea_settings']['trainers_randomizer'],
                                                      'champion_randomizer', allowed_pokemon)
                banned_pokes = set_banned_stages(config['paldea_settings']['trainers_randomizer'], 'champion_randomizer')

                spoilers.write("\n-----------------\nChampion\n-----------------\n")
                make_poke(config['paldea_settings']['trainers_randomizer']['champion_randomizer'],
                          config['paldea_settings']['trainers_randomizer'], allowed_pokemon, banned_pokes,
                          list_to_check, data['values'], spoilers)

            if config['paldea_settings']['trainers_randomizer']['raid_npc_randomizer']['is_enabled'] == "yes":
                list_to_check = SharedVariables.raid_npc_index

                allowed_pokemon = set_allowed_pokemon(config['paldea_settings']['trainers_randomizer'],
                                                      'raid_npc_randomizer', allowed_pokemon)
                banned_pokes = set_banned_stages(config['paldea_settings']['trainers_randomizer'], 'raid_npc_randomizer')

                spoilers.write("\n-----------------\nRaid NPCs\n-----------------\n")
                make_poke(config['paldea_settings']['trainers_randomizer']['raid_npc_randomizer'],
                          config['paldea_settings']['trainers_randomizer'], allowed_pokemon, banned_pokes,
                          list_to_check, data['values'], spoilers)
            paldea = True
        if config['kitakami_settings']['trainers_randomizer']['is_enabled'] == "yes":
            allowed_pokemon, allowed_legends, bpl = HelperFunctions.check_generation_limiter(
                config['kitakami_settings']['trainers_randomizer']
                ['all_trainers_settings']['generation_limiter'])

            calc_boosted_vars(config['kitakami_settings']['trainers_randomizer']["all_trainers_settings"])
            if config['kitakami_settings']['trainers_randomizer']['important_trainers_randomizer']['is_enabled'] == "yes":
                list_to_check = randomize_kieran_su1()
                list_to_check.extend(randomize_carmine_su1())
                list_to_check.extend(randomize_perrin())
                list_to_check.extend(randomize_billy_onare())

                allowed_pokemon = set_allowed_pokemon(config['kitakami_settings']['trainers_randomizer'],
                                                      'important_trainers_randomizer', allowed_pokemon)
                banned_pokes = set_banned_stages(config['kitakami_settings']['trainers_randomizer'], 'important_trainers_randomizer')

                spoilers.write("\n-----------------\nRival Fights\n-----------------\n")
                make_poke(config['kitakami_settings']['trainers_randomizer']['important_trainers_randomizer'],
                          config['kitakami_settings']['trainers_randomizer'], allowed_pokemon, banned_pokes,
                          list_to_check, data['values'], spoilers)

            if config['kitakami_settings']['trainers_randomizer']['route_trainers_randomizer']['is_enabled'] == "yes":
                list_to_check = SharedVariables.wild_trainer_index

                allowed_pokemon = set_allowed_pokemon(config['kitakami_settings']['trainers_randomizer'],
                                                      'route_trainers_randomizer', allowed_pokemon)
                banned_pokes = set_banned_stages(config['kitakami_settings']['trainers_randomizer'], 'route_trainers_randomizer')

                spoilers.write("\n-----------------\nRoute Trainers\n-----------------\n")
                make_poke(config['kitakami_settings']['trainers_randomizer']['route_trainers_randomizer'],
                          config['kitakami_settings']['trainers_randomizer'], allowed_pokemon, [],
                          list_to_check, data['values'], spoilers)

            if config['kitakami_settings']['trainers_randomizer']['ogre_clan_randomizer']['is_enabled'] == "yes":
                list_to_check = randomize_ogre_clan()

                allowed_pokemon = set_allowed_pokemon(config['kitakami_settings']['trainers_randomizer'],
                                                      'ogre_clan_randomizer', allowed_pokemon)
                banned_pokes = set_banned_stages(config['kitakami_settings']['trainers_randomizer'], 'ogre_clan_randomizer')

                spoilers.write("\n-----------------\nOgre Clan\n-----------------\n")
                make_poke(config['kitakami_settings']['trainers_randomizer']['ogre_clan_randomizer'],
                          config['kitakami_settings']['trainers_randomizer'], allowed_pokemon, [],
                          list_to_check, data['values'], spoilers)

            if config['kitakami_settings']['trainers_randomizer']['raid_npc_randomizer']['is_enabled'] == "yes":
                list_to_check = SharedVariables.raid_npc_index

                allowed_pokemon = set_allowed_pokemon(config['kitakami_settings']['trainers_randomizer'],
                                                      'raid_npc_randomizer', allowed_pokemon)
                banned_pokes = set_banned_stages(config['kitakami_settings']['trainers_randomizer'],
                                                 'raid_npc_randomizer')

                spoilers.write("\n-----------------\nRaid NPCs\n-----------------\n")
                make_poke(config['kitakami_settings']['trainers_randomizer']['raid_npc_randomizer'],
                          config['kitakami_settings']['trainers_randomizer'], allowed_pokemon, banned_pokes,
                          list_to_check, data['values'], spoilers)

            kitakami = True
        if config['blueberry_settings']['trainers_randomizer']['is_enabled'] == "yes":
            allowed_pokemon, allowed_legends, bpl = HelperFunctions.check_generation_limiter(
                config['blueberry_settings']['trainers_randomizer']
                ['all_trainers_settings']['generation_limiter'])
            calc_boosted_vars(config['blueberry_settings']['trainers_randomizer']["all_trainers_settings"])
            if config['blueberry_settings']['trainers_randomizer']['important_trainers_randomizer']['is_enabled'] == "yes":
                list_to_check = randomize_kieran_su2()
                list_to_check.extend(randomize_carmine_su2())
                list_to_check.extend(randomize_bb_e4())

                allowed_pokemon = set_allowed_pokemon(config['blueberry_settings']['trainers_randomizer'],
                                                      'important_trainers_randomizer', allowed_pokemon)
                banned_pokes = set_banned_stages(config['blueberry_settings']['trainers_randomizer'], 'important_trainers_randomizer')

                spoilers.write("\n-----------------\nRival Fights\n-----------------\n")
                make_poke(config['blueberry_settings']['trainers_randomizer']['important_trainers_randomizer'],
                          config['blueberry_settings']['trainers_randomizer'], allowed_pokemon, banned_pokes,
                          list_to_check, data['values'], spoilers)

            if config['blueberry_settings']['trainers_randomizer']['route_trainers_randomizer']['is_enabled'] == "yes":
                list_to_check = SharedVariables.wild_trainer_index

                allowed_pokemon = set_allowed_pokemon(config['blueberry_settings']['trainers_randomizer'],
                                                      'route_trainers_randomizer', allowed_pokemon)
                banned_pokes = set_banned_stages(config['blueberry_settings']['trainers_randomizer'], 'route_trainers_randomizer')

                spoilers.write("\n-----------------\nRoute Trainers\n-----------------\n")
                make_poke(config['paldea_settings']['trainers_randomizer']['route_trainers_randomizer'],
                          config['paldea_settings']['trainers_randomizer'], allowed_pokemon, banned_pokes,
                          list_to_check, data['values'], spoilers)

            if config['blueberry_settings']['trainers_randomizer']['bb4_league_randomizer']['is_enabled'] == "yes":
                list_to_check = randomize_bb_league()

                allowed_pokemon = set_allowed_pokemon(config['blueberry_settings']['trainers_randomizer'],
                                                      'bb4_league_randomizer', allowed_pokemon)
                banned_pokes = set_banned_stages(config['blueberry_settings']['trainers_randomizer'], 'bb4_league_randomizer')

                spoilers.write("\n-----------------\nBB Elite 4\n-----------------\n")
                make_poke(config['blueberry_settings']['trainers_randomizer']['bb4_league_randomizer'],
                          config['blueberry_settings']['trainers_randomizer'], allowed_pokemon, banned_pokes,
                          list_to_check, data['values'], spoilers)

            if config['blueberry_settings']['trainers_randomizer']['raid_npc_randomizer']['is_enabled'] == "yes":
                list_to_check = SharedVariables.raid_npc_index

                allowed_pokemon = set_allowed_pokemon(config['blueberry_settings']['trainers_randomizer'],
                                                      'raid_npc_randomizer', allowed_pokemon)
                banned_pokes = set_banned_stages(config['blueberry_settings']['trainers_randomizer'],
                                                 'raid_npc_randomizer')

                spoilers.write("\n-----------------\nRaid NPCs\n-----------------\n")
                make_poke(config['blueberry_settings']['trainers_randomizer']['raid_npc_randomizer'],
                          config['blueberry_settings']['trainers_randomizer'], allowed_pokemon, banned_pokes,
                          list_to_check, data['values'], spoilers)
            bluberry = True
        spoilers.close()
        print("Randomization of Trainers done !")
        return paldea, kitakami, bluberry