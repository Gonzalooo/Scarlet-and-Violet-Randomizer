import os
import platform
import subprocess
import json
import Randomizer.shared_Variables as SharedVariables
import random
import sys


def get_number_of_forms(pokemon_index: int):
    if pokemon_index in SharedVariables.has_alternate_form:
        match pokemon_index:
            case 25:
                return len([1, 2, 3, 4, 5, 6, 7, 9])+1
            case 52:
                return len([1, 2])+1
            case 80:
                return len([2])+1
            case 128:
                return len([1, 2, 3])+1
            case 386:
                return len([1, 2, 3])+1
            case 479:
                return len([1, 2, 3, 4, 5])+1
            case 493:
                return len([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])+1
            case 585:
                return len([1, 2, 3])+1
            case 586:
                return len([1, 2, 3])+1
            case 646:
                return len([1, 2])+1
            case 664:
                return len([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])+1
            case 665:
                return len([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])+1
            case 666:
                return len([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])+1
            case 669:
                return len([1, 2, 3, 4])+1
            case 670:
                return len([1, 2, 3, 4])+1
            case 671:
                return len([1, 2, 3, 4])+1
            case 741:
                return len([1, 2, 3])+1
            case 745:
                return len([1, 2])+1
            case 774:
                return len([1, 2, 3, 4, 5, 6])+1
            case 778:
                return len([])+1
            case 800:
                return len([1, 2])+1
            case 845:
                return len([])+1
            case 869:
                return len([1, 2, 3, 4, 5, 6, 7, 8])
            case 875:
                return len([])+1
            case 877:
                return len([])+1
            case 898:
                return len([1, 2])+1
            case 978:
                return len([1, 2])+1
            case 931:
                return len([1, 2, 3])+1
            case 1017:
                return len([1, 2, 3])+1
            case _:
                return len([1])+1
    else:
        return len([])+1


def check_if_all_forms_are_used(key: str, pokemon_id: int, pokemon_dict: dict, pokemon_dict_list: list[dict]):
    # Extract the value associated with the key in the single dictionary
    value_to_check = pokemon_dict.get(key, None)

    count = 0

    for d in pokemon_dict_list:
        if d.get(key) == value_to_check:
            count = count + 1

    if count == get_number_of_forms(pokemon_id):
        return True
    return False


def choose_tera_type(choice: int, form: int):
    match choice:
        case 1017:
            match form:
                case 0:
                    return "KUSA"
                case 1:
                    return "MIZU"
                case 2:
                    return "HONOO"
                case 3:
                    return "IWA"
        case 1024:
            return "NIJI"
        case _:
            return SharedVariables.tera_types[random.randint(0, len(SharedVariables.tera_types) - 1)].upper()


