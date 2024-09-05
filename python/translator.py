import sys

# To accomplish this task, will need to do following things:
#   Create a dictionaries that can convert a single char/segment from braille to alphabet and vice versa
#   Create a function that can detect whether the input string is in braille or in alphanumerics
#   Create functions that can convert the strings via the dictionaries
#   Grab the argument and then push it through the previous functions to return a final string.

# Dictionaries will be generated by looping through arrays containing braille, alphabetical, and numerical characters.
alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    " ",
]
braille = [
    "O.....",
    "O.O...",
    "OO....",
    "OO.O..",
    "O..O..",
    "OOO...",
    "OOOO..",
    "O.OO..",
    ".OO..",
    ".OOO..",
    "O...O.",
    "O.O.O.",
    "OO..O.",
    "OO.OO.",
    "O..OO.",
    "OOO.O.",
    "OOOOO.",
    "O.OOO.",
    ".OO.O.",
    ".OOOO.",
    "O...OO",
    "O.O.OO",
    ".OOO.O",
    "OO..OO",
    "OO.OOO",
    "O..OOO",
    "......",
]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

alphabet_to_braille = {}
braille_to_alphabet = {}
numbers_to_braille = {}
braille_to_numbers = {}

for i in range(len(alphabet)):
    alphabet_to_braille[alphabet[i]] = braille[i]
    braille_to_alphabet[braille[i]] = alphabet[i]

# Braille system has 1 -> 0 with the same six dot formation as A -> J - Thus, we can just reuse the first dict and loop through it.
for i in range(len(numbers)):
    numbers_to_braille[numbers[i]] = braille[i]
    braille_to_numbers[braille[i]] = numbers[i]

# Will need a final dict to check to if characters are numerical or need to be capitalized.
alpha_modes = {"capitalize": ".....O", "numerize": ".O.OOO"}


def is_braille(input):
    # Braille strings should exist in multiples of six.
    if len(input) % 6 != 0:
        return False
    # Additionally, braille strings should only consist of 'O' or '.'
    allowed = set("O.")
    if not set(input).issubset(allowed):
        return False
    # If other checks pass, string is braille.
    return True


def convert_to_braille(input):
    res = ""
    number_flag = False
    for char in input:
        if char.isdigit():
            # If number_flag hasn't yet been set been set to true, do so and then insert the numerize braille symbol.
            if not number_flag:
                number_flag = True
                res += alpha_modes["numerize"]
            res += numbers_to_braille[char]
            continue
        # If char is a space, then number_flag should be turned off.
        if char == " ":
            number_flag = False
        if char.isupper():
            res += alpha_modes["capitalize"]
            # Need to convert char to lowercase so the key can be found in the dictionary.
            char = char.lower()
        res += alphabet_to_braille[char]

    return res


def convert_to_alphanumerics(input):
    res = ""
    # As the string must be multiple of six, split the string into an array so each character can be easily parsed
    split = [input[i : i + 6] for i in range(0, len(input), 6)]
    number_flag = False
    capital_flag = False
    for segment in split:
        if segment == alpha_modes["numerize"]:
            number_flag = True
            continue
        elif segment == alpha_modes["capitalize"]:
            capital_flag = True
            continue

        # Check if space - if a space, turn off the number flag and then insert segment then continue.
        if segment == alphabet_to_braille[" "]:
            number_flag = False
            res += braille_to_alphabet[segment]
            continue

        # If the number flag is on, treat segment as a number and append, then continue.
        if number_flag:
            res += braille_to_numbers[segment]
            continue

        # If all other checks allow to pass to this point, segment must be a character - check for capitalization then insert into result.
        insertion = braille_to_alphabet[segment]
        if capital_flag:
            insertion = insertion.upper()
            capital_flag = False
        res += insertion

    return res


if __name__ == "__main__":
    # Need to get the arguments excluding the first, and then turn the arguments into one coherent string.
    args = sys.argv[1:]
    input = " ".join(args)

    # Check if the input string is in braille - if so, convert to alphanumerics. Otherwise, convert the string to braille.
    if is_braille(input):
        print(convert_to_alphanumerics(input))
    else:
        print(convert_to_braille(input))
