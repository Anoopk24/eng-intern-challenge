import sys

braille_map = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..', 
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..', 
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.', 
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.', 
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO', 
    'z': 'O..OOO', '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', 
    '5': 'O..O..', '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', 
    '0': '.OOO..', ' ': '......', '.': '..OO.O', ',': '..O...', '?': '..O.OO',
    '!': '..OO.O', ':': '...OO.', ';': '...O..', '-': '...O.O', '/': '..O..O',
    '(': '..OO..', ')': '..OOO.', 'capital': '.....O', 'number': '.O.OOO'
}

def translate_to_braille(text):
  result = []
  number_mode = False

  for char in text:
    
    if char.isupper():
      result.append(braille_map['capital'])
      char = char.lower()
    if char.isdigit() and number_mode == False:
      result.append(braille_map['number'])
      number_mode = True
    if char == ' ':
       number_mode = False

    result.append(braille_map.get(char, ''))
  return ''.join(result)

def translate_to_english(braille):
  pass


if __name__ == "__main__":
    input = sys.argv[1]
    
    # Determine if input is Braille or English
    if 'O' in input or '.' in input:
        print(translate_to_english(input))
    else:
        print(translate_to_braille(input))
