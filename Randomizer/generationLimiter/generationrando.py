import json
import random
import os
import shutil
from Randomizer.shared_Variables import starters_used as picked_starters
import Randomizer.shared_Variables as sharedVar

gen1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
        59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,
        87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111,
        112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133,
        134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151]
gen2 = [152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173,
        174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195,
        196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217,
        218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239,
        240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251]
gen3 = [252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273,
        274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295,
        296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317,
        318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339,
        340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361,
        362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383,
        384, 385, 386]
gen4 = [387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408,
        409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430,
        431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452,
        453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474,
        475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493]
gen5 = [494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515,
        516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537,
        538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559,
        560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581,
        582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603,
        604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625,
        626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647,
        648, 649]
gen6 = [650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671,
        672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693,
        694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715,
        716, 717, 718, 719, 720, 721]
gen7 = [722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743,
        744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765,
        766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787,
        788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809]
gen8 = [810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831,
        832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853,
        854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875,
        876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897,
        898, 899, 900, 901, 902, 903, 904, 905]
gen9 = [906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927,
        928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 949,
        950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971,
        972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993,
        994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012,
        1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025]
legends = [144, 145, 146, 150, 151, 243, 244, 245, 249, 250, 251, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 480,
           481, 482, 483, 484, 485, 486, 487, 489, 490, 491, 492, 493, 494, 638, 639, 640, 641, 642, 643, 644, 645, 646,
           647, 648, 649, 716, 717, 718, 719, 720, 721, 785, 786, 787, 788, 789, 790, 791, 792, 800, 801, 802, 807, 808,
           809, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 905, 994, 995, 996, 997, 998, 999, 1009, 1010,
           1011, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022]
gen1_legends = [144, 145, 146, 150, 151]
gen2_legends = [243, 244, 245, 249, 250, 251]
gen3_legends = [377, 378, 379, 380, 381, 382, 383, 384, 385, 386]
gen4_legends = [480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493]
gen5_legends = [494, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649]
gen6_legends = [716, 717, 718, 719, 720, 721]
gen7_legends = [785, 786, 787, 788, 789, 790, 791, 792, 800, 801, 802, 807, 808, 809]
UB = [793, 794, 795, 796, 797, 798, 799, 803, 804, 805, 806]
gen8_legends = [888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 905]
paradox = [978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 998, 999, 1021,
           1017, 1018, 1019, 1020]
gen9_legends = [994, 995, 996, 997, 998, 999, 1011, 1014, 1015, 1016, 1021, 1022]
bannedStages = []
recreated_species = []
recreated_altforms = []
chosen_biomes = []
picked_gifts = []  # for debugging
picked_evos = []  # for debugging
picked_statics = []  # for debugging
picked_trainer = []  # for debugging
tera_types = ['normal', 'kakutou', 'hikou', 'doku', 'jimen', 'iwa', 'mushi', 'ghost', 'hagane', 'honoo', 'mizu', 'kusa',
              'denki', 'esper', 'koori', 'dragon', 'aku', 'fairy', 'niji']
'''
normal = normal
kakutou = fightning
hikou = flying
doku = poison
jimen = ground
iwa = rock
mushi = bug
ghost = ghost
hagane = steel
honoo = fire
mizu = water
kusa = grass
denki = electric
esper = psychic
koori = ice
dragon = dragon
aku = dark
fairy = fairy (yousei everywhere else)
niji = stellar
'''


banned_pokemon = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 29, 30, 31, 32, 33, 34, 35, 41, 42, 46, 47, 63,
                  64, 65, 66, 67, 77, 78, 83, 95, 98, 99, 104, 105, 108, 114, 115, 118, 119, 120, 121, 122, 124, 127,
                  138, 139, 140, 141, 142, 165, 166, 169, 175, 176, 177, 178, 201, 202, 208, 213, 222, 223, 224, 226,
                  238, 241, 251, 263, 264, 265, 266, 267, 268, 269, 276, 277, 290, 291, 292, 293, 294, 295, 300, 301,
                  303, 304, 305, 306, 309, 310, 315, 318, 319, 320, 321, 327, 337, 338, 343, 344, 345, 346, 347, 348,
                  351, 352, 359, 360, 363, 364, 365, 366, 367, 368, 369, 399, 400, 406, 407, 412, 413, 414, 420, 421,
                  427, 428, 431, 432, 439, 441, 451, 452, 455, 458, 463, 465, 468, 494, 504, 505, 506, 507, 508, 509,
                  510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 524, 525, 526, 527, 528, 531, 535, 536,
                  537, 538, 539, 543, 544, 545, 554, 555, 556, 557, 558, 561, 562, 563, 564, 565, 566, 567, 568, 569,
                  582, 583, 584, 587, 588, 589, 592, 593, 597, 598, 599, 600, 601, 605, 606, 616, 617, 618, 621, 626,
                  631, 632, 649, 659, 660, 674, 675, 676, 679, 680, 681, 682, 683, 684, 685, 688, 689, 694, 695, 696,
                  697, 698, 699, 710, 711, 716, 717, 718, 746, 755, 756, 759, 760, 767, 768, 771, 772, 773, 776, 777,
                  780, 781, 785, 786, 787, 788, 793, 794, 795, 796, 797, 798, 799, 802, 803, 804, 805, 806, 807, 808,
                  809, 824, 825, 826, 827, 828, 829, 830, 831, 832, 835, 836, 850, 851, 852, 853, 864, 865, 866, 867,
                  880, 881, 882, 883]


# ## Utility functions for biomes ## #

recreated_species = []
recreated_altforms = []
chosen_biomes = []

def get_alt_form_paldea(index: int):
    has_alt = [25,  # pikachu
                26, #raichu
                28, #sandslash
               30, #ninetails
                50, #diglett
                51, #dugtrio
                52, #meowth, has two
                53, #persian
                58, #growlithe
                59, #arcanine
               74,  #geodude
               75,  #graveler
               76,  #golem
                79, #slowpoke
                80, #slowbro, seems to be form id 2
                88, #grimer
                89, #muk
                100, #voltorb
                101, #electrode
               103,  #exeggutor
               110,  # weezing
                128, #tauros, 3 form possible 1 2 3
                144, #articuno
                145, #zapdos
                146, #moltres
                157, #typhlosion
                194, #wooper
                199, #slowking
                211, #qwilfish
                215, #sneasel
               386,  #Deoxys
                422, #shellos
                423, #gastrodon
                479, #rotom: 5 forms 0 1 2 3 4 5
                483, #dialga
                484, #palkia
                487, #giratina
               492,  #shaymin
                503, #samurott
                549, #lilligant
                550, #basculin
                570, #zorua
                571, #zoroark
                628, #braviary
                641, #tornadus
                642, #thundurus
                645, #landorus
               646,  #Kyurem
                648, #meloetta
               658,  # greninja - added for future proofing and not forget it
               678,  # meowstic
                705, #sligoo
                706, #goodra
                713, #avalugg
                720, #hoopa
                724, #decidueye
               774,  #minior
               800,  #necrozma: 2 - 3 not in game
               801,  #magearna
               869,  #alcremie 8 forms
                892, #urshifu
                893, #zarude
                898, #calyrex, 2 forms 0 1 2
               901,  #Ursaluna
               902,  #basculegion
               905,  #enamorus
               1011, #ogerpon - 0 [Teal], 1[wellspring], 2[heartflame], 3[rock]; 4-7 is teraform
               1021, #terapagos
               1024, #poltchageist
               1025, #sinistcha
    ]
    if index in has_alt: #previously, we just shuffled around. Now we include all species, so we need more edge cases
        choice = 0
        match index:
            case 25:
                choice = [1,2,3,4,5,6,7,9]
                # form 8 not in the game (Partner Let's Go Pikachu)
                return choice
            case 52:
                choice = [1,2]
                return choice
            case 80:
                choice = [2]
                # form 1 not in the game (Mega Slowbro)
                return choice
            case 128:
                choice = [0]
                return choice
            case 194:
                choice = [0]
                return choice
            case 386:
                choice = [1,2,3]
                return choice
            case 479:
                choice = [1,2,3,4,5]
                return choice
            case 550:
                choice = [2]
                return choice
            case 646:
                choice = [1,2]
                return choice
            case 774:
                choice = [1,2,3,4,5,6]
                return choice
            case 800:
                choice = [1, 2]
                return choice
            case 869:
                choice = [1,2,3,4,5,6,7,8]
                return choice
            case 898:
                choice = [1,2]
                return choice
            case 952:
                choice = [1,2]
                return choice
            case 960:
                choice = [1,2,3]
                return choice
            case 1011:
                choice = [1,2,3]
                return choice
            case _:
                choice = [1]
                return choice
    else:
        return [0]


