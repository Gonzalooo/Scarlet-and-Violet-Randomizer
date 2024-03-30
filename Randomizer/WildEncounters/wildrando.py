import csv
import json
import random
import os

legends = [144, 145, 146, 150, 151, 243, 244, 245, 249, 250, 251, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 480,
           481, 482, 483, 484, 485, 486, 487, 489, 490, 491, 492, 493, 494, 638, 639, 640, 641, 642, 643, 644, 645, 646,
           647, 648, 649, 716, 717, 718, 719, 720, 721, 785, 786, 787, 788, 789, 790, 791, 792, 800, 801, 802, 807, 808,
           809, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 905, 994, 995, 996, 997, 998, 999, 1009, 1010,
           1011, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022]
legends_and_paradox = [
           144, 145, 146, 150, 151, 243, 244, 245, 249, 250, 251, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 480,
           481, 482, 483, 484, 485, 486, 487, 489, 490, 491, 492, 493, 494, 638, 639, 640, 641, 642, 643, 644, 645, 646,
           647, 648, 649, 716, 717, 718, 719, 720, 721, 785, 786, 787, 788, 789, 790, 791, 792, 800, 801, 802, 807, 808,
           809, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 905, 978, 979, 980, 981, 982, 983, 984, 985, 986,
           987, 988, 989, 990, 991, 992, 993, 1017, 1018, 1019, 1020, 994, 995, 996, 997, 998, 999, 1011, 1014, 1015,
           1016, 1021, 1022]


def fetch_devname(index: int, csvdata):
    return str.strip(csvdata[index])


def get_alt_form_paldea(index: int):
    has_alt = [25,  # pikachu
                26, #raichu
                28, #sandslash
               30, #ninetails
                50, #diglett
                51, #dugtrio
                52, #meowth, has two
                53, #persian
                58, #growlithe
                59, #arcanine
               74,  #geodude
               75,  #graveler
               76,  #golem
                79, #slowpoke
                80, #slowbro, seems to be form id 2
                88, #grimer
                89, #muk
                100, #voltorb
                101, #electrode
               103,  #exeggutor
               110,  # weezing
                128, #tauros, 3 form possible 1 2 3
                144, #articuno
                145, #zapdos
                146, #moltres
                157, #typhlosion
                194, #wooper
                199, #slowking
                211, #qwilfish
                215, #sneasel
               386,  #Deoxys
                422, #shellos
                423, #gastrodon
                479, #rotom: 5 forms 0 1 2 3 4 5
                483, #dialga
                484, #palkia
                487, #giratina
               492,  #shaymin
                503, #samurott
                549, #lilligant
                550, #basculin
                570, #zorua
                571, #zoroark
                628, #braviary
                641, #tornadus
                642, #thundurus
                645, #landorus
               646,  #Kyurem
                648, #meloetta
               658,  # greninja - added for future proofing and not forget it
               678,  # meowstic
                705, #sligoo
                706, #goodra
                713, #avalugg
                720, #hoopa
                724, #decidueye
               774,  #minior
               800,  #necrozma: 2 - 3 not in game
               801,  #magearna
               869,  #alcremie 8 forms
                892, #urshifu
                893, #zarude
                898, #calyrex, 2 forms 0 1 2
               901,  #Ursaluna
               902,  #basculegion
               905,  #enamorus
               1011, #ogerpon - 0 [Teal], 1[wellspring], 2[heartflame], 3[rock]; 4-7 is teraform
               1021, #terapagos
               1024, #poltchageist
               1025, #sinistcha
    ]
    if index in has_alt: #previously, we just shuffled around. Now we include all species, so we need more edge cases
        choice = 0
        match index:
            case 25:
                choice = [1,2,3,4,5,6,7,9]
                # form 8 not in the game (Partner Let's Go Pikachu)
                return choice
            case 52:
                choice = [1,2]
                return choice
            case 80:
                choice = [2]
                # form 1 not in the game (Mega Slowbro)
                return choice
            case 128:
                choice = [0]
                return choice
            case 194:
                choice = [0]
                return choice
            case 386:
                choice = [1,2,3]
                return choice
            case 479:
                choice = [1,2,3,4,5]
                return choice
            case 550:
                choice = [2]
                return choice
            case 646:
                choice = [1,2]
                return choice
            case 774:
                choice = [1,2,3,4,5,6]
                return choice
            case 800:
                choice = [1, 2]
                return choice
            case 869:
                choice = [1,2,3,4,5,6,7,8]
                return choice
            case 898:
                choice = [1,2]
                return choice
            case 952:
                choice = [1,2]
                return choice
            case 960:
                choice = [1,2,3]
                return choice
            case 1011:
                choice = [1,2,3]
                return choice
            case _:
                choice = [1]
                return choice
    else:
        return [0]


