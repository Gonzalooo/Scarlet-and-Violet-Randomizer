import json
import random
import os
import shutil
import Randomizer.shared_Variables as sharedVar
import Randomizer.helper_function as HelperFunctions

bannedStages = []

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
# Copies files of pokes needed. Right now gets all - later only form specific


def flip_starter_texture(starter_num: int):
    pokemon_file = HelperFunctions.fetch_animation_file(starter_num)

    shutil.copytree(os.getcwd() + "/Randomizer/StartersGifts/" +f'pokemon_clean/{pokemon_file}',
                    os.getcwd() + "/Randomizer/StartersGifts/" +f'output/romfs/pokemon/data/{pokemon_file}')

    current_check = os.getcwd() + "/Randomizer/StartersGifts/" +f'output/romfs/pokemon/data/{pokemon_file}'
    i = 0
    for pokemonfolder in os.listdir(current_check):
        pokemontextures_animations = current_check + "/" + pokemonfolder

        for files in os.listdir(pokemontextures_animations):
            if "rare" in files:
                replacedfile = files.replace("_rare", '')
                ogfiledir = pokemontextures_animations + "/" + f'{files}'
                newfiledir =pokemontextures_animations + "/" + f'{replacedfile}'
                shutil.copy2(ogfiledir, newfiledir)


def select_forced_starter(config, pokedata, starter_choice: str):
    choice = 1024
    if isinstance(config[f'force_starter_{starter_choice}'], str) is True:
        pokeName = config[f'force_starter_{starter_choice}'].replace(" ", "")
        pokeName = pokeName.upper()
        for entries in pokedata['pokemons']:
            entryName = entries['name'].replace(" ", "")
            if entryName.upper() == pokeName:
                choice = entries['natdex']
                if choice in sharedVar.banned_pokemon:
                    print(f"Invalid argument for Starter {starter_choice} - Try again")
                    exit(0)
                else:
                    break
    elif isinstance(config[f'force_starter_{starter_choice}'], int) is True:
        choice = pokedata['pokemons'][config[f'force_starter_{starter_choice}']]['natdex']
        if choice in sharedVar.banned_pokemon:
            print(f"Invalid argument for Starter {starter_choice} - Try again")
            exit(0)
    else:
        print(f"Invalid argument for Starter {starter_choice} - Try again")
        exit(0)
    return choice


def randomize_starter(config, pokemon_entry, check_forced_shiny: int, allowed_pokemon: list, starter: int):
    file = open(os.getcwd() + "/Randomizer/pokemon_list_info.json", 'r')
    pokedata = json.load(file)
    file.close()

    # Choose a pokemon -natdex order
    choice = random.randint(1, 1025)
    form_id = HelperFunctions.get_alternate_form(choice)
    choice_dict = {"id": choice, "form": form_id}
    # if the choice is a banned pokemon or already used or not allowed - reroll
    while (choice in sharedVar.banned_pokemon or
            choice_dict in sharedVar.starters_used
           or choice not in allowed_pokemon or choice in bannedStages):
        choice = random.randint(1, 1025)
        choice_dict['id'] = choice
        choice_dict['form'] = form_id

    if config[f'force_starter_{str(starter)}'] != 0:
        choice = select_forced_starter(config, pokedata, starter)
        form_id = HelperFunctions.get_alternate_form(choice)
        choice_dict['id'] = choice
        choice_dict['form'] = form_id
    # Change starters in files and getting it a random form
    pokemon_entry['pokeData']['devId'] = HelperFunctions.fetch_developer_name(choice)
    pokemon_entry['pokeData']['formId'] = form_id

    # If the form is Item Specific - giving he pokemon the item
    if choice in sharedVar.pokemon_with_item_only_form:
        item_obtained = HelperFunctions.get_pokemon_item_form(choice, form_id)
        pokemon_entry['pokeData']['item'] = item_obtained[0]

    # Giving Starter choice of main abilities
    pokemon_entry['pokeData']['tokusei'] = "RANDOM_12"

    # Changing Shiny-Chance - except ogerpon for lack of textures
    if choice != 1017:
        if config['make_all_starters_shiny'] == "yes":
            pokemon_entry['pokeData']['rareType'] = "RARE"
            if config['show_shiny_starters_in_overworld'] == "yes":
                flip_starter_texture(choice)
        elif config['force_shiny_starter'] == "yes" and check_forced_shiny == 1:
            pokemon_entry['pokeData']['rareType'] = "RARE"
            if config['show_shiny_starters_in_overworld'] == "yes":
                flip_starter_texture(choice)

    if (check_forced_shiny == 0 and config['make_all_starters_shiny'] != "yes"
            and config['higher_chance_shiny'] == "yes"):
        shiny_chance = random.randint(1, 10)
        if shiny_chance == 7:
            pokemon_entry['pokeData']['rareType'] = "RARE"
            if config['show_shiny_starters_in_overworld'] == "yes":
                flip_starter_texture(choice)

    # Change Pokeball
    if len(config['ball_for_starter']) != 0:
        ball_selected = HelperFunctions.get_pokeball_name(config['ball_for_starter'])
        pokemon_entry['pokeData']['ballId'] = ball_selected[0]

    # Change Tera Type
    if config['randomize_starters_tera_type'] == "yes":
        pokemon_entry['pokeData']['gemType'] = HelperFunctions.choose_tera_type(choice, form_id)

    if choice in sharedVar.set_tera_type_pokemon:
        pokemon_entry['pokeData']['gemType'] = HelperFunctions.choose_tera_type(choice, form_id)
    return choice_dict


