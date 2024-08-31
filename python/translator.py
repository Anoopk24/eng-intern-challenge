#first step is to determine whether the String is Braille or English
#can do this by scanning for letters other than . or 0
#also, if it is Braille, then we need to validate that the input is divisible by 6
#will need to create 2 hashmaps. one will map english to braille, the other will map braille to english.

import sys

english_to_braille = {
    "a": "0.....",
    "b": "0.0...",
    "c": "00....",
    "d": "00.0..",
    "e": "0..0..",
    "f": "000...",
    "g": "0000..",
    "h": "0.00..",
    "i": ".00...",
    "j": ".000..",
    "k": "0...0.",
    "l": "0.0.0.",
    "m": "00..0.",
    "n": "00.00.",
    "o": "0..00.",
    "p": "000.0.",
    "q": "00000.",
    "r": "0.000.",
    "s": ".00.0.",
    "t": ".0000.",
    "u": "0...00",
    "v": "0.0.00",
    "w": ".000.0",
    "x": "00..00",
    "y": "00.000",
    "z": "0..000",
    "1": "0.....",
    "2": "0.0...",
    "3": "00....",
    "4": "00.0..",
    "5": "0..0..",
    "6": "000...",
    "7": "0000..",
    "8": "0.00..",
    "9": ".00...",
    "0": ".000..",
    ".": "..00.0",
    ",": "..0...",
    "?": "..0.00",
    "!": "..000.",
    ":": "..00..",
    ";": "..0.0.",
    "-": "....00",
    "/": ".0..0.",
    "<": ".00..0",
    ">": "0..00.",
    "(": "0.0..0",
    ")": ".0.00.",
    " ": "......"
}

#didn't map capital follows, decimal follows, and number follows

if len(sys.argv) != 1:
    print("Please pass only 1 argument")
    sys.exit(1)

input_string = sys.argv[0]
isBrail = True

for letter in input_string:
    if letter != "0" and letter != ".":
        isBrail = False
        break

if isBrail:
    pass
else:
    pass