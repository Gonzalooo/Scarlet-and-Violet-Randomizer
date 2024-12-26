import json
import random
import os
import Randomizer.helper_function as HelperFunctions
import Randomizer.shared_Variables as SharedVariables

# abilities are any number between 1 and 298, inclusive
banned_abilities = [278, 307]  # Zero to Hero and Tera Shift banned
randomize_abilities = 0
randomize_moves = 0


def check_banned_ability(index):
    if index in banned_abilities:
        return True
    return False


def randomize_pokemon_abilities(pokemon):
    if pokemon['is_present'] is True:
        if pokemon['species']['species'] == 934:
            choice = random.randint(1, 310)
            while check_banned_ability(choice) is True:
                choice = random.randint(1, 298)
            pokemon['ability_hidden'] = choice
        elif pokemon['species']['species'] == 1021 and pokemon['species']['form'] != 0:
            i = 1
            while i < 4:
                choice = random.randint(1, 310)
                while check_banned_ability(choice) is True:
                    choice = random.randint(1, 310)
                else:
                    if i != 3:
                        pokemon["ability_" + str(i)] = choice
                    else:
                        pokemon['ability_hidden'] = choice
                    i = i + 1
        elif pokemon['species']['species'] == 1021 and pokemon['species']['form'] == 0:
            pass
        else:
            i = 1
            while i < 4:
                choice = random.randint(1, 310)
                while check_banned_ability(choice) is True:
                    choice = random.randint(1, 310)
                else:
                    if i != 3:
                        pokemon["ability_" + str(i)] = choice
                    else:
                        pokemon['ability_hidden'] = choice
                    i = i + 1
    return pokemon

def is_allowed_to_learn(species, form, moveid):
    match moveid:
        case 464:#Dark Void
            if species != 491 :#Darkrai
                print("NOT ALLOWED 2 LEARN THAT")
                return False
        case 621:#Hyperspace Fury
            if species == 720:#Hoopa
                if form != 1:#unbound
                    print("NOT ALLOWED 2 LEARN THAT")
                    return False
            else:
                print("NOT ALLOWED 2 LEARN THAT")
                return False
        case 783:#Aura Wheel
            if species != 877:#Morpeko
                return False
    return True

def randomize_pokemon_moves(pokemon):
    current_moves = []
    species = pokemon['species']['species']
    form = pokemon['species']['form']
    if pokemon['is_present'] is True:
        for move in pokemon['levelup_moves']:
            index = random.randint(0, len(SharedVariables.allowed_moves) - 1)
            while (SharedVariables.allowed_moves[index] in current_moves) and (is_allowed_to_learn(species, form, index) == True):
                index = random.randint(0, len(SharedVariables.allowed_moves) - 1)
            move['move'] = SharedVariables.allowed_moves[index]
            current_moves.append(SharedVariables.allowed_moves[index])

        current_moves = []
        for i in range(0, len(pokemon['reminder_moves'])):
            index = random.randint(0, len(SharedVariables.allowed_moves) - 1)
            while (SharedVariables.allowed_moves[index] in current_moves) and (is_allowed_to_learn(species, form, index) == True):
                index = random.randint(0, len(SharedVariables.allowed_moves) - 1)
            current_moves.append(SharedVariables.allowed_moves[index])
        pokemon['reminder_moves'] = []
        pokemon['reminder_moves'].extend(current_moves)

        current_moves = []
        for i in range(0, len(pokemon['egg_moves'])):
            index = random.randint(0, len(SharedVariables.allowed_moves) - 1)
            while (SharedVariables.allowed_moves[index] in current_moves) and (is_allowed_to_learn(species, form, index) == True):
                index = random.randint(0, len(SharedVariables.allowed_moves) - 1)
            current_moves.append(SharedVariables.allowed_moves[index])
        pokemon['egg_moves'] = []
        pokemon['egg_moves'].extend(current_moves)
    return pokemon