def get_alt_form_teal(index: int):
    has_alt = [25,  # pikachu
                26, #raichu
                27, #sandshrew
                28, #sandslash
               29, #vulpix
               30, #ninetails
                50, #diglett
                51, #dugtrio
                52, #meowth, has two
                53, #persian
                58, #growlithe
                59, #arcanine
               74,  #geodude
               75,  #graveler
               76,  #golem
                79, #slowpoke
                80, #slowbro, seems to be form id 2
                88, #grimer
                89, #muk
                100, #voltorb
                101, #electrode
               103,  #exeggutor
               110,  # weezing
                128, #tauros, 3 form possible 1 2 3
                144, #articuno
                145, #zapdos
                146, #moltres
                157, #typhlosion
                194, #wooper
                199, #slowking
                211, #qwilfish
                215, #sneasel
               386,  #Deoxys
                422, #shellos
                423, #gastrodon
                479, #rotom: 5 forms 0 1 2 3 4 5
                483, #dialga
                484, #palkia
                487, #giratina
               492,  #shaymin
                503, #samurott
                549, #lilligant
                550, #basculin
                570, #zorua
                571, #zoroark
               585,  #deerling
               586,  #sawsbuck
                628, #braviary
                641, #tornadus
                642, #thundurus
                645, #landorus
               646,  #Kyurem
                648, #meloetta
               658,  # greninja - added for future proofing and not forget it
               669,  #flabebe
               670,  #floette - 5 is eternal flower not in game
               671,  #florges
               678,  # meowstic
                705, #sligoo
                706, #goodra
                713, #avalugg
                720, #hoopa
                724, #decidueye
               774,  #minior
               778,  #mimikyu
               800,  #necrozma: 2 - 3 not in game
               801,  #magearna
                849, #toxtricity
               854,  #sineastea
               855,  # plteageist
               869,  #alcremie 8 forms
                892, #urshifu
                893, #zarude
                898, #calyrex, 2 forms 0 1 2
               901,  #Ursaluna
               902,  #basculegion
               905,  #enamorus
               916,  #Oinkolonge
               934,  #Palafin
               952,  #tatsugiri: 2 forms 0 1 2
               960,  #squakabily: 3 forms 0 1 2 3
               976,  #gimmighoul - 998 koraidon test, 999 miraidon test [0-4]
               1011, #ogerpon - 0 [Teal], 1[wellspring], 2[heartflame], 3[rock]; 4-7 is teraform
               1021, #terapagos
               1025, #sinistcha
    ]
    if index in has_alt: #previously, we just shuffled around. Now we include all species, so we need more edge cases
        choice = 0
        match index:
            case 25:
                choice = [1,2,3,4,5,6,7,8,9]
                # form 8 not in the game (Partner Let's Go Pikachu)
                return choice
            case 52:
                choice = [1,2]
                return choice
            case 80:
                choice = [1,2]
                # form 1 not in the game (Mega Slowbro)
                return choice
            case 128:
                choice = [1,2,3]
                return choice
            case 194:
                choice = [1]
                return choice
            case 386:
                choice = [1,2,3]
                return choice
            case 479:
                choice = [1,2,3,4,5]
                return choice
            case 550:
                choice = [0, 1]
                return choice
            case 585:
                choice = [1,2,3]
                return choice
            case 586:
                choice = [1,2,3]
                return choice
            case 646:
                choice = [1,2]
                return choice
            case 669:
                choice = [1,2,3,4]
                return choice
            case 670:
                choice = [1, 2, 3, 4]
                return choice
            case 671:
                choice = [1, 2, 3, 4]
                return choice
            case 774: # includes shield downs form
                choice = [1,2,3,4,5,6]
                return choice
            case 800:
                choice = [1, 2]
                return choice
            case 869:
                choice = [1,2,3,4,5,6,7,8]
                return choice
            case 898:
                choice = [1,2]
                return choice
            case 952:
                choice = [1,2]
                return choice
            case 960:
                choice = [1,2,3]
                return choice
            case 1011:
                choice = [1,2,3]
                return choice
            case _:
                choice = [1]
                return choice
    else:
        return [0]


def get_alt_form_indigo(index: int):
    has_alt = [25,  # pikachu
                26, #raichu
                27, #sandshrew - 0
                28, #sandslash - 0
               29, #vulpix - 0
               30, #ninetails - 0
                50, #diglett - 0
                51, #dugtrio - 0
                52, #meowth, has two
                53, #persian
                58, #growlithe
                59, #arcanine
               74,  #geodude - 0
               75,  #graveler - 0
               76,  #golem - 0
                79, #slowpoke - 0
                80, #slowbro, - 0
                88, #grimer - 0
                89, #muk - 0
                100, #voltorb
                101, #electrode
               103,  #exeggutor - 0
               110,  # weezing
                128, #tauros, 3 form possible 1 2 3
                144, #articuno
                145, #zapdos
                146, #moltres
                157, #typhlosion
                194, #wooper - 0, 1
                199, #slowking
                211, #qwilfish - 0
                215, #sneasel
               386,  #Deoxys
                422, #shellos
                423, #gastrodon
                479, #rotom: 5 forms 0 1 2 3 4 5
                483, #dialga
                484, #palkia
                487, #giratina
               492,  #shaymin
                503, #samurott
                549, #lilligant
                550, #basculin - 1 2
                570, #zorua
                571, #zoroark
                628, #braviary
                641, #tornadus
                642, #thundurus
                645, #landorus
               646,  #Kyurem
                648, #meloetta
               658,  # greninja - added for future proofing and not forget it
               669,  #flabebe
               670,  #floette - 5 is eternal flower not in game
               671,  #florges
                705, #sligoo
                706, #goodra
                713, #avalugg
                720, #hoopa
                724, #decidueye
                744, #rockruff
                745, #lycanroc: 2 forms 0 1 2
               800,  #necrozma: 2 - 3 not in game
               801,  #magearna
                849, #toxtricity
               854,  #sineastea
               855,  # plteageist
               869,  #alcremie 8 forms
               876,  #indeedee
                892, #urshifu
                893, #zarude
                898, #calyrex, 2 forms 0 1 2
               901,  #Ursaluna
               902,  #basculegion
               905,  #enamorus
               916,  #Oinkolonge
               917,  #Dudunsparce
               934,  #Palafin
               946,  #Mausehold
               952,  #tatsugiri: 2 forms 0 1 2
               960,  #squakabily: 3 forms 0 1 2 3
               976,  #gimmighoul - 998 koraidon test, 999 miraidon test [0-4]
               1011, #ogerpon - 0 [Teal], 1[wellspring], 2[heartflame], 3[rock]; 4-7 is teraform
               1021, #terapagos
               1024, #poltchageist
               1025, #sinistcha
    ]
    if index in has_alt: #previously, we just shuffled around. Now we include all species, so we need more edge cases
        choice = 0
        match index:
            case 25:
                choice = [1,2,3,4,5,6,7,8,9]
                # form 8 not in the game (Partner Let's Go Pikachu)
                return choice
            case 27:
                choice = [0]
                return choice
            case 28:
                choice = [0]
                return choice
            case 29:
                choice = [0]
                return choice
            case 30:
                choice = [0]
                return choice
            case 50:
                choice = [0]
                return choice
            case 51:
                choice = [0]
                return choice
            case 52:
                choice = [1,2]
                return choice
            case 74:
                choice = [0]
                return choice
            case 75:
                choice = [0]
                return choice
            case 76:
                choice = [0]
                return choice
            case 79:
                choice = [0]
                return choice
            case 80:
                choice = [0]
                # form 1 not in the game (Mega Slowbro)
                return choice
            case 103:
                choice = [0]
                return choice
            case 128:
                choice = [1,2,3]
                return choice
            case 211:
                choice = [0]
                return choice
            case 386:
                choice = [1,2,3]
                return choice
            case 479:
                choice = [1,2,3,4,5]
                return choice
            case 550:
                choice = [1,2]
                return choice
            case 646:
                choice = [1,2]
                return choice
            case 669:
                choice = [1,2,3,4]
                return choice
            case 670:
                choice = [1, 2, 3, 4]
                return choice
            case 671:
                choice = [1, 2, 3, 4]
                return choice
            case 745:
                choice = [1,2]
                return choice
            case 800:
                choice = [1, 2]
                return choice
            case 869:
                choice = [1,2,3,4,5,6,7,8]
                return choice
            case 898:
                choice = [1,2]
                return choice
            case 952:
                choice = [1,2]
                return choice
            case 960:
                choice = [1,2,3]
                return choice
            case 1011:
                choice = [1,2,3]
                return choice
            case _:
                choice = [1]
                return choice
    else:
        return [0]


