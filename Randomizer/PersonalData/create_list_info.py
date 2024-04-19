import os
import json
import Randomizer.shared_Variables as shared_variables

def to_little_endian_hex_with_spaces(value: int):
    hex_str = hex(value)[2:]

    if len(hex_str) % 2 != 0:
        hex_str = '0' + hex_str

    if len(hex_str) % 4 != 0:
        hex_str = '00' + hex_str

    little_endian_hex = ' '.join(reversed([hex_str[i:i + 2] for i in range(0, len(hex_str), 2)]))

    return little_endian_hex.upper()

def to_little_endian_hex_with_spaces_form(value: int):
    hex_str = hex(value)[2:]

    if len(hex_str) % 2 != 0:
        hex_str = '0' + hex_str

    little_endian_hex = ' '.join(reversed([hex_str[i:i + 2] for i in range(0, len(hex_str), 2)]))

    return little_endian_hex.upper()

file = open('personal_array_clean.json', 'r')
personal_json = json.load(file)
file.close()

# Pokemons{
#   {
#   devid:
#   name:
#   devname:
#   is_present:
#   forms: [{
#       form
#       type1
#       type2
#       bst
#       animation_file
#       evolutions
#       }
#       ]
#

current_species = 0
pokemon_json = {'pokemons': []}

form_list = []
for pokemon in personal_json['entry']:
    print(pokemon['species']['species'])
    pokemon_dict = {
        "devid": current_species,
        "name": "",
        "devName": "",
        "natdex": 0,
        "anim_folder": "",
        'hex': to_little_endian_hex_with_spaces(int(current_species)),
        "forms": []
    }
    if pokemon['species']['species'] == current_species:
        form_dict = {
            'form': pokemon['species']['form'],
            "formName": "",
            "evolutionary_stage": 0,
            'is_present': pokemon['is_present'],
            'type1': pokemon['type_1'],
            'type2': pokemon['type_2'],
            'bst': 0,
            'hex': to_little_endian_hex_with_spaces(int(current_species)) + ' ' + to_little_endian_hex_with_spaces_form(int(pokemon['species']['form'])),
            "anim_file": "",
            "evolutions": []
        }
        bst = 0
        for stat in pokemon['base_stats']:
            bst += pokemon['base_stats'][stat]
        form_dict['bst'] = bst

        evolutions_list = []
        evolution_dict = {
            "name": "",
            "devName": "",
            "level": 0,
            "condition": 0,
            "devid": 0,
            "natdex": 0,
            "form": 0
        }
        for evolutions in pokemon['evolutions']:
            evolution_dict['level'] = evolutions['level']
            evolution_dict['devid'] = evolutions['species']
            evolution_dict['natdex'] = 0
            evolution_dict['form'] = evolutions['form']
            evolution_dict['condition'] = evolutions['condition']
            evolutions_list.append(evolution_dict.copy())
        form_dict['evolutions'] = evolutions_list.copy()
        form_list.append(form_dict)

    else:
        pokemon_dict['forms'] = form_list.copy()
        pokemon_json['pokemons'].append(pokemon_dict)
        form_list.clear()
        current_species = pokemon['species']['species']
        if current_species == 1025:
            print("here")
        form_dict = {
            'form': pokemon['species']['form'],
            "formName": "",
            "evolutionary_stage": 0,
            'is_present': pokemon['is_present'],
            'type1': pokemon['type_1'],
            'type2': pokemon['type_2'],
            'bst': 0,
            'hex': to_little_endian_hex_with_spaces(int(current_species)) + ' ' + to_little_endian_hex_with_spaces_form(
                int(pokemon['species']['form'])),
            "anim_file": "",
            "evolutions": []
        }
        bst = 0
        for stat in pokemon['base_stats']:
            bst += pokemon['base_stats'][stat]
        form_dict['bst'] = bst

        evolutions_list = []
        evolution_dict = {
            "level": 0,
            "condition": 0,
            "name": "",
            "devName": "",
            "devid": 0,
            "natdex": 0,
            "form": 0
        }
        for evolutions in pokemon['evolutions']:
            evolution_dict['level'] = evolutions['level']
            evolution_dict['devid'] = evolutions['species']
            evolution_dict['natdex'] = 0
            evolution_dict['form'] = evolutions['form']
            evolution_dict['condition'] = evolutions['condition']
            evolutions_list.append(evolution_dict.copy())
        form_dict['evolutions'] = evolutions_list.copy()
        form_list.append(form_dict)

pokemon_dict['forms'] = form_list.copy()
pokemon_json['pokemons'].append(pokemon_dict)
outdata = json.dumps(pokemon_json, indent=2)
with open('updated_check.json', 'w') as outfile:
    outfile.write(outdata)

file = open('updated_check.json', 'r')
pokemon_json = json.load(file)
file.close()

comparefile = open('pokemon_list_info.json')
compare = json.load(comparefile)
comparefile.close()

for entry in pokemon_json['pokemons']:
    for compared in compare['pokemons']:
        if entry['devid'] == compared['id']:
            entry['name'] = compared['name']
            entry['devName'] = compared['devName']
            entry['natdex'] = compared['natdex']
            entry['anim_folder'] = compared['anim_file']
            for i in range(0, len(entry['forms'])):

                if entry['natdex'] in shared_variables.gen9Stage1:
                    entry['forms'][i]['evolutionary_stage'] = 1
                elif entry['natdex'] in shared_variables.gen9Stage2:
                    entry['forms'][i]['evolutionary_stage'] = 2
                elif entry['natdex'] in shared_variables.gen9Stage3:
                    entry['forms'][i]['evolutionary_stage'] = 3
                elif entry['natdex'] in shared_variables.no_evolution:
                    entry['forms'][i]['evolutionary_stage'] = 0

                for j in range(0, len(entry['forms'][i]['evolutions'])):
                    for evolution_check in compare['pokemons']:
                        if entry['forms'][i]['evolutions'][j]['devid'] == evolution_check['id']:
                            entry['forms'][i]['evolutions'][j]['name'] = evolution_check['name']
                            entry['forms'][i]['evolutions'][j]['devName'] = evolution_check['devName']
                            entry['forms'][i]['evolutions'][j]['natdex'] = evolution_check['natdex']

outdata = json.dumps(pokemon_json, indent=2)
with open('updated_check.json', 'w') as outfile:
    outfile.write(outdata)