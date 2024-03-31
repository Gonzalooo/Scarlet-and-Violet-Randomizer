#  dropitemdata_array - can be used to have pokemon drop stuff (don't edit)

#  hiddenItemDataTable + _su is the drop tables for the hidden items in game + DLC

#  itemdata_array can be used to give items a buy price.

#  monohiroItemData is the pick up ability

#  rummagingItemData is for pokemon in the lets go feature

#  item data to randomize shop (potentially - needs testing)
import json
import random
import os
import Randomizer.shared_Variables as SharedVariables


def randomizeHiddenItems():
    # emerge percent is % of it showing up
    # Get information on Items (using file to future proof for more options to check)
    item_info = open(os.getcwd() + '/Randomizer/Items/' + 'pokemon_items_dev.json', 'r')
    itemData = json.load(item_info)
    item_info.close()

    paldeaHiddenItemsFile = open(os.getcwd() + '/Randomizer/Items/' + 'hiddenItemDataTable_array_clean.json', 'r')
    paldeaItems = json.load(paldeaHiddenItemsFile)
    paldeaHiddenItemsFile.close()

    TealHiddenItemsFile = open(os.getcwd() + '/Randomizer/Items/' + 'hiddenItemDataTable_su1_array_clean.json', 'r')
    kitakamiItems = json.load(TealHiddenItemsFile)
    TealHiddenItemsFile.close()

    IndigoHiddenItemsFile = open(os.getcwd() + '/Randomizer/Items/' + 'hiddenItemDataTable_su2_array_clean.json', 'r')
    blueberryItems = json.load(IndigoHiddenItemsFile)
    IndigoHiddenItemsFile.close()

    lcHiddenItemsFile = open(os.getcwd() + '/Randomizer/Items/' + 'hiddenItemDataTable_lc_array_clean.json', 'r')
    lcItems = json.load(lcHiddenItemsFile)
    lcHiddenItemsFile.close()

    for i in range(0, len(paldeaItems['values'])):
        for j in range(1, 11):
            itemChoice = random.randint(1, 1090)
            while (itemData['items'][itemChoice]['ItemType'] == "ITEMTYPE_MATERIAL" or
                   itemData['items'][itemChoice]['id'] in SharedVariables.banned_items or
                   itemData['items'][itemChoice]['ItemType'] == "ITEMTYPE_EVENT" or
                   itemData['items'][itemChoice]['ItemType'] == "ITEMTYPE_BATTLE" or
                    itemData['items'][itemChoice]['ItemType'] == "ITEMTYPE_POCKET"):
                itemChoice = random.randint(1, 1090)
            paldeaItems['values'][i][f'item_{str(j)}']['itemId'] = itemData['items'][itemChoice]['devName']
            paldeaItems['values'][i][f'item_{str(j)}']['emergePercent'] = random.randint(100, 1000)
            paldeaItems['values'][i][f'item_{str(j)}']['dropCount'] = random.randint(1, 20)
        #print(paldeaItems['values'][i])

    for i in range(0, len(kitakamiItems['values'])):
        for j in range(1, 11):
            itemChoice = random.randint(1, 1090)
            while (itemData['items'][itemChoice]['ItemType'] == "ITEMTYPE_MATERIAL" or
                   itemData['items'][itemChoice]['id'] in SharedVariables.banned_items or
                   itemData['items'][itemChoice]['ItemType'] == "ITEMTYPE_EVENT" or
                   itemData['items'][itemChoice]['ItemType'] == "ITEMTYPE_BATTLE" or
                    itemData['items'][itemChoice]['ItemType'] == "ITEMTYPE_POCKET"):
                itemChoice = random.randint(1, 1090)
            kitakamiItems['values'][i][f'item_{str(j)}']['itemId'] = itemData['items'][itemChoice]['devName']
            kitakamiItems['values'][i][f'item_{str(j)}']['emergePercent'] = random.randint(100, 1000)
            kitakamiItems['values'][i][f'item_{str(j)}']['dropCount'] = random.randint(1, 20)
        #print(kitakamiItems['values'][i])

    for i in range(0, len(blueberryItems['values'])):
        for j in range(1, 11):
            itemChoice = random.randint(1, 1090)
            while (itemData['items'][itemChoice]['ItemType'] == "ITEMTYPE_MATERIAL" or
                   itemData['items'][itemChoice]['id'] in SharedVariables.banned_items or
                   itemData['items'][itemChoice]['ItemType'] == "ITEMTYPE_EVENT" or
                   itemData['items'][itemChoice]['ItemType'] == "ITEMTYPE_BATTLE" or
                    itemData['items'][itemChoice]['ItemType'] == "ITEMTYPE_POCKET"):
                itemChoice = random.randint(1, 1090)
            blueberryItems['values'][i][f'item_{str(j)}']['itemId'] = itemData['items'][itemChoice]['devName']
            blueberryItems['values'][i][f'item_{str(j)}']['emergePercent'] = random.randint(100, 1000)
            blueberryItems['values'][i][f'item_{str(j)}']['dropCount'] = random.randint(1, 20)
        #print(blueberryItems['values'][i])

    for i in range(0, len(lcItems['values'])):
        for j in range(1, 11):
            itemChoice = random.randint(1, 1090)
            while (itemData['items'][itemChoice]['ItemType'] == "ITEMTYPE_MATERIAL" or
                   itemData['items'][itemChoice]['id'] in SharedVariables.banned_items or
                   itemData['items'][itemChoice]['ItemType'] == "ITEMTYPE_EVENT" or
                   itemData['items'][itemChoice]['ItemType'] == "ITEMTYPE_BATTLE" or
                    itemData['items'][itemChoice]['ItemType'] == "ITEMTYPE_POCKET"):
                itemChoice = random.randint(1, 1090)
            lcItems['values'][i][f'item_{str(j)}']['itemId'] = itemData['items'][itemChoice]['devName']
            lcItems['values'][i][f'item_{str(j)}']['emergePercent'] = random.randint(100, 1000)
            lcItems['values'][i][f'item_{str(j)}']['dropCount'] = random.randint(1, 20)
        #print(lcItems['values'][i])

    outdata = json.dumps(lcItems, indent=2)
    with open(os.getcwd() + "/Randomizer/Items/" +"hiddenItemDataTable_lc_array.json", 'w') as outfile:
        outfile.write(outdata)

    outdata = json.dumps(blueberryItems, indent=2)
    with open(os.getcwd() + "/Randomizer/Items/" +"hiddenItemDataTable_su2_array.json", 'w') as outfile:
        outfile.write(outdata)

    outdata = json.dumps(kitakamiItems, indent=2)
    with open(os.getcwd() + "/Randomizer/Items/" +"hiddenItemDataTable_su1_array.json", 'w') as outfile:
        outfile.write(outdata)

    outdata = json.dumps(paldeaItems, indent=2)
    with open(os.getcwd() + "/Randomizer/Items/" +"hiddenItemDataTable_array.json", 'w') as outfile:
        outfile.write(outdata)

    print("Randomisation Of Hidden Items in Paldea/Kitakami/Blueberry Done!")