def get_alt_form_teal(index: int):
    has_alt = [25,  # pikachu
                26, #raichu
                27, #sandshrew
                28, #sandslash
               29, #vulpix
               30, #ninetails
                50, #diglett
                51, #dugtrio
                52, #meowth, has two
                53, #persian
                58, #growlithe
                59, #arcanine
               74,  #geodude
               75,  #graveler
               76,  #golem
                79, #slowpoke
                80, #slowbro, seems to be form id 2
                88, #grimer
                89, #muk
                100, #voltorb
                101, #electrode
               103,  #exeggutor
               110,  # weezing
                128, #tauros, 3 form possible 1 2 3
                144, #articuno
                145, #zapdos
                146, #moltres
                157, #typhlosion
                194, #wooper
                199, #slowking
                211, #qwilfish
                215, #sneasel
               386,  #Deoxys
                422, #shellos
                423, #gastrodon
                479, #rotom: 5 forms 0 1 2 3 4 5
                483, #dialga
                484, #palkia
                487, #giratina
               492,  #shaymin
                503, #samurott
                549, #lilligant
                550, #basculin
                570, #zorua
                571, #zoroark
               585,  #deerling
               586,  #sawsbuck
                628, #braviary
                641, #tornadus
                642, #thundurus
                645, #landorus
               646,  #Kyurem
                648, #meloetta
               658,  # greninja - added for future proofing and not forget it
               669,  #flabebe
               670,  #floette - 5 is eternal flower not in game
               671,  #florges
               678,  # meowstic
                705, #sligoo
                706, #goodra
                713, #avalugg
                720, #hoopa
                724, #decidueye
               774,  #minior
               778,  #mimikyu
               800,  #necrozma: 2 - 3 not in game
               801,  #magearna
                849, #toxtricity
               854,  #sineastea
               855,  # plteageist
               869,  #alcremie 8 forms
                892, #urshifu
                893, #zarude
                898, #calyrex, 2 forms 0 1 2
               901,  #Ursaluna
               902,  #basculegion
               905,  #enamorus
               916,  #Oinkolonge
               934,  #Palafin
               952,  #tatsugiri: 2 forms 0 1 2
               960,  #squakabily: 3 forms 0 1 2 3
               976,  #gimmighoul - 998 koraidon test, 999 miraidon test [0-4]
               1011, #ogerpon - 0 [Teal], 1[wellspring], 2[heartflame], 3[rock]; 4-7 is teraform
               1021, #terapagos
               1025, #sinistcha
    ]
    if index in has_alt: #previously, we just shuffled around. Now we include all species, so we need more edge cases
        choice = 0
        match index:
            case 25:
                choice = [1,2,3,4,5,6,7,8,9]
                # form 8 not in the game (Partner Let's Go Pikachu)
                return choice
            case 52:
                choice = [1,2]
                return choice
            case 80:
                choice = [1,2]
                # form 1 not in the game (Mega Slowbro)
                return choice
            case 128:
                choice = [1,2,3]
                return choice
            case 194:
                choice = [1]
                return choice
            case 386:
                choice = [1,2,3]
                return choice
            case 479:
                choice = [1,2,3,4,5]
                return choice
            case 550:
                choice = [0, 1]
                return choice
            case 585:
                choice = [1,2,3]
                return choice
            case 586:
                choice = [1,2,3]
                return choice
            case 646:
                choice = [1,2]
                return choice
            case 669:
                choice = [1,2,3,4]
                return choice
            case 670:
                choice = [1, 2, 3, 4]
                return choice
            case 671:
                choice = [1, 2, 3, 4]
                return choice
            case 774: # includes shield downs form
                choice = [1,2,3,4,5,6]
                return choice
            case 800:
                choice = [1, 2]
                return choice
            case 869:
                choice = [1,2,3,4,5,6,7,8]
                return choice
            case 898:
                choice = [1,2]
                return choice
            case 952:
                choice = [1,2]
                return choice
            case 960:
                choice = [1,2,3]
                return choice
            case 1011:
                choice = [1,2,3]
                return choice
            case _:
                choice = [1]
                return choice
    else:
        return [0]


def get_alt_form_indigo(index: int):
    has_alt = [25,  # pikachu
                26, #raichu
                27, #sandshrew - 0
                28, #sandslash - 0
               29, #vulpix - 0
               30, #ninetails - 0
                50, #diglett - 0
                51, #dugtrio - 0
                52, #meowth, has two
                53, #persian
                58, #growlithe
                59, #arcanine
               74,  #geodude - 0
               75,  #graveler - 0
               76,  #golem - 0
                79, #slowpoke - 0
                80, #slowbro, - 0
                88, #grimer - 0
                89, #muk - 0
                100, #voltorb
                101, #electrode
               103,  #exeggutor - 0
               110,  # weezing
                128, #tauros, 3 form possible 1 2 3
                144, #articuno
                145, #zapdos
                146, #moltres
                157, #typhlosion
                194, #wooper - 0, 1
                199, #slowking
                211, #qwilfish - 0
                215, #sneasel
               386,  #Deoxys
                422, #shellos
                423, #gastrodon
                479, #rotom: 5 forms 0 1 2 3 4 5
                483, #dialga
                484, #palkia
                487, #giratina
               492,  #shaymin
                503, #samurott
                549, #lilligant
                550, #basculin - 1 2
                570, #zorua
                571, #zoroark
                628, #braviary
                641, #tornadus
                642, #thundurus
                645, #landorus
               646,  #Kyurem
                648, #meloetta
               658,  # greninja - added for future proofing and not forget it
               669,  #flabebe
               670,  #floette - 5 is eternal flower not in game
               671,  #florges
                705, #sligoo
                706, #goodra
                713, #avalugg
                720, #hoopa
                724, #decidueye
                744, #rockruff
                745, #lycanroc: 2 forms 0 1 2
               800,  #necrozma: 2 - 3 not in game
               801,  #magearna
                849, #toxtricity
               854,  #sineastea
               855,  # plteageist
               869,  #alcremie 8 forms
               876,  #indeedee
                892, #urshifu
                893, #zarude
                898, #calyrex, 2 forms 0 1 2
               901,  #Ursaluna
               902,  #basculegion
               905,  #enamorus
               916,  #Oinkolonge
               917,  #Dudunsparce
               934,  #Palafin
               946,  #Mausehold
               952,  #tatsugiri: 2 forms 0 1 2
               960,  #squakabily: 3 forms 0 1 2 3
               976,  #gimmighoul - 998 koraidon test, 999 miraidon test [0-4]
               1011, #ogerpon - 0 [Teal], 1[wellspring], 2[heartflame], 3[rock]; 4-7 is teraform
               1021, #terapagos
               1024, #poltchageist
               1025, #sinistcha
    ]
    if index in has_alt: #previously, we just shuffled around. Now we include all species, so we need more edge cases
        choice = 0
        match index:
            case 25:
                choice = [1,2,3,4,5,6,7,8,9]
                # form 8 not in the game (Partner Let's Go Pikachu)
                return choice
            case 27:
                choice = [0]
                return choice
            case 28:
                choice = [0]
                return choice
            case 29:
                choice = [0]
                return choice
            case 30:
                choice = [0]
                return choice
            case 50:
                choice = [0]
                return choice
            case 51:
                choice = [0]
                return choice
            case 52:
                choice = [1,2]
                return choice
            case 74:
                choice = [0]
                return choice
            case 75:
                choice = [0]
                return choice
            case 76:
                choice = [0]
                return choice
            case 79:
                choice = [0]
                return choice
            case 80:
                choice = [0]
                # form 1 not in the game (Mega Slowbro)
                return choice
            case 103:
                choice = [0]
                return choice
            case 128:
                choice = [1,2,3]
                return choice
            case 211:
                choice = [0]
                return choice
            case 386:
                choice = [1,2,3]
                return choice
            case 479:
                choice = [1,2,3,4,5]
                return choice
            case 550:
                choice = [1,2]
                return choice
            case 646:
                choice = [1,2]
                return choice
            case 669:
                choice = [1,2,3,4]
                return choice
            case 670:
                choice = [1, 2, 3, 4]
                return choice
            case 671:
                choice = [1, 2, 3, 4]
                return choice
            case 745:
                choice = [1,2]
                return choice
            case 800:
                choice = [1, 2]
                return choice
            case 869:
                choice = [1,2,3,4,5,6,7,8]
                return choice
            case 898:
                choice = [1,2]
                return choice
            case 952:
                choice = [1,2]
                return choice
            case 960:
                choice = [1,2,3]
                return choice
            case 1011:
                choice = [1,2,3]
                return choice
            case _:
                choice = [1]
                return choice
    else:
        return [0]


