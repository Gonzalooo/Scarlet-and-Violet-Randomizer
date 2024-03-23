#  dropitemdata_array - can be used to have pokemon drop stuff (don't edit)

#  hiddenItemDataTable + _su is the drop tables for the hidden items in game + DLC

#  itemdata_array can be used to give items a buy price.

#  monohiroItemData is the pick up ability

#  rummagingItemData is for pokemon in the lets go feature

#  item data to randomize shop (potentially - needs testing)
import json
import random
import os

banned_items = [2311, 2313, 2314, 2315, 2316, 2317, 2318, 2319, 2320, 2321, 2322, 2323, 2324, 2325, 2326, 2327, 2329,
                2330, 2331, 2332, 2333, 2334, 2335, 2336, 2337, 2338, 2339, 2340, 2341, 2342, 2348, 2349, 2350, 2351,
                2352, 2353, 2354, 2355, 2356, 2357, 2358, 2359, 2360, 2361, 2362, 2363, 2364, 2365, 2366, 2367, 2368,
                2369, 2370, 2371, 2372, 2373, 2374, 2375, 2376, 2377, 2378, 2379, 2380, 2381, 2382, 2383, 2384, 2385,
                2386, 2387, 2388, 2389, 2390, 2391, 2392, 2393, 2394, 2395, 2396, 1857, 1858, 1889, 1890, 1891, 1892,
                1893, 1894, 1895, 1896, 1897, 1898, 1899, 1900, 1901, 1902, 1903, 1909, 1910, 1911, 1912, 1913, 1914,
                1915, 1916, 1917, 1918, 1919, 1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929, 1930, 1931,
                1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 2417, 2418,
                2419, 2420, 2421, 2422, 2423, 2424, 2425, 2426, 2427, 2428, 2429, 2430, 2431, 2432, 2433, 2434, 2435,
                2436, 2437, 2551, 2552]


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
                   itemData['items'][itemChoice]['id'] in banned_items or
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
                   itemData['items'][itemChoice]['id'] in banned_items or
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
                   itemData['items'][itemChoice]['id'] in banned_items or
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
                   itemData['items'][itemChoice]['id'] in banned_items or
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
                   itemData['items'][itemChoice]['id'] in banned_items or
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
                   itemData['items'][itemChoice]['id'] in banned_items or
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
               itemData['items'][itemChoice]['id'] in banned_items or
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

def randomize(config):
    if config['randomize_hidden_items'] == "yes":
        randomizeHiddenItems()
    if config['randomize_items_from_pickup_ability'] == "yes":
        randomizePickUpAbilityItems()
    if config['randomize_synchro_items'] == "yes":
        randomizeLetsGoItems()
    if config['randomize_pokemon_drops'] == "yes":
        randomizePokemonDrops()
