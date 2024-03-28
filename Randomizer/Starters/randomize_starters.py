import json
import random
import os
import shutil
from Randomizer.shared_Variables import starters_used as picked_starters
import Randomizer.shared_Variables as sharedVar

tera_types = ['normal', 'kakutou', 'hikou', 'doku', 'jimen', 'iwa', 'mushi', 'ghost', 'hagane', 'honoo', 'mizu', 'kusa',
              'denki', 'esper', 'koori', 'dragon', 'aku', 'fairy', 'niji']
'''
normal = normal
kakutou = fightning
hikou = flying
doku = poison
jimen = ground
iwa = rock
mushi = bug
ghost = ghost
hagane = steel
honoo = fire
mizu = water
kusa = grass
denki = electric
esper = psychic
koori = ice
dragon = dragon
aku = dark
fairy = fairy (yousei everywhere else)
niji = stellar
'''
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
           809, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 905, 994, 995, 996, 997, 998, 999, 1009, 1010,
           1011, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022]
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
bannedStages = []


def fetch_devname(index: int, csvdata):
    return str.strip(csvdata[index])

# Future-proof it by 2.0 release
def get_alt_form(index: int):
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
               493,  #arceus
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
               664,  #scatterbug
               665,  #sweppa
               666,  #vivillon - flabebe/floette/florges 0-4 (floette 5 but ot present)
               669,  #flabebe
               670,  #floette - 5 is eternal flower not in game
               671,  #florges
               678,  # meowstic
                705, #sligoo
                706, #goodra
                713, #avalugg
                720, #hoopa
                724, #decidueye
                741, #oricorio, 3 forms 0 1 2 3
                744, #rockruff
                745, #lycanroc: 2 forms 0 1 2
               774,  #minior
               778,  #mimikyu
               800,  #necrozma: 2 - 3 not in game
               801,  #magearna
               845,  #cramorant
                849, #toxtricity
               854,  #sineastea
               855,  # plteageist
               869,  #alcremie 8 forms
               875,  #Eiscue
               876,  #indeedee
               877,  #morpeko
               888,  #Zacian
               889,  #Zamazenta
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
                choice = random.randint(0, 9)
                # form 8 not in the game (Partner Let's Go Pikachu)
                while choice == 8:
                    choice = random.randint(0, 9)
                return choice
            case 52:
                choice = random.randint(0, 2)
                return choice
            case 80:
                choice = random.randint(0, 2)
                # form 1 not in the game (Mega Slowbro)
                while choice == 1:
                    choice = random.randint(0, 2)
                return choice
            case 128:
                choice = random.randint(0, 3)
                return choice
            case 386:
                choice = random.randint(0, 3)
                return choice
            case 479:
                choice = random.randint(0, 5)
                return choice
            case 493:
                choice = random.randint(0, 17)
                return choice
            case 550:
                choice = random.randint(0, 2)
                return choice
            case 585:
                choice = random.randint(0, 3)
                return choice
            case 586:
                choice = random.randint(0, 3)
                return choice
            case 646:
                choice = random.randint(0, 2)
                return choice
            case 664:
                choice = random.randint(0, 19)
                return choice
            case 665:
                choice = random.randint(0, 19)
                return choice
            case 666:
                choice = random.randint(0, 19)
                return choice
            case 669:
                choice = random.randint(0, 4)
                return choice
            case 670:
                choice = random.randint(0, 5)
                while choice == 5:
                    choice = random.randint(0, 5)
                return choice
            case 671:
                choice = random.randint(0, 4)
                return choice
            case 741:
                choice = random.randint(0, 3)
                return choice
            case 745:
                choice = random.randint(0, 2)
                return choice
            case 774: # includes shield downs form
                choice = random.randint(0, 13)
                return choice
            case 800:
                choice = random.randint(0, 3)
                while choice == 3:
                    choice = random.randint(0, 3)
                return choice
            case 845:
                choice = random.randint(0, 2)
                return choice
            case 869:
                choice = random.randint(0, 8)
                return choice
            case 898:
                choice = random.randint(0, 2)
                return choice
            case 952:
                choice = random.randint(0, 2)
                return choice
            case 960:
                choice = random.randint(0, 3)
                return choice
            case 1011:
                choice = random.randint(0, 3)
                return choice
            case _:
                choice = random.randint(0, 1)
                return choice
    else:
        return 0


