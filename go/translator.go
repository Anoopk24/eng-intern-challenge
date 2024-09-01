package main

import (
	"fmt"
	"os"
	"strings"
)

// Maps for translation
var englishToBraille = map[rune]string{
	'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..", 'e': "O..O..",
	'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..", 'i': ".OO...", 'j': ".OOO..",
	'k': "O...O.", 'l': "O.O.O.", 'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.",
	'p': "OOO.O.", 'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
	'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO", 'y': "OO.OOO",
	'z': "O..OOO",
	'1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..", '5': "O..O..",
	'6': "OOO...", '7': "OOOO..", '8': "O.OO..", '9': ".OO...", '0': ".OOO..",
	' ': "......",
	'.': "..OO.O", ',': ".O....", '?': "..O.OO", '!': "..OOO.", ':': "..OO..",
	';': "..0.0.", '-': "....00", '/': ".0..0.", '<': ".00..0", '>': "0..00.",
	'(': "0.0..0", ')': ".0.00.",
}

var brailleToEnglish = map[string]rune{
	"O.....": 'a', "O.O...": 'b', "OO....": 'c', "OO.O..": 'd', "O..O..": 'e',
	"OOO...": 'f', "OOOO..": 'g', "O.OO..": 'h', ".OO...": 'i', ".OOO..": 'j',
	"O...O.": 'k', "O.O.O.": 'l', "OO..O.": 'm', "OO.OO.": 'n', "O..OO.": 'o',
	"OOO.O.": 'p', "OOOOO.": 'q', "O.OOO.": 'r', ".OO.O.": 's', ".OOOO.": 't',
	"O...OO": 'u', "O.O.OO": 'v', ".OOO.O": 'w', "OO..OO": 'x', "OO.OOO": 'y',
	"O..OOO": 'z',
	"......": ' ',
}

// Mapping for numbers, identical to the first ten letters a-j but used when number mode is on
var brailleToNumbers = map[string]rune{
	"O.....": '1', "O.O...": '2', "OO....": '3', "OO.O..": '4', "O..O..": '5',
	"OOO...": '6', "OOOO..": '7', "O.OO..": '8', ".OO...": '9', ".OOO..": '0',
}

// Mapping for decimals, also using the first ten letters a-j but in decimal mode
var brailleToDecimals = map[string]rune{
	"..OO.O": '.', ".O....": ',', "..O.OO": '?', "..OOO.": '!', "..OO..": ':',
	"..0.0.": ';', "....00": '-', ".0..0.": '/', ".00..0": '<', "0..00.": '>',
	"0.0..0": '(', ".0.00.": ')',
}

// Special characters for capitalization, numbers, and decimals
var brailleSpecialCharacters = map[string]string{
	".....O": "capital follows", // Capital follows
	".O.OOO": "number follows",  // Number follows
	".O...O": "decimal follows", // Decimal follows
}

// translateToBraille converts an English string to Braille
func translateToBraille(input string) string {
	var result strings.Builder
	numberMode := false
	decimalMode := false

	for i := 0; i < len(input); i++ {
		char := rune(input[i])

		// Handle capital letters
		if char >= 'A' && char <= 'Z' {
			// Add Braille code for capital follows
			result.WriteString(".....O")
			char = char + 32 // Convert to lowercase
		}

		// Handle numbers
		if char >= '0' && char <= '9' {
			if !numberMode {
				// Add Braille code for number follows
				result.WriteString(".O.OOO")
				numberMode = true
			}
		} else {
			// Reset number mode on non-number characters
			numberMode = false
		}

		// Handle decimals
		if char == '.' {
			if !decimalMode {
				// Add Braille code for decimal follows
				result.WriteString(".O...O")
				decimalMode = true
			}
		} else {
			// Reset decimal mode on non-decimal characters
			decimalMode = false
		}

		// Translate the current character to Braille
		if braille, ok := englishToBraille[char]; ok {
			result.WriteString(braille)
		} else {
			result.WriteString("......") // Default to space for unknown characters
		}
	}

	return result.String()
}

// translateToEnglish converts a Braille string to English
func translateToEnglish(input string) string {
	var result strings.Builder
	capitalMode := false
	numberMode := false
	decimalMode := false

	for i := 0; i < len(input); i += 6 {
		brailleChar := input[i : i+6]

		if mode, ok := brailleSpecialCharacters[brailleChar]; ok {
			switch mode {
			case "capital follows":
				capitalMode = true
			case "number follows":
				numberMode = true
			case "decimal follows":
				decimalMode = true
			}
			continue
		}

		if numberMode {
			// Translate as number
			if number, ok := brailleToNumbers[brailleChar]; ok {
				result.WriteRune(number)
			} else {
				// If a non-number character is encountered, reset number mode
				numberMode = false
				i -= 6 // Re-process this character in non-number mode
			}
		} else if decimalMode {
			// Translate as decimal
			if decimal, ok := brailleToDecimals[brailleChar]; ok {
				result.WriteRune(decimal)
			}
			decimalMode = false // Reset decimal mode after one character
		} else {
			// Translate as letter
			if english, ok := brailleToEnglish[brailleChar]; ok {
				if capitalMode {
					result.WriteRune(english - 32) // Convert to uppercase
					capitalMode = false
				} else {
					result.WriteRune(english)
				}
			} else {
				result.WriteRune(' ') // Default to space for unknown Braille patterns
			}
		}
	}

	return result.String()
}

// isBraille checks if the input string is in Braille format
func isBraille(input string) bool {
	return strings.ContainsAny(input, "O.")
}

func main() {
	if len(os.Args) < 2 {
		fmt.Println("Please provide a string to translate.")
		return
	}

	// Combine all arguments into a single input string
	input := strings.Join(os.Args[1:], " ")

	if isBraille(input) {
		output := translateToEnglish(input)
		if output == "" {
			fmt.Println("Invalid Braille input.")
		} else {
			fmt.Println(output)
		}
	} else {
		output := translateToBraille(input)
		if output == "" {
			fmt.Println("Invalid English input.")
		} else {
			fmt.Println(output)
		}
	}
}
