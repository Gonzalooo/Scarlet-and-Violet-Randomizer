import json
import random
import os
import Randomizer.shared_Variables as sharedVar
import Randomizer.helper_function as HelperFunctions


def randomize_all_gifts(config, pokedata ,allowed_pokemon: list):
    for i in range(0, len(pokedata)):
        if "common_" in pokedata[i]['label'] or "gameclear" in pokedata[i]['label']:
            continue
        choice = random.randint(1, 1025)
        # if the choice is a banned pokemon or already used or not allowed - reroll
        while choice in sharedVar.banned_pokemon or choice not in allowed_pokemon:
            choice = random.randint(1, 1025)

        form_id = HelperFunctions.get_alternate_form(choice)
        pokedata[i]['pokeData']['devId'] = HelperFunctions.fetch_developer_name(choice)
        pokedata[i]['pokeData']['formId'] = form_id

        if choice in sharedVar.pokemon_with_item_only_form:
            item_obtained = HelperFunctions.get_pokemon_item_form(choice, form_id)
            pokedata[i]['pokeData']['item'] = item_obtained[0]

        pokedata[i]['pokeData']['tokusei'] = "RANDOM_12"

        if config['randomize_tera_types'] == "yes":
            pokedata[i]['pokeData']['gemType'] = HelperFunctions.choose_tera_type(choice, form_id)

        if choice in sharedVar.set_tera_type_pokemon:
            pokedata[i]['pokeData']['gemType'] = HelperFunctions.choose_tera_type(choice, form_id)


def randomize_gifts(config):
    if config['is_enabled'] == "yes":
        file = ""
        if os.path.exists(os.getcwd() + "/Randomizer/StartersGifts/eventAddPokemon_array.json"):
            file = open(os.getcwd() + "/Randomizer/StartersGifts/" + "eventAddPokemon_array.json", "r")
        else:
            file = open(os.getcwd() + "/Randomizer/StartersGifts/" + "eventAddPokemon_array_clean.json", "r")
        data = json.load(file)
        file.close()

        allowed_pokemon, allowed_legends, bpl  = HelperFunctions.check_generation_limiter(config['generation_limiter'])
        randomize_all_gifts(config, data['values'], allowed_pokemon)

        outdata = json.dumps(data, indent=2)
        with open(os.getcwd() + "/Randomizer/StartersGifts/" +"eventAddPokemon_array.json", 'w') as outfile:
            outfile.write(outdata)
        print("Randomization Of Gift Pokemon Done!")
        return True
    return False