def get_pokeball_name(pokeball: str):
    if pokeball == "Master Ball":
        return "MASUTAABOORU", "ITEMID_MASUTAABOORU"
    if pokeball == "Ultra Ball":
        return "HAIPAABOORU", "ITEMID_HAIPAABOORU"
    if pokeball == "Great Ball":
        return "SUUPAABOORU", "ITEMID_SUUPAABOORU"
    if pokeball == "Poke Ball":
        return "MONSUTAABOORU", "ITEMID_MONSUTAABOORU"
    if pokeball == "Safari Ball":
        return "SAFARIBOORU", "ITEMID_SAFARIBOORU"
    if pokeball == "Net Ball":
        return "NETTOBOORU", "ITEMID_NETTOBOORU"
    if pokeball == "Dive Ball":
        return "DAIBUBOORU", "ITEMID_DAIBUBOORU"
    if pokeball == "Nest Ball":
        return "NESUTOBOORU", "ITEMID_NESUTOBOORU"
    if pokeball == "Repeat Ball":
        return "RIPIITOBOORU", "ITEMID_RIPIITOBOORU"
    if pokeball == "Timer Ball":
        return "TAIMAABOORU", "ITEMID_TAIMAABOORU"
    if pokeball == "Luxury Ball":
        return "GOOZYASUBOORU", "ITEMID_GOOZYASUBOORU"
    if pokeball == "Premier Ball":
        return "PUREMIABOORU", "ITEMID_PUREMIABOORU"
    if pokeball == "Dusk Ball":
        return "DAAKUBOORU", "ITEMID_DAAKUBOORU"
    if pokeball == "Heal Ball":
        return "HIIRUBOORU", "ITEMID_HIIRUBOORU"
    if pokeball == "Quick Ball":
        return "KUIKKUBOORU", "ITEMID_KUIKKUBOORU"
    if pokeball == "Fast Ball":
        return "SUPIIDOBOORU", "ITEMID_SUPIIDOBOORU"
    if pokeball == "Level Ball":
        return "REBERUBOORU", "ITEMID_REBERUBOORU"
    if pokeball == "Lure Ball":
        return "RUAABOORU", "ITEMID_RUAABOORU"
    if pokeball == "Heavy Ball":
        return "HEBIIBOORU", "ITEMID_HEBIIBOORU"
    if pokeball == "Love Ball":
        return "RABURABUBOORU", "ITEMID_RABURABUBOORU"
    if pokeball == "Friend Ball":
        return "HURENDOBOORU", "ITEMID_HURENDOBOORU"
    if pokeball == "Moon Ball":
        return "MUUNBOORU", "ITEMID_MUUNBOORU"
    if pokeball == "Sport Ball":
        return "KONPEBOORU", "ITEMID_KONPEBOORU"
    if pokeball == "Dream Ball":
        return "DORIIMUBOORU", "ITEMID_DORIIMUBOORU"
    if pokeball == "Beast Ball":
        return "URUTORABOORU", "ITEMID_URUTORABOORU"

    print("Not a Valid Pokeball please to follow this template: {type of ball} Ball")
    return "MONSUTAABOORU", "ITEMID_MONSUTAABOORU"


def get_species_form(index: int):
    if index in SharedVariables.has_alternate_form:
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
    total_banned_pokemon = 0
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
        total_banned_pokemon = len(SharedVariables.banned_pokemon)
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
                    total_banned_pokemon = total_banned_pokemon + SharedVariables.gen1bannedlength
                    continue
                case 2:
                    if in_array[1] == 1:
                        print("Duplicate Generation 2")
                        exit(0)
                    allowed_pokemon.extend(SharedVariables.gen2)
                    allowed_legends.extend(SharedVariables.gen2_legends)
                    in_array[1] = 1
                    total_banned_pokemon = total_banned_pokemon + SharedVariables.gen2bannedlength
                    continue
                case 3:
                    if in_array[2] == 1:
                        print("Duplicate Generation 3")
                        exit(0)
                    allowed_pokemon.extend(SharedVariables.gen3)
                    allowed_legends.extend(SharedVariables.gen3_legends)
                    in_array[2] = 1
                    total_banned_pokemon = total_banned_pokemon + SharedVariables.gen3bannedlength
                    continue
                case 4:
                    if in_array[3] == 1:
                        print("Duplicate Generation 4")
                        exit(0)
                    allowed_pokemon.extend(SharedVariables.gen4)
                    allowed_legends.extend(SharedVariables.gen4_legends)
                    in_array[3] = 1
                    total_banned_pokemon = total_banned_pokemon + SharedVariables.gen4bannedlength
                    continue
                case 5:
                    if in_array[4] == 1:
                        print("Duplicate Generation 5")
                        exit(0)
                    allowed_pokemon.extend(SharedVariables.gen5)
                    allowed_legends.extend(SharedVariables.gen5_legends)
                    in_array[4] = 1
                    total_banned_pokemon = total_banned_pokemon + SharedVariables.gen5bannedlength
                    continue
                case 6:
                    if in_array[5] == 1:
                        print("Duplicate Generation 6")
                        exit(0)
                    allowed_pokemon.extend(SharedVariables.gen6)
                    allowed_legends.extend(SharedVariables.gen6_legends)
                    in_array[5] = 1
                    total_banned_pokemon = total_banned_pokemon + SharedVariables.gen6bannedlength
                    continue
                case 7:
                    if in_array[6] == 1:
                        print("Duplicate Generation 7")
                        exit(0)
                    allowed_pokemon.extend(SharedVariables.gen7)
                    allowed_legends.extend(SharedVariables.UB)
                    allowed_legends.extend(SharedVariables.gen7_legends)
                    in_array[6] = 1
                    total_banned_pokemon = total_banned_pokemon + SharedVariables.gen7bannedlength
                    continue
                case 8:
                    if in_array[7] == 1:
                        print("Duplicate Generation 8")
                        exit(0)
                    allowed_pokemon.extend(SharedVariables.gen8)
                    allowed_legends.extend(SharedVariables.gen8_legends)
                    in_array[7] = 1
                    total_banned_pokemon = total_banned_pokemon + SharedVariables.gen8bannedlength
                    continue
                case 9:
                    if in_array[8] == 1:
                        print("Duplicate Generation 9")
                        exit(0)
                    allowed_pokemon.extend(SharedVariables.gen9)
                    allowed_legends.extend(SharedVariables.paradox)
                    allowed_legends.extend(SharedVariables.gen9_legends)
                    in_array[8] = 1
                    total_banned_pokemon = total_banned_pokemon + SharedVariables.gen9bannedlength
                    continue
                case _:
                    print("Invalid Generation")
                    exit(0)
    allowed_pokemon = list(set(allowed_pokemon))
    allowed_legends = list(set(allowed_legends))
    return allowed_pokemon, allowed_legends, total_banned_pokemon


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
                case 1:  # Fighting
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
                    return "ITEMID_IDONOMEN", 100
                case 2:
                    return "ITEMID_KAMADONOMEN", 100
                case 3:
                    return "ITEMID_ISHIDUENOMEN", 100
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

