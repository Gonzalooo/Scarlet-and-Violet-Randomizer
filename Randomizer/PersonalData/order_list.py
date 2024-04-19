import json


def to_little_endian_hex_with_spaces(value: int):
    hex_str = hex(value)[2:]

    if len(hex_str) % 2 != 0:
        hex_str = '0' + hex_str

    if len(hex_str) % 4 != 0:
        hex_str = '00' + hex_str

    little_endian_hex = ' '.join(reversed([hex_str[i:i + 2] for i in range(0, len(hex_str), 2)]))

    return little_endian_hex.upper()


file = open('updated_check.json', 'r')
pokemon_json = json.load(file)
file.close()

file_2 = open('pokemon_info.json', 'r')
filled_form = json.load(file_2)
file_2.close()

for i in range(0, len(pokemon_json['pokemons'])):
    for j in range(0, len(pokemon_json['pokemons'][i]['forms'])):
        pokemon_json['pokemons'][i]['forms'][j]['formName'] = filled_form['pokemons'][i]['forms'][j]['formName']

# order the list by nat dex
ordered_list = sorted(pokemon_json['pokemons'], key=lambda x: x['natdex'])
pokemon_json['pokemons'] = ordered_list

# create a list by devName
pokemon_json['pokemons_dev'] = {}
for entry in pokemon_json['pokemons']:
    key = entry['devName']
    pokemon_json["pokemons_dev"][f'{key}'] = {
        "devid": entry['devid'],
        "name": entry['name'],
        "natdex": entry['natdex'],
        "anim_folder": entry['anim_folder'],
        "hex": entry['hex'],
        "forms": entry['forms']
    }

# create a list by name
pokemon_json['pokemons_name'] = {}
for entry in pokemon_json['pokemons']:
    key = entry['name']
    pokemon_json["pokemons_name"][f'{key}'] = {
        "devid": entry['devid'],
        "devName": entry['devName'],
        "natdex": entry['natdex'],
        "anim_folder": entry['anim_folder'],
        "hex": entry['hex'],
        "forms": entry['forms']
    }

outdata = json.dumps(pokemon_json, indent=2)
with open('ordered_test.json', 'w') as outfile:
    outfile.write(outdata)