# Arya Patel
# Eng Intern Challenge Submission
# Sept 22, 2024

import sys

# definne constants for special symbols
CAPITAL = '.....O'
DECIMAL = '.O...O'
NUMBER_FOLLOWS = '.O.OOO'
SPACE = '......'

eng_to_braille = {
    'A': 'O.....',
    'B': 'O.O...',
    'C': 'OO....',
    'D': 'OO.O..',
    'E': 'O..O..',
    'F': 'OOO...',
    'G': 'OOOO..',
    'H': 'O.OO..',
    'I': '.OO...',
    'J': '.OOO..',
    'K': 'O...O.',
    'L': 'O.O.O.',
    'M': 'OO..O.',
    'N': 'OO.OO.',
    'O': 'O..OO.',
    'P': 'OOO.O.',
    'Q': 'OOOOO.',
    'R': 'O.OOO.',
    'S': '.OO.O.',
    'T': '.OOOO.',
    'U': 'O...OO',
    'V': 'O.O.OO',
    'W': '.OOO.O',
    'X': 'OO..OO',
    'Y': 'OO.OOO',
    'Z': 'O..OOO',
    'capital': CAPITAL,
    'decimal': DECIMAL,
    'number': NUMBER_FOLLOWS,
    'space': SPACE,
}

eng_to_num = {
    '1': 'O.....',
    '2': 'O.O...',
    '3': 'OO....',
    '4': 'OO.O..',
    '5': 'O..O..',
    '6': 'OOO...',
    '7': 'OOOO..',
    '8': 'O.OO..',
    '9': '.OO...',
    '0': '.OOO..'
}

eng_to_punctuation = {
    ',': '..OO.O',
    '.': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    '<': '.OO..O',
    '>': 'O..OO.',
    '(': 'O.O..O',
    ')': '.O.OO.',
}

braille_to_eng = {value: key for key, value in eng_to_braille.items()}
braille_to_num = {value: key for key, value in eng_to_num.items()}
braille_to_punctuation = {value: key for key, value in eng_to_punctuation.items()}

def translate():
    # if we have no arguments output a blank statement back to the user
    if len(sys.argv) < 2:
        print('')
        return

    # collect the sentence(s) we will be translating
    str_to_translate = ' '.join(sys.argv[1:])

    # initilize a few starting variables 
    length = len(str_to_translate)
    idx, translation, in_number_mode = 0, "", False

    # Convert from English to Braille 
    if isEnglish(str_to_translate):
        while idx < length:
            char_to_translate = str_to_translate[idx]

            # for spaces
            if char_to_translate == ' ':
                in_number_mode = False # if in number mode it will now be false, if we aren't in number mode it stays false
                translation += SPACE

            # for a capital letter
            elif char_to_translate.isupper():
                in_number_mode = False
                translation += CAPITAL + eng_to_braille[char_to_translate]

            # for a number
            elif char_to_translate.isdigit():
                if not in_number_mode:
                    in_number_mode = True # enter number mode
                    translation += NUMBER_FOLLOWS # add the number follows symbol
                translation += eng_to_num[char_to_translate] 

            # for a decimal point within numbers
            elif char_to_translate == '.':
                if in_number_mode:
                    translation += DECIMAL + eng_to_punctuation['.'] # add the decimal follows symbol
                else:
                    translation += eng_to_punctuation['.']

            # for a lowercase letter
            elif char_to_translate.islower():
                in_number_mode = False
                translation += eng_to_braille[char_to_translate.upper()]

            # for a punctuation mark
            elif char_to_translate in eng_to_punctuation:
                in_number_mode = False  
                translation += eng_to_punctuation[char_to_translate]

            idx += 1

        # Convert from Braille to English
    else:
        while idx < length:
            char_to_translate = str_to_translate[idx : idx + 6]

            # for a space
            if char_to_translate == SPACE:
                translation += ' '

            # for a capital letter
            elif char_to_translate == CAPITAL_FOLLOWS:
                idx += 6
                char_to_translate = str_to_translate[idx:idx + 6]
                translation += (braille_to_eng[char_to_translate]).upper()

            # for a decimal follows symbol
            # assumption: the decimal follows symbol is for numbers only (ie. 123.45 would have a decimal follows symbol after the digit '3' followed by a decimal and then the rest of the numbers)
            elif char_to_translate == DECIMAL_FOLLOWS:
                idx += 6
                translation += '.'

            # for a number
            elif char_to_translate == NUMBER_FOLLOWS:
                in_number_mode = True  # enter number mode
                idx += 6
                while idx + 6 <= length:
                    char_to_translate = str_to_translate[idx:idx + 6]
                    if char_to_translate == SPACE:
                        in_number_mode = False  
                        translation += braille_to_eng[char_to_translate]
                        break
                    # handle decimal points while still in number mode
                    elif char_to_translate == DECIMAL_FOLLOWS: 
                        idx += 6
                        translation += '.'
                    else:
                        translation += braille_to_num[char_to_translate]
                    idx += 6

            # for regular English letters
            elif braille_to_eng[char_to_translate]:
                translation += (braille_to_eng[char_to_translate]).lower()
            
            # for punctuation marks
            else:
                translation += braille_to_punctuation[char_to_translate]
            
            idx += 6
    
    print(translation)
    return 0

# Check if the string is English or Braille
def isEnglish(str_to_translate):
    for char in str_to_translate:
        if char == ' ':
            continue
        elif char != 'O' and char != '.':
            return True
    return False

if __name__ == "__main__":
    translate()
