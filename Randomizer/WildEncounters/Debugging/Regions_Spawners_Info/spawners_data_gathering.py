import json

spawner_paldea_json = open('encount_data_su2.json', 'r')
spawner_paldea = json.load(spawner_paldea_json)
spawner_paldea_json.close()

spawner_area_location: dict[str, list[dict]] = {}
for entry in spawner_paldea['encount_point_list']:
    try:
        spawner_area_location[entry['area_no']].append(entry)
    except KeyError:
        spawner_area_location[entry['area_no']] = []
        spawner_area_location[entry['area_no']].append(entry)

for key, value in spawner_area_location.items():
    file = open(f'{key}-Blueberry.txt', 'w')
    for spawner in value:
        print(spawner, file=file)
