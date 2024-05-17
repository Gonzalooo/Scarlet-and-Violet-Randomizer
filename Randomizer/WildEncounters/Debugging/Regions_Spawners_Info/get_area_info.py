import os
import json

area_dictionary = {}
area_dictionary['area'] = []
paldea_mapping_name = {"1": "South Province (Area One)",
"2": "Unused Area",
"3": "Pokemon League",
"4": "South Province (Area Two)",
"5": "South Province (Area Four)",
"6": "South Province (Area Six)",
"7": "South Province (Area Five)",
"8": "South Province (Area Three)",
"9": "West Province (Area One)",
"10": "Asado Desert",
"11": "West Province (Area Two)",
"12": "West Province (Area Three)",
"13": "Tagtree Thicket",
"14": "East Province (Area Three)",
"15": "East Province (Area One)",
"16":  "East Province (Area Two)",
"17": "Dalizapa Passage",
"18": "Casseroya Lake",
"19": "Glaseado Mountain",
"20": "North Province (Area Three)",
"21": "North Province (Area One)",
"22": "North Province (Area Two)",
"23": "Area Zero",
"24": "South Paldean Sea",
"25": "West Paldean Sea",
"26": "East Paldean Sea",
"27": "North Paldean Sea"
}
kitakami_mapping_name = {
"1": "Kitakami Road",
"2": "Apple Hills",
"3": "Reveler's Road",
"4": "Oni Mountain",
"5": "Infernal Passage",
"6": "Crystal Pool",
"7": "Wistful Fields",
"8": "Mossfell Confluence",
"9": "Fellhorn Gorge",
"10": "Paradize Barrens",
"11": "kitakami wilds/timeless wood"
}
blueberry_mapping_name = {
"1": "Savannah",
"2": "Coastal",
"3": "Polar",
"4": "Canyon",
}
for filename in os.listdir('AZ-Spawners'):
    if filename.endswith('.txt'):
        min = []
        max = []
        biomes = []
        area_dict = {}
        file = open('AZ-Spawners/'+filename, 'r')
        number_area = filename[:2]
        if number_area[1] == "-":
            number_area = filename[:1]
        area_dict[f'{str(number_area)}'] = {}
        area_dict[f'{str(number_area)}']['name'] = paldea_mapping_name[number_area]
        for line in file:
            needed_information = line.split(',')[3:6]
            full_info = ",".join(needed_information)
            values_to_save = full_info.split(':')
            min_val = (values_to_save[2])[1:5].replace(',', "")
            max_val = (values_to_save[3])[1:5].replace(',', "")
            biomes_val = (values_to_save[4])[1:].replace(',', "")
            min_val = min_val.replace('}', "")
            max_val = max_val.replace('}', "")
            min.append(float(min_val.replace('\'', "")))
            max.append(float(max_val.replace('\'', "")))
            if 'prairie' in biomes_val:
                biomes_val = 'grass'
            if 'rocky_area' in biomes_val:
                biomes_val = 'rocky'
            if 'bamboo_forest' in biomes_val:
                biomes_val = 'bamboo'
            if 'ocean' in biomes_val:
                biomes_val = 'osean'
            if 'snowfield' in biomes_val:
                biomes_val = 'snow'
            if 'riverside' in biomes_val:
                biomes_val = 'river'
            biomes.append(biomes_val.replace('\'', "").upper())
        min = list(set(min))
        max = list(set(max))
        biomes = list(set(biomes))
        area_dict[f'{str(number_area)}']['min'] = min[0]
        area_dict[f'{str(number_area)}']['max'] = max[len(max)-1]
        area_dict[f'{str(number_area)}']['biomes'] = biomes

        file_area = open(f'../Pokemon_Spawning_Info/Pokemon_Area/area_{number_area}.txt', 'r')
        area_dict[f'{str(number_area)}']['pokemons'] = []
        counter = 0
        pokemon_dict_area = {}
        for line in file_area:
            if counter == 0:
                pokemon_dict_area['name'] = line[:-1]
                if "\n" in pokemon_dict_area['name']:
                    pokemon_dict_area['name'] = pokemon_dict_area['name'][:-1]
                pokemon_dict_area['locationname'] = ""
                counter += 1
                continue
            if counter == 1:
                pokemon_dict_area['form'] = line[:-1]
                counter += 1
                continue
            if counter == 2:
                pokemon_dict_area['minlevel'] = line[:-1]
                counter += 1
                continue
            if counter == 3:
                pokemon_dict_area['maxlevel'] = line[:-1]
                counter += 1
                continue
            if counter == 4:
                pokemon_dict_area['biomes'] = []
                pokemon_dict_area['biomes'].append(line[:-1])
                counter += 1
                continue
            if counter == 5:
                if "NONE" not in line and "------------------------------" not in line:
                    pokemon_dict_area['biomes'].append(line[:-1])
                counter += 1
                continue
            if counter == 6:
                if "NONE" not in line and "------------------------------" not in line:
                    pokemon_dict_area['biomes'].append(line[:-1])
                counter += 1
                continue
            if counter == 7:
                if "NONE" not in line and "------------------------------" not in line:
                    pokemon_dict_area['biomes'].append(line[:-1])
                counter += 1
                continue
            if counter == 8:
                if ((float(pokemon_dict_area['minlevel']) <= area_dict[f'{str(number_area)}']['max'])
                        and
                        (float(pokemon_dict_area['maxlevel']) >= area_dict[f'{str(number_area)}']['min'])):
                    area_dict[f'{str(number_area)}']['pokemons'].append(pokemon_dict_area)
                else:
                    print(
                        f'{area_dict[f'{str(number_area)}']['name']} is not allowed for: {pokemon_dict_area['name']}')
                    print(
                        f'{area_dict[f'{str(number_area)}']['name']} range is: {str(area_dict[f'{str(number_area)}']['min'])}' + ' - ' +
                        str(area_dict[f'{str(number_area)}']['max']))
                    print(
                        f'{pokemon_dict_area['name']} level ranges are: {str(pokemon_dict_area['minlevel'])} - {str(pokemon_dict_area['maxlevel'])}')
                pokemon_dict_area = {}
                counter = 0

        for filename in os.listdir('../Pokemon_Spawning_Info/Pokemon_No_A_L'):
            if filename.endswith('.txt'):
                pokemon_file = open(f'../Pokemon_Spawning_Info/Pokemon_No_A_L/{filename}', 'r')
                counter = 0
                print(area_dict)
                for line in pokemon_file:
                    if counter == 0:
                        pokemon_dict_area['name'] = line[:-1]
                        if "\n" in pokemon_dict_area['name']:
                            pokemon_dict_area['name'] = pokemon_dict_area['name'][:-1]
                        pokemon_dict_area['locationname'] = ""
                        counter += 1
                        continue
                    if counter == 1:
                        pokemon_dict_area['form'] = line[:-1]
                        counter += 1
                        continue
                    if counter == 2:
                        pokemon_dict_area['minlevel'] = line[:-1]
                        counter += 1
                        continue
                    if counter == 3:
                        pokemon_dict_area['maxlevel'] = line[:-1]
                        counter += 1
                        continue
                    if counter == 4:
                        pokemon_dict_area['biomes'] = []
                        pokemon_dict_area['biomes'].append(line[:-1])
                        counter += 1
                        continue
                    if counter == 5:
                        if "NONE" not in line and "------------------------------" not in line:
                            pokemon_dict_area['biomes'].append(line[:-1])
                        counter += 1
                        continue
                    if counter == 6:
                        if "NONE" not in line and "------------------------------" not in line:
                            pokemon_dict_area['biomes'].append(line[:-1])
                        counter += 1
                        continue
                    if counter == 7:
                        if "NONE" not in line and "------------------------------" not in line:
                            pokemon_dict_area['biomes'].append(line[:-1])
                        counter += 1
                        continue
                    if counter == 8:
                        #print(pokemon_dict_area)
                        if ((float(pokemon_dict_area['minlevel']) <= area_dict[f'{str(number_area)}']['max'])
                                and
                                (float(pokemon_dict_area['maxlevel']) >= area_dict[f'{str(number_area)}']['min'])):
                            area_dict[f'{str(number_area)}']['pokemons'].append(pokemon_dict_area)
                        else:
                            print(
                                f'{area_dict[f'{str(number_area)}']['name']} is not allowed for: {pokemon_dict_area['name']}')
                            print(
                                f'{area_dict[f'{str(number_area)}']['name']} range is: {str(area_dict[f'{str(number_area)}']['min'])}' + ' - ' +
                                str(area_dict[f'{str(number_area)}']['max']))
                            print(
                                f'{pokemon_dict_area['name']} level ranges are: {str(pokemon_dict_area['minlevel'])} - {str(pokemon_dict_area['maxlevel'])}')
                        pokemon_dict_area = {}
                        counter = 0

        for filename in os.listdir(f'../Pokemon_Spawning_Info/Pokemon_Location'):
            if filename.endswith('.txt') and "a_w23_" in filename:
                file = open('../Pokemon_Spawning_Info/Pokemon_Location/' + filename, 'r')
                if str(number_area) == "23":
                    counter = 0
                    pokemon_dict_area = {}
                    for line in file:
                        if counter == 0:
                            pokemon_dict_area['name'] = line[:-1]
                            if "\n" in pokemon_dict_area['name']:
                                pokemon_dict_area['name'] = pokemon_dict_area['name'][:-1]
                            pokemon_dict_area['locationname'] = filename[:-4]
                            counter += 1
                            continue
                        if counter == 1:
                            pokemon_dict_area['form'] = line[:-1]
                            counter += 1
                            continue
                        if counter == 2:
                            pokemon_dict_area['minlevel'] = line[:-1]
                            counter += 1
                            continue
                        if counter == 3:
                            pokemon_dict_area['maxlevel'] = line[:-1]
                            counter += 1
                            continue
                        if counter == 4:
                            pokemon_dict_area['biomes'] = []
                            pokemon_dict_area['biomes'].append(line[:-1])
                            counter += 1
                            continue
                        if counter == 5:
                            if "NONE" not in line and "------------------------------" not in line:
                                pokemon_dict_area['biomes'].append(line[:-1])
                            counter += 1
                            continue
                        if counter == 6:
                            if "NONE" not in line and "------------------------------" not in line:
                                pokemon_dict_area['biomes'].append(line[:-1])
                            counter += 1
                            continue
                        if counter == 7:
                            if "NONE" not in line and "------------------------------" not in line:
                                pokemon_dict_area['biomes'].append(line[:-1])
                            counter += 1
                            continue
                        if counter == 8:
                            if ((float(pokemon_dict_area['minlevel']) <= area_dict[f'{str(number_area)}']['max'])
                                    and
                                    (float(pokemon_dict_area['maxlevel']) >= area_dict[f'{str(number_area)}']['min'])):
                                area_dict[f'{str(number_area)}']['pokemons'].append(pokemon_dict_area)
                            else:
                                print(
                                    f'{area_dict[f'{str(number_area)}']['name']} is not allowed for: {pokemon_dict_area['name']}')
                                print(
                                    f'{area_dict[f'{str(number_area)}']['name']} range is: {str(area_dict[f'{str(number_area)}']['min'])}' + ' - ' +
                                    str(area_dict[f'{str(number_area)}']['max']))
                                print(
                                    f'{pokemon_dict_area['name']} level ranges are: {str(pokemon_dict_area['minlevel'])} - {str(pokemon_dict_area['maxlevel'])}')
                            pokemon_dict_area = {}
                            counter = 0

        area_dictionary['area'].append(area_dict)

