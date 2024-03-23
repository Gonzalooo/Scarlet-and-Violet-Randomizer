import json
import random
import os

legends = [144, 145, 146, 150, 151, 243, 244, 245, 249, 250, 251, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 480,
           481, 482, 483, 484, 485, 486, 487, 489, 490, 491, 492, 493, 494, 638, 639, 640, 641, 642, 643, 644, 645, 646,
           647, 648, 649, 716, 717, 718, 719, 720, 721, 785, 786, 787, 788, 789, 790, 791, 792, 800, 801, 802, 807, 808,
           809, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 905, 994, 995, 996, 997, 998, 999, 1009, 1010,
           1011, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022]
legends_and_paradox = [
           144, 145, 146, 150, 151, 243, 244, 245, 249, 250, 251, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 480,
           481, 482, 483, 484, 485, 486, 487, 489, 490, 491, 492, 493, 494, 638, 639, 640, 641, 642, 643, 644, 645, 646,
           647, 648, 649, 716, 717, 718, 719, 720, 721, 785, 786, 787, 788, 789, 790, 791, 792, 800, 801, 802, 807, 808,
           809, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 905, 978, 979, 980, 981, 982, 983, 984, 985, 986,
           987, 988, 989, 990, 991, 992, 993, 1017, 1018, 1019, 1020, 994, 995, 996, 997, 998, 999, 1011, 1014, 1015,
           1016, 1021, 1022]
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
                  880, 881, 882, 883, 1011, 1021]
UB = [793, 794, 795, 796, 797, 798, 799, 803, 804, 805, 806]
paradox = [978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 998, 999, 1021,
           1017, 1018, 1019, 1020]
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
in_array = [0] * 9
has_alt_form_with_item = [483, 484, 487, 493, 888, 889]
gen1bannedlength = 52
gen2bannedlength = 18
gen3bannedlength = 48
gen4bannedlength = 22
gen5bannedlength = 70
gen6bannedlength = 25
gen7bannedlength = 25
gen8bannedlength = 31
gen9bannedlength = 2
totalbannedlength = 0
generationLimter = False
forcedShiny = False
increasedShiny = False


def get_item_for_alt_form(index: int, form: int, raidJSON):
    if index in has_alt_form_with_item:
        match index:
            case 483:
                if form == 1:
                    raidJSON['item'] = "ITEMID_DAIKONGOUDAMA"
            case 484:
                if form == 1:
                    raidJSON['item'] = "ITEMID_DAISIRATAMA"
            case 487:
                if form == 1:
                    raidJSON['item'] = "ITEMID_DAIHAKKINDAMA"
            case 493:
                match form:
                    case 1:  # Fightning
                        raidJSON['item'] = "ITEMID_KOBUSINOPUREETO"
                    case 2:  # Flying
                        raidJSON['item'] = "ITEMID_AOZORAPUREETO"
                    case 3:  # poison
                        raidJSON['item'] = "ITEMID_MOUDOKUPUREETO"
                    case 4:  # ground
                        raidJSON['item'] = "ITEMID_DAITINOPUREETO"
                    case 5:  # rock
                        raidJSON['item'] = "ITEMID_GANSEKIPUREETO"
                    case 6:  # bug
                        raidJSON['item'] = "ITEMID_TAMAMUSIPUREETO"
                    case 7:  # ghost
                        raidJSON['item'] = "ITEMID_MONONOKEPUREETO"
                    case 8:  # steel
                        raidJSON['item'] = "ITEMID_KOUTETUPUREETO"
                    case 9:  # fire
                        raidJSON['item'] = "ITEMID_HINOTAMAPUREETO"
                    case 10:  # water
                        raidJSON['item'] = "ITEMID_SIZUKUPUREETO"
                    case 11:  # grass
                        raidJSON['item'] = "ITEMID_MIDORINOPUREETO"
                    case 12:  # electric
                        raidJSON['item'] = "ITEMID_IKAZUTIPUREETO"
                    case 13:  # psychic
                        raidJSON['item'] = "ITEMID_HUSIGINOPUREETO"
                    case 14:  # ice
                        raidJSON['item'] = "ITEMID_TURARANOPUREETO"
                    case 15:  # dragon
                        raidJSON['item'] = "ITEMID_RYUUNOPUREETO"
                    case 16:  # dark
                        raidJSON['item'] = "ITEMID_KOWAMOTEPUREETO"
                    case 17:  # Fairy
                        raidJSON['item'] = "ITEMID_SEIREIPUREETO"
            case 888:
                if form == 1:
                    raidJSON['item'] = "ITEMID_KUTITATURUGI"
            case 889:
                if form == 1:
                    raidJSON['item'] = "ITEMID_KUTITATATE"
    return raidJSON


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
    #print(csvdata[index])
    return str.strip(csvdata[index])