def spoilerindex(rngseed, versiontxt):
    f = open("spoilers.log", "a", encoding='utf-8')#Open/create spoiler log and start new header
    f.write("\n\n---------------------------\n"+
"Spoiler Log Index"+
"\n---------------------------\n"+
"TM Changes\n"+
"Wild Encounters: Paldea\n"+
"Wild Encounters: Kitakami\n"+
"Wild Encounters: Blueberry\n"+
"Static Teratypes\n"+
"Pokemon Stats\n"+
"Hidden Items\n"+
"--Paldea Hidden\n"+
"--KitaKami Hidden\n"+
"--Blueberry Hidden\n"+
"--LC Hidden\n"+
"Pickup Ability Items\n"+
"Lets Go Items\n"+
"Starters\n"+
"Trainers\n"+
"--Rival Fights\n"+
"--Route Trainers\n"+
"--Gyms\n"+
"--Elite 4 | BB Elite 4 | Ogre Clan\n"+
"--Champions\n"+
"--Raid NPCs\n"+
"Gift Pokemon\n"+
"paldea Raids\n"+
"kitakami Raids\n"+
"blueberry Raids\n")
    f.write("\n\nLog file extra details:\n")
    f.write("Some of the names such as trainers and areas are listed as the internal code.\nUpdated descriptions and layout are planned for a future update to make it easier to read\n")
    f.write("\nNOTE: A few items such as wild spawns not yet added")
    f.write("\n\nSeed: "+str(rngseed))
    f.write("\nVersion: "+versiontxt)


def spoilerlog(title: str):
    f = open("spoilers.log", "a", encoding='utf-8')#Open/create spoiler log and start new header
    f.write("\n\n---------------------------\n")
    f.write("| "+title+" |\n")
    f.write("---------------------------\n")
    return f

def gen_itemname_lookup():
    inamesfile = open_json_file('pokemon_items_dev.json')
    for item in inamesfile['items']:
        SharedVariables.itemnames[item['id']] = item['name']
        SharedVariables.itemids[item['devName']] = item['id']
        