# ## Utility functions for biomes ## #
def pick_random_biome1():
    possible_biomes = ["GRASS", "FOREST", "SWAMP", "LAKE", "TOWN", "MOUNTAIN", "BAMBOO", "MINE", "CAVE", "OLIVE",
                       "UNDERGROUND", "RIVER", "ROCKY", "BEACH", "SNOW", "OSEAN", "RUINS", "FLOWER",]
    choice = possible_biomes[random.randint(0, len(possible_biomes) - 1)]
    chosen_biomes.append(choice)
    return choice


def pick_random_biomerest():
    possible_biomes = ["GRASS", "FOREST", "SWAMP", "LAKE", "TOWN", "MOUNTAIN", "BAMBOO", "MINE", "CAVE", "OLIVE",
                       "UNDERGROUND", "RIVER", "ROCKY", "BEACH", "SNOW", "OSEAN", "RUINS", "FLOWER"]
    choice = possible_biomes[random.randint(0, len(possible_biomes) - 1)]
    while choice in chosen_biomes:
        choice = possible_biomes[random.randint(0, len(possible_biomes) - 1)]
        if len(chosen_biomes) > 4:
            break
    chosen_biomes.append(choice)
    return choice


def generate_lot_value_for_biome(biome_type: str):
    if biome_type == "NONE":
        return 0
    else:
        return random.randint(1, 50)


def generate_area():
    return(random.sample(range(1, 27), 10))


def generate_area_list():
    return(str(generate_area()).replace('[','"').replace(']','"').replace(' ',''))


# ## Utility function because otherwise, randomize() would be fucked up
def make_template(new_template, index, csvdata, form=0):
    new_template['devid'] = fetch_devname(index, csvdata)
    new_template['formno'] = form
    new_template['minlevel'] = 2
    new_template['maxlevel'] = 99
    new_template['lotvalue'] = random.randint(1, 50)
    new_template['biome1'] = pick_random_biome1()
    new_template['biome2'] = pick_random_biomerest()
    new_template['biome3'] = pick_random_biomerest()
    new_template['biome4'] = pick_random_biomerest()
    new_template['lotvalue1'] = generate_lot_value_for_biome(new_template['biome1'])
    new_template['lotvalue2'] = generate_lot_value_for_biome(new_template['biome2'])
    new_template['lotvalue3'] = generate_lot_value_for_biome(new_template['biome3'])
    new_template['lotvalue4'] = generate_lot_value_for_biome(new_template['biome4'])
    chosen_biomes.clear()
    new_template['area'] = generate_area_list()
    new_template['locationName'] = ""
    new_template['enabletable']['land'] = True
    new_template['enabletable']['up_water'] = True
    new_template['enabletable']['underwater'] = True
    new_template['enabletable']['air1'] = True
    new_template['enabletable']['air2'] = True
    new_template['timetable']['morning'] = True
    new_template['timetable']['noon'] = True
    new_template['timetable']['evening'] = True
    new_template['timetable']['night'] = True
    new_template['flagName'] = ""
    new_template['versiontable']['A'] = True
    new_template['versiontable']['B'] = True
    new_template['bringItem']['itemID'] = "ITEMID_NONE"
    new_template['bringItem']['bringRate'] = 0
    return new_template


### Actual shit going on here ###
def randomize_paldea(config, allowedpokemon):
    # print(os.getcwd())
    # load information
    file = open(os.getcwd() + "/Randomizer/WildEncounters/" + "pokedata_array_clean.json", "r")
    data = json.load(file)

    csvfile = open(os.getcwd() + "/Randomizer/WildEncounters/" + "pokemon_to_id.txt", "r")
    csvdata = []
    for i in csvfile:
        csvdata.append(i)
    csvfile.close()

    # recreate data entries so all mons are present.
    # simplest way of doing it, is to edit all existing entries to have devid's ascending from allowed species, and simply paste another entry with the new ids n shti
    # copy an entry
    template_entry = data['values'][0].copy()

    i = len(data) - 1
    # edit existing entries
    poke_dict = {}
    poke_dict['values'] = []

    for index in range(1, 1026):
        if index in banned_pokemon:
            continue
        if index not in allowedpokemon:
            continue
        if config['exclude_legendaries'] == "yes":
            if index in legends:
                pass
            else:
                if fetch_devname(index, csvdata) not in recreated_species:
                    new_template = template_entry.copy()
                    recreated_species.append(fetch_devname(index, csvdata))
                    new_template = make_template(new_template, index, csvdata)
                    poke_dict['values'].append(new_template)
                    i = i + 1
                    # check alt forms for this mon
                forms = get_alt_form_paldea(index)
                for form in forms:  # previously was too high, now it should also pass on mons that alraedy have entries
                    # so aside from 128 and 194, all 0's should be ignored
                    form_template = template_entry.copy()  # gotta copy again the template from the start
                    form_template = make_template(form_template, index, csvdata,
                                                  form)  # randomize the template before changing the formno
                    if form == 0:
                        if index == 194 or index == 128:
                            poke_dict['values'].append(form_template)
                        else:
                            continue  # NOT ALLOWED !!!
                    else:  # should let pass 0's if correct id's
                        # print(form_template)
                        poke_dict['values'].append(form_template)
        else:
            if fetch_devname(index, csvdata) not in recreated_species:
                new_template = template_entry.copy()
                recreated_species.append(fetch_devname(index, csvdata))
                new_template = make_template(new_template, index, csvdata)
                poke_dict['values'].append(new_template)
                i = i + 1
                # check alt forms for this mon
            forms = get_alt_form_paldea(index)
            for form in forms:  # previously was too high, now it should also pass on mons that alraedy have entries
                # so aside from 128 and 194, all 0's should be ignored
                form_template = template_entry.copy()  # gotta copy again the template from the start
                form_template = make_template(form_template, index, csvdata,
                                              form)  # randomize the template before changing the formno
                if form == 0:
                    if index == 194 or index == 128:
                        poke_dict['values'].append(form_template)
                    else:
                        continue  # NOT ALLOWED !!!
                else:  # should let pass 0's if correct id's
                    # print(form_template)
                    poke_dict['values'].append(form_template)

    outdata = json.dumps(poke_dict, indent=4)
    with open(os.getcwd() + "/Randomizer/WildEncounters/" + "pokedata_array.json", 'w') as outfile:
        outfile.write(outdata)
    print("Limted Generation Randomisation - Paldea done !")


def randomize_teal(config, allowedpokemon):
    recreated_species = []
    # print(os.getcwd())
    # load information
    file = open(os.getcwd() + "/Randomizer/WildEncounters/" + "pokedata_su1_array_clean.json", "r")
    data = json.load(file)

    csvfile = open(os.getcwd() + "/Randomizer/WildEncounters/" + "pokemon_to_id.txt", "r")
    csvdata = []
    for i in csvfile:
        csvdata.append(i)
    csvfile.close()

    # recreate data entries so all mons are present.
    # simplest way of doing it, is to edit all existing entries to have devid's ascending from allowed species, and simply paste another entry with the new ids n shti
    # copy an entry
    template_entry = data['values'][0].copy()

    i = len(data) - 1
    # edit existing entries
    poke_dict = {}
    poke_dict['values'] = []

    for index in range(1, 1026):
        if index in banned_pokemon:
            continue
        if index not in allowedpokemon:
            continue
        if config['exclude_legendaries'] == "yes":
            if index in legends:
                pass
            else:
                if fetch_devname(index, csvdata) not in recreated_species:
                    new_template = template_entry.copy()
                    recreated_species.append(fetch_devname(index, csvdata))
                    new_template = make_template(new_template, index, csvdata)
                    poke_dict['values'].append(new_template)
                    i = i + 1
                    # check alt forms for this mon
                forms = get_alt_form_teal(index)
                for form in forms:  # previously was too high, now it should also pass on mons that alraedy have entries
                    # so aside from 128 and 194, all 0's should be ignored
                    form_template = template_entry.copy()  # gotta copy again the template from the start
                    form_template = make_template(form_template, index, csvdata,
                                                  form)  # randomize the template before changing the formno
                    if form == 0:
                        if index == 550:
                            poke_dict['values'].append(form_template)
                        else:
                            continue  # NOT ALLOWED !!!
                    else:  # should let pass 0's if correct id's
                        # print(form_template)
                        poke_dict['values'].append(form_template)
        else:
            if fetch_devname(index, csvdata) not in recreated_species:
                new_template = template_entry.copy()
                recreated_species.append(fetch_devname(index, csvdata))
                new_template = make_template(new_template, index, csvdata)
                poke_dict['values'].append(new_template)
                i = i + 1
                # check alt forms for this mon
            forms = get_alt_form_teal(index)
            for form in forms:  # previously was too high, now it should also pass on mons that alraedy have entries
                # so aside from 128 and 194, all 0's should be ignored
                form_template = template_entry.copy()  # gotta copy again the template from the start
                form_template = make_template(form_template, index, csvdata,
                                              form)  # randomize the template before changing the formno
                if form == 0:
                    if index == 550:
                        poke_dict['values'].append(form_template)
                    else:
                        continue  # NOT ALLOWED !!!
                else:  # should let pass 0's if correct id's
                    # print(form_template)
                    poke_dict['values'].append(form_template)

    outdata = json.dumps(poke_dict, indent=4)
    with open(os.getcwd() + "/Randomizer/WildEncounters/" + "pokedata_su1_array.json", 'w') as outfile:
        outfile.write(outdata)
    print("Limted Generation Randomisation - Teal done !")


