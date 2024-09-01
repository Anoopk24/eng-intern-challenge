
def braille_char(letter):
    braille_dict = {
        'a': 'O.....',
        'b': 'O.O...',
        'c': 'OO....',
        'd': 'OO.O..',
        'e': 'O..O..',
        'f': 'OOO...',
        'g': 'OOOO..',
        'h': 'O.OO..',
        'i': '.OO...',
        'j': '.OOO..',
        'k': 'O...O.',
        'l': 'O.O.O.',
        'm': 'OO..O.',
        'n': 'OO.OO.',
        'o': 'O..OO.',
        'p': 'OOO.O.',
        'q': 'OOOOO.',
        'r': 'O.OOO.',
        's': '.OO.O.',
        't': '.OOOO.',
        'u': 'O...OO',
        'v': 'O.O.OO',
        'w': '.OOO.O',
        'x': 'OO..OO',
        'y': 'OO.OOO',
        'z': 'O..OOO',
        '1': 'O.....',
        '2': 'O.O...',
        '3': 'OO....',
        '4': 'OO.O..',
        '5': 'O..O..',
        '6': 'OOO...',
        '7': 'OOOO..',
        '8': 'O.OO..',
        '9': '.OO...',
        '0': '.OOO..',
        ',': '..O...',
        ':': '..OO..',
        ';': '..O.O.',
        '.': '..OO.O',
        '!': '..OOO.',
        '(': 'O.O..O',
        ')': '.O.OO.',
        '?': '..O.OO',
        '-': '....OO',
        '/': '.O..O.',
        '<': '.OO..O',
        '>': 'O..OO.',
        ' ': '......'
    }
    return braille_dict[letter]


def eng_char(letter):
    eng_dict = {
        'O.....': ['a', 1],
        'O.O...': ['b', 2],
        'OO....': ['c', 3],
        'OO.O..': ['d', 4],
        'O..O..': ['e', 5],
        'OOO...': ['f', 6],
        'OOOO..': ['g', 7],
        'O.OO..': ['h', 8],
        '.OO...': ['i', 9],
        '.OOO..': ['j', 0],
        'O...O.': 'k',
        'O.O.O.': 'l',
        'OO..O.': 'm',
        'OO.OO.': 'n',
        'O..OO.': ['o', ">"],
        'OOO.O.': 'p',
        'OOOOO.': 'q',
        'O.OOO.': 'r',
        '.OO.O.': 's',
        '.OOOO.': 't',
        'O...OO': 'u',
        'O.O.OO': 'v',
        '.OOO.O': 'w',
        'OO..OO': 'x',
        'OO.OOO': 'y',
        'O..OOO': 'z',
        '..O...': ',',
        '..OO..': ';',
        '...O..': ':',
        '..OO.O': '.',
        '..OOO.': '!',
        'O.O..O': '(',
        '.O.OO.': ')',
        '..O.OO': '?',
        '....OO': '-',
        '.O..O.': '/',
        '.OO..O': '<',
        '......': ' '
    }
    return eng_dict[letter]


#  =  o  +

def eng_to_braille(w):
    hold_status = False
    string_builder = ""
    for letter in w:
        if letter.isupper():
            string_builder += ".....O"
        if letter.isnumeric() and hold_status == False:
            hold_status = True
            string_builder += ".O.OOO"
        if letter == " ":
            hold_status = False

        string_builder += braille_char(letter.lower())
    print(string_builder)


def braille_to_eng(w):
    string_builder = ""
    next_cap = False
    hold_status = False

    for chunk in range(0, len(w), 6):
        braille = (w[chunk:chunk+6])
        if braille == ".....O":
            next_cap = True
            continue
        elif braille == ".O.OOO":
            hold_status = True
            continue

        elif braille == "......":
            hold_status = False
            string_builder += eng_char(braille)

        elif next_cap:
            string_builder += eng_char(braille)[0].upper()
            next_cap = False

        elif hold_status == True:
            string_builder += str(eng_char(braille)[1])

        else:
            string_builder += eng_char(braille)[0]

    print(string_builder)


inp = input()

inpset = set(inp)
if inpset == {'O', '.'} or inpset == {'.'} or inpset == {'O'}:
    braille_to_eng(inp)
else:
    eng_to_braille(inp)