def gen_monname_lookup():
    monnamesfile = open_json_file('pokemon_list_info.json')
    for mon in monnamesfile['pokemons']:
        SharedVariables.monnames[mon['id']] = mon['name']
        SharedVariables.monids[mon['devName']] = mon['id']
        
        
def gen_movename_lookup():
    movenamesfile = open_json_file('TMs/move_list.json')
    for move in movenamesfile['moves']:
        SharedVariables.movenames[move['id']] = move['name']
        SharedVariables.movedevnames[move['id']] = move['devName']
        
        
def gen_all_lookups():
    gen_itemname_lookup()
    gen_monname_lookup()
    gen_movename_lookup()

def get_itemname(itemid: int):
    if itemid not in SharedVariables.itemnames:
        return "ITEM_ID_"+str(itemid)
    else:
        return SharedVariables.itemnames[itemid]
        
def get_itemid(itemdevname: str):
    if itemdevname not in SharedVariables.itemids:
        print("Error getting Item ID for Devname: "+devname)
        return 0
    else:
        return SharedVariables.itemids[itemdevname]
        
def get_movename(moveid: int):
    if moveid not in SharedVariables.movenames:
        return "MOVE_ID_"+str(itemid)
    else:
        return SharedVariables.movenames[moveid]
        
def get_movedevname(moveid: int):
    if moveid not in SharedVariables.movedevnames:
        return "MOVE_ID_"+str(itemid)
    else:
        return SharedVariables.movedevnames[moveid]
        
def get_monname(monid: int):
    if monid not in SharedVariables.monnames:
        return "POKE_ID_"+str(monid)
    else:
        return SharedVariables.monnames[monid]
        
def get_monid(devname: str):
    if devname not in SharedVariables.monids:
        print("Error getting Mon ID for Devname: "+devname)
        return 0
    else:
        return SharedVariables.monids[devname]
        
def get_type_txt(montype: int):
    return SharedVariables.tera_types_eng[montype]
    
def get_gem_txt(gem: str):
    if gem.lower() == "default":
        return gem
    if gem.lower() not in SharedVariables.tera_types:
        return "err: "+gem
    return SharedVariables.tera_types_eng[SharedVariables.tera_types.index(gem.lower())]
    
def get_form_txt(form: int):
    if form == 0:
        return ""
    return " Form: "+str(form+1)#need to do a proper form name lookup

def update_shiny_rate(config):
    if (config['shiny_boosted_rate'] != 0):
        SharedVariables.boostedshiny = config['shiny_boosted_rate']

def seedgen(fixed_seed):
    seed = random.randrange(sys.maxsize)
    if fixed_seed:
        if type(fixed_seed) is str:
            if fixed_seed != "":
                seed = fixed_seed
        if type(fixed_seed) is int:
            if fixed_seed != 0:
                seed = fixed_seed
    random.seed(seed)
    print("Seed is: ", seed)
    return seed

def basestat_txt(stats):
    if stats:
        return "hp:"+str(stats['hp'])+" atk:"+str(stats['atk'])+" def:"+str(stats['def'])+" spAtk:"+str(stats['spAtk'])+" spDef:"+str(stats['spDef'])+" spe: "+str(stats['agi'])
    else:
        return "Stats error"

