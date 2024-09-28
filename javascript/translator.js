const brailleMap = {
    'A': 'O.....', 'B': 'O.O...', 'C': 'OO....', 'D': 'OO.O..', 'E': 'O..O..',
    'F': 'OOO...', 'G': 'OOOO..', 'H': 'O.OO..', 'I': '.OO...', 'J': '.OOO..',
    'K': 'O...O.', 'L': 'O.O.O.', 'M': 'OO..O.', 'N': 'OO.OO.', 'O': 'O..OO.',
    'P': 'OOO.O.', 'Q': 'OOOOO.', 'R': 'O.OOO.', 'S': '.OO..O', 'T': '.OOO.O',
    'U': 'O...OO', 'V': 'O.O.OO', 'W': '.OOO.O', 'X': 'OO..OO', 'Y': 'OO.OOO',
    'Z': 'O..OOO', ' ': '......',
    '1': '.O.....', '2': '.O.O...', '3': '.OO....', '4': '.OO.O..', '5': '.O..O..',
    '6': '.OOO...', '7': '.OOOO..', '8': '.O.OO..', '9': '..OO...', '0': '..OOO..',
};

function translate(input) {
    let output = '';
    const isBraille = input.split('').every(char => char === 'O' || char === '.');

    if (isBraille) {
        // Translate from Braille to English
        const brailleChars = input.match(/.{1,6}/g);
        for (const brailleChar of brailleChars) {
            const englishChar = Object.keys(brailleMap).find(key => brailleMap[key] === brailleChar);
            output += englishChar ? englishChar : '?'; // Handle unknown Braille characters
        }
    } else {
        // Translate from English to Braille
        const upperInput = input.toUpperCase();
        for (const char of upperInput) {
            if (brailleMap[char]) {
                output += brailleMap[char]; // Add corresponding Braille
            } else {
                output += '......'; // For any unknown characters
            }
        }
    }
    return output;
}

// Get input from command line
const input = process.argv.slice(2).join(' ') || '';
console.log(translate(input));