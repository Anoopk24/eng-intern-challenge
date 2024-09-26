# Braille to English mapping
BRAILLE_MAP = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 'f': 'OOO...',
    'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 'k': 'O...O.', 'l': 'O.O.O.',
    'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.',
    's': '.OO.O.', 't': '.OOOO.', 'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO',
    'y': 'OO.OOO', 'z': 'O..OOO', '0': '.O.OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....',
    '4': 'OO.O..', '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...'
}

# Special markers
CAPITAL_MARKER = '.....O'
NUMBER_MARKER = '.O.OOO'
SPACE = '......'

# Reverse the Braille map to get Braille to English mappings
ENGLISH_MAP = {v: k for k, v in BRAILLE_MAP.items()}

# Determine if input is Braille
def is_braille(input):
    return all(c in 'O.' for c in input)

# Translate English to Braille
def english_to_braille(text):
    result = []
    number_mode = False
    for char in text:
        if char.isdigit():
            if not number_mode:
                result.append(NUMBER_MARKER)
                number_mode = True
            result.append(BRAILLE_MAP[char])
        elif char == ' ':
            result.append(SPACE)
            number_mode = False
        elif char.isupper():
            result.append(CAPITAL_MARKER)
            result.append(BRAILLE_MAP[char.lower()])
            number_mode = False
        else:
            result.append(BRAILLE_MAP[char])
            number_mode = False
    return ''.join(result)

# Translate Braille to English
def braille_to_english(braille):
    result = []
    number_mode = False
    i = 0
    while i < len(braille):
        symbol = braille[i:i+6]
        if symbol == CAPITAL_MARKER:
            next_symbol = braille[i+6:i+12]
            result.append(ENGLISH_MAP[next_symbol].upper())
            i += 12
        elif symbol == NUMBER_MARKER:
            number_mode = True
            i += 6
        elif symbol == SPACE:
            result.append(' ')
            i += 6
        else:
            char = ENGLISH_MAP[symbol]
            if number_mode and char.isdigit():
                result.append(char)
            else:
                result.append(char)
            i += 6
    return ''.join(result)

# Main function to determine translation
def translator(input_text):
    if is_braille(input_text):
        print(braille_to_english(input_text))
    else:
        print(english_to_braille(input_text))

# Get input from command-line arguments
if __name__ == '__main__':
    import sys
    input_text = ' '.join(sys.argv[1:])
    translator(input_text)