def randomizeRaids(raidsJSON, limiter):
    global totalbannedlength
    csvfile = open(os.getcwd() + "/Randomizer/WildEncounters/" + "pokemon_to_id.txt", "r")
    csvdata = []
    for i in csvfile:
        csvdata.append(i)
    csvfile.close()

    newRaidJSON = {}
    newRaidJSON['values'] = []
    counter = 0

    usedPokemon = []
    dialgaForms = []
    palkiaForms = []
    giratinaForms = []
    arceusForms = []
    zacianForms = []
    zamazentaForms = []
    for i in range(0, len(raidsJSON['values'])):
        addedToUsed = False
        pokeChoice = random.randint(0, len(limiter) - 1)
        altformNumber = get_alt_form(limiter[pokeChoice])
        if limiter[pokeChoice] in has_alt_form_with_item:
            match limiter[pokeChoice]:
                case 483:
                    if limiter[pokeChoice] in usedPokemon:
                        pass
                    else:
                        while altformNumber in dialgaForms:
                            altformNumber = get_alt_form(limiter[pokeChoice])
                        dialgaForms.append(altformNumber)
                        if len(dialgaForms) < 2:
                            addedToUsed = True
                        else:
                            addedToUsed = False
                case 484:
                    if limiter[pokeChoice] in usedPokemon:
                        pass
                    else:
                        while altformNumber in palkiaForms:
                            altformNumber = get_alt_form(limiter[pokeChoice])
                        palkiaForms.append(altformNumber)
                        if len(palkiaForms) < 2:
                            addedToUsed = True
                        else:
                            addedToUsed = False
                case 487:
                    if limiter[pokeChoice] in usedPokemon:
                        pass
                    else:
                        while altformNumber in giratinaForms:
                            altformNumber = get_alt_form(limiter[pokeChoice])
                        giratinaForms.append(altformNumber)
                        if len(giratinaForms) < 2:
                            addedToUsed = True
                        else:
                            addedToUsed = False
                case 493:
                    if limiter[pokeChoice] in usedPokemon:
                        pass
                    else:
                        while altformNumber in arceusForms:
                            altformNumber = get_alt_form(limiter[pokeChoice])
                        arceusForms.append(altformNumber)
                        if len(arceusForms) < 18:
                            addedToUsed = True
                        else:
                            addedToUsed = False
                case 888:
                    if limiter[pokeChoice] in usedPokemon:
                        pass
                    else:
                        while altformNumber in zacianForms:
                            altformNumber = get_alt_form(limiter[pokeChoice])
                        zacianForms.append(altformNumber)
                        if len(zacianForms) < 2:
                            addedToUsed = True
                        else:
                            addedToUsed = False
                case 889:
                    if limiter[pokeChoice] in usedPokemon:
                        pass
                    else:
                        while altformNumber in zamazentaForms:
                            altformNumber = get_alt_form(limiter[pokeChoice])
                        zamazentaForms.append(altformNumber)
                        if len(zamazentaForms) < 2:
                            addedToUsed = True
                        else:
                            addedToUsed = False
                case _:
                    pass
        while limiter[pokeChoice] in banned_pokemon or limiter[pokeChoice] in usedPokemon:
            pokeChoice = random.randint(0, len(limiter) - 1)

            if len(limiter) - len(usedPokemon) == totalbannedlength:
                break
            altformNumber = get_alt_form(limiter[pokeChoice])
            if limiter[pokeChoice] in has_alt_form_with_item:
                match limiter[pokeChoice]:
                    case 483:
                        if limiter[pokeChoice] in usedPokemon:
                            pass
                        else:
                            while altformNumber in dialgaForms:
                                altformNumber = get_alt_form(limiter[pokeChoice])
                            dialgaForms.append(altformNumber)
                            if len(dialgaForms) < 2:
                                addedToUsed = True
                            else:
                                addedToUsed = False
                    case 484:
                        if limiter[pokeChoice] in usedPokemon:
                            pass
                        else:
                            while altformNumber in palkiaForms:
                                altformNumber = get_alt_form(limiter[pokeChoice])
                            palkiaForms.append(altformNumber)
                            if len(palkiaForms) < 2:
                                addedToUsed = True
                            else:
                                addedToUsed = False
                    case 487:
                        if limiter[pokeChoice] in usedPokemon:
                            pass
                        else:
                            while altformNumber in giratinaForms:
                                altformNumber = get_alt_form(limiter[pokeChoice])
                            giratinaForms.append(altformNumber)
                            if len(giratinaForms) < 2:
                                addedToUsed = True
                            else:
                                addedToUsed = False
                    case 493:
                        if limiter[pokeChoice] in usedPokemon:
                            pass
                        else:
                            while altformNumber in arceusForms:
                                altformNumber = get_alt_form(limiter[pokeChoice])
                            arceusForms.append(altformNumber)
                            if len(arceusForms) < 18:
                                addedToUsed = True
                            else:
                                addedToUsed = False
                    case 888:
                        if limiter[pokeChoice] in usedPokemon:
                            pass
                        else:
                            while altformNumber in zacianForms:
                                altformNumber = get_alt_form(limiter[pokeChoice])
                            zacianForms.append(altformNumber)
                            if len(zacianForms) < 2:
                                addedToUsed = True
                            else:
                                addedToUsed = False
                    case 889:
                        if limiter[pokeChoice] in usedPokemon:
                            pass
                        else:
                            while altformNumber in zamazentaForms:
                                altformNumber = get_alt_form(limiter[pokeChoice])
                            zamazentaForms.append(altformNumber)
                            if len(zamazentaForms) < 2:
                                addedToUsed = True
                            else:
                                addedToUsed = False
                    case _:
                        pass
        if len(limiter) - len(usedPokemon) == totalbannedlength:
            break
        if addedToUsed is False:
            usedPokemon.append(limiter[pokeChoice])

        counter = counter + 1
        raidsJSON['values'][i]['raidEnemyInfo']['romVer'] = "BOTH"
        raidsJSON['values'][i]['raidEnemyInfo']['bossPokePara']['devId'] = fetch_devname(limiter[pokeChoice], csvdata)
        raidsJSON['values'][i]['raidEnemyInfo']['bossPokePara']['formId'] = altformNumber
        get_item_for_alt_form(limiter[pokeChoice], altformNumber, raidsJSON['values'][i]['raidEnemyInfo']['bossPokePara'])
        raidsJSON['values'][i]['raidEnemyInfo']['bossPokePara']['wazaType'] = "DEFAULT"
        raidsJSON['values'][i]['raidEnemyInfo']['bossPokePara']['waza1']['wazaId'] = "WAZA_TERABAASUTO"
        raidsJSON['values'][i]['raidEnemyInfo']['bossPokePara']['waza2']['wazaId'] = "WAZA_NULL"
        raidsJSON['values'][i]['raidEnemyInfo']['bossPokePara']['waza3']['wazaId'] = "WAZA_NULL"
        raidsJSON['values'][i]['raidEnemyInfo']['bossPokePara']['waza4']['wazaId'] = "WAZA_NULL"
        if forcedShiny is True:
            raidsJSON['values'][i]['raidEnemyInfo']['bossPokePara']['rareType'] = "RARE"
        elif increasedShiny is True:
            choice = random.randint(1, 10)
            if choice == 10:
                raidsJSON['values'][i]['raidEnemyInfo']['bossPokePara']['rareType'] = "RARE"

        if len(usedPokemon) == len(limiter):
            break

    if len(raidsJSON['values']) - counter < 0:
        newRaidJSON['values'] = raidsJSON['values'][:len(raidsJSON['values'])-1]
    elif len(raidsJSON['values']) - counter > 0:
        newRaidJSON['values'] = raidsJSON['values'][:counter]
    else:
        newRaidJSON['values'] = raidsJSON['values']
    usedPokemon = []
    dialgaForms = []
    palkiaForms = []
    giratinaForms = []
    arceusForms = []
    zacianForms = []
    zamazentaForms = []
    return newRaidJSON


