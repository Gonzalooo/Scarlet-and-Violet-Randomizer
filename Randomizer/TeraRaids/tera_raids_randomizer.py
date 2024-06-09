import json
import random
import os
import Randomizer.shared_Variables as SharedVariables
import Randomizer.helper_function as HelperFunctions

has_alt_form_with_item = [483, 484, 487, 493, 888, 889, 1017]


def set_item_for_raid_form(index: int, form: int, raidJSON):
    if index in has_alt_form_with_item:
        match index:
            case 483:
                if form == 1:
                    raidJSON['item'] = "ITEMID_DAIKONGOUDAMA"
            case 484:
                if form == 1:
                    raidJSON['item'] = "ITEMID_DAISIRATAMA"
            case 487:
                if form == 1:
                    raidJSON['item'] = "ITEMID_DAIHAKKINDAMA"
            case 493:
                match form:
                    case 1:  # Fightning
                        raidJSON['item'] = "ITEMID_KOBUSINOPUREETO"
                    case 2:  # Flying
                        raidJSON['item'] = "ITEMID_AOZORAPUREETO"
                    case 3:  # poison
                        raidJSON['item'] = "ITEMID_MOUDOKUPUREETO"
                    case 4:  # ground
                        raidJSON['item'] = "ITEMID_DAITINOPUREETO"
                    case 5:  # rock
                        raidJSON['item'] = "ITEMID_GANSEKIPUREETO"
                    case 6:  # bug
                        raidJSON['item'] = "ITEMID_TAMAMUSIPUREETO"
                    case 7:  # ghost
                        raidJSON['item'] = "ITEMID_MONONOKEPUREETO"
                    case 8:  # steel
                        raidJSON['item'] = "ITEMID_KOUTETUPUREETO"
                    case 9:  # fire
                        raidJSON['item'] = "ITEMID_HINOTAMAPUREETO"
                    case 10:  # water
                        raidJSON['item'] = "ITEMID_SIZUKUPUREETO"
                    case 11:  # grass
                        raidJSON['item'] = "ITEMID_MIDORINOPUREETO"
                    case 12:  # electric
                        raidJSON['item'] = "ITEMID_IKAZUTIPUREETO"
                    case 13:  # psychic
                        raidJSON['item'] = "ITEMID_HUSIGINOPUREETO"
                    case 14:  # ice
                        raidJSON['item'] = "ITEMID_TURARANOPUREETO"
                    case 15:  # dragon
                        raidJSON['item'] = "ITEMID_RYUUNOPUREETO"
                    case 16:  # dark
                        raidJSON['item'] = "ITEMID_KOWAMOTEPUREETO"
                    case 17:  # Fairy
                        raidJSON['item'] = "ITEMID_SEIREIPUREETO"
            case 888:
                if form == 1:
                    raidJSON['item'] = "ITEMID_KUTITATURUGI"
            case 889:
                if form == 1:
                    raidJSON['item'] = "ITEMID_KUTITATATE"
            case 1017:
                match form:
                    case 1:
                        raidJSON['item'] = "ITEMID_IDONOMEN"
                    case 2:
                        raidJSON['item'] = "ITEMID_KAMADONOMEN"
                    case 3:
                        raidJSON['item'] = "ITEMID_ISHIDUENOMEN"
    return raidJSON