# ## Utility functions for biomes ## #
def pick_random_biome1():
    possible_biomes = ["GRASS", "FOREST", "SWAMP", "LAKE", "TOWN", "MOUNTAIN", "BAMBOO", "MINE", "CAVE", "OLIVE",
                       "UNDERGROUND", "RIVER", "ROCKY", "BEACH", "SNOW", "OSEAN", "RUINS", "FLOWER",]
    choice = possible_biomes[random.randint(0, len(possible_biomes) - 1)]
    chosen_biomes.append(choice)
    return choice


def pick_random_biomerest():
    possible_biomes = ["GRASS", "FOREST", "SWAMP", "LAKE", "TOWN", "MOUNTAIN", "BAMBOO", "MINE", "CAVE", "OLIVE",
                       "UNDERGROUND", "RIVER", "ROCKY", "BEACH", "SNOW", "OSEAN", "RUINS", "FLOWER"]
    choice = possible_biomes[random.randint(0, len(possible_biomes) - 1)]
    while choice in chosen_biomes:
        choice = possible_biomes[random.randint(0, len(possible_biomes) - 1)]
        if len(chosen_biomes) > 4:
            break
    chosen_biomes.append(choice)
    return choice


def generate_lot_value_for_biome(biome_type: str):
    return random.randint(1, 50)


def generate_area():
    return(random.sample(range(1, 27), 10))


def generate_area_list():
    return(str(generate_area()).replace('[','"').replace(']','"').replace(' ',''))


# ## Utility function because otherwise, randomize() would be fucked up
def make_template(new_template, index, csvdata, form=0):
    new_template['devid'] = fetch_devname(index, csvdata)
    new_template['formno'] = form
    new_template['minlevel'] = 2
    new_template['maxlevel'] = 99
    new_template['lotvalue'] = random.randint(1, 50)
    new_template['biome1'] = pick_random_biome1()
    new_template['biome2'] = pick_random_biomerest()
    new_template['biome3'] = pick_random_biomerest()
    new_template['biome4'] = pick_random_biomerest()
    new_template['lotvalue1'] = generate_lot_value_for_biome(new_template['biome1'])
    new_template['lotvalue2'] = generate_lot_value_for_biome(new_template['biome2'])
    new_template['lotvalue3'] = generate_lot_value_for_biome(new_template['biome3'])
    new_template['lotvalue4'] = generate_lot_value_for_biome(new_template['biome4'])
    chosen_biomes.clear()
    new_template['area'] = generate_area_list()
    new_template['locationName'] = ""
    new_template['enabletable']['land'] = True
    new_template['enabletable']['up_water'] = True
    new_template['enabletable']['underwater'] = True
    new_template['enabletable']['air1'] = True
    new_template['enabletable']['air2'] = True
    new_template['timetable']['morning'] = True
    new_template['timetable']['noon'] = True
    new_template['timetable']['evening'] = True
    new_template['timetable']['night'] = True
    new_template['flagName'] = ""
    new_template['versiontable']['A'] = True
    new_template['versiontable']['B'] = True
    new_template['bringItem']['itemID'] = "ITEMID_NONE"
    new_template['bringItem']['bringRate'] = 0
    return new_template


# ## Global variables ## #
banned_pokemon = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 29, 30, 31, 32, 33, 34, 35, 41, 42, 46, 47, 63,
                  64, 65, 66, 67, 77, 78, 83, 95, 98, 99, 104, 105, 108, 114, 115, 118, 119, 120, 121, 122, 124, 127,
                  138, 139, 140, 141, 142, 165, 166, 169, 175, 176, 177, 178, 201, 202, 208, 213, 222, 223, 224, 226,
                  238, 241, 251, 263, 264, 265, 266, 267, 268, 269, 276, 277, 290, 291, 292, 293, 294, 295, 300, 301,
                  303, 304, 305, 306, 309, 310, 315, 318, 319, 320, 321, 327, 337, 338, 343, 344, 345, 346, 347, 348,
                  351, 352, 359, 360, 363, 364, 365, 366, 367, 368, 369, 399, 400, 406, 407, 412, 413, 414, 420, 421,
                  427, 428, 431, 432, 439, 441, 451, 452, 455, 458, 463, 465, 468, 494, 504, 505, 506, 507, 508, 509,
                  510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 524, 525, 526, 527, 528, 531, 535, 536,
                  537, 538, 539, 543, 544, 545, 554, 555, 556, 557, 558, 561, 562, 563, 564, 565, 566, 567, 568, 569,
                  582, 583, 584, 587, 588, 589, 592, 593, 597, 598, 599, 600, 601, 605, 606, 616, 617, 618, 621, 626,
                  631, 632, 649, 659, 660, 674, 675, 676, 679, 680, 681, 682, 683, 684, 685, 688, 689, 694, 695, 696,
                  697, 698, 699, 710, 711, 716, 717, 718, 746, 755, 756, 759, 760, 767, 768, 771, 772, 773, 776, 777,
                  780, 781, 785, 786, 787, 788, 793, 794, 795, 796, 797, 798, 799, 802, 803, 804, 805, 806, 807, 808,
                  809, 824, 825, 826, 827, 828, 829, 830, 831, 832, 835, 836, 850, 851, 852, 853, 864, 865, 866, 867,
                  880, 881, 882, 883]