def randomize_pokemon_types(pokemon, chancedual):
    if pokemon['is_present'] is True:
        pokemon['type_1'] = random.randint(0, 17)
        
        if random.randint(1, 100) <= chancedual:
            pokemon['type_2'] = random.randint(0, 17)
            while (pokemon['type_1'] == pokemon['type_2']):
                pokemon['type_2'] = random.randint(0, 17)
        else:
            pokemon['type_2'] = pokemon['type_1']
    return pokemon


def randomize_pokemon_evolutions(pokemon, allowed_mons: list):
    for evo in pokemon['evolutions']:
        choice = random.randint(1, 1025)
        while choice in SharedVariables.banned_pokemon or choice not in allowed_mons:
            choice = random.randint(1, 1025)
        evo['species'] = choice
        evo['form'] = HelperFunctions.get_species_form(choice)

    return pokemon


def force_tera_blast(pokemon):
    teraBlastForced = {
        "move": 851,
        "level": 0
    }

    for i in range(5, 105, 5):
        teraBlastForced['level'] = i
        pokemon['levelup_moves'].append(teraBlastForced)
        teraBlastForced = {
            "move": 851,
            "level": 0
        }
    return pokemon


def randomize_evolutions_every_level(allowed_mons: list):
    template_evolution = {
        "level": 0,
        "condition": 0,
        "parameter": 0,
        "reserved3": 0,
        "reserved4": 0,
        "reserved5": 0,
        "species": 0,
        "form": 0
    }

    evoList = []
    for i in range(1, 101):
        template_evolution['level'] = i
        template_evolution['condition'] = 4
        species_choice = random.randint(1, 1025)
        while species_choice in SharedVariables.banned_pokemon or species_choice not in allowed_mons:
            species_choice = random.randint(1, 1025)
        template_evolution['species'] = species_choice
        template_evolution['form'] = HelperFunctions.get_species_form(species_choice)
        evoList.append(template_evolution)

        template_evolution = {
            "level": 0,
            "condition": 0,
            "parameter": 0,
            "reserved3": 0,
            "reserved4": 0,
            "reserved5": 0,
            "species": 0,
            "form": 0
        }

    return evoList


# To be completed - Trying to figure out how to keep
# same total.
def randomize_base_stats_weighted(pokemon):
    total = 0
    total = total + pokemon['base_stats']['hp']
    total = total + pokemon['base_stats']['atk']
    total = total + pokemon['base_stats']['def']
    total = total + pokemon['base_stats']['spa']
    total = total + pokemon['base_stats']['spd']
    total = total + pokemon['base_stats']['spe']

    if pokemon['species']['species'] == 0:
        return pokemon
    # add hard check for shedninja once back in the game
    # to have it hard coded to 1 for HP
    newstats = [15]*6
    total = total - (15*6)

    # Loop to ensure all stats are always correctly randomized
    randomizeStats = True
    while randomizeStats:
        statschecked = []
        while total != 0:
            no_infite_loop = 1
            checktotal = total
            changinStat = random.randint(0,5)

            while changinStat in statschecked:
                changinStat = random.randint(0, 5)
                if no_infite_loop == 6:
                    break
                no_infite_loop = no_infite_loop + 1
            if no_infite_loop == 6:
                break

            statschecked.append(changinStat)

            new_base_stat = random.randint(0, 240)
            while checktotal - new_base_stat < 0:
                new_base_stat = random.randint(0, total)
            while newstats[changinStat] + new_base_stat > 255:
                new_base_stat = random.randint(0, 240)

            newstats[changinStat] = newstats[changinStat] + new_base_stat
            total = total - new_base_stat
            if total == 0:
                randomizeStats = False

    pokemon['base_stats']['hp'] = newstats[0]
    pokemon['base_stats']['atk'] = newstats[1]
    pokemon['base_stats']['def'] = newstats[2]
    pokemon['base_stats']['spa'] = newstats[3]
    pokemon['base_stats']['spd'] = newstats[4]
    pokemon['base_stats']['spe'] = newstats[5]

    return pokemon


