import os
import json
import copy

sprigattio_offset = 0x3D8A #6c 02
fuecoco_offset = 0x158A #6d 02
quaxly_offset = 0x2992 #6e 02


def patch_starter_selection_scenes():
    # load starters - 0 is fuecoco, 1 is sprigattio, 2 is quaxly
    starterfile = open(os.getcwd() + "/Randomizer/StartersGifts/" + "eventAddPokemon_array.json", "r")
    starters = json.load(starterfile)
    starterfile.close()

    # get pokemon dictionary with hex values
    pokemon_dict_json = open(os.getcwd() + "/Randomizer/Scenes/" + "pokemon_dict_info.json", "r")
    pokemon_dict = json.load(pokemon_dict_json)
    pokemon_dict_json.close()

    scarlet_scene = open(os.getcwd() + "/Randomizer/Scenes/common_0070_always_0_clean.trsog", "rb")
    violet_scene = open(os.getcwd() + "/Randomizer/Scenes/common_0070_always_1_clean.trsog", "rb")
    scarlet_scene_bytes = scarlet_scene.read()
    violet_scene_bytes = violet_scene.read()
    scarlet_scene.close()
    violet_scene.close()

    hex_checks = [pokemon_dict['pokemons'][starters['values'][0]['pokeData']['devId']]['hex'],
                  pokemon_dict['pokemons'][starters['values'][1]['pokeData']['devId']]['hex'],
                  pokemon_dict['pokemons'][starters['values'][2]['pokeData']['devId']]['hex']]

    for i in range(0, 2):
        with open(os.getcwd() + f"/Randomizer/Scenes/common_0070_always_{str(i)}.trsog", "w+b") as file:
            if i == 0:
                file.write(scarlet_scene_bytes)
            elif i == 1:
                file.write(violet_scene_bytes)
            file.seek(sprigattio_offset)
            file.write(bytearray.fromhex(hex_checks[1]))
            file.seek(fuecoco_offset)
            file.write(bytearray.fromhex(hex_checks[0]))
            file.seek(quaxly_offset)
            file.write(bytearray.fromhex(hex_checks[2]))

    print("Patched starters in overworld")