def randomize_indigo(config, allowedpokemon):
    recreated_species = []
    # print(os.getcwd())
    # load information
    file = open(os.getcwd() + "/Randomizer/WildEncounters/" + "pokedata_su2_array_clean.json", "r")
    data = json.load(file)

    csvfile = open(os.getcwd() + "/Randomizer/WildEncounters/" + "pokemon_to_id.txt", "r")
    csvdata = []
    for i in csvfile:
        csvdata.append(i)
    csvfile.close()

    # recreate data entries so all mons are present.
    # simplest way of doing it, is to edit all existing entries to have devid's ascending from allowed species, and simply paste another entry with the new ids n shti
    # copy an entry
    template_entry = data['values'][0].copy()

    i = len(data) - 1
    # edit existing entries
    poke_dict = {}
    poke_dict['values'] = []

    for index in range(1, 1026):
        if index in banned_pokemon:
            continue
        if index not in allowedpokemon:
            continue
        if config['exclude_legendaries'] == "yes":
            if index in legends:
                pass
            else:
                if fetch_devname(index, csvdata) not in recreated_species:
                    new_template = template_entry.copy()
                    recreated_species.append(fetch_devname(index, csvdata))
                    new_template = make_template(new_template, index, csvdata)
                    poke_dict['values'].append(new_template)
                    i = i + 1
                    # check alt forms for this mon
                forms = get_alt_form_indigo(index)
                for form in forms:  # previously was too high, now it should also pass on mons that alraedy have entries
                    # so aside from 128 and 194, all 0's should be ignored
                    form_template = template_entry.copy()  # gotta copy again the template from the start
                    form_template = make_template(form_template, index, csvdata,
                                                  form)  # randomize the template before changing the formno
                    if form == 0:
                        if index == 27:
                            poke_dict['values'].append(form_template)
                        elif index == 28:
                            poke_dict['values'].append(form_template)
                        elif index == 29:
                            poke_dict['values'].append(form_template)
                        elif index == 30:
                            poke_dict['values'].append(form_template)
                        elif index == 50:
                            poke_dict['values'].append(form_template)
                        elif index == 51:
                            poke_dict['values'].append(form_template)
                        elif index == 74:
                            poke_dict['values'].append(form_template)
                        elif index == 75:
                            poke_dict['values'].append(form_template)
                        elif index == 76:
                            poke_dict['values'].append(form_template)
                        elif index == 79:
                            poke_dict['values'].append(form_template)
                        elif index == 80:
                            poke_dict['values'].append(form_template)
                        elif index == 211:
                            poke_dict['values'].append(form_template)
                        else:
                            continue
                    else:  # should let pass 0's if correct id's
                        # print(form_template)
                        poke_dict['values'].append(form_template)
        else:
            if fetch_devname(index, csvdata) not in recreated_species:
                new_template = template_entry.copy()
                recreated_species.append(fetch_devname(index, csvdata))
                new_template = make_template(new_template, index, csvdata)
                poke_dict['values'].append(new_template)
                i = i + 1
                # check alt forms for this mon
            forms = get_alt_form_indigo(index)
            for form in forms:  # previously was too high, now it should also pass on mons that alraedy have entries
                # so aside from 128 and 194, all 0's should be ignored
                form_template = template_entry.copy()  # gotta copy again the template from the start
                form_template = make_template(form_template, index, csvdata,
                                              form)  # randomize the template before changing the formno
                if form == 0:
                    if index == 27:
                        poke_dict['values'].append(form_template)
                    elif index == 28:
                        poke_dict['values'].append(form_template)
                    elif index == 29:
                        poke_dict['values'].append(form_template)
                    elif index == 30:
                        poke_dict['values'].append(form_template)
                    elif index == 50:
                        poke_dict['values'].append(form_template)
                    elif index == 51:
                        poke_dict['values'].append(form_template)
                    elif index == 74:
                        poke_dict['values'].append(form_template)
                    elif index == 75:
                        poke_dict['values'].append(form_template)
                    elif index == 76:
                        poke_dict['values'].append(form_template)
                    elif index == 79:
                        poke_dict['values'].append(form_template)
                    elif index == 80:
                        poke_dict['values'].append(form_template)
                    elif index == 211:
                        poke_dict['values'].append(form_template)
                    else:
                        continue
                else:  # should let pass 0's if correct id's
                    # print(form_template)
                    poke_dict['values'].append(form_template)

    outdata = json.dumps(poke_dict, indent=4)
    with open(os.getcwd() + "/Randomizer/WildEncounters/" + "pokedata_su2_array.json", 'w') as outfile:
        outfile.write(outdata)
    print("Limted Generation Randomisation - Indigo done !")