def randomize_base_stats_total(pokemon):
    pokemon['base_stats']['hp'] = random.randint(15, 255)
    pokemon['base_stats']['atk'] = random.randint(15, 255)
    pokemon['base_stats']['def'] = random.randint(15, 255)
    pokemon['base_stats']['spa'] = random.randint(15, 255)
    pokemon['base_stats']['spd'] = random.randint(15, 255)
    pokemon['base_stats']['spe'] = random.randint(15, 255)

    return pokemon


def fix_evolutions(pokemon, ind):
    if pokemon['species']['species'] == 25:
        template_evolution = {
            "level": 36,
            "condition": 4,
            "parameter": 0,
            "reserved3": 0,
            "reserved4": 0,
            "reserved5": 0,
            "species": 26,
            "form": 1
        }
        pokemon['evolutions'].append(template_evolution)
    elif pokemon['species']['species'] == 102:
        template_evolution = {
            "level": 36,
            "condition": 4,
            "parameter": 0,
            "reserved3": 0,
            "reserved4": 0,
            "reserved5": 0,
            "species": 103,
            "form": 1
        }
        pokemon['evolutions'].append(template_evolution)
    elif pokemon['species']['species'] == 109:
        template_evolution = {
            "level": 36,
            "condition": 4,
            "parameter": 0,
            "reserved3": 0,
            "reserved4": 0,
            "reserved5": 0,
            "species": 110,
            "form": 1
        }
        pokemon['evolutions'].append(template_evolution)
    elif pokemon['species']['species'] == 156:
        template_evolution = {
            "level": 36,
            "condition": 4,
            "parameter": 0,
            "reserved3": 0,
            "reserved4": 0,
            "reserved5": 0,
            "species": 157,
            "form": 1
        }
        pokemon['evolutions'].append(template_evolution)
    elif pokemon['species']['species'] == 234:
        template_evolution = {
            "level": 36,
            "condition": 4,
            "parameter": 0,
            "reserved3": 0,
            "reserved4": 0,
            "reserved5": 0,
            "species": 899,
            "form": 0
        }
        pokemon['evolutions'].append(template_evolution)
    elif pokemon['species']['species'] == 502:
        template_evolution = {
            "level": 36,
            "condition": 4,
            "parameter": 0,
            "reserved3": 0,
            "reserved4": 0,
            "reserved5": 0,
            "species": 503,
            "form": 1
        }
        pokemon['evolutions'].append(template_evolution)
    elif pokemon['species']['species'] == 723:
        template_evolution = {
            "level": 36,
            "condition": 4,
            "parameter": 0,
            "reserved3": 0,
            "reserved4": 0,
            "reserved5": 0,
            "species": 724,
            "form": 1
        }
        pokemon['evolutions'].append(template_evolution)
    elif pokemon['species']['species'] == 548:
        template_evolution = {
            "level": 36,
            "condition": 4,
            "parameter": 0,
            "reserved3": 0,
            "reserved4": 0,
            "reserved5": 0,
            "species": 549,
            "form": 1
        }
        pokemon['evolutions'].append(template_evolution)
    elif pokemon['species']['species'] == 627:
        template_evolution = {
            "level": 36,
            "condition": 4,
            "parameter": 0,
            "reserved3": 0,
            "reserved4": 0,
            "reserved5": 0,
            "species": 628,
            "form": 1
        }
        pokemon['evolutions'].append(template_evolution)
    elif pokemon['species']['species'] == 712:
        template_evolution = {
            "level": 36,
            "condition": 4,
            "parameter": 0,
            "reserved3": 0,
            "reserved4": 0,
            "reserved5": 0,
            "species": 713,
            "form": 1
        }
        pokemon['evolutions'].append(template_evolution)
    else:
        if len(ind) == 1:
            pokemon['evolutions'][ind[0]]['level'] = 36
            pokemon['evolutions'][ind[0]]['condition'] = 33
        elif len(ind) > 1:
            if pokemon['species']['species'] == 217:
                pokemon['evolutions'][ind[0]]['level'] = 36
                pokemon['evolutions'][ind[0]]['condition'] = 32
                template_evolution = {
                        "level": 36,
                        "condition": 4,
                        "parameter": 0,
                        "reserved3": 0,
                        "reserved4": 0,
                        "reserved5": 0,
                        "species": 901,
                        "form": 1
                }
                pokemon['evolutions'].append(template_evolution)
            else:
                pokemon['evolutions'][ind[0]]['level'] = 36
                pokemon['evolutions'][ind[0]]['condition'] = 32
                pokemon['evolutions'][ind[1]]['level'] = 36
                pokemon['evolutions'][ind[1]]['condition'] = 33
    return pokemon


