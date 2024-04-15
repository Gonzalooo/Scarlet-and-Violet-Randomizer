import json
import os

pokemon_dict_json = open("/Users/gonzalo/Desktop/Scarlet-and-Violet-Randomizer" + "/Randomizer/Scenes/" + "pokemon_dict_info.json", "r")
pokemon_dict = json.load(pokemon_dict_json)
pokemon_dict_json.close()

paldea_json = open('pokedata_array_clean.json', 'r')
paldea = json.load(paldea_json)
paldea_json.close()

area_check = True
location_check = True
no_area_location_check = True

if area_check is True:
    values: dict[str, list[str]] = {}

    for i in range(1, 28):
        values[f"{i}"] = []
    values['4.5'] = []

    for entry in paldea['values']:
        if entry['area'] == '':
            continue

        test = entry['area'].replace("\"", "").split(',')
        for area in test:
            if entry['bandtype'] == "BOSS":
                values[area].append(pokemon_dict['pokemons'][entry['devid']]['name'] + " - BOSS")
                values[area].append(entry['formno'])
                values[area].append(entry['minlevel'])
                values[area].append(entry['maxlevel'])
                values[area].append(entry['biome1'])
                values[area].append(entry['biome2'])
                values[area].append(entry['biome3'])
                values[area].append(entry['biome4'])
            elif entry['bandtype'] == "SAME":
                values[area].append(pokemon_dict['pokemons'][entry['devid']]['name'] + " - SAME")
                values[area].append(entry['formno'])
                values[area].append(entry['minlevel'])
                values[area].append(entry['maxlevel'])
                values[area].append(entry['biome1'])
                values[area].append(entry['biome2'])
                values[area].append(entry['biome3'])
                values[area].append(entry['biome4'])
            else:
                values[area].append(pokemon_dict['pokemons'][entry['devid']]['name'])
                values[area].append(entry['formno'])
                values[area].append(entry['minlevel'])
                values[area].append(entry['maxlevel'])
                values[area].append(entry['biome1'])
                values[area].append(entry['biome2'])
                values[area].append(entry['biome3'])
                values[area].append(entry['biome4'])

    for i in range(1, 28):
        filename = f'Pokemon_Area/area_{str(i)}.txt'
        file_check = open(filename, 'w')
        for j in range(0, len(values[f'{str(i)}'])):
            print(values[f'{str(i)}'][j], file=file_check)
        file_check.close()

    filename = f'Pokemon_Area/area_4_5.txt'
    file_check = open(filename, 'w')
    for j in range(0, len(values['4.5'])):
        print(values['4.5'][j], file=file_check)
    file_check.close()

# ---------------------------------------------------------------------------------------------------------------------
if location_check is True:
    location_values: dict[str, list[str]] = {}

    for entry in paldea['values']:
        if entry['locationName'] == '':
            continue

        location_names = entry['locationName'].split(',')

        for location in location_names:
            location_values[location] = []

    for entry in paldea['values']:
        if entry['locationName'] == '':
            continue

        location_names = entry['locationName'].split(',')

        for location in location_names:
            if entry['bandtype'] == "BOSS":
                location_values[location].append(pokemon_dict['pokemons'][entry['devid']]['name'] + " - BOSS")
                location_values[location].append(entry['formno'])
                location_values[location].append(entry['minlevel'])
                location_values[location].append(entry['maxlevel'])
                location_values[location].append(entry['biome1'])
                location_values[location].append(entry['biome2'])
                location_values[location].append(entry['biome3'])
                location_values[location].append(entry['biome4'])
            elif entry['bandtype'] == "SAME":
                location_values[location].append(pokemon_dict['pokemons'][entry['devid']]['name'] + " - SAME")
                location_values[location].append(entry['formno'])
                location_values[location].append(entry['minlevel'])
                location_values[location].append(entry['maxlevel'])
                location_values[location].append(entry['biome1'])
                location_values[location].append(entry['biome2'])
                location_values[location].append(entry['biome3'])
                location_values[location].append(entry['biome4'])
            else:
                location_values[location].append(pokemon_dict['pokemons'][entry['devid']]['name'])
                location_values[location].append(entry['formno'])
                location_values[location].append(entry['minlevel'])
                location_values[location].append(entry['maxlevel'])
                location_values[location].append(entry['biome1'])
                location_values[location].append(entry['biome2'])
                location_values[location].append(entry['biome3'])
                location_values[location].append(entry['biome4'])

    for key, value in location_values.items():
        filename = f'Pokemon_Location/{key}.txt'
        file_check = open(filename, 'w')
        for pokemon in value:
            print(f'{pokemon}', file=file_check)