def randomizeRaids(raidsJSON, limiter, totalbannedlength, config):
    newRaidJSON = {}
    newRaidJSON['values'] = []
    counter = 0

    usedPokemon = []
    usedForms = [{"id": 0, "form": 0}]

    try:
        limiter.remove(1024)
    except ValueError:
        pass

    for i in range(0, len(raidsJSON['values'])):
        if len(limiter) - len(usedPokemon) == 0:
            break
        elif len(limiter) - len(usedPokemon) == totalbannedlength:
            break

        pokeChoice = random.randint(0, len(limiter)-1)
        altformNumber = HelperFunctions.get_alternate_form(limiter[pokeChoice])

        choice_dict = {"id": 0, "form": 0}
        choice_dict['id'] = limiter[pokeChoice]
        choice_dict['form'] = altformNumber

        while (limiter[pokeChoice] in SharedVariables.banned_pokemon or
           limiter[pokeChoice] in usedPokemon or choice_dict in usedForms):

            pokeChoice = random.randint(0, len(limiter) - 1)
            altformNumber = HelperFunctions.get_alternate_form(limiter[pokeChoice])
            choice_dict['id'] = limiter[pokeChoice]
            choice_dict['form'] = altformNumber

        usedForms.append(choice_dict)
        if HelperFunctions.check_if_all_forms_are_used("id", limiter[pokeChoice], choice_dict, usedForms) is True:
            usedPokemon.append(limiter[pokeChoice])

        counter = counter + 1
        raidsJSON['values'][i]['raidEnemyInfo']['romVer'] = "BOTH"
        raidsJSON['values'][i]['raidEnemyInfo']['bossPokePara']['devId'] = HelperFunctions.fetch_developer_name(limiter[pokeChoice])
        raidsJSON['values'][i]['raidEnemyInfo']['bossPokePara']['formId'] = altformNumber
        set_item_for_raid_form(limiter[pokeChoice], altformNumber, raidsJSON['values'][i]['raidEnemyInfo']['bossPokePara'])
        raidsJSON['values'][i]['raidEnemyInfo']['bossPokePara']['wazaType'] = "DEFAULT"
        raidsJSON['values'][i]['raidEnemyInfo']['bossPokePara']['waza1']['wazaId'] = "WAZA_NULL"
        raidsJSON['values'][i]['raidEnemyInfo']['bossPokePara']['waza2']['wazaId'] = "WAZA_NULL"
        raidsJSON['values'][i]['raidEnemyInfo']['bossPokePara']['waza3']['wazaId'] = "WAZA_NULL"
        raidsJSON['values'][i]['raidEnemyInfo']['bossPokePara']['waza4']['wazaId'] = "WAZA_NULL"

        # Ogerpon edge-case (Stellar Not Supported so no Terapagos)
        if choice_dict['id'] == 1017:
            if choice_dict['form'] == 0:
                raidsJSON['values'][i]['raidEnemyInfo']['bossPokePara']['gemType'] = "KUSA"
            if choice_dict['form'] == 1:
                raidsJSON['values'][i]['raidEnemyInfo']['bossPokePara']['gemType'] = "MIZU"
            if choice_dict['form'] == 2:
                raidsJSON['values'][i]['raidEnemyInfo']['bossPokePara']['gemType'] = "HONOO"
            if choice_dict['form'] == 3:
                raidsJSON['values'][i]['raidEnemyInfo']['bossPokePara']['gemType'] = "IWA"

        if config['force_shiny'] == "yes":
            raidsJSON['values'][i]['raidEnemyInfo']['bossPokePara']['rareType'] = "RARE"
        elif config['increased_shiny_chance'] is True:
            choice = random.randint(1, 10)
            if choice == 10:
                raidsJSON['values'][i]['raidEnemyInfo']['bossPokePara']['rareType'] = "RARE"

    if len(raidsJSON['values']) - counter < 0:
        newRaidJSON['values'] = raidsJSON['values'][:len(raidsJSON['values'])-1]
    elif len(raidsJSON['values']) - counter > 0:
        newRaidJSON['values'] = raidsJSON['values'][:counter]
    else:
        newRaidJSON['values'] = raidsJSON['values']

    return newRaidJSON


def region_file(region: str, index: int):
    if region == "paldea":
        return f'raid_enemy_0{str(index)}_array_clean.json'
    if region == "blueberry":
        return f'su1_raid_enemy_0{str(index)}_array_clean.json'
    if region == "kitakami":
        return f'su2_raid_enemy_0{str(index)}_array_clean.json'


