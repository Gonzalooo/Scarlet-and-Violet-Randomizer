--- Pokemon Scarlet and Violet Randomizer by XLuma updated by Gonzalo----
Go to: https://github.com/Gonzalooo/Scarlet-and-Violet-Randomizer for latest Version.

***IMPORTANT: GO TO Randomizer/Starters/pokemon_clean before running the randomizer***
VIDEO TUTORIAL on how to use randomizer tool: https://youtu.be/eO10cWC6QT0
Tutorial on how to use Generation Limiter: https://youtu.be/dCUUXFHNRcA
Trinity Loader Nightly Version: https://github.com/pkZukan/gftool/releases/tag/nightly (Needed for the first steps - nightly version automatically updates so it has the stuff you need)
New discord link to keep up with udpates btw: https://discord.gg/d7UBuXGrT2

*** THIS RANDOMIZER WORKS ONLY WITH VERSION 3.0.1/3.0.0***
PREFACE: Make sure you have at least Python 3.10 installed on your computer, anything lower will not work!
PS: If after installing, and running the randomize batch script you see the Microsoft store open instead, in your windows search bar type "Manage App Execution Aliases" and turn off the ones that have "python.exe" and "python3.exe" under them (They are named App Installer)

ALTERNATE WAY HOW TO USE: (ONLY READ IF YOU DON'T WANT TO USE AUTO-PATCHER)

- If not done, install Python 3.10 from either the Microsoft Store, or the official python website

Step 1: Open the config.json in any text editor (even notepad works) and configure the file how you want it. To enable an option, type yes between quotes. If you want to disable , then type no instead.
Step 2: Save your edits to the config.json, and double click the randomize.bat file. A window will appear with some logs, and eventually a Press Enter to continue will appear, then you can close that window.
Step 3: A new folder called "output" will be created. Go inside of it, and you will see a romfs folder as well as a randomizer.zip file. The randomizer.zip is the compressed, ready-to-use modpack to be imported in Trinity Mod Loader.
		- Romfs Folder is there for legacy reasons. Will be useful in the future.
Step 4: Open Trinity Loader, click "Add Mod (.zip)" and select the randomizer.zip inside the output folder, make sure it is ticked in the window, and then click Apply mod. 
        - Copy the resulting romfs folder to your mods folder on your switch or emulator, and launch the game
Step 5: Enjoy :)

TITLEID'S

Scarlet: 0100A3D008C5C000
Violet: 01008F6008C5E000

--- General Info ----

This is a rework of my previous randomizer that I made via code injection. This randomizer went through multiple reworks, at first having individual randomizers, now to having an easy-to-use configuration file
and program that does all the randomization and packaging for you. It currently randomizes Wild Encounters, Trainers, Static encounters, Personal Data (Abilities, and Movesets), Starters (and all gifted pokemons by extension),
and also provides a few extra options to customize your randomisation. It packages the resulting randomization to a zip file in the output folder, so all you need to do is import it in Trinity Loader and apply the mod.

If you use this program for content, credits in the description is not required, but always appreciated ! If there are any problems with the program whatsoever, yall know where to find me :)

KNOWM BUGS/ISSUES

- Palafin and his alt form will not get their normal ability randomized, due to being absolute garbage without it (and then game crashing if the ability is given via PkHex). Thus, only the hidden ability is randomized. Furthermore, no other pokemon can obtain the Zero to Hero ability.
- Terapagos will not have its ability randomized either and Tera-Shift has been banned as well to prevent others from using it
    - Will add option to randomize Terapagos forms abilities later on (Same with Ogerpon).
- Base Stat Randomizer not completed but it has been started.
- Boss Pokemon Battles and Initial Lechonk battle are not yet randomized (Will be added later)
- Snackworth's legendaries are not yet randomized - I know how but I haven't implemented it

FUTURE FEATURES
- Working on way to give more freedom on randomizer selection
    - ie: having more options for starters, wild settings, etc...
- Adding option to have item only forms to show up on overworld too
- Randomize Tera Raid Battles


For issues with 3.0.0/3.0.1 please make an issue and I'll fix it when I can.