def randomizePickUpAbilityItems():
    # Under construction as I need to figure out how to weight the rates correctly
    item_info = open(os.getcwd() + '/Randomizer/Items/' + 'pokemon_items_dev.json', 'r')
    itemData = json.load(item_info)
    item_info.close()
    pickupItemsFile = open(os.getcwd() + '/Randomizer/Items/' + 'monohiroiItemData_array_clean.json', 'r')
    pickitems = json.load(pickupItemsFile)
    pickupItemsFile.close()

    for i in range(0, len(pickitems['values'])):
        for j in range(1, 31):
            itemChoice = random.randint(1, 1090)
            while (itemData['items'][itemChoice]['ItemType'] == "ITEMTYPE_MATERIAL" or
                   itemData['items'][itemChoice]['id'] in SharedVariables.banned_items or
                   itemData['items'][itemChoice]['ItemType'] == "ITEMTYPE_EVENT" or
                   itemData['items'][itemChoice]['ItemType'] == "ITEMTYPE_BATTLE" or
                    itemData['items'][itemChoice]['ItemType'] == "ITEMTYPE_POCKET"):
                itemChoice = random.randint(1, 1090)

            itemstring = ""
            if j < 10:
                itemstring = f"0{str(j)}"
            else:
                itemstring = f"{str(j)}"
            pickitems['values'][i]["item_"+itemstring]['itemId'] = itemData['items'][itemChoice]['devName']

        #print(pickitems['values'][i])

    outdata = json.dumps(pickitems, indent=2)
    with open(os.getcwd() + "/Randomizer/Items/" +"monohiroiItemData_array.json", 'w') as outfile:
        outfile.write(outdata)
    print("Randomized Items for PickUp Ability!")