def flip_starter_texture(starter_num: int):
    file = open(os.getcwd() + "/Randomizer/Starters/" +"pokemon_to_file.txt", "r")
    names = []
    for name in file:
        names.append(name)
    pokemon_file = fetch_devname(starter_num, names)
    print(starter_num)
    print(pokemon_file)
    # _00 - male
    # _01 - female
    # _51 and _52 - mega/primal forms
    # _61 - Alolan Form
    # _81 - GMAX form
    # _XX_31 - Galarian form
    # _XX_41 - Hisuian
    # _XX_51 - Paldean
    # _71_XX - Noble
    # --------------- 1X is only for non-regional forms
    # _11 - form0
    # _12 - form1
    # _13 - form2
    # _14 - form3
    # _XY - formZ./pokemon_clean/{pokemon_file}
    # Copies files of pokemon needed. Right now gets all - later only form specific
    shutil.copytree(os.getcwd() + "/Randomizer/Starters/" +f'pokemon_clean/{pokemon_file}',
                 os.getcwd() + "/Randomizer/Starters/" +f'output/romfs/pokemon/data/{pokemon_file}')
    current_check = os.getcwd() + "/Randomizer/Starters/" +f'output/romfs/pokemon/data/{pokemon_file}'
    i = 0
    for pokemonfolder in os.listdir(current_check):
        # print(pokemonfolder)
        pokemontextures_animations = current_check + "/" + pokemonfolder

        for files in os.listdir(pokemontextures_animations):
            if "rare" in files:
                # print(files)
                # print(files.replace("_rare", ''))
                replacedfile = files.replace("_rare", '')
                ogfiledir = pokemontextures_animations + "/" + f'{files}'
                newfiledir =pokemontextures_animations + "/" + f'{replacedfile}'
                #print(f'OG File Dir: {ogfiledir}')
                #print(f'New File Dir: {newfiledir}')
                shutil.copy2(ogfiledir, newfiledir)


def checkStarter1(config, pokedata):
    choice = 1021
    if isinstance(config['force_starter_1'], str) is True:
        pokeName = config['force_starter_1'].replace(" ", "")
        pokeName = pokeName.upper()
        for entries in pokedata['pokemons']:
            entryName = entries['name'].replace(" ", "")
            if entryName.upper() == pokeName:
                choice = entries['id']
                if choice in banned_pokemon:
                    print("Invalid argument for Starter 1 - Try again")
                    exit(0)
                else:
                    break
    elif isinstance(config['force_starter_1'], int) is True:
        choice = pokedata['pokemons'][config['force_starter_1']]['id']
        if choice in banned_pokemon:
            print("Invalid argument for Starter 1 - Try again")
            exit(0)
    else:
        print("Invalid argument for Starter 1 - Try again")
        exit(0)
    return choice


def checkStarter2(config, pokedata):
    choice = 1021
    if isinstance(config['force_starter_2'], str) is True:
        pokeName = config['force_starter_2'].replace(" ", "")
        pokeName = pokeName.upper()
        for entries in pokedata['pokemons']:
            entryName = entries['name'].replace(" ", "")
            if entryName.upper() == pokeName:
                choice = entries['id']
                if choice in banned_pokemon:
                    print("Invalid argument for Starter 1 - Try again")
                    exit(0)
                else:
                    break
    elif isinstance(config['force_starter_2'], int) is True:
        choice = pokedata['pokemons'][config['force_starter_2']]['id']
        if choice in banned_pokemon:
            print("Invalid argument for Starter 2 - Try again")
            exit(0)
    else:
        print("Invalid argument for Starter 2 - Try again")
        exit(0)

    return choice


def checkStarter3(config, pokedata):
    choice = 1021
    if isinstance(config['force_starter_3'], str) is True:
        pokeName = config['force_starter_3'].replace(" ", "")
        pokeName = pokeName.upper()
        for entries in pokedata['pokemons']:
            entryName = entries['name'].replace(" ", "")
            if entryName.upper() == pokeName:
                choice = entries['id']
                if choice in banned_pokemon:
                    print("Invalid argument for Starter 3 - Try again")
                    exit(0)
                else:
                    break
    elif isinstance(config['force_starter_3'], int) is True:
        choice = pokedata['pokemons'][config['force_starter_3']]['id']
        if choice in banned_pokemon:
            print("Invalid argument for Starter 3 - Try again")
            exit(0)
    else:
        print("Invalid argument for Starter 3 - Try again")
        exit(0)

    return choice