def new_region_file(region: str, index: int):
    if region == "paldea":
        return f'raid_enemy_0{str(index)}_array.json'
    if region == "blueberry":
        return f'su1_raid_enemy_0{str(index)}_array.json'
    if region == "kitakami":
        return f'su2_raid_enemy_0{str(index)}_array.json'


def randomize_region(config, region: str, pokemonAllowed: list, allowed_legends: list, total_banned_length):
    for i in range(1, 7):
        file_to_open = region_file(region, i)
        paldeaTeraRaids = open(os.getcwd() + '/Randomizer/TeraRaids/' + file_to_open, 'r')
        paldeaRaids = json.load(paldeaTeraRaids)
        paldeaTeraRaids.close()
        randomized = False

        if config['only_legendary_and_paradox'] == "yes":
            paldeaRaids = randomizeRaids(paldeaRaids, SharedVariables.legends_and_paradox, total_banned_length, config)
            randomized = True
        if config['only_legendary_pokemon'] == "yes" and randomized is False:
            allowed_legends = [poke for poke in allowed_legends if poke not in SharedVariables.banned_pokemon]
            paldeaRaids = randomizeRaids(paldeaRaids, allowed_legends, total_banned_length, config)
            randomized = True
        if config['only_paradox_pokemon'] == "yes" and randomized is False:
            paldeaRaids = randomizeRaids(paldeaRaids, SharedVariables.paradox, total_banned_length, config)
            randomized = True

        if randomized is False:
            paldeaRaids = randomizeRaids(paldeaRaids, pokemonAllowed, total_banned_length, config)

        outdata = json.dumps(paldeaRaids, indent=4)
        file_to_create = new_region_file(region, i)
        with open(os.getcwd() + '/Randomizer/TeraRaids/' + file_to_create, 'w') as outfile:
            outfile.write(outdata)
        print(f"Randomization of {region} Raids Star {str(i)} Done !")


def randomize_items_tables():
    lottery_items = open(os.getcwd() + '/Randomizer/TeraRaids/' + 'raid_lottery_reward_item_array_clean.json',
                           'r')
    lottery = json.load(lottery_items)
    lottery_items.close()

    fixed_items = open(os.getcwd() + '/Randomizer/TeraRaids/' + 'raid_fixed_reward_item_array_clean.json',
                           'r')
    fixed = json.load(fixed_items)
    fixed_items.close()

    item_info = open(os.getcwd() + '/Randomizer/Items/' + 'pokemon_items_dev.json', 'r')
    item_data = json.load(item_info)
    item_info.close()
    # rate: 0 - 10000 (0% to 100%)
    # num: # of drops
    # if category == POKE ignore (pokemon drops - if changed could crash game)

    # fixed
    # category == poke ignore
    # no rate

    for i in range(0, len(fixed['values'])):
        for j in range(0, 15):
            testName = f'0{str(j)}'
            if j > 9:
                testName = str(j)

            if (fixed['values'][i][f'reward_item_{testName}']['category'] == "POKE" or
            fixed['values'][i][f'reward_item_{testName}']['category'] == "GEM"):
                continue
            itemChoice = random.randint(1, 1090)
            while (item_data['items'][itemChoice]['ItemType'] == "ITEMTYPE_MATERIAL" or
                   item_data['items'][itemChoice]['id'] in SharedVariables.banned_items or
                   item_data['items'][itemChoice]['ItemType'] == "ITEMTYPE_EVENT" or
                   item_data['items'][itemChoice]['ItemType'] == "ITEMTYPE_BATTLE" or
                   item_data['items'][itemChoice]['ItemType'] == "ITEMTYPE_POCKET"):
                itemChoice = random.randint(1, 1090)

            fixed['values'][i][f'reward_item_{testName}']['itemID'] = item_data['items'][itemChoice]['devName']
            fixed['values'][i][f'reward_item_{testName}']['num'] = random.randint(1, 5)

    for i in range(0, len(lottery['values'])):
        for j in range(0, 15):
            testName = f'0{str(j)}'
            if j > 9:
                testName = str(j)

            if (lottery['values'][i][f'reward_item_{testName}']['category'] == "POKE" or
            lottery['values'][i][f'reward_item_{testName}']['category'] == "GEM"):
                continue
            itemChoice = random.randint(1, 1090)
            while (item_data['items'][itemChoice]['ItemType'] == "ITEMTYPE_MATERIAL" or
                   item_data['items'][itemChoice]['id'] in SharedVariables.banned_items or
                   item_data['items'][itemChoice]['ItemType'] == "ITEMTYPE_EVENT" or
                   item_data['items'][itemChoice]['ItemType'] == "ITEMTYPE_BATTLE" or
                   item_data['items'][itemChoice]['ItemType'] == "ITEMTYPE_POCKET"):
                itemChoice = random.randint(1, 1090)

            lottery['values'][i][f'reward_item_{testName}']['itemID'] = item_data['items'][itemChoice]['devName']
            lottery['values'][i][f'reward_item_{testName}']['num'] = random.randint(1, 5)
            lottery['values'][i][f'reward_item_{testName}']['rate'] = random.randint(500, 10000)
    outdata = json.dumps(fixed, indent=2)
    with open(os.getcwd() + '/Randomizer/TeraRaids/' + f'raid_fixed_reward_item_array.json', 'w') as outfile:
        outfile.write(outdata)

    outdata = json.dumps(lottery, indent=2)
    with open(os.getcwd() + '/Randomizer/TeraRaids/' + f'raid_lottery_reward_item_array.json', 'w') as outfile:
        outfile.write(outdata)
    print(f"Randomization of Tera Raid Tables Done !")