def get_alt_form(index: int):
    has_alt = [25,  # pikachu
                26, #raichu
                27, #sandshrew
                28, #sandslash
               29, #vulpix
               30, #ninetails
                50, #diglett
                51, #dugtrio
                52, #meowth, has two
                53, #persian
                58, #growlithe
                59, #arcanine
               74,  #geodude
               75,  #graveler
               76,  #golem
                79, #slowpoke
                80, #slowbro, seems to be form id 2
                88, #grimer
                89, #muk
                100, #voltorb
                101, #electrode
               103,  #exeggutor
               110,  # weezing
                128, #tauros, 3 form possible 1 2 3
                144, #articuno
                145, #zapdos
                146, #moltres
                157, #typhlosion
                194, #wooper
                199, #slowking
                211, #qwilfish
                215, #sneasel
               386,  #Deoxys
                422, #shellos
                423, #gastrodon
                479, #rotom: 5 forms 0 1 2 3 4 5
                483, #dialga
                484, #palkia
                487, #giratina
               492,  #shaymin
               493,  #arceus
                503, #samurott
                549, #lilligant
                550, #basculin
                570, #zorua
                571, #zoroark
               585,  #deerling
               586,  #sawsbuck
                628, #braviary
                641, #tornadus
                642, #thundurus
                645, #landorus
               646,  #Kyurem
                648, #meloetta
               658,  # greninja - added for future proofing and not forget it
               664,  #scatterbug
               665,  #sweppa
               666,  #vivillon - flabebe/floette/florges 0-4 (floette 5 but ot present)
               669,  #flabebe
               670,  #floette - 5 is eternal flower not in game
               671,  #florges
               678,  # meowstic
                705, #sligoo
                706, #goodra
                713, #avalugg
                720, #hoopa
                724, #decidueye
                741, #oricorio, 3 forms 0 1 2 3
                744, #rockruff
                745, #lycanroc: 2 forms 0 1 2
               774,  #minior
               778,  #mimikyu
               800,  #necrozma: 2 - 3 not in game
               801,  #magearna
               845,  #cramorant
                849, #toxtricity
               854,  #sineastea
               855,  # plteageist
               869,  #alcremie 8 forms
               875,  #Eiscue
               876,  #indeedee
               877,  #morpeko
               888,  #Zacian
               889,  #Zamazenta
                892, #urshifu
                893, #zarude
                898, #calyrex, 2 forms 0 1 2
               901,  #Ursaluna
               902,  #basculegion
               905,  #enamorus
               916,  #Oinkolonge
               917,  #Dudunsparce
               934,  #Palafin
               946,  #Mausehold
               952,  #tatsugiri: 2 forms 0 1 2
               960,  #squakabily: 3 forms 0 1 2 3
               976,  #gimmighoul - 998 koraidon test, 999 miraidon test [0-4]
               1011, #ogerpon - 0 [Teal], 1[wellspring], 2[heartflame], 3[rock]; 4-7 is teraform
               1021, #terapagos
               1024, #poltchageist
               1025, #sinistcha
    ]
    if index in has_alt: #previously, we just shuffled around. Now we include all species, so we need more edge cases
        choice = 0
        match index:
            case 25:
                choice = random.randint(0, 9)
                # form 8 not in the game (Partner Let's Go Pikachu)
                while choice == 8:
                    choice = random.randint(0, 9)
                return choice
            case 52:
                choice = random.randint(0, 2)
                return choice
            case 80:
                choice = random.randint(0, 2)
                # form 1 not in the game (Mega Slowbro)
                while choice == 1:
                    choice = random.randint(0, 2)
                return choice
            case 128:
                choice = random.randint(0, 3)
                return choice
            case 386:
                choice = random.randint(0, 3)
                return choice
            case 479:
                choice = random.randint(0, 5)
                return choice
            case 493:
                choice = random.randint(0, 17)
                return choice
            case 550:
                choice = random.randint(0, 2)
                return choice
            case 585:
                choice = random.randint(0, 3)
                return choice
            case 586:
                choice = random.randint(0, 3)
                return choice
            case 646:
                choice = random.randint(0, 2)
                return choice
            case 664:
                choice = random.randint(0, 19)
                return choice
            case 665:
                choice = random.randint(0, 19)
                return choice
            case 666:
                choice = random.randint(0, 19)
                return choice
            case 669:
                choice = random.randint(0, 4)
                return choice
            case 670:
                choice = random.randint(0, 5)
                while choice == 5:
                    choice = random.randint(0, 5)
                return choice
            case 671:
                choice = random.randint(0, 4)
                return choice
            case 741:
                choice = random.randint(0, 3)
                return choice
            case 745:
                choice = random.randint(0, 2)
                return choice
            case 774: # includes shield downs form
                choice = random.randint(0, 13)
                return choice
            case 800:
                choice = random.randint(0, 3)
                while choice == 3:
                    choice = random.randint(0, 3)
                return choice
            case 845:
                choice = random.randint(0, 2)
                return choice
            case 869:
                choice = random.randint(0, 8)
                return choice
            case 898:
                choice = random.randint(0, 2)
                return choice
            case 952:
                choice = random.randint(0, 2)
                return choice
            case 960:
                choice = random.randint(0, 3)
                return choice
            case 1011:
                choice = random.randint(0, 3)
                return choice
            case _:
                choice = random.randint(0, 1)
                return choice
    else:
        return 0


def fetch_devname(index: int, csvdata):
    return str.strip(csvdata[index])


def flip_starter_texture(starter_num: int):
    file = open(os.getcwd() + "/Randomizer/Starters/" +"pokemon_to_file.txt", "r")
    names = []
    for name in file:
        names.append(name)
    pokemon_file = fetch_devname(starter_num, names)
    print(starter_num)
    print(pokemon_file)
    # _00 - male
    # _01 - female
    # _51 and _52 - mega/primal forms
    # _61 - Alolan Form
    # _81 - GMAX form
    # _XX_31 - Galarian form
    # _XX_41 - Hisuian
    # _XX_51 - Paldean
    # _71_XX - Noble
    # --------------- 1X is only for non-regional forms
    # _11 - form0
    # _12 - form1
    # _13 - form2
    # _14 - form3
    # _XY - formZ./pokemon_clean/{pokemon_file}
    # Copies files of pokemon needed. Right now gets all - later only form specific
    shutil.copytree(os.getcwd() + "/Randomizer/Starters/" +f'pokemon_clean/{pokemon_file}',
                 os.getcwd() + "/Randomizer/Starters/" +f'output/romfs/pokemon/data/{pokemon_file}')
    current_check = os.getcwd() + "/Randomizer/Starters/" +f'output/romfs/pokemon/data/{pokemon_file}'
    i = 0
    for pokemonfolder in os.listdir(current_check):
        # print(pokemonfolder)
        pokemontextures_animations = current_check + "/" + pokemonfolder

        for files in os.listdir(pokemontextures_animations):
            if "rare" in files:
                # print(files)
                # print(files.replace("_rare", ''))
                replacedfile = files.replace("_rare", '')
                ogfiledir = pokemontextures_animations + "/" + f'{files}'
                newfiledir =pokemontextures_animations + "/" + f'{replacedfile}'
                #print(f'OG File Dir: {ogfiledir}')
                #print(f'New File Dir: {newfiledir}')
                shutil.copy2(ogfiledir, newfiledir)


def make_poke(pokemon, names, config, allowedpokemon):
    chosenmon = allowedpokemon[random.randint(0, len(allowedpokemon)-1)]
    while chosenmon in banned_pokemon:
        chosenmon = allowedpokemon[random.randint(0, len(allowedpokemon)-1)]
    pokemon['pokeDataSymbol']['devId'] = fetch_devname(chosenmon, names)
    pokemon['pokeDataSymbol']['formId'] = get_alt_form(chosenmon)
    pokemon['pokeDataSymbol']['wazaType'] = "DEFAULT"
    pokemon['pokeDataSymbol']['waza1']['wazaId'] = "WAZA_NULL"
    pokemon['pokeDataSymbol']['waza2']['wazaId'] = "WAZA_NULL"
    pokemon['pokeDataSymbol']['waza3']['wazaId'] = "WAZA_NULL"
    pokemon['pokeDataSymbol']['waza4']['wazaId'] = "WAZA_NULL"
    if config['randomize_tera_type_for_static_tera'] == "yes" and pokemon['pokeDataSymbol']['gemType'] != "DEFAULT":
        pokemon['pokeDataSymbol']['gemType'] = tera_types[random.randint(0, len(tera_types) - 1)].upper()
    picked_statics.append(chosenmon)


def randomizeEvolutions(pokemon, allowedlist):
    for evo in pokemon['evolutions']:
        choice = allowedlist[random.randint(0, len(allowedlist)-1)]
        while choice in banned_pokemon:
            choice = allowedlist[random.randint(0, len(allowedlist)-1)]
        evo['species'] = choice
        evo['form'] = get_alt_form(choice)
        picked_evos.append(choice)
    return pokemon