def randomizeBlueberry(config, pokemonAllowed, legendsAllowed):
    if pokemonAllowed is None:
        pokemonAllowed = [i for i in range(1, 1026)]
    for i in range(1, 7):
        blueberryTeraRaids = open(os.getcwd() + '/Randomizer/blueberryTeraRaids/' + f'su2_raid_enemy_0{str(i)}_array_clean.json', 'r')
        blueberryRaids = json.load(blueberryTeraRaids)
        blueberryTeraRaids.close()

        randomizeRaids(blueberryRaids, pokemonAllowed)

        if generationLimter is False:
            if config['only_paradox'] == "yes":
                blueberryRaids = randomizeRaids(blueberryRaids, paradox)
            if config['only_legends'] == "yes":
                blueberryRaids = randomizeRaids(blueberryRaids, legends)
            if config['only_legends_and_paradox'] == "yes":
                blueberryRaids = randomizeRaids(blueberryRaids, legends_and_paradox)
        if generationLimter is True:
            if config['only_paradox'] == "yes" and in_array[8] == 1:
                blueberryRaids = randomizeRaids(blueberryRaids, paradox)
            if config['only_legends'] == "yes":
                blueberryRaids = randomizeRaids(blueberryRaids, legendsAllowed)
            if config['only_legends_and_paradox'] == "yes" and in_array[8] == 1:
                blueberryRaids = randomizeRaids(blueberryRaids, legendsAllowed)

        outdata = json.dumps(blueberryRaids, indent=4)
        with open(os.getcwd() + '/Randomizer/blueberryTeraRaids/' + f'su2_raid_enemy_0{str(i)}_array.json', 'w') as outfile:
            outfile.write(outdata)
        print(f"Randomisation of Blueberry Raids Star {str(i)} Done !")


