
# . -> dot, O -> raised dot

import sys

# braille -> letters
letter_braille_map = {
    'a' : 'O.....',
    'b' : 'O.O...',
    'c' : 'OO....',
    'd' : 'OO.O..',
    'e' : 'O..O..',
    'f' : 'OOO...',
    'g' : 'OOOO..',
    'h' : 'O.OO..',
    'i' : '.OO...',
    'j' : '.OOO..',
    'k' : 'O...O.',
    'l' : 'O.O.O.',
    'm' : 'OO..O.',
    'n' : 'OO.OO.',
    'o' : 'O..OO.',
    'q' : 'OOOOO.',
    'r' : 'O.OOO.',
    's' : '.OO.O.',
    't' : '.OOOO.',
    'u' : 'O...OO',
    'v' : 'O.O.OO',
    'w' : '.OOO.O',
    'x' : 'OO..OO',
    'y' : 'OO.OOO',
    'z' : 'O..OOO'
}

# can be done with list comprehension, but kept for clarity
# number -> braille
number_braille_map = {
    '1' : letter_braille_map['a'],
    '2' : letter_braille_map['b'],
    '3' : letter_braille_map['c'],
    '4' : letter_braille_map['d'],
    '5' : letter_braille_map['e'],
    '6' : letter_braille_map['f'],
    '7' : letter_braille_map['g'],
    '8' : letter_braille_map['h'],
    '9' : letter_braille_map['i'],
    '0' : letter_braille_map['j']
}

# 0 -> capital follows, 1 -> number input until space
modifier_map = {
    '.....O' : 0,
    '.O.OOO' : 1 
}

# braille -> letter
braille_letter_map = { b : l for l, b in letter_braille_map.items()}

# braille -> number
braille_number_map = { b : n for n, b in number_braille_map.items()}

'''
chunks a string into sections of 6 (with remainder)

returns a list
'''
def chunk_string(string):
    return list(string[0+i : 6 + i] for i in range(0, len(string), 6))

'''
checks if a given input string is in braille or not.
check for multiple of 6, validate each chunk of 6 to see if it exists in braille set
TODO: if the input includes '.', it is braille. "English" specification does not include '.' so can safely
assume all input containing '.' is valid braille input
'''
def is_braille(string):
    if len(string) % 6 != 0:
        return False
    chunks = chunk_string(string)
    for chunk in chunks:
        # 6 character chunk does not exist in the braille set
        if not (chunk in letter_braille_map.values()):
            return False
    return True

input_str = ' '.join(sys.argv[1:])

print(is_braille(input_str))