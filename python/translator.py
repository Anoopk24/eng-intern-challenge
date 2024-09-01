from translators.english_to_braille_translator_class import *
from translators.braille_to_english_translator_class import *
import sys

def translate(input_string: str) -> str:
    # Deterine whether we are translating from english or braille
    if len(input_string) % 6 == 0 and all(c in ".O" for c in input_string) :
        # Case 1: We are working with braille data
        translator = BrailleToEnglishTranslator(input_string)
    else:
        translator = EnglishToBrailleTranslator(input_string)
    return translator.translate()


if __name__ == "__main__":
    print(translate(" ".join(sys.argv[1:])))