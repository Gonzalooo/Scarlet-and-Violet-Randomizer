import os
import platform
import subprocess
import json
import random


def open_json_file(filename: str):
    file = open(f'{filename}', 'r')
    file_json = json.load(file)
    file.close()

    return file_json


names_json = open_json_file('pokemon_list_info.json')
spawners_json = open_json_file('encount_data_100000.json')
spawnsers2_json = open_json_file('encount_data_atlantis.json')
spawners_kikakami = open_json_file('encount_data_su1.json')
spawners_blueberry = open_json_file('encount_data_su2.json')
devname_list = {}
arealist = {}
loclist = {}
biomelist = {}

for mon_data in names_json['pokemons']:
    devname_list[mon_data["devName"]] = {
    "name":mon_data["name"],
    "forms":mon_data["forms"],
    "natdex":mon_data["natdex"],
    "id":mon_data["id"]
    }


def safe_get(data, varname: str):
    if varname in data:
        get = data[varname]
    else:
        get = ""
    return get


def generate_spawner_sheet():
    filename = open('spanwers_merged_blueberry.csv', 'w')
    print("X,Y,Z,Min Lvl,Max Lvl,Biome,Substance,area", file=filename)
    biome_list = []
    biome_list += [[]] * (30 - len(biome_list))
    sub_list = []
    sub_list += [[]] * (30 - len(sub_list))
    for spawner_data in spawners_blueberry['encount_point_list']:
        get_biome = safe_get(spawner_data, "biome")
        get_area = safe_get(spawner_data, "area_no")
        get_substance = safe_get(spawner_data, "substance")
        print(safe_get(spawner_data["position"], "x"),",",
        safe_get(spawner_data["position"], "y"),",",
        safe_get(spawner_data["position"], "z"),",",
        safe_get(spawner_data["level_range"], "x"),",",
        safe_get(spawner_data["level_range"], "y"),",",
        get_biome,",",
        get_substance,",",
        get_area, file=filename)
        if get_area != "":
            if get_biome not in biome_list[get_area]:
                biome_list[get_area].append(get_biome)
            if get_substance not in sub_list[get_area]:
                sub_list[get_area].append(get_substance)
        else:
            biome_list[0].append(get_biome)
            sub_list[0].append(get_biome)
    print("---")
    print("extra data")
    for biome_data in biome_list:
        print("---")
        print(biome_data)
    for sub_data in sub_list:
        print("---")
        print(sub_data)


def generate_spawn_sheet():
    spawns_json = open_json_file('pokedata_array.json')
    print("name-Min lvl-Max lvl-Lot-Biome1-Lot1-Biome2-Lot2-Biome3-Lot3-Biome4-Lot4-Area-locationName-land-up_water-underwater-air1-air2-morning-noon-evening-night-flagName-bandrate-bandtype-bandpoke-outbreakLotvalue-pokeVoiceClassification-versiontable_A-versiontable_B-bringItem-bringRate")
    for mon_data in spawns_json['values']:
        namedata = safe_get(devname_list, safe_get(mon_data, "devid"))
        name = namedata["name"]
        
        bandpokedata = safe_get(devname_list, safe_get(mon_data, "bandpoke"))
        if isinstance(bandpokedata, str):
            bandpokename = "";
        else:
            bandpokename = bandpokedata["name"]
            
        getbiome = safe_get(mon_data, "biome1")
        if getbiome != "":
            biomelist[getbiome] = 1;
        getbiome = safe_get(mon_data, "biome2")
        if getbiome != "":
            biomelist[getbiome] = 1;
        getbiome = safe_get(mon_data, "biome3")
        if getbiome != "":
            biomelist[getbiome] = 1;
        getbiome = safe_get(mon_data, "biome4")
        if getbiome != "":
            biomelist[getbiome] = 1;
        getbiome = safe_get(mon_data, "area")
        if getbiome != "":
            arealist[getbiome] = 1;
        getbiome = safe_get(mon_data, "locationName")
        if getbiome != "":
            loclist[getbiome] = 1;

        print(name,"-",
         safe_get(mon_data, "minlevel"),"-",
         safe_get(mon_data, "maxlevel"),"-",
         safe_get(mon_data, "lotvalue"),"-",
         safe_get(mon_data, "biome1"),"-",
         safe_get(mon_data, "lotvalue1"),"-",
         safe_get(mon_data, "biome2"),"-",
         safe_get(mon_data, "lotvalue2"),"-",
         safe_get(mon_data, "biome3"),"-",
         safe_get(mon_data, "lotvalue3"),"-",
         safe_get(mon_data, "biome4"),"-",
         safe_get(mon_data, "lotvalue4"),"-",
         safe_get(mon_data, "area"),"-",
         safe_get(mon_data, "locationName"),"-",
         safe_get(mon_data["enabletable"], "land"),"-",
         safe_get(mon_data["enabletable"], "up_water"),"-",
         safe_get(mon_data["enabletable"], "underwater"),"-",
         safe_get(mon_data["enabletable"], "air1"),"-",
         safe_get(mon_data["enabletable"], "air2"),"-",
         safe_get(mon_data["timetable"], "morning"),"-",
         safe_get(mon_data["timetable"], "noon"),"-",
         safe_get(mon_data["timetable"], "evening"),"-",
         safe_get(mon_data["timetable"], "night"),"-",
         safe_get(mon_data, "flagName"),"-",
         safe_get(mon_data, "bandrate"),"-",
         safe_get(mon_data, "bandtype"),"-",
         bandpokename,"-",
         safe_get(mon_data, "outbreakLotvalue"),"-",
         mon_data["pokeVoiceClassification"],"-",
         safe_get(mon_data["versiontable"], "A"),"-",
         safe_get(mon_data["versiontable"], "B"),"-",
         mon_data["bringItem"]["itemID"],"-",
         mon_data["bringItem"]["bringRate"]
         )
    print("extra data")
    print(arealist)
    print(loclist)
    print(biomelist)
    
    
generate_spawner_sheet()