def change_tms_of_pokemon(pokemon):
    current_moves = []
    if pokemon['is_present'] is True:
        if len(SharedVariables.usedMoves) == 0:
            for i in range(0, len(pokemon['tm_moves'])):
                index = random.randint(0, len(SharedVariables.tm_moves) - 1)
                while SharedVariables.tm_moves[index] in current_moves:
                    index = random.randint(0, len(SharedVariables.tm_moves) - 1)
                current_moves.append(SharedVariables.tm_moves[index])
        else:
            if pokemon['species']['species'] == 151:
                current_moves.extend(SharedVariables.usedMoves)
            else:
                for i in range(0, len(pokemon['tm_moves'])):
                    index = random.randint(0, len(SharedVariables.usedMoves) - 1)
                    # print(f'pokemon: {pokemon['species']}')
                    # print(f'current moves length: {len(current_moves)}')
                    # print(f'usedmoves length: {len(SharedVariables.usedMoves)}')
                    # print(f'pokemon moves length: {len(pokemon['tm_moves'])}')
                    while SharedVariables.usedMoves[index] in current_moves:
                        index = random.randint(0, len(SharedVariables.usedMoves) - 1)
                    current_moves.append(SharedVariables.usedMoves[index])
        pokemon['tm_moves'] = []
        pokemon['tm_moves'].extend(current_moves)

    return pokemon