# ---------------------------------------------------------------------------------------------------------------------
if no_area_location_check is True:
    location_area_values: dict[str, list[str]] = {}

    for entry in paldea['values']:
        if entry['area'] == '' and entry['locationName'] == '':
            location_area_values[pokemon_dict['pokemons'][entry['devid']]['name']] = []

    for entry in paldea['values']:
        if entry['area'] == '' and entry['locationName'] == '':
            if entry['bandtype'] == "BOSS":
                location_area_values[pokemon_dict['pokemons'][entry['devid']]['name']].append(pokemon_dict['pokemons'][entry['devid']]['name'] + " - BOSS")
                location_area_values[pokemon_dict['pokemons'][entry['devid']]['name']].append(entry['formno'])
                location_area_values[pokemon_dict['pokemons'][entry['devid']]['name']].append(entry['minlevel'])
                location_area_values[pokemon_dict['pokemons'][entry['devid']]['name']].append(entry['maxlevel'])
                location_area_values[pokemon_dict['pokemons'][entry['devid']]['name']].append(entry['biome1'])
                location_area_values[pokemon_dict['pokemons'][entry['devid']]['name']].append(entry['biome2'])
                location_area_values[pokemon_dict['pokemons'][entry['devid']]['name']].append(entry['biome3'])
                location_area_values[pokemon_dict['pokemons'][entry['devid']]['name']].append(entry['biome4'])
            elif entry['bandtype'] == "SAME":
                location_area_values[pokemon_dict['pokemons'][entry['devid']]['name']].append(pokemon_dict['pokemons'][entry['devid']]['name'] + " - SAME")
                location_area_values[pokemon_dict['pokemons'][entry['devid']]['name']].append(entry['formno'])
                location_area_values[pokemon_dict['pokemons'][entry['devid']]['name']].append(entry['minlevel'])
                location_area_values[pokemon_dict['pokemons'][entry['devid']]['name']].append(entry['maxlevel'])
                location_area_values[pokemon_dict['pokemons'][entry['devid']]['name']].append(entry['biome1'])
                location_area_values[pokemon_dict['pokemons'][entry['devid']]['name']].append(entry['biome2'])
                location_area_values[pokemon_dict['pokemons'][entry['devid']]['name']].append(entry['biome3'])
                location_area_values[pokemon_dict['pokemons'][entry['devid']]['name']].append(entry['biome4'])
            else:
                location_area_values[pokemon_dict['pokemons'][entry['devid']]['name']].append(pokemon_dict['pokemons'][entry['devid']]['name'])
                location_area_values[pokemon_dict['pokemons'][entry['devid']]['name']].append(entry['formno'])
                location_area_values[pokemon_dict['pokemons'][entry['devid']]['name']].append(entry['minlevel'])
                location_area_values[pokemon_dict['pokemons'][entry['devid']]['name']].append(entry['maxlevel'])
                location_area_values[pokemon_dict['pokemons'][entry['devid']]['name']].append(entry['biome1'])
                location_area_values[pokemon_dict['pokemons'][entry['devid']]['name']].append(entry['biome2'])
                location_area_values[pokemon_dict['pokemons'][entry['devid']]['name']].append(entry['biome3'])
                location_area_values[pokemon_dict['pokemons'][entry['devid']]['name']].append(entry['biome4'])

    for key, value in location_area_values.items():
        filename = f'Pokemon_No_A_L/{key}.txt'
        file_check = open(filename, 'w')
        for pokemon in value:
            print(f'{pokemon}', file=file_check)