legends = [144, 145, 146, 150, 151, 243, 244, 245, 249, 250, 251, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 480,
           481, 482, 483, 484, 485, 486, 487, 489, 490, 491, 492, 493, 494, 638, 639, 640, 641, 642, 643, 644, 645, 646,
           647, 648, 649, 716, 717, 718, 719, 720, 721, 785, 786, 787, 788, 789, 790, 791, 792, 800, 801, 802, 807, 808,
           809, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 905, 994, 995, 996, 997, 998, 999, 1011, 1014,
           1015, 1016, 1021, 1022]
UB = [793, 794, 795, 796, 797, 798, 799, 803, 804, 805, 806]
paradox = [978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 998, 999, 1021,
           1017, 1018, 1019, 1020]
legends_and_paradox = [
           144, 145, 146, 150, 151, 243, 244, 245, 249, 250, 251, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 480,
           481, 482, 483, 484, 485, 486, 487, 489, 490, 491, 492, 493, 494, 638, 639, 640, 641, 642, 643, 644, 645, 646,
           647, 648, 649, 716, 717, 718, 719, 720, 721, 785, 786, 787, 788, 789, 790, 791, 792, 800, 801, 802, 807, 808,
           809, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 905, 978, 979, 980, 981, 982, 983, 984, 985, 986,
           987, 988, 989, 990, 991, 992, 993, 1017, 1018, 1019, 1020, 994, 995, 996, 997, 998, 999, 1011, 1014, 1015,
           1016, 1021, 1022]

recreated_species = []
recreated_altforms = []
chosen_biomes = []