def randomizeLetsGoItems(): # rummagingItemDataTable
    item_info = open(os.getcwd() + '/Randomizer/Items/' + 'pokemon_items_dev.json', 'r')
    itemData = json.load(item_info)
    item_info.close()
    pickupItemsFile = open(os.getcwd() + '/Randomizer/Items/' + 'rummagingItemDataTable_array_clean.json', 'r')
    pickitems = json.load(pickupItemsFile)
    pickupItemsFile.close()

    for i in range(0, len(pickitems['values'])):
        for j in range(0, 5):
            itemChoice = random.randint(1, 1090)
            while (itemData['items'][itemChoice]['ItemType'] == "ITEMTYPE_MATERIAL" or
                   itemData['items'][itemChoice]['id'] in SharedVariables.banned_items or
                   itemData['items'][itemChoice]['ItemType'] == "ITEMTYPE_EVENT" or
                   itemData['items'][itemChoice]['ItemType'] == "ITEMTYPE_BATTLE" or
                    itemData['items'][itemChoice]['ItemType'] == "ITEMTYPE_POCKET"):
                itemChoice = random.randint(1, 1090)

            itemstring = ""
            if j < 10:
                itemstring = f"0{str(j)}"
            else:
                itemstring = f"{str(j)}"
            pickitems['values'][i]["Item"+itemstring] = itemData['items'][itemChoice]['devName']
        #print(pickitems['values'][i])

    outdata = json.dumps(pickitems, indent=2)
    with open(os.getcwd() + "/Randomizer/Items/" +"rummagingItemDataTable_array.json", 'w') as outfile:
        outfile.write(outdata)
    print("Randomized Items for LetsGo/Synchro!")


def randomizePokemonDrops():
    item_info = open(os.getcwd() + '/Randomizer/Items/' + 'pokemon_items_dev.json', 'r')
    itemData = json.load(item_info)
    item_info.close()
    pickupItemsFile = open(os.getcwd() + '/Randomizer/Items/' + 'dropitemdata_array_clean.json', 'r')
    pickitems = json.load(pickupItemsFile)
    pickupItemsFile.close()

    for i in range(0, len(pickitems['values'])):
        itemChoice = random.randint(1, 1090)
        while (itemData['items'][itemChoice]['ItemType'] == "ITEMTYPE_MATERIAL" or
               itemData['items'][itemChoice]['id'] in SharedVariables.banned_items or
               itemData['items'][itemChoice]['ItemType'] == "ITEMTYPE_EVENT" or
               itemData['items'][itemChoice]['ItemType'] == "ITEMTYPE_BATTLE" or
               itemData['items'][itemChoice]['ItemType'] == "ITEMTYPE_POCKET"):
            itemChoice = random.randint(1, 1090)

        pickitems['values'][i]["item1"]['itemid'] = itemData['items'][itemChoice]['devName']

        #print(pickitems['values'][i])

    outdata = json.dumps(pickitems, indent=2)
    with open(os.getcwd() + "/Randomizer/Items/" + "dropitemdata_array.json", 'w') as outfile:
        outfile.write(outdata)
    print("Randomized Items for Pokemon Drops!")


def randomize_items(config):
    if config['is_enabled'] == "yes":
        hidden = False
        pickup = False
        synchro = False
        drops = False
        if config['randomize_hidden_items'] == "yes":
            randomizeHiddenItems()
            hidden = True
        if config['randomize_items_from_pickup_ability'] == "yes":
            randomizePickUpAbilityItems()
            pickup = True
        if config['randomize_synchro_items'] == "yes":
            randomizeLetsGoItems()
            synchro = True
        if config['randomize_pokemon_drops'] == "yes":
            randomizePokemonDrops()
            drops = True

        return hidden, pickup, synchro, drops
    return False, False, False, False
