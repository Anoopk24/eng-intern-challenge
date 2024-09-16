
import sys

alphabet = {
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
    'cf': '.....O',
    'df': '.O...O',
    'nf': '.O.OOO',
    '.': '..OO.O',
    ',': '..O...',
    '?': '..O.OO',
    '!': '..OOO.',
    ':': '..OO..',
    ';': '..O.O.',
    '-': '....OO',
    '/': '.O..O.',
    ')': '.O.OO.',
    '(': 'O.O..O',
    ' ': '......'
}

braille_alphabet = {
    'O.....': 'a',
    'O.O...': 'b',
    'OO....': 'c',
    'OO.O..': 'd',
    'O..O..': 'e',
    'OOO...': 'f',
    'OOOO..': 'g',
    'O.OO..': 'h',
    '.OO...': 'i',
    '.OOO..': 'j',
    'O...O.': 'k',
    'O.O.O.': 'l',
    'OO..O.': 'm',
    'OO.OO.': 'n',
    'O..OO.': 'o',
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
    'O.....': '1',
    'O.O...': '2', 
    'OO....': '3',
    'OO.O..': '4',
    'O..O..': '5',
    'OOO...': '6',
    'OOOO..': '7',
    'O.OO..': '8', 
    '.OO...': '9', 
    '.OOO..': '0', 
    '.....O': 'cf',
    '.O...O': 'df',
    '.O.OOO': 'nf',
    '..OO.O': '.',
    '..O...': ',',
    '..O.OO': '?',
    '..OOO.': '!',
    '..OO..': ':',
    '..O.O.': ';',
    '....OO': '-',
    '.O..O.': '/',
    '.O.OO.': ')',
    'O.O..O': '(',
    '......': ' '
}


def braille_translator(braille):
  segments = []
  word = ''
  for i in range(0, len(braille), 6):
    segment = braille[i:i + 6]
    segments.append(segment)
  
  index = 0
  while index < len(segments):
    if braille_alphabet[segments[index]] == 'cf':
      if index + 1 < len(segments):
        word += braille_alphabet[segments[index + 1]].upper()
        index += 2 
      else:
        index += 1
    else:
      word += braille_alphabet[segments[index]]
      index += 1
  print(word)
  return

def word_translator(string):
  braille = ''
  first_number = False
  for letter in string:

    if letter.isupper():
      braille += alphabet['cf']
      braille += alphabet[letter.lower()]

    elif letter.isdigit():
      if not first_number:
        braille += alphabet['nf']
        first_number = True
      braille += alphabet[letter]

    elif letter == ' ':
      braille += alphabet[' ']
      first_number = False

    else:
      braille += alphabet[letter]
  print(string)
  print(braille)
  print(len(braille))
  return braille
    
def translator(argument):
    braille_char = ['.', 'O']
    if all(letter in braille_char for letter in argument):
        return braille_translator(argument) 
    else:
        return word_translator(argument)

    
if __name__ == '__main__':
  argument = ' '.join(sys.argv[1:])
  translator(argument)