def randomizeStarters(config, pokemon, allowedlist, names, allowed_legends, allowed_generations):
    file = open(os.getcwd() + "/Randomizer/Starters/" + "pokemon_list_info.json", 'r')
    pokedata = json.load(file)
    file.close()
    i = 0
    shinyforced = [0] * 3
    if config['ban_stage1_pokemon'] == "yes":
        bannedStages.extend(sharedVar.gen9Stage1)
    if config['ban_stage2_pokemon'] == "yes":
        bannedStages.extend(sharedVar.gen9Stage2)
    if config['ban_singlestage_pokemon'] == "yes":
        bannedStages.extend(sharedVar.no_evolution)
    if config['force_one_starter_to_be_shiny'] == "yes":
        choice = random.randint(0,2)
        shinyforced[choice] = 1

    for entry in pokemon['values']:
        if config['randomize_all_gifts'] == "no":  # only starters
            if "common_0065_" in entry['label']:
                choice = allowedlist[random.randint(0, len(allowedlist)-1)]
                while choice in banned_pokemon or choice in picked_starters or pokedata['pokemons'][choice]['natdex'] in bannedStages:
                    choice = allowedlist[random.randint(0, len(allowedlist)-1)]

                if config['only_legends'] == "yes":
                    val = random.randint(0, len(allowed_legends)-1)
                    choice = allowed_legends[val]
                    while choice in banned_pokemon or choice in picked_starters or choice in paradox:
                        val = random.randint(0, len(allowed_legends)-1)
                        choice = allowed_legends[val]
                if config['only_paradox'] == "yes" and 9 in allowed_generations:
                    val = random.randint(0, len(paradox)-1)
                    choice = paradox[val]
                    while choice in banned_pokemon or choice in picked_starters:
                        val = random.randint(0, len(paradox)-1)
                        choice = paradox[val]
                if config['only_legends_and_paradox'] == "yes" and 9 in allowed_generations:
                    val = random.randint(0, len(allowed_legends)-1)
                    choice = allowed_legends[val]
                    while choice in banned_pokemon or choice in picked_starters:
                        val = random.randint(0, len(allowed_legends)-1)
                        choice = allowed_legends[val]

                if choice not in picked_starters:

                    entry['pokeData']['devId'] = fetch_devname(choice, names)
                    alt_form_choosen = get_alt_form(choice)
                    entry['pokeData']['formId'] = alt_form_choosen

                    # Hard code tera types for ogerpon and terapagos so that they don't break.
                    if config['randomize_tera_type'] == "yes":
                        entry['pokeData']['gemType'] = tera_types[random.randint(0, len(tera_types) - 1)].upper()

                        match choice:
                            case 1011:
                                match alt_form_choosen:
                                    case 0:
                                        entry['pokeData']['gemType'] = "KUSA"
                                        pass
                                    case 1:
                                        entry['pokeData']['gemType'] = "MIZU"
                                        pass
                                    case 2:
                                        entry['pokeData']['gemType'] = "HONOO"
                                        pass
                                    case 3:
                                        entry['pokeData']['gemType'] = "IWA"
                                        pass
                            case 1021:
                                entry['pokeData']['gemType'] = "NIJI"
                            case _:
                                pass

                    if config['all_shiny'] == "yes":
                        entry['pokeData']['rareType'] = "RARE"
                        if config['shiny_overworld'] == "yes":
                            flip_starter_texture(choice)
                    elif config['higher_shiny_chance'] == "yes":
                        chance = random.randint(1, 10)
                        if chance == 10:
                            entry['pokeData']['rareType'] = "RARE"
                            if config['shiny_overworld'] == "yes":
                                flip_starter_texture(choice)
                        else:
                            entry['pokeData']['rareType'] = "NO_RARE"
                    if i < 3:
                        if shinyforced[i] == 1:
                            entry['pokeData']['rareType'] = "RARE"
                            if config['shiny_overworld'] == "yes":
                                flip_starter_texture(choice)
                    i = i +1
                    picked_starters.append(choice)
        else:  # everything plus starters
            choice = allowedlist[random.randint(0, len(allowedlist)-1)]
            while choice in banned_pokemon or choice in picked_starters or pokedata['pokemons'][choice]['natdex'] in bannedStages:
                choice = allowedlist[random.randint(0, len(allowedlist)-1)]

            if config['only_legends'] == "yes":
                val = random.randint(0, len(allowed_legends) - 1)
                choice = allowed_legends[val]
                while choice in banned_pokemon or choice in picked_starters or choice in paradox:
                    val = random.randint(0, len(allowed_legends) - 1)
                    choice = allowed_legends[val]
            if config['only_paradox'] == "yes" and 9 in allowed_generations:
                val = random.randint(0, len(paradox) - 1)
                choice = paradox[val]
                while choice in banned_pokemon or choice in picked_starters:
                    val = random.randint(0, len(paradox) - 1)
                    choice = paradox[val]
            if config['only_legends_and_paradox'] == "yes" and 9 in allowed_generations:
                val = random.randint(0, len(allowed_legends) - 1)
                choice = allowed_legends[val]
                while choice in banned_pokemon or choice in picked_starters:
                    val = random.randint(0, len(allowed_legends) - 1)
                    choice = allowed_legends[val]

            entry['pokeData']['devId'] = fetch_devname(choice, names)
            entry['pokeData']['formId'] = get_alt_form(choice)

            if config['all_shiny'] == "yes":
                entry['pokeData']['rareType'] = "RARE"
            elif config['higher_shiny_chance'] == "yes":
                chance = random.randint(0, 10)
                if chance == 10:
                    entry['pokeData']['rareType'] = "RARE"
                else:
                    entry['pokeData']['rareType'] = "NO_RARE"
            if i < 3:
                if shinyforced[i] == 1:
                    entry['pokeData']['rareType'] = "RARE"
            i = i +1

            if config['randomize_tera_type'] == "yes":
                entry['pokeData']['gemType'] = tera_types[random.randint(0, len(tera_types) - 1)].upper()

                match choice:
                    case 1011:
                        match alt_form_choosen:
                            case 0:
                                entry['pokeData']['gemType'] = "KUSA"
                                pass
                            case 1:
                                entry['pokeData']['gemType'] = "MIZU"
                                pass
                            case 2:
                                entry['pokeData']['gemType'] = "HONOO"
                                pass
                            case 3:
                                entry['pokeData']['gemType'] = "IWA"
                                pass
                    case 1021:
                        entry['pokeData']['gemType'] = "NIJI"
                    case _:
                        pass

        entry['pokeData']['wazaType'] = "DEFAULT"
        entry['pokeData']['waza1']['wazaId'] = "WAZA_NULL"
        entry['pokeData']['waza2']['wazaId'] = "WAZA_NULL"
        entry['pokeData']['waza3']['wazaId'] = "WAZA_NULL"
        entry['pokeData']['waza4']['wazaId'] = "WAZA_NULL"
        picked_gifts.append(choice)

    return pokemon


def make_poke_random(pokeEntry, index: str, csvdata, config, beginner: bool, allowedpokemon):
    chosenmon = allowedpokemon[random.randint(0, len(allowedpokemon)-1)]
    while chosenmon in banned_pokemon:
        chosenmon = allowedpokemon[random.randint(0, len(allowedpokemon)-1)]
    pokeEntry['poke' + index]['devId'] = fetch_devname(chosenmon, csvdata)
    alt_form_choosen = get_alt_form(chosenmon)
    pokeEntry['poke' + index]['formId'] = alt_form_choosen
    pokeEntry['poke' + index]['sex'] = "DEFAULT"
    pokeEntry['poke' + index]['level'] = pokeEntry['poke1']['level']
    if beginner is False:
        choice = random.randint(1, 4)
        pokeEntry['poke' + index]['level'] = pokeEntry['poke' + index]['level'] + choice
    pokeEntry['poke' + index]['wazaType'] = "DEFAULT"
    pokeEntry['poke' + index]['waza1']['wazaId'] = "WAZA_TERABAASUTO"
    pokeEntry['poke' + index]['waza2']['wazaId'] = "WAZA_NULL"
    pokeEntry['poke' + index]['waza3']['wazaId'] = "WAZA_NULL"
    pokeEntry['poke' + index]['waza4']['wazaId'] = "WAZA_NULL" #6 mons on gyms, elite 4 champ
    if config['force_perfect_ivs'] == "yes":
        talentvalue = {
            "hp": 31,
            "atk": 31,
            "def": 31,
            "spAtk": 31,
            "spDef": 31,
            "agi": 31
        }
        pokeEntry['poke' + index]['talentValue'] = talentvalue
    if config['randomize_fixed_tera_type'] == "yes" and pokeEntry['poke' + index]['gemType'] != "DEFAULT":
        pokeEntry['poke' + index]['gemType'] = tera_types[random.randint(0, len(tera_types) - 1)].upper()
    if config['randomize_all_tera_type'] == "yes":
        pokeEntry['poke' + index]['gemType'] = tera_types[random.randint(0, len(tera_types) - 1)].upper()
    if config['allow_trainers_shiny_pokemon'] == "yes":
        shinychance = random.randint(0, 15)
        if shinychance == 7:
            pokeEntry['poke' + index]['rareType'] = "RARE"
        else:
            pokeEntry['poke' + index]['rareType'] = "NO_RARE"
    # Add check for ogerpon later
    match chosenmon:
        case 1011:
            match alt_form_choosen:
                case 0:
                    pokeEntry['poke' + index]['gemType'] = "KUSA"
                    pass
                case 1:
                    pokeEntry['poke' + index]['gemType'] = "MIZU"
                    pass
                case 2:
                    pokeEntry['poke' + index]['gemType'] = "HONOO"
                    pass
                case 3:
                    pokeEntry['poke' + index]['gemType'] = "IWA"
                    pass
        case 1021:
            pokeEntry['poke' + index]['gemType'] = "NIJI"
    picked_trainer.append(chosenmon)


