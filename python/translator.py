import sys

ENG_TO_BR= {
    "a": "O.....",
    "b": "O.O...",
    "c": "OO....",
    "d": "OO.O..",
    "e": "O..O..",
    "f": "OOO...",
    "g": "OOOO..",
    "h": "O.OO..",
    "i": ".OO...",
    "j": ".OOO..",
    "k": "O...O.",
    "l": "O.O.O.",
    "m": "OO..O.",
    "n": "OO.OO.",
    "o": "O..OO.",
    "p": "OOO.O.",
    "q": "OOOOO.",
    "r": "O.OOO.",
    "s": ".OO.O.",
    "t": ".OOOO.",
    "u": "O...OO",
    "v": "O.O.OO",
    "w": ".OOO.O",
    "x": "OO..OO",
    "y": "OO.OOO",
    "z": "O..OOO",
    " ": "......",
    "cap": ".....O",
    "num": ".O.OOO"
}

BR_TO_ENG = {v: k for k, v in ENG_TO_BR.items()}

def translate_br_to_eng(braille) -> str:
    english = ""

    capitalized = False
    number = False

    for i in range(0, len(braille), 6):
        curr = braille[i:i+6]
        curr_char = BR_TO_ENG[curr]
        
        if curr_char == "cap":
            capitalized = True
        elif curr_char == "num":
            number = True
        else:
            if capitalized:
                english += curr_char.upper()
                capitalized = False
            elif not capitalized and not number:
                english += curr_char
            elif number and curr_char != " ":
                english += str(ord(curr_char) - ord("a") + 1)
            elif number and curr_char == " ":
                english += " "
                number = False

    return english

def translate_en_to_br(english) -> str:
    braille = ""
    number = False
    for n in english:
        if n.isupper():
            braille += ENG_TO_BR["cap"]
            n = n.lower()
        if n.isdigit():
            if not number:
                braille += ENG_TO_BR["num"]
                number = True
            n = chr(ord("a") + int(n) - 1)
        if number and n == " ":
            number = False
        braille += ENG_TO_BR[n]

    return braille

def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    args = sys.argv[1:]
    user_input = " ".join(args)

    isBraile = True

    # Determine if the input is in Braille or English
    if len(user_input) % 6 != 0:
        isBraile = False

    for n in user_input:
        if n != "." and n != "O":
            isBraile = False
            break

    conversion = ""

    # Execute appropriate translation
    if isBraile:
        conversion = translate_br_to_eng(user_input)
    else:
        conversion = translate_en_to_br(user_input)

    print(conversion)

if __name__ == "__main__":
    main()
