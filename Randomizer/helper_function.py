import os
import platform
import subprocess
import json
import Randomizer.shared_Variables as SharedVariables
import random


def get_alternate_form(index: int):
    if index in SharedVariables.has_alternate_form: #previously, we just shuffled around. Now we include all species, so we need more edge cases
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
                choice = random.randint(0, 2)
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
            case 978:
                choice = random.randint(0, 2)
                return choice
            case 931:
                choice = random.randint(0, 3)
                return choice
            case 1017:
                choice = random.randint(0, 3)
                return choice
            case _:
                choice = random.randint(0, 1)
                return choice
    else:
        return 0


def check_generation_limiter(allowed_generations: list):
    allowed_pokemon = []
    allowed_legends = []
    if len(allowed_generations) == 0:
        allowed_pokemon.extend(SharedVariables.gen1)
        allowed_legends.extend(SharedVariables.gen1_legends)
        allowed_pokemon.extend(SharedVariables.gen2)
        allowed_legends.extend(SharedVariables.gen2_legends)
        allowed_pokemon.extend(SharedVariables.gen3)
        allowed_legends.extend(SharedVariables.gen3_legends)
        allowed_pokemon.extend(SharedVariables.gen4)
        allowed_legends.extend(SharedVariables.gen4_legends)
        allowed_pokemon.extend(SharedVariables.gen5)
        allowed_legends.extend(SharedVariables.gen5_legends)
        allowed_pokemon.extend(SharedVariables.gen6)
        allowed_legends.extend(SharedVariables.gen6_legends)
        allowed_pokemon.extend(SharedVariables.gen7)
        allowed_legends.extend(SharedVariables.UB)
        allowed_legends.extend(SharedVariables.gen7_legends)
        allowed_pokemon.extend(SharedVariables.gen8)
        allowed_legends.extend(SharedVariables.gen8_legends)
        allowed_pokemon.extend(SharedVariables.gen9)
        allowed_legends.extend(SharedVariables.paradox)
        allowed_legends.extend(SharedVariables.gen9_legends)
    else:
        in_array = [0] * 9
        for generations in allowed_generations:
            match generations:
                case 1:
                    if in_array[0] == 1:
                        print("Duplicate Generation 1")
                        exit(0)
                    allowed_pokemon.extend(SharedVariables.gen1)
                    allowed_legends.extend(SharedVariables.gen1_legends)
                    in_array[0] = 1
                    continue
                case 2:
                    if in_array[1] == 1:
                        print("Duplicate Generation 2")
                        exit(0)
                    allowed_pokemon.extend(SharedVariables.gen2)
                    allowed_legends.extend(SharedVariables.gen2_legends)
                    in_array[1] = 1
                    continue
                case 3:
                    if in_array[2] == 1:
                        print("Duplicate Generation 3")
                        exit(0)
                    allowed_pokemon.extend(SharedVariables.gen3)
                    allowed_legends.extend(SharedVariables.gen3_legends)
                    in_array[2] = 1
                    continue
                case 4:
                    if in_array[3] == 1:
                        print("Duplicate Generation 4")
                        exit(0)
                    allowed_pokemon.extend(SharedVariables.gen4)
                    allowed_legends.extend(SharedVariables.gen4_legends)
                    in_array[3] = 1
                    continue
                case 5:
                    if in_array[4] == 1:
                        print("Duplicate Generation 5")
                        exit(0)
                    allowed_pokemon.extend(SharedVariables.gen5)
                    allowed_legends.extend(SharedVariables.gen5_legends)
                    in_array[4] = 1
                    continue
                case 6:
                    if in_array[5] == 1:
                        print("Duplicate Generation 6")
                        exit(0)
                    allowed_pokemon.extend(SharedVariables.gen6)
                    allowed_legends.extend(SharedVariables.gen6_legends)
                    in_array[5] = 1
                    continue
                case 7:
                    if in_array[6] == 1:
                        print("Duplicate Generation 7")
                        exit(0)
                    allowed_pokemon.extend(SharedVariables.gen7)
                    allowed_legends.extend(SharedVariables.UB)
                    allowed_legends.extend(SharedVariables.gen7_legends)
                    in_array[6] = 1
                    continue
                case 8:
                    if in_array[7] == 1:
                        print("Duplicate Generation 8")
                        exit(0)
                    allowed_pokemon.extend(SharedVariables.gen8)
                    allowed_legends.extend(SharedVariables.gen8_legends)
                    in_array[7] = 1
                    continue
                case 9:
                    if in_array[8] == 1:
                        print("Duplicate Generation 9")
                        exit(0)
                    allowed_pokemon.extend(SharedVariables.gen9)
                    allowed_legends.extend(SharedVariables.paradox)
                    allowed_legends.extend(SharedVariables.gen9_legends)
                    in_array[8] = 1
                    continue
                case _:
                    print("Invalid Generation")
                    exit(0)
    return allowed_pokemon, allowed_legends