def randomize_pokemon_stats(config, tms_randomized):
    tms = False
    if config['is_enabled'] == "yes":
        #file = open(os.getcwd() + "/Randomizer/PersonalData/" +"personal_array_clean.json", "r")
        #data = json.load(file)
        #file.close()
        data = HelperFunctions.open_json_file('PersonalData/personal_array_clean.json')
        allowed_pokemon = HelperFunctions.check_generation_limiter(config['generation_limiter'])
        spoilers = HelperFunctions.spoilerlog("Pokemon Stats")
        if config['ban_wonder_guard'] == "yes":
            banned_abilities.append(25)

        for pokemon in data['entry']:
            if pokemon['is_present'] is False:
                continue
            if pokemon['species']['species'] in SharedVariables.pokemon_with_regional_evolutions:
                if pokemon['species']['species'] == 217:
                    pokemon = fix_evolutions(pokemon, [0, 1])
                else:
                    if pokemon['species']['form'] == 0:
                        pokemon = fix_evolutions(pokemon, [1])
            elif pokemon['species']['species'] in SharedVariables.pokemon_with_trade_evolutions:
                if pokemon['species']['species'] == 366:
                    pokemon = fix_evolutions(pokemon, [0, 1])
                else:
                    match pokemon['species']['species']:
                        case 61:
                            pokemon = fix_evolutions(pokemon, [1])
                        case 79:
                            pokemon = fix_evolutions(pokemon, [1])
                        case _:
                            pokemon = fix_evolutions(pokemon, [0])

            spoilers.write(HelperFunctions.get_monname(pokemon['species']['species'])+HelperFunctions.get_form_txt(pokemon['species']['form'])+"\n")
            if config['randomize_abilities'] == "yes":
                pokemon = randomize_pokemon_abilities(pokemon)
                spoilers.write("Abilities 1: "+SharedVariables.ability_list[pokemon['ability_1']]+" | 2: "+SharedVariables.ability_list[pokemon['ability_2']]+" | Hidden: "+SharedVariables.ability_list[pokemon['ability_hidden']]+"\n")
            if config['randomize_types'] == "yes":
                pokemon = randomize_pokemon_types(pokemon, config['percent_chance_dual_type'])
                spoilers.write("Type: "+HelperFunctions.get_type_txt(pokemon['type_1'])+" - "+HelperFunctions.get_type_txt(pokemon['type_2'])+"\n")
            if config['randomize_movesets'] == "yes":
                pokemon = randomize_pokemon_moves(pokemon)
                spoilers.write("---Level up moves---\n")
                for move in pokemon['levelup_moves']:
                    if (move['level'] == 253):
                        spoilers.write("On Evolution: "+HelperFunctions.get_movename(move['move'])+"\n")
                    else:    
                        spoilers.write('Lvl '+str(move['level'])+": "+HelperFunctions.get_movename(move['move'])+"\n")
                spoilers.write("---Egg moves---\n")
                for move in pokemon['egg_moves']:
                    spoilers.write(HelperFunctions.get_movename(move)+"\n")
            if config['randomize_stats_with_same_total'] == "yes":
                pokemon = randomize_base_stats_weighted(pokemon)
            if config['randomize_stats_with_different_total'] == "yes":
                pokemon = randomize_base_stats_total(pokemon)
            if config['randomize_evolutions'] == "yes":
                pokemon = randomize_pokemon_evolutions(pokemon, allowed_pokemon[0])
            if config['let_pokemon_evolve_every_level'] == "yes":
                pokemon['evolutions'] = randomize_evolutions_every_level(allowed_pokemon[0])
            if config['force_tera_blast_every_5_levels'] == "yes":
                pokemon = force_tera_blast(pokemon)
            if tms_randomized == "yes":
                tms = True
                pokemon = change_tms_of_pokemon(pokemon)
                spoilers.write("---TM moves---\n")
                if pokemon is not None:
                    for move in pokemon['tm_moves']:
                        spoilers.write(HelperFunctions.get_movename(move)+"\n")
            if pokemon['evolutions'] != []:
                spoilers.write("---Evolutions---"+"\n")
                for evodata in pokemon['evolutions']:
                    spoilers.write("Lvl "+str(evodata['level']))
                    if evodata['condition'] != 4:
                        spoilers.write(" Condition: "+str(evodata['condition']))
                    spoilers.write(" | "+HelperFunctions.get_monname(evodata['species'])+HelperFunctions.get_form_txt(evodata['form'])+"\n")
            spoilers.write("------------------\n")

        outdata = json.dumps(data, indent=4)
        with open(os.getcwd() + "/Randomizer/PersonalData/" +"personal_array.json", 'w') as outfile:
            outfile.write(outdata)
        print("Randomization Of Stats/Abilities/Moves/Evos Done !")
        spoilers.close()
        return True

    if tms is False:
        if tms_randomized == "yes":
            spoilers = HelperFunctions.spoilerlog("Pokemon Stats")
            file = open(os.getcwd() + "/Randomizer/PersonalData/" + "personal_array_clean.json", "r")
            data = json.load(file)
            file.close()
            spoilers = HelperFunctions.spoilerlog("Pokemon Stats")
            for pokemon in data['entry']:
                spoilers.write(HelperFunctions.get_monname(pokemon['species']['species'])+HelperFunctions.get_form_txt(pokemon['species']['form'])+"\n")
                pokemon = change_tms_of_pokemon(pokemon)
                spoilers.write("---TM moves---\n")
                if pokemon is not None:
                    for move in pokemon['tm_moves']:
                        spoilers.write(HelperFunctions.get_movename(move)+"\n")

            outdata = json.dumps(data, indent=4)
            with open(os.getcwd() + "/Randomizer/PersonalData/" +"personal_array.json", 'w') as outfile:
                outfile.write(outdata)
            print("Randomization Of TMs Done !")

        return True
    return False

