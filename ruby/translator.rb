$letters = {
    'a' => 'O.....',
    'b' => 'O.O...',
    'c' => 'OO....',
    'd' => 'OO.O..',
    'e' => 'O..O..',
    'f' => 'OOO...',
    'g' => 'OOOO..',
    'h' => 'O.OO..',
    'i' => '.OO...',
    'j' => '.OOO..',
    'k' => 'O...O.',
    'l' => 'O.O.O.',
    'm' => 'OO..O.',
    'n' => 'OO.OO.',
    'o' => 'O..OO.',
    'p' => 'OOO.O.',
    'q' => 'OOOOO.',
    'r' => 'O.OOO.',
    's' => '.OO.O.',
    't' => '.OOOO.',
    'u' => 'O...OO',
    'v' => 'O.O.OO',
    'w' => '.OOO.O',
    'x' => 'OO..OO',
    'y' => 'OO.OOO',
    'z' => 'O..OOO',
    'capital'   => '.....O',
    'number'    => '.O.OOO',
    'space' => '......',
}

$non_letters = {
    '.' => '..OO.O',
    ',' => '..O...',
    '?' => '..O.OO',
    '!' => '..OOO.',
    ':' => '..OO..',
    ';' => '..O.O.',
    '-' => '....OO',
    '/' => '.O..O.',
    '<' => '.OO..O',
    '>' => 'O..OO.',
    '(' => 'O.O..O',
    ')' => '.O.OO.',
}

$numbers = {
    '1' => 'O.....',
    '2' => 'O.O...',
    '3' => 'OO....',
    '4' => 'OO.O..',
    '5' => 'O..O..',
    '6' => 'OOO...',
    '7' => 'OOOO..',
    '8' => 'O.OO..',
    '9' => '.OO...',
    '0' => '.OOO..',
}

$braille_letters = $letters.invert
$braille_numbers = $numbers.invert
$braille_non_letters = $non_letters.invert

def translate_english_to_braille(word)
    result = ""
    flag_digit = false

    word.each_char do |char|
        # Check for capital letters
        if char.match?(/[A-Z]/)
            result += $letters['capital']
            result += $letters[char.downcase]
        
        # Check for digits
        elsif char.match?(/[0-9]/)
            if !flag_digit
                result += $letters['number']
                flag_digit = true
            end
            result += $numbers[char]
        
        # Check for lowercase letters
        elsif char.match?(/[a-z]/)
            result += $letters[char.downcase]
        
        # Check for non-letters
        elsif char.match?(/[.,?!:;\/<>()\-]/)
            result += $non_letters[char]
        
        # Check for spaces
        elsif char == ' '
            result += $letters['space']
            flag_digit = false
        end
    end

    return result
end

def translate_braille_to_english(word)
    result = ""
    flag_capital = false
    flag_digit = false

    word.chars.each_slice(6) do |slice|
        char = slice.join
        
        # update flags when seen
        if $braille_letters[char] == 'capital'
            flag_capital = true
        elsif $braille_letters[char] == 'number'
            flag_digit = true
        elsif $braille_letters[char] == 'space'
            result += ' '
            flag_digit = false
        
        # update the result based on the flags
        # add capital letters when seen
        elsif flag_capital == true  
            result += $braille_letters[char].upcase
            flag_capital = false

        # add numbers when seen
        elsif flag_digit == true
            result += $braille_numbers[char]
        # add letters or special characters when seen
        else 
            result += $braille_letters[char]
        end
    end
    return result
end

def main
    # check if the input is empty
    if ARGV.empty?
        puts 'Usage: ruby translator.rb <english or braille to be translated>'
        return
    end

    word = ARGV.join(' ')

    # check if the input is braille or english and print the translation
    if word.chars.all? { |char| ['.', 'O'].include?(char) }
        puts translate_braille_to_english(word)
    else 
        puts translate_english_to_braille(word)
    end
end

main
