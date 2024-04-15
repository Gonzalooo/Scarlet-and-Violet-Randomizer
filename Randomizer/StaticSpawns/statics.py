import json
import random
import os
import Randomizer.shared_Variables as SharedVariables
import Randomizer.helper_function as HelperFunctions


def make_poke(pokemon, config):
    chosenmon = random.randint(1, 1025)
    while chosenmon in SharedVariables.banned_pokemon:
        chosenmon = random.randint(1, 1025)

    if config['only_legendary_pokemon'] == "yes":
        chosenmon = SharedVariables.legends[random.randint(0, len(SharedVariables.legends)-1)]
        while chosenmon in SharedVariables.banned_pokemon:
            chosenmon = SharedVariables.legends[random.randint(0, len(SharedVariables.legends) - 1)]
    if config['only_paradox_pokemon'] == "yes":
        chosenmon = SharedVariables.paradox[random.randint(0, len(SharedVariables.paradox)-1)]
        while chosenmon in SharedVariables.banned_pokemon:
            chosenmon = SharedVariables.paradox[random.randint(0, len(SharedVariables.paradox) - 1)]
    if config['only_legendary_and_paradox'] == "yes":
        chosenmon = SharedVariables.legends_and_paradox[random.randint(0, len(SharedVariables.legends_and_paradox)-1)]
        while chosenmon in SharedVariables.banned_pokemon:
            chosenmon = SharedVariables.legends_and_paradox[random.randint(0, len(SharedVariables.legends_and_paradox) - 1)]

    form_id = HelperFunctions.get_alternate_form(chosenmon)
    # prevent ogerpon from spawning as a static stellar type pokemon
    while "niji" in pokemon['tableKey'] and chosenmon == 1017:
        chosenmon = random.randint(1, 1025)

    pokemon['pokeDataSymbol']['devId'] = HelperFunctions.fetch_developer_name(chosenmon)
    # Hard coding form to 0 as they can't hold items
    pokemon['pokeDataSymbol']['formId'] = 0
    pokemon['pokeDataSymbol']['wazaType'] = "DEFAULT"
    pokemon['pokeDataSymbol']['waza1']['wazaId'] = "WAZA_NULL"
    pokemon['pokeDataSymbol']['waza2']['wazaId'] = "WAZA_NULL"
    pokemon['pokeDataSymbol']['waza3']['wazaId'] = "WAZA_NULL"
    pokemon['pokeDataSymbol']['waza4']['wazaId'] = "WAZA_NULL"
    if config['randomize_tera_types'] == "yes" and pokemon['pokeDataSymbol']['gemType'] != "DEFAULT":
        pokemon['pokeDataSymbol']['gemType'] = SharedVariables.tera_types[random.randint(0,
                                                                                         len(SharedVariables.tera_types)
                                                                                         - 1)].upper()
    

def randomize_statics(config):
    if config['is_enabled'] == "yes":
        file = open(os.getcwd() + "/Randomizer/StaticSpawns/fixed_symbol_table_array_clean.json", "r")
        data = json.load(file)
        file.close()

        for pokemon in data['values']:
            make_poke(pokemon, config)

        outdata = json.dumps(data, indent=4)
        with open(os.getcwd() + "/Randomizer/StaticSpawns/" +"fixed_symbol_table_array.json", 'w') as outfile:
            outfile.write(outdata)
        print("Randomization for Statics Done!")
        return True
    return False