### Actual shit going on here ###
def randomize(config):
    recreated_species = []
    # print(os.getcwd())
    # load information
    file = open(os.getcwd() + "/Randomizer/WildEncounters/" + "pokedata_array_clean.json", "r")
    data = json.load(file)

    csvfile = open(os.getcwd() + "/Randomizer/WildEncounters/" + "pokemon_to_id.txt", "r")
    csvdata = []
    for i in csvfile:
        csvdata.append(i)
    csvfile.close()

    # recreate data entries so all mons are present.
    # simplest way of doing it, is to edit all existing entries to have devid's ascending from allowed species, and simply paste another entry with the new ids n shti
    # copy an entry
    template_entry = data['values'][0].copy()

    i = len(data) - 1
    # edit existing entries
    poke_dict = {}
    poke_dict['values'] = []

    for entry in data['values']:
        # entry['devid'] = fetch_devname(allowed_species[i])
        # entry['sex'] = "DEFAULT"
        recreated_species.append(entry['devid'])
        if entry['formno'] != 0:
            recreated_altforms.append(entry['devid'])
        entry['minlevel'] = 2
        entry['maxlevel'] = 99
        entry['lotvalue'] = random.randint(1, 50)
        entry['biome1'] = pick_random_biome1()
        entry['biome2'] = pick_random_biomerest()
        entry['biome3'] = pick_random_biomerest()
        entry['biome4'] = pick_random_biomerest()
        entry['lotvalue1'] = generate_lot_value_for_biome(entry['biome1'])
        entry['lotvalue2'] = generate_lot_value_for_biome(entry['biome2'])
        entry['lotvalue3'] = generate_lot_value_for_biome(entry['biome3'])
        entry['lotvalue4'] = generate_lot_value_for_biome(entry['biome4'])
        chosen_biomes.clear()
        entry['area'] = generate_area_list()
        entry['locationName'] = ""
        entry['enabletable']['land'] = True
        entry['enabletable']['up_water'] = True
        entry['enabletable']['underwater'] = True
        entry['enabletable']['air1'] = True
        entry['enabletable']['air2'] = True
        entry['timetable']['morning'] = True
        entry['timetable']['noon'] = True
        entry['timetable']['evening'] = True
        entry['timetable']['night'] = True
        entry['flagName'] = ""
        entry['versiontable']['A'] = True
        entry['versiontable']['B'] = True
        entry['bringItem']['itemID'] = "ITEMID_NONE"
        entry['bringItem']['bringRate'] = 0
    # add in mons that were not present previously
    # i shoudl really cleanup this bullshit later
    for index in range(1, 1025):
        if index in banned_pokemon:
            continue
        if config['exclude_legendaries'] == "yes":
            if index in legends:
                pass
            else:
                if fetch_devname(index, csvdata) not in recreated_species:
                    new_template = template_entry.copy()
                    recreated_species.append(fetch_devname(index, csvdata))
                    new_template = make_template(new_template, index, csvdata)
                    data['values'].append(new_template)
                    i = i + 1
                    # check alt forms for this mon
                forms = get_alt_form_paldea(index)
                for form in forms:  # previously was too high, now it should also pass on mons that alraedy have entries
                    # so aside from 128 and 194, all 0's should be ignored
                    form_template = template_entry.copy()  # gotta copy again the template from the start
                    form_template = make_template(form_template, index, csvdata,
                                                  form)  # randomize the template before changing the formno
                    if form == 0:
                        if index == 194 or index == 128:
                            data['values'].append(form_template)
                        else:
                            continue  # NOT ALLOWED !!!
                    else:  # should let pass 0's if correct id's
                        # print(form_template)
                        data['values'].append(form_template)
        elif config['only_legends'] == "yes":
            if index not in legends:
                pass
            else:
                new_template = template_entry.copy()
                recreated_species.append(fetch_devname(index, csvdata))
                new_template = make_template(new_template, index, csvdata)
                data['values'].append(new_template)
                poke_dict['values'].append(new_template)
                i = i + 1
                # check alt forms for this mon
                forms = get_alt_form_paldea(index)
                for form in forms:  # previously was too high, now it should also pass on mons that alraedy have entries
                    # so aside from 128 and 194, all 0's should be ignored
                    form_template = template_entry.copy()  # gotta copy again the template from the start
                    form_template = make_template(form_template, index, csvdata,
                                                  form)  # randomize the template before changing the formno
                    if form == 0:
                        if index == 194 or index == 128:
                            data['values'].append(form_template)
                        else:
                            continue  # NOT ALLOWED !!!
                    else:  # should let pass 0's if correct id's
                        # print(form_template)
                        data['values'].append(form_template)
                        poke_dict['values'].append(form_template)
        elif config['only_paradox'] == "yes":
            if index not in paradox:
                pass
            else:
                new_template = template_entry.copy()
                recreated_species.append(fetch_devname(index, csvdata))
                new_template = make_template(new_template, index, csvdata)
                data['values'].append(new_template)
                poke_dict['values'].append(new_template)
                i = i + 1
                    # check alt forms for this mon
                forms = get_alt_form_paldea(index)
                for form in forms:  # previously was too high, now it should also pass on mons that alraedy have entries
                    # so aside from 128 and 194, all 0's should be ignored
                    form_template = template_entry.copy()  # gotta copy again the template from the start
                    form_template = make_template(form_template, index, csvdata,
                                                  form)  # randomize the template before changing the formno
                    if form == 0:
                        if index == 194 or index == 128:
                            data['values'].append(form_template)
                        else:
                            continue  # NOT ALLOWED !!!
                    else:  # should let pass 0's if correct id's
                        # print(form_template)
                        data['values'].append(form_template)
                        poke_dict['values'].append(form_template)
        elif config['only_legends_and_paradoxes'] == "yes":
            if index not in legends_and_paradox:
                pass
            else:
                new_template = template_entry.copy()
                recreated_species.append(fetch_devname(index, csvdata))
                new_template = make_template(new_template, index, csvdata)
                data['values'].append(new_template)
                poke_dict['values'].append(new_template)
                i = i + 1
                # check alt forms for this mon
                forms = get_alt_form_paldea(index)
                for form in forms:  # previously was too high, now it should also pass on mons that alraedy have entries
                    # so aside from 128 and 194, all 0's should be ignored
                    form_template = template_entry.copy()  # gotta copy again the template from the start
                    form_template = make_template(form_template, index, csvdata,
                                                  form)  # randomize the template before changing the formno
                    if form == 0:
                        if index == 194 or index == 128:
                            data['values'].append(form_template)
                        else:
                            continue  # NOT ALLOWED !!!
                    else:  # should let pass 0's if correct id's
                        # print(form_template)
                        data['values'].append(form_template)
                        poke_dict['values'].append(form_template)
        else:
            if fetch_devname(index, csvdata) not in recreated_species:
                new_template = template_entry.copy()
                recreated_species.append(fetch_devname(index, csvdata))
                new_template = make_template(new_template, index, csvdata)
                data['values'].append(new_template)
                i = i + 1
                # check alt forms for this mon
            forms = get_alt_form_paldea(index)
            for form in forms:  # previously was too high, now it should also pass on mons that alraedy have entries
                # so aside from 128 and 194, all 0's should be ignored
                form_template = template_entry.copy()  # gotta copy again the template from the start
                form_template = make_template(form_template, index, csvdata,
                                              form)  # randomize the template before changing the formno
                if form == 0:
                    if index == 194 or index == 128:
                        data['values'].append(form_template)
                    else:
                        continue  # NOT ALLOWED !!!
                else:  # should let pass 0's if correct id's
                    # print(form_template)
                    data['values'].append(form_template)

    outdata = json.dumps(data, indent=4)
    if len(poke_dict['values']) != 0 and (config['only_legends'] == "yes" or config['only_paradox'] == "yes" or
                                          config['only_legends_and_paradoxes'] == "yes"):
        outdata = json.dumps(poke_dict, indent=4)
    with open(os.getcwd() + "/Randomizer/WildEncounters/" + "pokedata_array.json", 'w') as outfile:
        outfile.write(outdata)
    print("Randomisation - Paldea done !")


