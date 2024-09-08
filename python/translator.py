import sys


# Mapping from English letters and numbers to Braille symbols
english_to_braille_map = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
    'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
    'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
    'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
    'z': "O..OOO",
    '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..",
    '6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO..",
    ' ': "......",  # Space character
}

# Mapping from Braille symbols to English letters and numbers
braille_to_english_map = {
    "O.....": 'a', "O.O...": 'b', "OO....": 'c', "OO.O..": 'd', "O..O..": 'e',
    "OOO...": 'f', "OOOO..": 'g', "O.OO..": 'h', ".OO...": 'i', ".OOO..": 'j',
    "O...O.": 'k', "O.O.O.": 'l', "OO..O.": 'm', "OO.OO.": 'n', "O..OO.": 'o',
    "OOO.O.": 'p', "OOOOO.": 'q', "O.OOO.": 'r', ".OO.O.": 's', ".OOOO.": 't',
    "O...OO": 'u', "O.O.OO": 'v', ".OOO.O": 'w', "OO..OO": 'x', "OO.OOO": 'y',
    "O..OOO": 'z', "......": ' ',  # Braille for space
}

# Mapping for numbers (similar to letters 'a' to 'j', but in number mode)
braille_to_number_map = {
    "O.....": '1', "O.O...": '2', "OO....": '3', "OO.O..": '4', "O..O..": '5',
    "OOO...": '6', "OOOO..": '7', "O.OO..": '8', ".OO...": '9', ".OOO..": '0',
}

# Special Braille characters for flags like capitalization and numbers
special_braille_chars = {
    ".....O": "capital flag",  # Indicates the next letter is uppercase
    ".O.OOO": "number flag",   # Indicates the following characters are numbers
}

def convert_english_to_braille(text):
    """
    Converts an English text into a Braille string.
    Handles capital letters and number mode using special Braille indicators.
    """
    result = []
    in_number_mode = False

    for char in text:
        # If it's a capital letter, add the 'capital flag' before converting
        if 'A' <= char <= 'Z':
            result.append(".....O")
            char = char.lower()  # Convert to lowercase for translation

        # If it's a digit, activate number mode if not already in it
        if '0' <= char <= '9':
            if not in_number_mode:
                result.append(".O.OOO")  # Add 'number flag'
                in_number_mode = True
        else:
            in_number_mode = False  # Exit number mode when a non-digit is found

        # Get the Braille symbol for the character, defaulting to a space if not found
        braille = english_to_braille_map.get(char, "......")
        result.append(braille)

    return ''.join(result)

def convert_braille_to_english(braille_text):
    """
    Converts a Braille string back into English.
    Handles capital letters and number mode using special Braille indicators.
    """
    output = []
    in_capital_mode = False
    in_number_mode = False

    for i in range(0, len(braille_text), 6):
        braille_char = braille_text[i:i + 6]

        # Check for special Braille indicators (capital or number mode)
        if braille_char in special_braille_chars:
            mode = special_braille_chars[braille_char]
            if mode == "capital flag":
                in_capital_mode = True
            elif mode == "number flag":
                in_number_mode = True
            continue

        # Handle number mode
        if in_number_mode:
            if braille_char in braille_to_number_map:
                output.append(braille_to_number_map[braille_char])
            else:
                # Exit number mode if an invalid number is encountered
                in_number_mode = False
                i -= 6  # Re-check this Braille char after exiting number mode
        else:
            # Translate Braille to English letters, accounting for capital letters
            if braille_char in braille_to_english_map:
                char = braille_to_english_map[braille_char]
                if in_capital_mode:
                    output.append(char.upper())  # Convert to uppercase if needed
                    in_capital_mode = False
                else:
                    output.append(char)
            else:
                output.append(' ')  # Default to space if no matching Braille pattern found

    return ''.join(output)

def is_braille(text):
    """
    Determines if a given text is valid Braille by checking its length and characters.
    """
    # Braille input should have length divisible by 6 (each symbol is 6 characters)
    if len(text) % 6 != 0:
        return False

    # Verify that every 6-character chunk is a valid Braille symbol or special flag
    for i in range(0, len(text), 6):
        chunk = text[i:i + 6]
        if chunk not in braille_to_english_map and \
           chunk not in special_braille_chars and \
           chunk not in braille_to_number_map:
            return False

    return True

def main():
    """
    Takes input from the command line and determines whether to translate from English to Braille or vice versa.
    """
    if len(sys.argv) < 2:
        print("Please provide text to translate.")
        return

    # Combine all command line arguments into a single input string
    input_text = ' '.join(sys.argv[1:])

    # Determine if the input is Braille or English, then translate accordingly
    # if is_braille(input_text):
    #     output = convert_braille_to_english(input_text)
    #     if output:
    #         print(output)
    #     else:
    #         print("Invalid Braille input.")
    # else:
    #     output = convert_english_to_braille(input_text)
    #     if output:
    #         print(output)
    #     else:
    #         print("Invalid English input.")

if __name__ == "__main__":
    main()