outdata = json.dumps(area_dictionary, indent=2)
with open('az_areas_mapping.json', 'w') as outfile:
    outfile.write(outdata)

second_check_json = open('az_areas_mapping.json', 'r')
second_check = json.load(second_check_json)
second_check_json.close()

second_check_array = []
for entry in second_check['area']:
    for areas in entry:
        biomes_check = entry[areas]['biomes']
        for pokemon in entry[areas]['pokemons']:
            biome_counter = 0
            for i in range(0, len(pokemon['biomes'])):
                if pokemon['biomes'][i] not in biomes_check:
                    biome_counter += 1
            if biome_counter == len(pokemon['biomes']):
                print(f'No Biome for {pokemon['name']}')
            else:
                second_check_array.append(pokemon)
        entry[areas]['pokemons'] = second_check_array
        second_check_array = []
if True is True:
    bst_file = open('../../../pokemon_mapping.json', 'r')
    bstcheck = json.load(bst_file)
    bst_file.close()
    count_entry = 0
    for entry in second_check['area']:
        for areas in entry:
            areanum = "0"
            if len(areas) == 1:
                areanum = "0" + str(areas)
            else:
                areanum = str(areas)
            area_bst = 0
            bst_count = 0
            print(f'Currently checking {areanum} - {areas} - {count_entry}')
            for pokemon in entry[areas]['pokemons']:
                location_check = ""
                if "subarea_su01" in pokemon['locationname']:
                    location_check = pokemon['locationname'].replace("subarea_su02", "")
                elif "a_su01" in pokemon['locationname']:
                    location_check = pokemon['locationname'].replace("a_su02", "")
                elif pokemon['locationname'] == "":
                    pass

                if location_check != "":
                    try:
                        second_check_index = location_check.index(f'{areas}')
                        if second_check_index == 0:
                            pass
                        elif second_check_index == 1:
                            pass
                        elif second_check_index >= 2:
                            continue
                    except ValueError:
                        #print(f"error with: {location_check}")
                        pass

                if location_check == "" or areanum in location_check:
                    name_check = ""
                    if " - SAME" in pokemon['name']:
                        name_check = pokemon['name'].replace(" - SAME", "")
                    if " - BOSS" in pokemon['name']:
                        name_check = pokemon['name'].replace(" - BOSS", "")
                    if " - SAME" not in pokemon['name'] and " - BOSS" not in pokemon['name']:
                        name_check = pokemon['name']

                    area_bst += bstcheck['pokemons_name'][name_check]['forms'][int(pokemon['form'])]['bst']
                    bst_count += 1

                    print(f'{name_check} in area: {areanum} is in location: {location_check}')

            try:
                print(int(area_bst/bst_count))
                second_check['area'][count_entry][areas]['avg_bst'] = int(area_bst/bst_count)
                count_entry += 1
            except ZeroDivisionError:
                print(area_bst)
                count_entry += 1


outdata = json.dumps(second_check, indent=2)
with open('az_areas_mapping.json', 'w') as outfile:
    outfile.write(outdata)