def randomize(config):
    if os.path.exists(os.getcwd() + "/Randomizer/Starters/" +f'output'):
        shutil.rmtree(os.getcwd() + "/Randomizer/Starters/" +f'output')
    file = open(os.getcwd() + "/Randomizer/Starters/" + "pokemon_list_info.json", 'r')
    pokedata = json.load(file)
    file.close()
    file = open(os.getcwd() + "/Randomizer/Starters/" +"eventAddPokemon_array_clean.json", "r")
    data = json.load(file)
    file.close()
    file = open(os.getcwd() + "/Randomizer/Starters/" +"pokemon_to_id.txt", "r")
    names = []
    for name in file:
        names.append(name)
    file.close()
    i = 1
    shinyforced = [0] * 3
    if config['ban_stage1_pokemon'] == "yes":
        bannedStages.extend(sharedVar.gen9Stage1)
    if config['ban_stage2_pokemon'] == "yes":
        bannedStages.extend(sharedVar.gen9Stage2)
    if config['ban_singlestage_pokemon'] == "yes":
        bannedStages.extend(sharedVar.no_evolution)
    if config['force_one_starter_to_be_shiny'] == "yes":
        choice = random.randint(0,2)
        shinyforced[choice] = 1

    for entry in data['values']:
        if config['randomize_all_gifts'] == "no":  # only starters
            if "common_0065_hono" in entry['label'] and config['force_starter_3'] != 0:
                choice = checkStarter3(config, pokedata)

                entry['pokeData']['devId'] = fetch_devname(choice, names)
                alt_form_choosen = get_alt_form(choice)
                entry['pokeData']['formId'] = alt_form_choosen

                # Hard code tera types for ogerpon and terapagos so that they don't break.
                if config['randomize_tera_type'] == "yes":
                    entry['pokeData']['gemType'] = tera_types[random.randint(0, len(tera_types) - 1)].upper()

                    match choice:
                        case 1011:
                            match alt_form_choosen:
                                case 0:
                                    entry['pokeData']['gemType'] = "KUSA"
                                    pass
                                case 1:
                                    entry['pokeData']['gemType'] = "MIZU"
                                    pass
                                case 2:
                                    entry['pokeData']['gemType'] = "HONOO"
                                    pass
                                case 3:
                                    entry['pokeData']['gemType'] = "IWA"
                                    pass
                        case 1021:
                            entry['pokeData']['gemType'] = "NIJI"
                        case _:
                            pass

                if config['all_shiny'] == "yes" or shinyforced[2] == 1:
                    entry['pokeData']['rareType'] = "RARE"
                    if config['shiny_overworld'] == "yes":
                        flip_starter_texture(choice)
                elif config['higher_shiny_chance'] == "yes":
                    chance = random.randint(1, 10)
                    if chance == 10:
                        entry['pokeData']['rareType'] = "RARE"
                        if config['shiny_overworld'] == "yes":
                            flip_starter_texture(choice)
                    else:
                        entry['pokeData']['rareType'] = "NO_RARE"
            elif "common_0065_hono" in entry['label'] and config['force_starter_3'] == 0:
                choice = random.randint(1, 1025)

                while choice in banned_pokemon or choice in picked_starters or pokedata['pokemons'][choice]['natdex'] in bannedStages:
                    choice = random.randint(1, 1025)

                if config['only_legends'] == "yes":
                    val = random.randint(0, len(legends) - 1)
                    choice = legends[val]
                    while choice in banned_pokemon or choice in picked_starters:
                        val = random.randint(0, len(legends) - 1)
                        choice = legends[val]
                if config['only_paradox'] == "yes":
                    val = random.randint(0, len(paradox) - 1)
                    choice = paradox[val]
                    while choice in banned_pokemon or choice in picked_starters:
                        val = random.randint(0, len(paradox) - 1)
                        choice = paradox[val]
                if config['only_legends_and_paradox'] == "yes":
                    val = random.randint(0, len(legends_and_paradox) - 1)
                    choice = legends_and_paradox[val]
                    while choice in banned_pokemon or choice in picked_starters:
                        val = random.randint(0, len(legends_and_paradox) - 1)
                        choice = legends_and_paradox[val]

                if choice not in picked_starters:
                    entry['pokeData']['devId'] = fetch_devname(choice, names)
                    alt_form_choosen = get_alt_form(choice)
                    entry['pokeData']['formId'] = alt_form_choosen

                    # Hard code tera types for ogerpon and terapagos so that they don't break.
                    if config['randomize_tera_type'] == "yes":
                        entry['pokeData']['gemType'] = tera_types[random.randint(0, len(tera_types) - 1)].upper()

                        match choice:
                            case 1011:
                                match alt_form_choosen:
                                    case 0:
                                        entry['pokeData']['gemType'] = "KUSA"
                                        pass
                                    case 1:
                                        entry['pokeData']['gemType'] = "MIZU"
                                        pass
                                    case 2:
                                        entry['pokeData']['gemType'] = "HONOO"
                                        pass
                                    case 3:
                                        entry['pokeData']['gemType'] = "IWA"
                                        pass
                            case 1021:
                                entry['pokeData']['gemType'] = "NIJI"
                            case _:
                                pass

                    if config['all_shiny'] == "yes" or shinyforced[2] == 1:
                        entry['pokeData']['rareType'] = "RARE"
                        if config['shiny_overworld'] == "yes":
                            flip_starter_texture(choice)
                    elif config['higher_shiny_chance'] == "yes":
                        chance = random.randint(1, 10)
                        if chance == 10:
                            entry['pokeData']['rareType'] = "RARE"
                            if config['shiny_overworld'] == "yes":
                                flip_starter_texture(choice)
                        else:
                            entry['pokeData']['rareType'] = "NO_RARE"
                    picked_starters.append(choice)
            if "common_0065_mizu" in entry['label'] and config['force_starter_2'] != 0:
                choice = checkStarter2(config, pokedata)

                entry['pokeData']['devId'] = fetch_devname(choice, names)
                alt_form_choosen = get_alt_form(choice)
                entry['pokeData']['formId'] = alt_form_choosen

                # Hard code tera types for ogerpon and terapagos so that they don't break.
                if config['randomize_tera_type'] == "yes":
                    entry['pokeData']['gemType'] = tera_types[random.randint(0, len(tera_types) - 1)].upper()

                    match choice:
                        case 1011:
                            match alt_form_choosen:
                                case 0:
                                    entry['pokeData']['gemType'] = "KUSA"
                                    pass
                                case 1:
                                    entry['pokeData']['gemType'] = "MIZU"
                                    pass
                                case 2:
                                    entry['pokeData']['gemType'] = "HONOO"
                                    pass
                                case 3:
                                    entry['pokeData']['gemType'] = "IWA"
                                    pass
                        case 1021:
                            entry['pokeData']['gemType'] = "NIJI"
                        case _:
                            pass

                if config['all_shiny'] == "yes" or shinyforced[1] == 1:
                    entry['pokeData']['rareType'] = "RARE"
                    if config['shiny_overworld'] == "yes":
                        flip_starter_texture(choice)
                elif config['higher_shiny_chance'] == "yes":
                    chance = random.randint(1, 10)
                    if chance == 10:
                        entry['pokeData']['rareType'] = "RARE"
                        if config['shiny_overworld'] == "yes":
                            flip_starter_texture(choice)
                    else:
                        entry['pokeData']['rareType'] = "NO_RARE"
            elif "common_0065_mizu" in entry['label'] and config['force_starter_2'] == 0:
                choice = random.randint(1, 1025)
                while choice in banned_pokemon or choice in picked_starters or pokedata['pokemons'][choice]['natdex'] in bannedStages:
                    choice = random.randint(1, 1025)

                if config['only_legends'] == "yes":
                    val = random.randint(0, len(legends) - 1)
                    choice = legends[val]
                    while choice in banned_pokemon or choice in picked_starters:
                        val = random.randint(0, len(legends) - 1)
                        choice = legends[val]
                if config['only_paradox'] == "yes":
                    val = random.randint(0, len(paradox) - 1)
                    choice = paradox[val]
                    while choice in banned_pokemon or choice in picked_starters:
                        val = random.randint(0, len(paradox) - 1)
                        choice = paradox[val]
                if config['only_legends_and_paradox'] == "yes":
                    val = random.randint(0, len(legends_and_paradox) - 1)
                    choice = legends_and_paradox[val]
                    while choice in banned_pokemon or choice in picked_starters:
                        val = random.randint(0, len(legends_and_paradox) - 1)
                        choice = legends_and_paradox[val]

                if choice not in picked_starters:
                    entry['pokeData']['devId'] = fetch_devname(choice, names)
                    alt_form_choosen = get_alt_form(choice)
                    entry['pokeData']['formId'] = alt_form_choosen

                    # Hard code tera types for ogerpon and terapagos so that they don't break.
                    if config['randomize_tera_type'] == "yes":
                        entry['pokeData']['gemType'] = tera_types[random.randint(0, len(tera_types) - 1)].upper()

                        match choice:
                            case 1011:
                                match alt_form_choosen:
                                    case 0:
                                        entry['pokeData']['gemType'] = "KUSA"
                                        pass
                                    case 1:
                                        entry['pokeData']['gemType'] = "MIZU"
                                        pass
                                    case 2:
                                        entry['pokeData']['gemType'] = "HONOO"
                                        pass
                                    case 3:
                                        entry['pokeData']['gemType'] = "IWA"
                                        pass
                            case 1021:
                                entry['pokeData']['gemType'] = "NIJI"
                            case _:
                                pass

                    if config['all_shiny'] == "yes" or shinyforced[1] == 1:
                        entry['pokeData']['rareType'] = "RARE"
                        if config['shiny_overworld'] == "yes":
                            flip_starter_texture(choice)
                    elif config['higher_shiny_chance'] == "yes":
                        chance = random.randint(1, 10)
                        if chance == 10:
                            entry['pokeData']['rareType'] = "RARE"
                            if config['shiny_overworld'] == "yes":
                                flip_starter_texture(choice)
                        else:
                            entry['pokeData']['rareType'] = "NO_RARE"
                    picked_starters.append(choice)
            if "common_0065_kusa" in entry['label'] and config['force_starter_1'] != 0:
                choice = checkStarter1(config, pokedata)

                entry['pokeData']['devId'] = fetch_devname(choice, names)
                alt_form_choosen = get_alt_form(choice)
                entry['pokeData']['formId'] = alt_form_choosen

                # Hard code tera types for ogerpon and terapagos so that they don't break.
                if config['randomize_tera_type'] == "yes":
                    entry['pokeData']['gemType'] = tera_types[random.randint(0, len(tera_types) - 1)].upper()

                    match choice:
                        case 1011:
                            match alt_form_choosen:
                                case 0:
                                    entry['pokeData']['gemType'] = "KUSA"
                                    pass
                                case 1:
                                    entry['pokeData']['gemType'] = "MIZU"
                                    pass
                                case 2:
                                    entry['pokeData']['gemType'] = "HONOO"
                                    pass
                                case 3:
                                    entry['pokeData']['gemType'] = "IWA"
                                    pass
                        case 1021:
                            entry['pokeData']['gemType'] = "NIJI"
                        case _:
                            pass

                if config['all_shiny'] == "yes" or shinyforced[0] == 1:
                    entry['pokeData']['rareType'] = "RARE"
                    if config['shiny_overworld'] == "yes":
                        flip_starter_texture(choice)
                elif config['higher_shiny_chance'] == "yes":
                    chance = random.randint(1, 10)
                    if chance == 10:
                        entry['pokeData']['rareType'] = "RARE"
                        if config['shiny_overworld'] == "yes":
                            flip_starter_texture(choice)
                    else:
                        entry['pokeData']['rareType'] = "NO_RARE"
            elif "common_0065_kusa" in entry['label'] and config['force_starter_1'] == 0:
                choice = random.randint(1, 1025)
                while choice in banned_pokemon or choice in picked_starters or pokedata['pokemons'][choice]['natdex'] in bannedStages:
                    choice = random.randint(1, 1025)

                if config['only_legends'] == "yes":
                    val = random.randint(0, len(legends) - 1)
                    choice = legends[val]
                    while choice in banned_pokemon or choice in picked_starters:
                        val = random.randint(0, len(legends) - 1)
                        choice = legends[val]
                if config['only_paradox'] == "yes":
                    val = random.randint(0, len(paradox) - 1)
                    choice = paradox[val]
                    while choice in banned_pokemon or choice in picked_starters:
                        val = random.randint(0, len(paradox) - 1)
                        choice = paradox[val]
                if config['only_legends_and_paradox'] == "yes":
                    val = random.randint(0, len(legends_and_paradox) - 1)
                    choice = legends_and_paradox[val]
                    while choice in banned_pokemon or choice in picked_starters:
                        val = random.randint(0, len(legends_and_paradox) - 1)
                        choice = legends_and_paradox[val]

                if choice not in picked_starters:
                    entry['pokeData']['devId'] = fetch_devname(choice, names)
                    alt_form_choosen = get_alt_form(choice)
                    entry['pokeData']['formId'] = alt_form_choosen

                    # Hard code tera types for ogerpon and terapagos so that they don't break.
                    if config['randomize_tera_type'] == "yes":
                        entry['pokeData']['gemType'] = tera_types[random.randint(0, len(tera_types) - 1)].upper()

                        match choice:
                            case 1011:
                                match alt_form_choosen:
                                    case 0:
                                        entry['pokeData']['gemType'] = "KUSA"
                                        pass
                                    case 1:
                                        entry['pokeData']['gemType'] = "MIZU"
                                        pass
                                    case 2:
                                        entry['pokeData']['gemType'] = "HONOO"
                                        pass
                                    case 3:
                                        entry['pokeData']['gemType'] = "IWA"
                                        pass
                            case 1021:
                                entry['pokeData']['gemType'] = "NIJI"
                            case _:
                                pass

                    if config['all_shiny'] == "yes" or shinyforced[0] == 1:
                        entry['pokeData']['rareType'] = "RARE"
                        if config['shiny_overworld'] == "yes":
                            flip_starter_texture(choice)
                    elif config['higher_shiny_chance'] == "yes":
                        chance = random.randint(1, 10)
                        if chance == 10:
                            entry['pokeData']['rareType'] = "RARE"
                            if config['shiny_overworld'] == "yes":
                                flip_starter_texture(choice)
                        else:
                            entry['pokeData']['rareType'] = "NO_RARE"
                    picked_starters.append(choice)

        else:  # everything plus starters
            if "common_0065" not in entry['label']:
                choice = random.randint(1, 1025)
                while choice in banned_pokemon or pokedata['pokemons'][choice]['natdex'] in bannedStages:
                    choice = random.randint(1, 1025)


                if config['only_legends'] == "yes":
                    val = random.randint(0, len(legends)-1)
                    choice = legends[val]
                    while choice in banned_pokemon or choice in picked_starters:
                        val = random.randint(0, len(legends)-1)
                        choice = legends[val]
                if config['only_paradox'] == "yes":
                    val = random.randint(0, len(paradox)-1)
                    choice = paradox[val]
                    while choice in banned_pokemon or choice in picked_starters:
                        val = random.randint(0, len(paradox)-1)
                        choice = paradox[val]
                if config['only_legends_and_paradox'] == "yes":
                    val = random.randint(0, len(legends_and_paradox)-1)
                    choice = legends_and_paradox[val]
                    while choice in banned_pokemon or choice in picked_starters:
                        val = random.randint(0, len(legends_and_paradox)-1)
                        choice = legends_and_paradox[val]

                entry['pokeData']['devId'] = fetch_devname(choice, names)
                entry['pokeData']['formId'] = get_alt_form(choice)

                if config['all_shiny'] == "yes":
                    entry['pokeData']['rareType'] = "RARE"
                elif config['higher_shiny_chance'] == "yes":
                    chance = random.randint(0, 10)
                    if chance == 10:
                        entry['pokeData']['rareType'] = "RARE"
                    else:
                        entry['pokeData']['rareType'] = "NO_RARE"

                if config['randomize_tera_type'] == "yes":
                    entry['pokeData']['gemType'] = tera_types[random.randint(0, len(tera_types) - 1)].upper()

                    match choice:
                        case 1011:
                            match alt_form_choosen:
                                case 0:
                                    entry['pokeData']['gemType'] = "KUSA"
                                    pass
                                case 1:
                                    entry['pokeData']['gemType'] = "MIZU"
                                    pass
                                case 2:
                                    entry['pokeData']['gemType'] = "HONOO"
                                    pass
                                case 3:
                                    entry['pokeData']['gemType'] = "IWA"
                                    pass
                        case 1021:
                            entry['pokeData']['gemType'] = "NIJI"
                        case _:
                            pass
            if "common_0065_hono" in entry['label'] and config['force_starter_3'] != 0:
                choice = checkStarter3(config, pokedata)

                entry['pokeData']['devId'] = fetch_devname(choice, names)
                alt_form_choosen = get_alt_form(choice)
                entry['pokeData']['formId'] = alt_form_choosen

                # Hard code tera types for ogerpon and terapagos so that they don't break.
                if config['randomize_tera_type'] == "yes":
                    entry['pokeData']['gemType'] = tera_types[random.randint(0, len(tera_types) - 1)].upper()

                    match choice:
                        case 1011:
                            match alt_form_choosen:
                                case 0:
                                    entry['pokeData']['gemType'] = "KUSA"
                                    pass
                                case 1:
                                    entry['pokeData']['gemType'] = "MIZU"
                                    pass
                                case 2:
                                    entry['pokeData']['gemType'] = "HONOO"
                                    pass
                                case 3:
                                    entry['pokeData']['gemType'] = "IWA"
                                    pass
                        case 1021:
                            entry['pokeData']['gemType'] = "NIJI"
                        case _:
                            pass

                if config['all_shiny'] == "yes" or shinyforced[2] == 1:
                    entry['pokeData']['rareType'] = "RARE"
                    if config['shiny_overworld'] == "yes":
                        flip_starter_texture(choice)
                elif config['higher_shiny_chance'] == "yes":
                    chance = random.randint(1, 10)
                    if chance == 10:
                        entry['pokeData']['rareType'] = "RARE"
                        if config['shiny_overworld'] == "yes":
                            flip_starter_texture(choice)
                    else:
                        entry['pokeData']['rareType'] = "NO_RARE"
            elif "common_0065_hono" in entry['label'] and config['force_starter_3'] == 0:
                choice = random.randint(1, 1025)
                while choice in banned_pokemon or choice in picked_starters or pokedata['pokemons'][choice]['natdex'] in bannedStages:
                    choice = random.randint(1, 1025)
                if config['only_legends'] == "yes":
                    val = random.randint(0, len(legends) - 1)
                    choice = legends[val]
                    while choice in banned_pokemon or choice in picked_starters:
                        val = random.randint(0, len(legends) - 1)
                        choice = legends[val]
                if config['only_paradox'] == "yes":
                    val = random.randint(0, len(paradox) - 1)
                    choice = paradox[val]
                    while choice in banned_pokemon or choice in picked_starters:
                        val = random.randint(0, len(paradox) - 1)
                        choice = paradox[val]
                if config['only_legends_and_paradox'] == "yes":
                    val = random.randint(0, len(legends_and_paradox) - 1)
                    choice = legends_and_paradox[val]
                    while choice in banned_pokemon or choice in picked_starters:
                        val = random.randint(0, len(legends_and_paradox) - 1)
                        choice = legends_and_paradox[val]

                if choice not in picked_starters:
                    entry['pokeData']['devId'] = fetch_devname(choice, names)
                    alt_form_choosen = get_alt_form(choice)
                    entry['pokeData']['formId'] = alt_form_choosen

                    # Hard code tera types for ogerpon and terapagos so that they don't break.
                    if config['randomize_tera_type'] == "yes":
                        entry['pokeData']['gemType'] = tera_types[random.randint(0, len(tera_types) - 1)].upper()

                        match choice:
                            case 1011:
                                match alt_form_choosen:
                                    case 0:
                                        entry['pokeData']['gemType'] = "KUSA"
                                        pass
                                    case 1:
                                        entry['pokeData']['gemType'] = "MIZU"
                                        pass
                                    case 2:
                                        entry['pokeData']['gemType'] = "HONOO"
                                        pass
                                    case 3:
                                        entry['pokeData']['gemType'] = "IWA"
                                        pass
                            case 1021:
                                entry['pokeData']['gemType'] = "NIJI"
                            case _:
                                pass

                    if config['all_shiny'] == "yes" or shinyforced[2] == 1:
                        entry['pokeData']['rareType'] = "RARE"
                        if config['shiny_overworld'] == "yes":
                            flip_starter_texture(choice)
                    elif config['higher_shiny_chance'] == "yes":
                        chance = random.randint(1, 10)
                        if chance == 10:
                            entry['pokeData']['rareType'] = "RARE"
                            if config['shiny_overworld'] == "yes":
                                flip_starter_texture(choice)
                        else:
                            entry['pokeData']['rareType'] = "NO_RARE"
                    picked_starters.append(choice)
            if "common_0065_mizu" in entry['label'] and config['force_starter_2'] != 0:
                choice = checkStarter2(config, pokedata)

                entry['pokeData']['devId'] = fetch_devname(choice, names)
                alt_form_choosen = get_alt_form(choice)
                entry['pokeData']['formId'] = alt_form_choosen

                # Hard code tera types for ogerpon and terapagos so that they don't break.
                if config['randomize_tera_type'] == "yes":
                    entry['pokeData']['gemType'] = tera_types[random.randint(0, len(tera_types) - 1)].upper()

                    match choice:
                        case 1011:
                            match alt_form_choosen:
                                case 0:
                                    entry['pokeData']['gemType'] = "KUSA"
                                    pass
                                case 1:
                                    entry['pokeData']['gemType'] = "MIZU"
                                    pass
                                case 2:
                                    entry['pokeData']['gemType'] = "HONOO"
                                    pass
                                case 3:
                                    entry['pokeData']['gemType'] = "IWA"
                                    pass
                        case 1021:
                            entry['pokeData']['gemType'] = "NIJI"
                        case _:
                            pass

                if config['all_shiny'] == "yes" or shinyforced[1] == 1:
                    entry['pokeData']['rareType'] = "RARE"
                    if config['shiny_overworld'] == "yes":
                        flip_starter_texture(choice)
                elif config['higher_shiny_chance'] == "yes":
                    chance = random.randint(1, 10)
                    if chance == 10:
                        entry['pokeData']['rareType'] = "RARE"
                        if config['shiny_overworld'] == "yes":
                            flip_starter_texture(choice)
                    else:
                        entry['pokeData']['rareType'] = "NO_RARE"
            elif "common_0065_mizu" in entry['label'] and config['force_starter_2'] == 0:
                choice = random.randint(1, 1025)
                while choice in banned_pokemon or choice in picked_starters or pokedata['pokemons'][choice]['natdex'] in bannedStages:
                    choice = random.randint(1, 1025)

                if config['only_legends'] == "yes":
                    val = random.randint(0, len(legends) - 1)
                    choice = legends[val]
                    while choice in banned_pokemon or choice in picked_starters:
                        val = random.randint(0, len(legends) - 1)
                        choice = legends[val]
                if config['only_paradox'] == "yes":
                    val = random.randint(0, len(paradox) - 1)
                    choice = paradox[val]
                    while choice in banned_pokemon or choice in picked_starters:
                        val = random.randint(0, len(paradox) - 1)
                        choice = paradox[val]
                if config['only_legends_and_paradox'] == "yes":
                    val = random.randint(0, len(legends_and_paradox) - 1)
                    choice = legends_and_paradox[val]
                    while choice in banned_pokemon or choice in picked_starters:
                        val = random.randint(0, len(legends_and_paradox) - 1)
                        choice = legends_and_paradox[val]

                if choice not in picked_starters:
                    entry['pokeData']['devId'] = fetch_devname(choice, names)
                    alt_form_choosen = get_alt_form(choice)
                    entry['pokeData']['formId'] = alt_form_choosen

                    # Hard code tera types for ogerpon and terapagos so that they don't break.
                    if config['randomize_tera_type'] == "yes":
                        entry['pokeData']['gemType'] = tera_types[random.randint(0, len(tera_types) - 1)].upper()

                        match choice:
                            case 1011:
                                match alt_form_choosen:
                                    case 0:
                                        entry['pokeData']['gemType'] = "KUSA"
                                        pass
                                    case 1:
                                        entry['pokeData']['gemType'] = "MIZU"
                                        pass
                                    case 2:
                                        entry['pokeData']['gemType'] = "HONOO"
                                        pass
                                    case 3:
                                        entry['pokeData']['gemType'] = "IWA"
                                        pass
                            case 1021:
                                entry['pokeData']['gemType'] = "NIJI"
                            case _:
                                pass

                    if config['all_shiny'] == "yes" or shinyforced[1] == 1:
                        entry['pokeData']['rareType'] = "RARE"
                        if config['shiny_overworld'] == "yes":
                            flip_starter_texture(choice)
                    elif config['higher_shiny_chance'] == "yes":
                        chance = random.randint(1, 10)
                        if chance == 10:
                            entry['pokeData']['rareType'] = "RARE"
                            if config['shiny_overworld'] == "yes":
                                flip_starter_texture(choice)
                        else:
                            entry['pokeData']['rareType'] = "NO_RARE"
                    picked_starters.append(choice)
            if "common_0065_kusa" in entry['label'] and config['force_starter_1'] != 0:
                choice = checkStarter1(config, pokedata)

                entry['pokeData']['devId'] = fetch_devname(choice, names)
                alt_form_choosen = get_alt_form(choice)
                entry['pokeData']['formId'] = alt_form_choosen

                # Hard code tera types for ogerpon and terapagos so that they don't break.
                if config['randomize_tera_type'] == "yes":
                    entry['pokeData']['gemType'] = tera_types[random.randint(0, len(tera_types) - 1)].upper()

                    match choice:
                        case 1011:
                            match alt_form_choosen:
                                case 0:
                                    entry['pokeData']['gemType'] = "KUSA"
                                    pass
                                case 1:
                                    entry['pokeData']['gemType'] = "MIZU"
                                    pass
                                case 2:
                                    entry['pokeData']['gemType'] = "HONOO"
                                    pass
                                case 3:
                                    entry['pokeData']['gemType'] = "IWA"
                                    pass
                        case 1021:
                            entry['pokeData']['gemType'] = "NIJI"
                        case _:
                            pass

                if config['all_shiny'] == "yes" or shinyforced[0] == 1:
                    entry['pokeData']['rareType'] = "RARE"
                    if config['shiny_overworld'] == "yes":
                        flip_starter_texture(choice)
                elif config['higher_shiny_chance'] == "yes":
                    chance = random.randint(1, 10)
                    if chance == 10:
                        entry['pokeData']['rareType'] = "RARE"
                        if config['shiny_overworld'] == "yes":
                            flip_starter_texture(choice)
                    else:
                        entry['pokeData']['rareType'] = "NO_RARE"
            elif "common_0065_kusa" in entry['label'] and config['force_starter_1'] == 0:
                choice = random.randint(1, 1025)
                while choice in banned_pokemon or choice in picked_starters or pokedata['pokemons'][choice]['natdex'] in bannedStages:
                    choice = random.randint(1, 1025)

                if config['only_legends'] == "yes":
                    val = random.randint(0, len(legends) - 1)
                    choice = legends[val]
                    while choice in banned_pokemon or choice in picked_starters:
                        val = random.randint(0, len(legends) - 1)
                        choice = legends[val]
                if config['only_paradox'] == "yes":
                    val = random.randint(0, len(paradox) - 1)
                    choice = paradox[val]
                    while choice in banned_pokemon or choice in picked_starters:
                        val = random.randint(0, len(paradox) - 1)
                        choice = paradox[val]
                if config['only_legends_and_paradox'] == "yes":
                    val = random.randint(0, len(legends_and_paradox) - 1)
                    choice = legends_and_paradox[val]
                    while choice in banned_pokemon or choice in picked_starters:
                        val = random.randint(0, len(legends_and_paradox) - 1)
                        choice = legends_and_paradox[val]

                if choice not in picked_starters:
                    entry['pokeData']['devId'] = fetch_devname(choice, names)
                    alt_form_choosen = get_alt_form(choice)
                    entry['pokeData']['formId'] = alt_form_choosen

                    # Hard code tera types for ogerpon and terapagos so that they don't break.
                    if config['randomize_tera_type'] == "yes":
                        entry['pokeData']['gemType'] = tera_types[random.randint(0, len(tera_types) - 1)].upper()

                        match choice:
                            case 1011:
                                match alt_form_choosen:
                                    case 0:
                                        entry['pokeData']['gemType'] = "KUSA"
                                        pass
                                    case 1:
                                        entry['pokeData']['gemType'] = "MIZU"
                                        pass
                                    case 2:
                                        entry['pokeData']['gemType'] = "HONOO"
                                        pass
                                    case 3:
                                        entry['pokeData']['gemType'] = "IWA"
                                        pass
                            case 1021:
                                entry['pokeData']['gemType'] = "NIJI"
                            case _:
                                pass

                    if config['all_shiny'] == "yes" or shinyforced[0] == 1:
                        entry['pokeData']['rareType'] = "RARE"
                        if config['shiny_overworld'] == "yes":
                            flip_starter_texture(choice)
                    elif config['higher_shiny_chance'] == "yes":
                        chance = random.randint(1, 10)
                        if chance == 10:
                            entry['pokeData']['rareType'] = "RARE"
                            if config['shiny_overworld'] == "yes":
                                flip_starter_texture(choice)
                        else:
                            entry['pokeData']['rareType'] = "NO_RARE"
                    picked_starters.append(choice)

        entry['pokeData']['wazaType'] = "DEFAULT"
        entry['pokeData']['waza1']['wazaId'] = "WAZA_NULL"
        entry['pokeData']['waza2']['wazaId'] = "WAZA_NULL"
        entry['pokeData']['waza3']['wazaId'] = "WAZA_NULL"
        entry['pokeData']['waza4']['wazaId'] = "WAZA_NULL"

    print(picked_starters)
    outdata = json.dumps(data, indent=4)
    with open(os.getcwd() + "/Randomizer/Starters/" +"eventAddPokemon_array.json", 'w') as outfile:
        outfile.write(outdata)
    print("Randomisation Of Starter Pokemon Done !")


def main():
   randomize()


if __name__ == "__main__":
    main()