def randomizeEvolutionsEveryLevel(allowedpokemon):
    template_evolution = {
        "level": 0,
        "condition": 0,
        "parameter": 0,
        "reserved3": 0,
        "reserved4": 0,
        "reserved5": 0,
        "species": 0,
        "form": 0
    }

    evoList = []
    for i in range(1, 101):
        template_evolution['level'] = i
        template_evolution['condition'] = 4
        species_choice = allowedpokemon[random.randint(0, len(allowedpokemon)-1)]
        while species_choice in banned_pokemon:
            species_choice = allowedpokemon[random.randint(0, len(allowedpokemon)-1)]
        template_evolution['species'] = species_choice
        template_evolution['form'] = get_alt_form(species_choice)
        evoList.append(template_evolution)

        template_evolution = {
            "level": 0,
            "condition": 0,
            "parameter": 0,
            "reserved3": 0,
            "reserved4": 0,
            "reserved5": 0,
            "species": 0,
            "form": 0
        }

    return evoList


def checkTrainerImportance(entry):
    trainerId = entry['trid']
    if "raid_assist_NPC" in trainerId:
        return "raid"
    elif "botan_" in trainerId:  # Penny
        return True
    elif "dan_" in trainerId:  # Team Star
        return True
    elif "e4_" in trainerId:  # Elite 4
        return True
    elif "gym_" in trainerId:  # Gym Leader/Gym Trainer
        return True
    elif "kihada_" in trainerId:  # Dendra
        return True
    elif "mimoza_" in trainerId:  # Miriam
        return True
    elif "pepper_" in trainerId:  # Arven
        return True
    elif "professor_A_01" in trainerId:  # Sada 6v6
        return True
    elif "professor_B_01" in trainerId:  # Turo 6v6
        return True
    elif "rehoru_" in trainerId:  # Raifort
        return True
    elif "richf_" in trainerId:  # O'Nare Base Game
        return True
    elif "rival_" in trainerId:  # Nemona
        return True
    elif "sawaro" in trainerId:  # Saguaro
        return True
    elif "seizi" in trainerId:  # Salvatore
        return True
    elif "brother" in trainerId:  # kieran
        return True
    elif "camera" in trainerId:  # Perrin
        return True
    elif "serebu" in trainerId:  # O'Nare
        return True
    elif "sp_trainer" in trainerId:  # Ogre Clan
        return True
    elif "sister" in trainerId:  # Carmine
        return True
    elif "s2_side" in trainerId:  # Epilogue Fights
        return True
    elif "dragon4" in trainerId:  # Dragon BBL
        return True
    elif "dragonchallenge" in trainerId:  # Dragon Fights
        return True
    elif "fairy4" in trainerId:  # Fairy BBL
        return True
    elif "fairychallenge" in trainerId:  # Fairy Fights
        return True
    elif "hagane4" in trainerId:  # Steel BBL
        return True
    elif "hono4" in trainerId:  # Fire BBL
        return True
    elif "honochallenge" in trainerId:  # Fire Fights
        return True
    elif "su2_bukatu" in trainerId:  # BBL Extra Fights
        return True
    elif "shiano" in trainerId:  # Cirano
        return True
    elif "taimu" in trainerId:  # Ryme
        return True
    elif "zinia" in trainerId:  # Bio Teacher
        return True
    else:
        return False


