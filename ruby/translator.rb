# translator.rb

braille_alphabet = {
  "a" => "O.....", "b" => "O.O...", "c" => "OO....", "d" => "OO.O..",
  "e" => "O..O..", "f" => "OOO...", "g" => "OOOO..", "h" => "O.OO..",
  "i" => ".OO...", "j" => ".OOO..", "k" => "O...O.", "l" => "O.O.O.",
  "m" => "OO..O.", "n" => "OO.OO.", "o" => "O..OO.", "p" => "OOO.O.",
  "q" => "OOOOO.", "r" => "O.OOO.", "s" => ".OO.O.", "t" => ".OOOO.",
  "u" => "O...OO", "v" => "O.O.OO", "w" => ".OOO.O", "x" => "OO..OO",
  "y" => "OO.OOO", "z" => "O..OOO", " " => "......",
  "capital" => ".....O", "number" => ".O.OOO",
  "0" => ".OOO..", "1" => "O.....", "2" => "O.O...", "3" => "OO....",
  "4" => "OO.O..", "5" => "O..O..", "6" => "OOO...", "7" => "OOOO..",
  "8" => "O.OO..", "9" => ".OO..."
}

def english_to_braille(text, braille_alphabet)
  output = ""
  text.each_char do |char|
    if char =~ /[A-Z]/
      output += braille_alphabet["capital"] + braille_alphabet[char.downcase]
    elsif char =~ /\d/
      output += braille_alphabet["number"] + braille_alphabet[char]
    else
      output += braille_alphabet[char] || ''
    end
  end
  output
end

def braille_to_english(braille, braille_alphabet)
  reversed_alphabet = braille_alphabet.invert
  english = ""
  i = 0
  while i < braille.length
    current_symbol = braille[i, 6]
    if current_symbol == braille_alphabet["capital"]
      i += 6
      next_symbol = braille[i, 6]
      english << (reversed_alphabet[next_symbol] || '').upcase
    elsif current_symbol == braille_alphabet["number"]
      i += 6
      while i < braille.length && braille[i, 6] != braille_alphabet[" "]
        english << (reversed_alphabet[braille[i, 6]] || '')
        i += 6
      end
    else
      english << (reversed_alphabet[current_symbol] || '')
    end
    i += 6
  end
  english
end

input = ARGV[0]

if input =~ /^[O.]+$/
  puts braille_to_english(input, braille_alphabet)
else
  puts english_to_braille(input, braille_alphabet)
end
