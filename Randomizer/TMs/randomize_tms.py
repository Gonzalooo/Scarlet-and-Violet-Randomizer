import json
import random
import os
import Randomizer.shared_Variables as SharedVariables
import Randomizer.helper_function as HelperFunctions


def randomize_tms(config):
    if config["randomize_tms"] == "yes":
        tmsfile = HelperFunctions.open_json_file('TMs/itemdata_array_clean.json')
        movesfile = HelperFunctions.open_json_file('TMs/move_list.json')

        for item in tmsfile['values']:
            if item['ItemType'] == "ITEMTYPE_WAZA":
                choice_name = movesfile['moves'][random.randint(0, len(movesfile['moves']) - 1)]['devName']
                choice_id = movesfile['moves'][random.randint(0, len(movesfile['moves']) - 1)]['id']

                if config["include_tms_without_animations"] == "yes":
                    while choice_id in SharedVariables.usedMoves:
                        choice_name = movesfile['moves'][random.randint(0, len(movesfile['moves']) - 1)]['devName']
                        choice_id = movesfile['moves'][random.randint(0, len(movesfile['moves']) - 1)]['id']
                else:
                    while choice_id in SharedVariables.usedMoves and choice_id not in SharedVariables.allowed_moves:
                        choice_name = movesfile['moves'][random.randint(0, len(movesfile['moves']) - 1)]['devName']
                        choice_id = movesfile['moves'][random.randint(0, len(movesfile['moves']) - 1)]['id']

                item['MachineWaza'] = choice_name
                SharedVariables.usedMoves.append(choice_id)

        outdata = json.dumps(tmsfile, indent=2)
        with open(os.getcwd() + "/Randomizer/TMs/" + "itemdata_array.json", 'w') as outfile:
            outfile.write(outdata)

        return True
    return False