def randomize_teal(config):
    recreated_species = []
    # print(os.getcwd())
    # load information
    file = open(os.getcwd() + "/Randomizer/WildEncounters/" + "pokedata_su1_array_clean.json", "r")
    data = json.load(file)

    csvfile = open(os.getcwd() + "/Randomizer/WildEncounters/" + "pokemon_to_id.txt", "r")
    csvdata = []
    for i in csvfile:
        csvdata.append(i)
    csvfile.close()

    # recreate data entries so all mons are present.
    # simplest way of doing it, is to edit all existing entries to have devid's ascending from allowed species, and simply paste another entry with the new ids n shti
    # copy an entry
    template_entry = data['values'][0].copy()

    i = len(data) - 1
    # edit existing entries
    poke_dict = {}
    poke_dict['values'] = []

    for entry in data['values']:
        # entry['devid'] = fetch_devname(allowed_species[i])
        # entry['sex'] = "DEFAULT"
        recreated_species.append(entry['devid'])
        if entry['formno'] != 0:
            recreated_altforms.append(entry['devid'])
        entry['minlevel'] = 2
        entry['maxlevel'] = 99
        entry['lotvalue'] = random.randint(1, 50)
        entry['biome1'] = pick_random_biome1()
        entry['biome2'] = pick_random_biomerest()
        entry['biome3'] = pick_random_biomerest()
        entry['biome4'] = pick_random_biomerest()
        entry['lotvalue1'] = generate_lot_value_for_biome(entry['biome1'])
        entry['lotvalue2'] = generate_lot_value_for_biome(entry['biome2'])
        entry['lotvalue3'] = generate_lot_value_for_biome(entry['biome3'])
        entry['lotvalue4'] = generate_lot_value_for_biome(entry['biome4'])
        chosen_biomes.clear()
        entry['area'] = generate_area_list()
        entry['locationName'] = ""
        entry['enabletable']['land'] = True
        entry['enabletable']['up_water'] = True
        entry['enabletable']['underwater'] = True
        entry['enabletable']['air1'] = True
        entry['enabletable']['air2'] = True
        entry['timetable']['morning'] = True
        entry['timetable']['noon'] = True
        entry['timetable']['evening'] = True
        entry['timetable']['night'] = True
        entry['flagName'] = ""
        entry['versiontable']['A'] = True
        entry['versiontable']['B'] = True
        entry['bringItem']['itemID'] = "ITEMID_NONE"
        entry['bringItem']['bringRate'] = 0
    # add in mons that were not present previously
    # i shoudl really cleanup this bullshit later
    for index in range(1, 1025):
        if index in banned_pokemon:
            continue
        if config['exclude_legendaries'] == "yes":
            if index in legends:
                pass
            else:
                if fetch_devname(index, csvdata) not in recreated_species:
                    new_template = template_entry.copy()
                    recreated_species.append(fetch_devname(index, csvdata))
                    new_template = make_template(new_template, index, csvdata)
                    data['values'].append(new_template)
                    i = i + 1
                    # check alt forms for this mon
                forms = get_alt_form_teal(index)
                for form in forms:  # previously was too high, now it should also pass on mons that alraedy have entries
                    # so aside from 128 and 194, all 0's should be ignored
                    form_template = template_entry.copy()  # gotta copy again the template from the start
                    form_template = make_template(form_template, index, csvdata,
                                                  form)  # randomize the template before changing the formno
                    if form == 0:
                        if index == 550:
                            data['values'].append(form_template)
                        else:
                            continue  # NOT ALLOWED !!!
                    else:  # should let pass 0's if correct id's
                        # print(form_template)
                        data['values'].append(form_template)
        elif config['only_legends'] == "yes":
            if index not in legends:
                pass
            else:
                new_template = template_entry.copy()
                recreated_species.append(fetch_devname(index, csvdata))
                new_template = make_template(new_template, index, csvdata)
                data['values'].append(new_template)
                poke_dict['values'].append(new_template)
                i = i + 1
                # check alt forms for this mon
                forms = get_alt_form_teal(index)
                for form in forms:  # previously was too high, now it should also pass on mons that alraedy have entries
                    # so aside from 128 and 194, all 0's should be ignored
                    form_template = template_entry.copy()  # gotta copy again the template from the start
                    form_template = make_template(form_template, index, csvdata,
                                                  form)  # randomize the template before changing the formno
                    if form == 0:
                        if index == 550:
                            data['values'].append(form_template)
                        else:
                            continue  # NOT ALLOWED !!!
                    else:  # should let pass 0's if correct id's
                        # print(form_template)
                        data['values'].append(form_template)
                        poke_dict['values'].append(form_template)
        elif config['only_paradox'] == "yes":
            if index not in paradox:
                pass
            else:
                new_template = template_entry.copy()
                recreated_species.append(fetch_devname(index, csvdata))
                new_template = make_template(new_template, index, csvdata)
                data['values'].append(new_template)
                poke_dict['values'].append(new_template)
                i = i + 1
                # check alt forms for this mon
                forms = get_alt_form_teal(index)
                for form in forms:  # previously was too high, now it should also pass on mons that alraedy have entries
                    # so aside from 128 and 194, all 0's should be ignored
                    form_template = template_entry.copy()  # gotta copy again the template from the start
                    form_template = make_template(form_template, index, csvdata,
                                                  form)  # randomize the template before changing the formno
                    if form == 0:
                        if index == 550:
                            data['values'].append(form_template)
                        else:
                            continue  # NOT ALLOWED !!!
                    else:  # should let pass 0's if correct id's
                        # print(form_template)
                        data['values'].append(form_template)
                        poke_dict['values'].append(form_template)
        elif config['only_legends_and_paradoxes'] == "yes":
            if index not in legends_and_paradox:
                pass
            else:
                new_template = template_entry.copy()
                recreated_species.append(fetch_devname(index, csvdata))
                new_template = make_template(new_template, index, csvdata)
                data['values'].append(new_template)
                poke_dict['values'].append(new_template)
                i = i + 1
                # check alt forms for this mon
                forms = get_alt_form_teal(index)
                for form in forms:  # previously was too high, now it should also pass on mons that alraedy have entries
                    # so aside from 128 and 194, all 0's should be ignored
                    form_template = template_entry.copy()  # gotta copy again the template from the start
                    form_template = make_template(form_template, index, csvdata,
                                                  form)  # randomize the template before changing the formno
                    if form == 0:
                        if index == 550:
                            data['values'].append(form_template)
                        else:
                            continue  # NOT ALLOWED !!!
                    else:  # should let pass 0's if correct id's
                        # print(form_template)
                        data['values'].append(form_template)
                        poke_dict['values'].append(form_template)
        else:
            if fetch_devname(index, csvdata) not in recreated_species:
                new_template = template_entry.copy()
                recreated_species.append(fetch_devname(index, csvdata))
                new_template = make_template(new_template, index, csvdata)
                data['values'].append(new_template)
                i = i + 1
                # check alt forms for this mon
            forms = get_alt_form_teal(index)
            for form in forms:  # previously was too high, now it should also pass on mons that alraedy have entries
                # so aside from 128 and 194, all 0's should be ignored
                form_template = template_entry.copy()  # gotta copy again the template from the start
                form_template = make_template(form_template, index, csvdata,
                                              form)  # randomize the template before changing the formno
                if form == 0:
                    if index == 550:
                        data['values'].append(form_template)
                    else:
                        continue  # NOT ALLOWED !!!
                else:  # should let pass 0's if correct id's
                    # print(form_template)
                    data['values'].append(form_template)

    outdata = json.dumps(data, indent=4)
    if len(poke_dict['values']) != 0 and (config['only_legends'] == "yes" or config['only_paradox'] == "yes" or
                                          config['only_legends_and_paradoxes'] == "yes"):
        outdata = json.dumps(poke_dict, indent=4)
    with open(os.getcwd() + "/Randomizer/WildEncounters/" + "pokedata_su1_array.json", 'w') as outfile:
        outfile.write(outdata)
    print("Randomisation - Teal done !")