def randomize_all_starters(config):
    if config['is_enabled'] == "yes":
        if os.path.exists(os.getcwd() + "/Randomizer/StartersGifts/" + 'output'):
            shutil.rmtree(os.getcwd() + "/Randomizer/StartersGifts/" + 'output')

        file = open(os.getcwd() + "/Randomizer/StartersGifts/" + "eventAddPokemon_array_clean.json", "r")
        data = json.load(file)
        file.close()

        shinyforced = [0] * 3
        allowed_pokemon, allowed_legends, bpl  = HelperFunctions.check_generation_limiter(config['generation_limiter'])
        if config['only_legendary_and_paradox'] == "yes":
            allowed_pokemon = sharedVar.legends_and_paradox
        elif config['only_legendary_pokemon'] == "yes":
            allowed_pokemon = allowed_legends
        elif config['only_paradox_pokemon'] == "yes":
            allowed_pokemon = sharedVar.paradox

        if config['ban_stage1_pokemon'] == "yes":
            bannedStages.extend(sharedVar.gen9Stage1)
        if config['ban_stage2_pokemon'] == "yes":
            bannedStages.extend(sharedVar.gen9Stage2)
        if config['ban_single_stage_pokemon'] == "yes":
            bannedStages.extend(sharedVar.no_evolution)
        if config['force_shiny_starter'] == "yes":
            choice = random.randint(0, 2)
            shinyforced[choice] = 1
        # sprigatito
        sharedVar.current_starters_selected['kusa'] = randomize_starter(config, data['values'][1],
                                                                        shinyforced[1], allowed_pokemon, 1)
        sharedVar.starters_used.append(sharedVar.current_starters_selected['kusa'])

        # fuecoco
        sharedVar.current_starters_selected['hono'] = randomize_starter(config, data['values'][0],
                                                                        shinyforced[0], allowed_pokemon, 2)
        sharedVar.starters_used.append(sharedVar.current_starters_selected['hono'])

        # quaxly
        sharedVar.current_starters_selected['mizu'] = randomize_starter(config, data['values'][2],
                                                                        shinyforced[2], allowed_pokemon, 3)
        sharedVar.starters_used.append(sharedVar.current_starters_selected['mizu'])

        # print(sharedVar.starters_used)
        print(sharedVar.current_starters_selected)

        outdata = json.dumps(data, indent=4)
        with open(os.getcwd() + "/Randomizer/StartersGifts/" +"eventAddPokemon_array.json", 'w') as outfile:
            outfile.write(outdata)
        print("Randomization Of Starter Pokemon Done!")
        return True
    return False
