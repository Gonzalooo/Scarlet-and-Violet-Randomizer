import os
import platform
import subprocess


def create_folder_hierarchy(folder: str ):
    """
    Parameter should be a folder inside the main output folder.\n
    Ex: output/romfs/world/data/pokemon
    :param folder: Output/ folder to create
    :return: nothing
    """
    test = os.path.abspath(folder)
    test = test.replace("\\", '/')
    folders = test.split('/')
    index_value = 0
    for i in range(0, len(folders)):
        index_value = index_value + 1
        if folders[i] == "output":
            break

    test = folders[index_value:]

    foldertogetperms = "/"
    for i in range(1, index_value):
        foldertogetperms = foldertogetperms + f"{folders[i]}/"

    for i in range(0, len(test)):
        foldertogetperms = foldertogetperms + f"{test[i]}/"
        os.makedirs(foldertogetperms, mode=0o777, exist_ok=True)


def generate_binary(schema: str, json: str, path: str):
    iswindows = platform.system() == "Windows"
    flatc = os.path.abspath("flatc/flatc.exe") if iswindows else "flatc"

    create_folder_hierarchy('output/romfs/'+path+"/")
    outpath = os.path.abspath("output/romfs/" + path + "/")

    proc = subprocess.run(
        [flatc,
        "-b",
        "-o",
        outpath,
        os.path.abspath(schema),
        os.path.abspath(json)
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )

    return proc