def get_pokemon_item_form(index: int, form: int):
    if index in SharedVariables.paradox and index != 1007 and index != 1008 and index != 1024:
        return "ITEMID_BUUSUTOENAJII", 25

    match index:
        case 25:
            return "ITEMID_DENKIDAMA", 5
        case 113:
            return "ITEMID_MANMARUISI", 30
        case 242:
            return "ITEMID_MANMARUISI", 30
        case 283:
            return "ITEMID_AMAIMITU", 5
        case 285:
            return "ITEMID_TIISANAKINOKO", 5
        case 286:
            return "ITEMID_TIISANAKINOKO", 30
        case 316:
            return "ITEMID_ORENNOMI", 30
        case 317:
            return "ITEMID_OBONNOMI", 5
        case 415:
            return "ITEMID_AMAIMITU", 30
        case 440:
            return "ITEMID_MANMARUISI", 5
        case 590:
            return "ITEMID_TIISANAKINOKO", 5
        case 591:
            return "ITEMID_TIISANAKINOKO", 30
        case 625:
            return "ITEMID_KASIRANOAKASI", 100
        case 734:
            return "ITEMID_MOMONNOMI", 5
        case 739:
            return "ITEMID_NANASINOMI", 5
        case 740:
            return "ITEMID_KURABONOMI", 5
        case 741:
            return "ITEMID_YAMABUKINOMITU", 5
        case 778:
            return "ITEMID_KAGONOMI", 5
        case 819:
            return "ITEMID_ORENNOMI", 5
        case 948:
            return "ITEMID_TIISANAKINOKO", 5
        case 949:
            return "ITEMID_TIISANAKINOKO", 30
        case 483:
            if form == 1:
                return "ITEMID_DAIKONGOUDAMA", 100
        case 484:
            if form == 1:
                return "ITEMID_DAISIRATAMA", 100
        case 487:
            if form == 1:
                return "ITEMID_DAIHAKKINDAMA", 100
        case 493:
            match form:
                case 1:  # Fightning
                    return "ITEMID_KOBUSINOPUREETO", 100
                case 2:  # Flying
                    return "ITEMID_AOZORAPUREETO", 100
                case 3:  # poison
                    return "ITEMID_MOUDOKUPUREETO", 100
                case 4:  # ground
                    return "ITEMID_DAITINOPUREETO", 100
                case 5:  # rock
                    return "ITEMID_GANSEKIPUREETO", 100
                case 6:  # bug
                    return "ITEMID_TAMAMUSIPUREETO", 100
                case 7:  # ghost
                    return "ITEMID_MONONOKEPUREETO", 100
                case 8:  # steel
                    return "ITEMID_KOUTETUPUREETO", 100
                case 9:  # fire
                    return "ITEMID_HINOTAMAPUREETO", 100
                case 10:  # water
                    return "ITEMID_SIZUKUPUREETO", 100
                case 11:  # grass
                    return "ITEMID_MIDORINOPUREETO", 100
                case 12:  # electric
                    return "ITEMID_IKAZUTIPUREETO", 100
                case 13:  # psychic
                    return "ITEMID_HUSIGINOPUREETO", 100
                case 14:  # ice
                    return "ITEMID_TURARANOPUREETO", 100
                case 15:  # dragon
                    return "ITEMID_RYUUNOPUREETO", 100
                case 16:  # dark
                    return "ITEMID_KOWAMOTEPUREETO", 100
                case 17:  # Fairy
                    return "ITEMID_SEIREIPUREETO", 100
        case 888:
            if form == 1:
                return "ITEMID_KUTITATURUGI", 100
        case 889:
            if form == 1:
                return "ITEMID_KUTITATATE", 100
        case 1017:
            match form:
                case 1:
                    return "ITEMID_ISHIDUENOMEN", 100
                case 2:
                    return "ITEMID_IDONOMEN", 100
                case 3:
                    return "ITEMID_KAMADONOMEN", 100
    return "ITEMID_NONE", 0


def open_json_file(filename: str):
    file = open(f'Randomizer/{filename}', 'r')
    file_json = json.load(file)
    file.close()

    return file_json


def fetch_developer_name(index: int):
    pokemon_json = open_json_file('pokemon_list_info.json')

    return pokemon_json['pokemons'][index]['devName']


def fetch_animation_file(index: int):
    animation_json = open_json_file('pokemon_list_info.json')

    return animation_json['pokemons'][index]['anim_file']


def create_folder_hierarchy(folder: str):
    """
    Parameter should be a folder inside the main output folder.\n
    Ex: output/romfs/world/data/pokemon
    :param folder: Output/ folder to create
    :return: nothing
    """
    test = os.path.abspath(folder)
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

    for i in range(0, len(test)):
        foldertogetperms = foldertogetperms + f"{test[i]}/"
        os.makedirs(foldertogetperms, mode=0o777, exist_ok=True)


def generate_binary(schema: str, json_file: str, path: str, debug=False):
    iswindows = platform.system() == "Windows"
    flatc = os.path.abspath("flatc/flatc.exe") if iswindows else "flatc"

    create_folder_hierarchy('output/romfs/'+path+"/")
    outpath = os.path.abspath("output/romfs/" + path + "/")

    proc = subprocess.run(
        [flatc,
        "-b",
        "-o",
        outpath,
        os.path.abspath(schema),
        os.path.abspath(json_file)
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    if debug is True:
        print(proc.stdout)
        print(proc.stderr)
        print(proc.args)

    return proc