def randomize_tera_raids(config):
    if config['use_paldea_settings_for_all'] == "yes":
        if config['paldea_settings']['tera_raid_randomizer']['is_enabled'] == "yes":
            allowed, legends, banned = HelperFunctions.check_generation_limiter(
                config['paldea_settings']['tera_raid_randomizer']
                ['generation_limiter'])
            randomize_region(config['paldea_settings']['tera_raid_randomizer'], "paldea", allowed, legends, banned)
            randomize_region(config['paldea_settings']['tera_raid_randomizer'], "kitakami", allowed, legends, banned)
            randomize_region(config['paldea_settings']['tera_raid_randomizer'], "blueberry", allowed, legends, banned)

            return True, True, True
        return False, False, False
    else:
        paldea = False
        kitakami = False
        blueberry = False
        if config['paldea_settings']['tera_raid_randomizer']['is_enabled'] == "yes":
            allowed, legends, banned = HelperFunctions.check_generation_limiter(config['paldea_settings']['tera_raid_randomizer']
                                                     ['generation_limiter'])
            randomize_region(config['paldea_settings']['tera_raid_randomizer'], "paldea", allowed, legends, banned)
            paldea = True
        if config['kitakami_settings']['tera_raid_randomizer']['is_enabled'] == "yes":
            allowed, legends, banned = HelperFunctions.check_generation_limiter(config['kitakami_settings']['tera_raid_randomizer']
                                                     ['generation_limiter'])
            randomize_region(config['kitakami_settings']['tera_raid_randomizer'], "kitakami", allowed, legends, banned)
            kitakami = True
        if config['blueberry_settings']['tera_raid_randomizer']['is_enabled'] == "yes":
            allowed, legends, banned = HelperFunctions.check_generation_limiter(config['blueberry_settings']['tera_raid_randomizer']
                                                     ['generation_limiter'])
            randomize_region(config['blueberry_settings']['tera_raid_randomizer'], "blueberry", allowed, legends, banned)
            blueberry = True

        randomize_items_tables()

        return paldea, kitakami, blueberry