def randomize(config, globalconfig):
    allowed_pokemon = []
    allowed_legends = []
    if len(config['generations_allowed']) == 0:
        allowed_pokemon.extend(gen1)
        allowed_legends.extend(gen1_legends)
        allowed_pokemon.extend(gen2)
        allowed_legends.extend(gen2_legends)
        allowed_pokemon.extend(gen3)
        allowed_legends.extend(gen3_legends)
        allowed_pokemon.extend(gen4)
        allowed_legends.extend(gen4_legends)
        allowed_pokemon.extend(gen5)
        allowed_legends.extend(gen5_legends)
        allowed_pokemon.extend(gen6)
        allowed_legends.extend(gen6_legends)
        allowed_pokemon.extend(gen7)
        allowed_legends.extend(gen7_legends)
        allowed_pokemon.extend(gen8)
        allowed_legends.extend(gen8_legends)
        allowed_pokemon.extend(gen9)
        allowed_legends.extend(paradox)
        allowed_legends.extend(gen9_legends)
    else:
        in_array = [0] * 9
        for generations in config['generations_allowed']:
            match generations:
                case 1:
                    if in_array[0] == 1:
                        print("Duplicate Generation 1")
                        exit(0)
                    allowed_pokemon.extend(gen1)
                    allowed_legends.extend(gen1_legends)
                    in_array[0] = 1
                    continue
                case 2:
                    if in_array[1] == 1:
                        print("Duplicate Generation 2")
                        exit(0)
                    allowed_pokemon.extend(gen2)
                    allowed_legends.extend(gen2_legends)
                    in_array[1] = 1
                    continue
                case 3:
                    if in_array[2] == 1:
                        print("Duplicate Generation 3")
                        exit(0)
                    allowed_pokemon.extend(gen3)
                    allowed_legends.extend(gen3_legends)
                    in_array[2] = 1
                    continue
                case 4:
                    if in_array[3] == 1:
                        print("Duplicate Generation 4")
                        exit(0)
                    allowed_pokemon.extend(gen4)
                    allowed_legends.extend(gen4_legends)
                    in_array[3] = 1
                    continue
                case 5:
                    if in_array[4] == 1:
                        print("Duplicate Generation 5")
                        exit(0)
                    allowed_pokemon.extend(gen5)
                    allowed_legends.extend(gen5_legends)
                    in_array[4] = 1
                    continue
                case 6:
                    if in_array[5] == 1:
                        print("Duplicate Generation 6")
                        exit(0)
                    allowed_pokemon.extend(gen6)
                    allowed_legends.extend(gen6_legends)
                    in_array[5] = 1
                    continue
                case 7:
                    if in_array[6] == 1:
                        print("Duplicate Generation 7")
                        exit(0)
                    allowed_pokemon.extend(gen7)
                    allowed_legends.extend(gen7_legends)
                    in_array[6] = 1
                    continue
                case 8:
                    if in_array[7] == 1:
                        print("Duplicate Generation 8")
                        exit(0)
                    allowed_pokemon.extend(gen8)
                    allowed_legends.extend(gen8_legends)
                    in_array[7] = 1
                    continue
                case 9:
                    if in_array[8] == 1:
                        print("Duplicate Generation 9")
                        exit(0)
                    allowed_pokemon.extend(gen9)
                    allowed_legends.extend(paradox)
                    allowed_legends.extend(gen9_legends)
                    in_array[8] = 1
                    continue
                case _:
                    print("Invalid Generation")
                    exit(0)

    if config['is_enabled'] == "yes":
        # Add option for checking if every level evolution later
        if (globalconfig['personal_data_randomizer']['is_enabled'] == "yes" and
            globalconfig['personal_data_randomizer']['randomize_evolutions'] == "yes"
            and config['evolution_limiter'] == "yes"):
            file = open(os.getcwd() + "/Randomizer/PersonalData/" + "personal_array_clean.json", "r")
            data = json.load(file)
            file.close()
            for pokemon in data['entry']:
                pokemon = randomizeEvolutions(pokemon, allowed_pokemon)

            outdata = json.dumps(data, indent=4)
            with open(os.getcwd() + "/Randomizer/PersonalData/" + "personal_array.json", 'w') as outfile:
                outfile.write(outdata)
            print("Limted Generation Randomisation Of Evos Done !")
        if (globalconfig['personal_data_randomizer']['is_enabled'] == "yes" and
            globalconfig['personal_data_randomizer']['let_pokemon_evolve_every_level'] == "yes"
            and config['evolution_limiter'] == "yes"):
            file = open(os.getcwd() + "/Randomizer/PersonalData/" + "personal_array.json", "r")
            data = json.load(file)
            file.close()
            for pokemon in data['entry']:
                pokemon['evolutions'] = randomizeEvolutionsEveryLevel(allowed_pokemon)

            outdata = json.dumps(data, indent=4)
            with open(os.getcwd() + "/Randomizer/PersonalData/" + "personal_array.json", 'w') as outfile:
                outfile.write(outdata)
            print("Limted Generation Randomisation Of Evos Done !")
        if (globalconfig['starter_randomizer']['is_enabled'] == "yes"
            and config['starter_limiter'] == "yes"):
            if os.path.exists(os.getcwd() + "/Randomizer/Starters/" + f'output'):
                shutil.rmtree(os.getcwd() + "/Randomizer/Starters/" + f'output')

            file = open(os.getcwd() + "/Randomizer/Starters/" + "eventAddPokemon_array_clean.json", "r")
            data = json.load(file)
            file.close()
            file = open(os.getcwd() + "/Randomizer/Starters/" + "pokemon_to_id.txt", "r")
            names = []
            for name in file:
                names.append(name)
            file.close()

            data2 = randomizeStarters(globalconfig['starter_randomizer'], data, allowed_pokemon, names, allowed_legends,
                                      config['generations_allowed'])
            data = data2
            outdata = json.dumps(data, indent=4)
            with open(os.getcwd() + "/Randomizer/Starters/" + "eventAddPokemon_array.json", 'w') as outfile:
                outfile.write(outdata)
            print("Limted Generation Randomisation Of Starter Pokemon Done !")
        if (globalconfig['static_randomizer']['is_enabled'] == "yes"
            and config['static_limiter'] == "yes"):
            file = open(os.getcwd() + "/Randomizer/StaticSpawns/fixed_symbol_table_array_clean.json", "r")
            data = json.load(file)
            file.close()
            names = []
            file = open(os.getcwd() + "/Randomizer/StaticSpawns/pokemon_to_id.txt", "r")
            for x in file:
                names.append(x)
            file.close()

            for pokemon in data['values']:
                make_poke(pokemon, names, globalconfig['static_randomizer'], allowed_pokemon)

            outdata = json.dumps(data, indent=4)
            with open(os.getcwd() + "/Randomizer/StaticSpawns/" + "fixed_symbol_table_array.json", 'w') as outfile:
                outfile.write(outdata)
            print("Limted Generation Randomisation for Statics Done (Not including Boss/Snackworth)!")
        if (globalconfig['trainer_randomizer']['is_enabled'] == "yes"
            and config['trainer_limiter'] == "yes"):
            file = open(os.getcwd() + "/Randomizer/Trainers/" + "trdata_array_clean.json", "r")
            data = json.load(file)

            csvfile = open(os.getcwd() + "/Randomizer/Trainers/" + "pokemon_to_id.txt", "r")
            csvdata = []
            for i in csvfile:
                csvdata.append(i)
            csvfile.close()

            for entry in data['values']:
                if globalconfig['trainer_randomizer']['only_randomize_important_trainers'] == "yes":
                    if checkTrainerImportance(entry) is False:
                        continue
                if entry['trainerType'] == "su2_brother_kodaigame":
                    continue
                elif entry['trid'] == "professor_A_02":
                    continue
                elif entry['trid'] == "professor_B_02":
                    continue
                # Counter to see how many pokemon there are to randomize originally
                counter = 1
                for j in range(0, 6):
                    t = j + 1
                    if entry['poke' + str(t)]['devId'] != "DEV_NULL":
                        counter = counter + 1
                pokemon_to_randomize = counter

                if globalconfig['trainer_randomizer']['give_trainers_extra_mons'] == "yes":
                    new_counter = 1
                    # Counter to see how many free slots there are
                    for j in range(2, 6):
                        if entry['poke' + str(j)]['devId'] == "DEV_NULL":
                            new_counter = new_counter + 1
                    # If none then just randomize all 6
                    if new_counter == 0:
                        pokemon_to_randomize = 6
                    else:
                        # if some then choose a random number between 1 and itself
                        pokemon_to_randomize = random.randint(1, new_counter)
                        pokemon_to_randomize = pokemon_to_randomize + counter
                        if pokemon_to_randomize > 6:
                            pokemon_to_randomize = 6
                if globalconfig['trainer_randomizer']['force_6_pokemons_on_trainers'] == "yes":
                    # If user wants all 6 then set to all 6
                    pokemon_to_randomize = 6

                # a way to prevent any errors
                beginner = False
                if pokemon_to_randomize > 6:
                    pokemon_to_randomize = 6
                elif pokemon_to_randomize < 1:
                    # get exact number if its less than 1 (should never happen)
                    counter = 1
                    for j in range(0, 6):
                        t = j + 1
                        if entry['poke' + str(t)]['devId'] != "DEV_NULL":
                            counter = counter + 1
                    pokemon_to_randomize = counter
                temp_legends = globalconfig['trainer_randomizer']['only_legends']
                temp_paradox = globalconfig['trainer_randomizer']['only_paradox']
                temp_both = globalconfig['trainer_randomizer']['only_legends_and_paradoxes']
                if checkTrainerImportance(entry) == "raid":
                    if globalconfig['trainer_randomizer']['tera_raid_trainers_only_legends'] == "yes":
                        globalconfig['trainer_randomizer']['only_legends'] = "yes"
                    if globalconfig['trainer_randomizer']['tera_raid_trainers_only_paradox'] == "yes":
                        globalconfig['trainer_randomizer']['only_paradox'] = "yes"
                    if globalconfig['trainer_randomizer']['tera_raid_trainers_only_both'] == "yes":
                        globalconfig['trainer_randomizer']['only_legends_and_paradoxes'] = "yes"
                elif checkTrainerImportance(entry) is True:
                    if globalconfig['trainer_randomizer']["force_important_trainers_to6_pokemon"] == "yes":
                        pokemon_to_randomize = 6
                    if globalconfig['trainer_randomizer']['impo_trainers_only_legends'] == "yes":
                        globalconfig['trainer_randomizer']['only_legends'] = "yes"
                    if globalconfig['trainer_randomizer']['impo_trainers_only_paradox'] == "yes":
                        globalconfig['trainer_randomizer']['only_paradox'] = "yes"
                    if globalconfig['trainer_randomizer']['impo_trainers_only_both'] == "yes":
                        globalconfig['trainer_randomizer']['only_legends_and_paradoxes'] = "yes"

                if entry['trid'] == "rival_01_hono" or entry['trid'] == "rival_01_kusa" or entry[
                    'trid'] == "rival_01_mizu":
                    pokemon_to_randomize = 1
                    beginner = True

                i = 1
                while i <= pokemon_to_randomize:
                    make_poke_random(entry, str(i), csvdata, globalconfig['trainer_randomizer'], beginner, allowed_pokemon)
                    i = i + 1
                globalconfig['trainer_randomizer']['only_legends'] = temp_legends
                globalconfig['trainer_randomizer']['only_paradox'] = temp_paradox
                globalconfig['trainer_randomizer']['only_legends_and_paradoxes'] = temp_both
                if globalconfig['trainer_randomizer']['make_ai_smart_for_all_trainers'] == "yes" and beginner is False:
                    entry['aiBasic'] = True
                    entry['aiHigh'] = True
                    entry['aiExpert'] = True
                    entry['aiChange'] = True
                if globalconfig['trainer_randomizer']['allow_all_trainers_to_terastalize'] == "yes" and beginner is False:
                    entry['changeGem'] = True
                if "raid_assist_NPC" not in entry['trid']:
                    if globalconfig['trainer_randomizer']['randomnly_choose_single_or_double'] == "yes" and beginner is False:
                        battleformat = random.randint(1, 2)
                        if battleformat == 2 and pokemon_to_randomize < 2:
                            make_poke_random(entry, str(2), csvdata, globalconfig['trainer_randomizer'], beginner, allowed_pokemon)
                        if battleformat == 2:
                            entry['aiDouble'] = True
                        type_of_battle = f"_{battleformat}vs{battleformat}"
                        entry['battleType'] = type_of_battle
                    if globalconfig['trainer_randomizer']['only_double'] == "yes" and beginner is False:
                        entry['battleType'] = "_2vs2"
                        entry['aiDouble'] = True
                        if pokemon_to_randomize < 2:
                            make_poke_random(entry, str(2), csvdata, globalconfig['trainer_randomizer'], beginner, allowed_pokemon)


            outdata = json.dumps(data, indent=4)
            with open(os.getcwd() + "/Randomizer/Trainers/" + "trdata_array.json", 'w') as outfile:
                outfile.write(outdata)
            print("Limted Generation Randomisation of Trainers done !")
        if (globalconfig['wild_randomizer']['is_enabled'] == "yes"
            and config['wild_limiter'] == "yes"):
            randomize_paldea(globalconfig['wild_randomizer'], allowed_pokemon)
            randomize_teal(globalconfig['wild_randomizer'], allowed_pokemon)
            randomize_indigo(globalconfig['wild_randomizer'], allowed_pokemon)

    print(f'Completed Randomization for Pokemon of only the following generations: ')
    if len(config['generations_allowed']) == 0:
        for i in range(0, 9):
            gen = i + 1
            print(f'Generation - {str(gen)}')
    else:
        for i in range(0, len(config['generations_allowed'])):
            gen = config['generations_allowed'][i]
            print(f'Generation - {str(gen)}')