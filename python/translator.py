import sys

inputs = sys.argv[1:]
inputs = " ".join(inputs)
#print("Input: ", inputs)

dicts = {
    "A": "O.....",
    "B": "O.O...",
    "C": "OO....",
    "D": "OO.O..",
    "E": "O..O..",
    "F": "OOO...",
    "G": "OOOO..",
    "H": "O.OO..",
    "I": ".OO...",
    "J": ".OOO..",
    "K": "O...O.",
    "L": "O.O.O.",
    "M": "OO..O.",
    "N": "OO.OO.",
    "O": "O..OO.",
    "P": "OOO.O.",
    "Q": "OOOOO.",
    "R": "O.OOO.",
    "S": ".OO.O.",
    "T": ".OOOO.",
    "U": "O...OO",
    "V": "O.O.OO",
    "W": ".OOO.O",
    "X": "OO..OO",
    "Y": "OO.OOO",
    "Z": "O..OOO",
    "1": "O.....",
    "2": "O.O...",
    "3": "OO....",
    "4": "OO.O..",
    "5": "O..O..",
    "6": "OOO...",
    "7": "OOOO..",
    "8": "O.OO..",
    "9": ".OO...",
    "0": ".OOO..",
    "capital follows": ".....O",
    "number follows": ".O.OOO",
    "space": "......"
}

braille = {
    "O.....": "A",
    "O.O...": "B",
    "OO....": "C",
    "OO.O..": "D",
    "O..O..": "E",
    "OOO...": "F",
    "OOOO..": "G",
    "O.OO..": "H",
    ".OO...": "I",
    ".OOO..": "J",
    "O...O.": "K",
    "O.O.O.": "L",
    "OO..O.": "M",
    "OO.OO.": "N",
    "O..OO.": "O",
    "OOO.O.": "P",
    "OOOOO.": "Q",
    "O.OOO.": "R",
    ".OO.O.": "S",
    ".OOOO.": "T",
    "O...OO": "U",
    "O.O.OO": "V",
    ".OOO.O": "W",
    "OO..OO": "X",
    "OO.OOO": "Y",
    "O..OOO": "Z",
    ".....O": "capital follows",
    ".O.OOO": "number follows",
    "......": "space"
}

braille_num = {
    "O.....": "1",
    "O.O...": "2",
    "OO....": "3",
    "OO.O..": "4",
    "O..O..": "5",
    "OOO...": "6",
    "OOOO..": "7",
    "O.OO..": "8",
    ".OO...": "9",
    ".OOO..": "0"
}

def braille_check(text):
    if(len(text)%6 != 0):
        return False

    for i in range(0, len(text), 6):
        cur = text[i:i+6]
        if(cur not in braille and cur not in braille_num):
            #print(cur)
            return False
    
    return True

#print(braille_check(inputs))

if(braille_check(inputs) == False):
    #Input is an English sentence
    res = ""
    isNum = False

    for i in range(0, len(inputs)):
        if(inputs[i].isupper()):
            res += dicts["capital follows"]
            res += dicts[inputs[i]]
        elif(inputs[i].isdigit() and isNum==False):
            res += dicts["number follows"]
            res += dicts[inputs[i]]
            isNum = True
        elif(inputs[i].isspace()):
            res += dicts["space"]
            isNum = False
        else:
            res += dicts[inputs[i].upper()]
    
    print(res)

else:
    #Braille to English Translation

    res = ""
    isNum = False
    isCap = False

    for i in range(0, len(inputs), 6):
        cur = inputs[i:i+6]

        if(braille[cur] == "number follows"):
            isNum = True
        elif(braille[cur] == "capital follows"):
            isCap = True
        elif(braille[cur] == "space"):
            res += " "
            isNum = False
        elif(isCap == True):
            res += braille[cur]
            isCap = False
        elif(isNum == True):
            res += braille_num[cur]
        else:
            res += braille[cur].lower()

    print(res)