def randomize_indigo(config):
    recreated_species = []
    # print(os.getcwd())
    # load information
    file = open(os.getcwd() + "/Randomizer/WildEncounters/" + "pokedata_su2_array_clean.json", "r")
    data = json.load(file)

    csvfile = open(os.getcwd() + "/Randomizer/WildEncounters/" + "pokemon_to_id.txt", "r")
    csvdata = []
    for i in csvfile:
        csvdata.append(i)
    csvfile.close()

    # recreate data entries so all mons are present.
    # simplest way of doing it, is to edit all existing entries to have devid's ascending from allowed species, and simply paste another entry with the new ids n shti
    # copy an entry
    template_entry = data['values'][0].copy()

    i = len(data) - 1
    poke_dict = {}
    poke_dict['values'] = []
    # edit existing entries
    for entry in data['values']:
        # entry['devid'] = fetch_devname(allowed_species[i])
        # entry['sex'] = "DEFAULT"
        recreated_species.append(entry['devid'])
        if entry['formno'] != 0:
            recreated_altforms.append(entry['devid'])
        entry['minlevel'] = 2
        entry['maxlevel'] = 99
        entry['lotvalue'] = random.randint(1, 50)
        entry['biome1'] = pick_random_biome1()
        entry['biome2'] = pick_random_biomerest()
        entry['biome3'] = pick_random_biomerest()
        entry['biome4'] = pick_random_biomerest()
        entry['lotvalue1'] = generate_lot_value_for_biome(entry['biome1'])
        entry['lotvalue2'] = generate_lot_value_for_biome(entry['biome2'])
        entry['lotvalue3'] = generate_lot_value_for_biome(entry['biome3'])
        entry['lotvalue4'] = generate_lot_value_for_biome(entry['biome4'])
        chosen_biomes.clear()
        entry['area'] = generate_area_list()
        entry['locationName'] = ""
        entry['enabletable']['land'] = True
        entry['enabletable']['up_water'] = True
        entry['enabletable']['underwater'] = True
        entry['enabletable']['air1'] = True
        entry['enabletable']['air2'] = True
        entry['timetable']['morning'] = True
        entry['timetable']['noon'] = True
        entry['timetable']['evening'] = True
        entry['timetable']['night'] = True
        entry['flagName'] = ""
        entry['versiontable']['A'] = True
        entry['versiontable']['B'] = True
        entry['bringItem']['itemID'] = "ITEMID_NONE"
        entry['bringItem']['bringRate'] = 0
    # add in mons that were not present previously
    # i shoudl really cleanup this bullshit later
    for index in range(1, 1025):
        if index in banned_pokemon:
            continue
        if config['exclude_legendaries'] == "yes":
            if index in legends:
                pass
            else:
                if fetch_devname(index, csvdata) not in recreated_species:
                    new_template = template_entry.copy()
                    recreated_species.append(fetch_devname(index, csvdata))
                    new_template = make_template(new_template, index, csvdata)
                    data['values'].append(new_template)
                    i = i + 1
                    # check alt forms for this mon
                forms = get_alt_form_indigo(index)
                for form in forms:  # previously was too high, now it should also pass on mons that alraedy have entries
                    # so aside from 128 and 194, all 0's should be ignored
                    form_template = template_entry.copy()  # gotta copy again the template from the start
                    form_template = make_template(form_template, index, csvdata,
                                                  form)  # randomize the template before changing the formno
                    if form == 0:
                        if index == 27:
                            data['values'].append(form_template)
                        elif index == 28:
                            data['values'].append(form_template)
                        elif index == 29:
                            data['values'].append(form_template)
                        elif index == 30:
                            data['values'].append(form_template)
                        elif index == 50:
                            data['values'].append(form_template)
                        elif index == 51:
                            data['values'].append(form_template)
                        elif index == 74:
                            data['values'].append(form_template)
                        elif index == 75:
                            data['values'].append(form_template)
                        elif index == 76:
                            data['values'].append(form_template)
                        elif index == 79:
                            data['values'].append(form_template)
                        elif index == 80:
                            data['values'].append(form_template)
                        elif index == 211:
                            data['values'].append(form_template)
                        else:
                            continue
                    else:  # should let pass 0's if correct id's
                        # print(form_template)
                        data['values'].append(form_template)
        elif config['only_legends'] == "yes":
            if index not in legends:
                pass
            else:
                new_template = template_entry.copy()
                recreated_species.append(fetch_devname(index, csvdata))
                new_template = make_template(new_template, index, csvdata)
                data['values'].append(new_template)
                poke_dict['values'].append(new_template)
                i = i + 1
                # check alt forms for this mon
                forms = get_alt_form_indigo(index)
                for form in forms:  # previously was too high, now it should also pass on mons that alraedy have entries
                    # so aside from 128 and 194, all 0's should be ignored
                    form_template = template_entry.copy()  # gotta copy again the template from the start
                    form_template = make_template(form_template, index, csvdata,
                                                  form)  # randomize the template before changing the formno
                    if form == 0:
                        if index == 27:
                            data['values'].append(form_template)
                        elif index == 28:
                            data['values'].append(form_template)
                        elif index == 29:
                            data['values'].append(form_template)
                        elif index == 30:
                            data['values'].append(form_template)
                        elif index == 50:
                            data['values'].append(form_template)
                        elif index == 51:
                            data['values'].append(form_template)
                        elif index == 74:
                            data['values'].append(form_template)
                        elif index == 75:
                            data['values'].append(form_template)
                        elif index == 76:
                            data['values'].append(form_template)
                        elif index == 79:
                            data['values'].append(form_template)
                        elif index == 80:
                            data['values'].append(form_template)
                        elif index == 211:
                            data['values'].append(form_template)
                        else:
                            continue
                    else:  # should let pass 0's if correct id's
                        # print(form_template)
                        data['values'].append(form_template)
                        poke_dict['values'].append(form_template)
        elif config['only_paradox'] == "yes":
            if index not in paradox:
                pass
            else:
                new_template = template_entry.copy()
                recreated_species.append(fetch_devname(index, csvdata))
                new_template = make_template(new_template, index, csvdata)
                data['values'].append(new_template)
                poke_dict['values'].append(new_template)
                i = i + 1
                # check alt forms for this mon
                forms = get_alt_form_indigo(index)
                for form in forms:  # previously was too high, now it should also pass on mons that alraedy have entries
                    # so aside from 128 and 194, all 0's should be ignored
                    form_template = template_entry.copy()  # gotta copy again the template from the start
                    form_template = make_template(form_template, index, csvdata,
                                                  form)  # randomize the template before changing the formno
                    if form == 0:
                        if index == 27:
                            data['values'].append(form_template)
                        elif index == 28:
                            data['values'].append(form_template)
                        elif index == 29:
                            data['values'].append(form_template)
                        elif index == 30:
                            data['values'].append(form_template)
                        elif index == 50:
                            data['values'].append(form_template)
                        elif index == 51:
                            data['values'].append(form_template)
                        elif index == 74:
                            data['values'].append(form_template)
                        elif index == 75:
                            data['values'].append(form_template)
                        elif index == 76:
                            data['values'].append(form_template)
                        elif index == 79:
                            data['values'].append(form_template)
                        elif index == 80:
                            data['values'].append(form_template)
                        elif index == 211:
                            data['values'].append(form_template)
                        else:
                            continue
                    else:  # should let pass 0's if correct id's
                        # print(form_template)
                        data['values'].append(form_template)
                        poke_dict['values'].append(form_template)
        elif config['only_legends_and_paradoxes'] == "yes":
            if index not in legends_and_paradox:
                pass
            else:
                new_template = template_entry.copy()
                recreated_species.append(fetch_devname(index, csvdata))
                new_template = make_template(new_template, index, csvdata)
                data['values'].append(new_template)
                poke_dict['values'].append(new_template)
                i = i + 1
                # check alt forms for this mon
                forms = get_alt_form_indigo(index)
                for form in forms:  # previously was too high, now it should also pass on mons that alraedy have entries
                    # so aside from 128 and 194, all 0's should be ignored
                    form_template = template_entry.copy()  # gotta copy again the template from the start
                    form_template = make_template(form_template, index, csvdata,
                                                  form)  # randomize the template before changing the formno
                    if form == 0:
                        if index == 27:
                            data['values'].append(form_template)
                        elif index == 28:
                            data['values'].append(form_template)
                        elif index == 29:
                            data['values'].append(form_template)
                        elif index == 30:
                            data['values'].append(form_template)
                        elif index == 50:
                            data['values'].append(form_template)
                        elif index == 51:
                            data['values'].append(form_template)
                        elif index == 74:
                            data['values'].append(form_template)
                        elif index == 75:
                            data['values'].append(form_template)
                        elif index == 76:
                            data['values'].append(form_template)
                        elif index == 79:
                            data['values'].append(form_template)
                        elif index == 80:
                            data['values'].append(form_template)
                        elif index == 211:
                            data['values'].append(form_template)
                        else:
                            continue
                    else:  # should let pass 0's if correct id's
                        # print(form_template)
                        data['values'].append(form_template)
                        poke_dict['values'].append(form_template)
        else:
            if fetch_devname(index, csvdata) not in recreated_species:
                new_template = template_entry.copy()
                recreated_species.append(fetch_devname(index, csvdata))
                new_template = make_template(new_template, index, csvdata)
                data['values'].append(new_template)
                i = i + 1
                # check alt forms for this mon
            forms = get_alt_form_indigo(index)
            for form in forms:  # previously was too high, now it should also pass on mons that alraedy have entries
                # so aside from 128 and 194, all 0's should be ignored
                form_template = template_entry.copy()  # gotta copy again the template from the start
                form_template = make_template(form_template, index, csvdata,
                                              form)  # randomize the template before changing the formno
                if form == 0:
                    if index == 27:
                        data['values'].append(form_template)
                    elif index == 28:
                        data['values'].append(form_template)
                    elif index == 29:
                        data['values'].append(form_template)
                    elif index == 30:
                        data['values'].append(form_template)
                    elif index == 50:
                        data['values'].append(form_template)
                    elif index == 51:
                        data['values'].append(form_template)
                    elif index == 74:
                        data['values'].append(form_template)
                    elif index == 75:
                        data['values'].append(form_template)
                    elif index == 76:
                        data['values'].append(form_template)
                    elif index == 79:
                        data['values'].append(form_template)
                    elif index == 80:
                        data['values'].append(form_template)
                    elif index == 211:
                        data['values'].append(form_template)
                    else:
                        continue
                else:  # should let pass 0's if correct id's
                    # print(form_template)
                    data['values'].append(form_template)

    outdata = json.dumps(data, indent=4)
    if len(poke_dict['values']) != 0 and (config['only_legends'] == "yes" or config['only_paradox'] == "yes" or
                                          config['only_legends_and_paradoxes'] == "yes"):
        outdata = json.dumps(poke_dict, indent=4)
    with open(os.getcwd() + "/Randomizer/WildEncounters/" + "pokedata_su2_array.json", 'w') as outfile:
        outfile.write(outdata)
    print("Randomisation - Indigo done !")


def main():
    randomize()
    randomize_teal()
    randomize_indigo()


if __name__ == "__main__":
    main()