def fix_config(config):
    if "shiny_boosted_rate" not in config:
        config["shiny_boosted_rate"] = 10
        print("config option not found: 'shiny_boosted_rate'")
        print("defaulting to 1 in 10 chance to be shiny... where possible")
        
    if "percent_chance_dual_type" not in config['pokemon_stats_randomizer']:
        config['pokemon_stats_randomizer']["percent_chance_dual_type"] = 60
        print("config option not found: 'pokemon_stats_randomizer''percent_chance_dual_type'")
        print("defaulting to 60% chance to be dual type")
        
    if "exclude_legendaries" not in config['kitakami_settings']['wild_randomizer']:
        if "exclude_legendary" in config['kitakami_settings']['wild_randomizer']:
            _gettxt = config['kitakami_settings']['wild_randomizer']["exclude_legendary"]
        else:
            _gettxt = "no"
        config['kitakami_settings']['wild_randomizer']["exclude_legendaries"] = _gettxt
        
    if "exclude_legendaries" not in config['blueberry_settings']['wild_randomizer']:
        if "exclude_legendary" in config['blueberry_settings']['wild_randomizer']:
            _gettxt = config['blueberry_settings']['wild_randomizer']["exclude_legendary"]
        else:
            _gettxt = "no"
        config['blueberry_settings']['wild_randomizer']["exclude_legendaries"] = _gettxt
        
    if "show_shiny_starters_in_overworld" not in config['starter_pokemon_randomizer']:
        if "show_starters_in_overworld" in config['starter_pokemon_randomizer']:
            _gettxt = config['starter_pokemon_randomizer']["show_starters_in_overworld"]
        else:
            _gettxt = "no"
        config['starter_pokemon_randomizer']['show_shiny_starters_in_overworld'] = _gettxt
        
    isthere = False
    if "boostpercent" not in config["paldea_settings"]["trainers_randomizer"]["all_trainers_settings"]:
        config["paldea_settings"]["trainers_randomizer"]["all_trainers_settings"]["boostpercent"] = 10
        isthere = True
    if "boostpercent" not in config["kitakami_settings"]["trainers_randomizer"]["all_trainers_settings"]:
        config["kitakami_settings"]["trainers_randomizer"]["all_trainers_settings"]["boostpercent"] = 10
        isthere = True
    if "boostpercent" not in config["blueberry_settings"]["trainers_randomizer"]["all_trainers_settings"]:
        config["blueberry_settings"]["trainers_randomizer"]["all_trainers_settings"]["boostpercent"] = 10
        isthere = True
    if isthere == True:
        print("config option not found: 'boostpercent' in 'all_trainers_settings' section(s)")
        print("defaulting to 10% boost")
        print("NOTE: boostlevels still needs to be yes for this to apply")
        
    isthere = False
    if "boostlevels" not in config["paldea_settings"]["trainers_randomizer"]["all_trainers_settings"]:
        config["paldea_settings"]["trainers_randomizer"]["all_trainers_settings"]["boostlevels"] = "no"
        isthere = True
    if "boostlevels" not in config["kitakami_settings"]["trainers_randomizer"]["all_trainers_settings"]:
        config["kitakami_settings"]["trainers_randomizer"]["all_trainers_settings"]["boostlevels"] = "no"
        isthere = True
    if "boostlevels" not in config["blueberry_settings"]["trainers_randomizer"]["all_trainers_settings"]:
        config["blueberry_settings"]["trainers_randomizer"]["all_trainers_settings"]["boostlevels"] = "no"
        isthere = True
    if isthere == True:
        print("config option not found: 'boostlevels' in 'all_trainers_settings' section(s)")
        print("defaulting to no level boosting for trainers")
        
    if "useondomathforboost" not in config["paldea_settings"]["trainers_randomizer"]["all_trainers_settings"]:
        config["paldea_settings"]["trainers_randomizer"]["all_trainers_settings"]["useondomathforboost"] = "no"
    if "useondomathforboost" not in config["kitakami_settings"]["trainers_randomizer"]["all_trainers_settings"]:
        config["kitakami_settings"]["trainers_randomizer"]["all_trainers_settings"]["useondomathforboost"] = "no"
    if "useondomathforboost" not in config["blueberry_settings"]["trainers_randomizer"]["all_trainers_settings"]:
        config["blueberry_settings"]["trainers_randomizer"]["all_trainers_settings"]["useondomathforboost"] = "no"
        
    #writes the changes to file, writes to the bottom of file unsure if there is a way around it to make it more user friendly, disabled for now
    #with open('new_config.json', 'w', encoding='utf-8') as f:
    #    json.dump(config, f, ensure_ascii=False, indent=2)
    return config