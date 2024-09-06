import sys

def translator(string):

    braille_characters = ".O"
    difference_set = set(string).difference(set(braille_characters))

    # states
    isCapitalized = False
    isNumber = False

    braille_to_english_dict = {
        "O.....": 'a',
        "O.O...": 'b',
        "OO....": 'c',
        "OO.O..": 'd',
        "O..O..": 'e',
        "OOO...": 'f',
        "OOOO..": 'g',
        "O.OO..": 'h',
        ".OO...": 'i',
        ".OOO..": 'j',
        "O...O.": 'k',
        "O.O.O.": 'l',
        "OO..O.": 'm',
        "OO.OO.": 'n',
        "O..OO.": 'o',
        "OOO.O.": 'p',
        "OOOOO.": 'q',
        "O.OOO.": 'r',
        ".OO.O.": 's',
        ".OOOO.": 't',
        "O...OO": 'u',
        "O.O.OO": 'v',
        ".OOO.O": 'w',
        "OO..OO": 'x',
        "OO.OOO": 'y',
        "O..OOO": 'z',
        # "..OO.O": '.',
        # "..O...": ',',
        # "..O.OO": '?',
        # "..OO..": ':',
        # "..O.O.": ';',
        # "....OO": '-',
        # ".O..O.": '/',
        # ".OO..O": '<',
        # "O..OO.": '>',
        # "O.O..O": '(',
        # ".O.OO.": ')',
        "......": ' '
    }

    braille_to_english_dict_num = {
        "O.....": '1',
        "O.O...": '2',
        "OO....": '3',
        "OO.O..": '4',
        "O..O..": '5',
        "OOO...": '6',
        "OOOO..": '7',
        "O.OO..": '8',
        ".OO...": '9',
        ".OOO..": '0'
    }

    english_to_braille_dict = {
        'a': "O.....",
        'b': "O.O...",
        'c': "OO....",
        'd': "OO.O..",
        'e': "O..O..",
        'f': "OOO...",
        'g': "OOOO..",
        'h': "O.OO..",
        'i': ".OO...",
        'j': ".OOO..",
        'k': "O...O.",
        'l': "O.O.O.",
        'm': "OO..O.",
        'n': "OO.OO.",
        'o': "O..OO.",
        'p': "OOO.O.",
        'q': "OOOOO.",
        'r': "O.OOO.",
        's': ".OO.O.",
        't': ".OOOO.",
        'u': "O...OO",
        'v': "O.O.OO",
        'w': ".OOO.O",
        'x': "OO..OO",
        'y': "OO.OOO",
        'z': "O..OOO",
        # "..OO.O": '.',
        # "..O...": ',',
        # "..O.OO": '?',
        # "..OO..": ':',
        # "..O.O.": ';',
        # "....OO": '-',
        # ".O..O.": '/',
        # ".OO..O": '<',
        # "O..OO.": '>',
        # "O.O..O": '(',
        # ".O.OO.": ')',
        ' ': "......"
    }

    english_to_braille_dict_num = {
        '1': "O.....",
        '2': "O.O...",
        '3': "OO....",
        '4': "OO.O..",
        '5': "O..O..",
        '6': "OOO...",
        '7': "OOOO..",
        '8': "O.OO..",
        '9': ".OO...",
        '0': ".OOO.."
    }

    english_translation = ""
    braille_translation = ""

    if len(difference_set) == 0:
        # It is Braille
        braille_characters = [(string[i:i+6]) for i in range(0, len(string), 6)]
        for braille in braille_characters:
            if braille == ".....O":
                # capital follows
                isCapitalized = True
                continue
            if braille == ".O...O":
                # decimal follows
                isNumber = True
                english_translation += '.'
                continue
            if braille == ".O.OOO":
                #number follows
                isNumber = True
                continue

            if isCapitalized:
                english_translation += braille_to_english_dict[braille].upper()
                isCapitalized = False
            elif isNumber:
                if braille == "......":
                    # space after a number
                    english_translation += ' '
                    isNumber = False
                else:
                    english_translation += braille_to_english_dict_num[braille]
            else:
                english_translation += braille_to_english_dict[braille]
        print(english_translation, end='')
    else:
        # It is English
        english_characters = [(string[i:i+1]) for i in range(0, len(string), 1)]
        for char in english_characters:
            if char.isupper():
                braille_translation += ".....O"
                braille_translation += english_to_braille_dict[char.lower()]
            elif isNumber:
                if char == ' ':
                    braille_translation += "......"
                    isNumber = False
                else:
                    braille_translation += english_to_braille_dict_num[char]
            elif char.isnumeric():
                braille_translation += ".O.OOO"
                braille_translation += english_to_braille_dict_num[char]
                isNumber = True
            else:
                braille_translation += english_to_braille_dict[char]
        print(braille_translation, end='')

for i in range(1, len(sys.argv)):
    translator(sys.argv[i])