def limitBlueberryRaids(config, actualconfig):
    global totalbannedlength
    global generationLimter
    generationLimter = True
    for i in range(0, 9):
        in_array[i] = 0
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
        totalbannedlength = len(banned_pokemon)
    else:
        for generations in config['generations_allowed']:
            match generations:
                case 1:
                    if in_array[0] == 1:
                        print("Duplicate Generation 1")
                        exit(0)
                    allowed_pokemon.extend(gen1)
                    allowed_legends.extend(gen1_legends)
                    in_array[0] = 1
                    totalbannedlength = totalbannedlength + gen1bannedlength
                    continue
                case 2:
                    if in_array[1] == 1:
                        print("Duplicate Generation 2")
                        exit(0)
                    allowed_pokemon.extend(gen2)
                    allowed_legends.extend(gen2_legends)
                    totalbannedlength = totalbannedlength + gen2bannedlength
                    in_array[1] = 1
                    continue
                case 3:
                    if in_array[2] == 1:
                        print("Duplicate Generation 3")
                        exit(0)
                    allowed_pokemon.extend(gen3)
                    allowed_legends.extend(gen3_legends)
                    totalbannedlength = totalbannedlength + gen3bannedlength
                    in_array[2] = 1
                    continue
                case 4:
                    if in_array[3] == 1:
                        print("Duplicate Generation 4")
                        exit(0)
                    allowed_pokemon.extend(gen4)
                    allowed_legends.extend(gen4_legends)
                    totalbannedlength = totalbannedlength + gen4bannedlength
                    in_array[3] = 1
                    continue
                case 5:
                    if in_array[4] == 1:
                        print("Duplicate Generation 5")
                        exit(0)
                    allowed_pokemon.extend(gen5)
                    allowed_legends.extend(gen5_legends)
                    totalbannedlength = totalbannedlength + gen5bannedlength
                    in_array[4] = 1
                    continue
                case 6:
                    if in_array[5] == 1:
                        print("Duplicate Generation 6")
                        exit(0)
                    allowed_pokemon.extend(gen6)
                    allowed_legends.extend(gen6_legends)
                    totalbannedlength = totalbannedlength + gen6bannedlength
                    in_array[5] = 1
                    continue
                case 7:
                    if in_array[6] == 1:
                        print("Duplicate Generation 7")
                        exit(0)
                    allowed_pokemon.extend(gen7)
                    allowed_legends.extend(gen7_legends)
                    totalbannedlength = totalbannedlength + gen7bannedlength
                    in_array[6] = 1
                    continue
                case 8:
                    if in_array[7] == 1:
                        print("Duplicate Generation 8")
                        exit(0)
                    allowed_pokemon.extend(gen8)
                    allowed_legends.extend(gen8_legends)
                    totalbannedlength = totalbannedlength + gen8bannedlength
                    in_array[7] = 1
                    continue
                case 9:
                    if in_array[8] == 1:
                        print("Duplicate Generation 9")
                        exit(0)
                    allowed_pokemon.extend(gen9)
                    allowed_legends.extend(paradox)
                    allowed_legends.extend(gen9_legends)
                    totalbannedlength = totalbannedlength + gen9bannedlength
                    in_array[8] = 1
                    continue
                case _:
                    print("Invalid Generation")
                    exit(0)

    randomizeBlueberry(actualconfig, allowed_pokemon, allowed_legends)
    totalbannedlength = 0


def randomize(config, configGlobal):
    if config['force_shiny'] == "yes":
        global forcedShiny
        forcedShiny = True
    if config['increased_shiny_chance'] == "yes":
        global increasedShiny
        increasedShiny = True

    if configGlobal['limit_generation']['is_enabled'] == "yes" and configGlobal['limit_generation']['teraRaid_limiter'] == "yes":
        limitBlueberryRaids(configGlobal['limit_generation'], config)
    elif config['is_enabled'] == "yes":
        randomizeBlueberry(config, None, legends)