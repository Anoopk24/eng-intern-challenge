RSpec.describe 'Braille Translator Script' do
  it 'outputs the correct string' do
    output = `ruby translator.rb Abc 123 xYz` # 'ruby translator.rb Abc 234 xYz' should be the corrected command for the given output
    expect(output.strip).to eq('.....OO.....O.O...OO...........O.OOOO.O...OO....OO.O........OO..OO.....OOO.OOOO..OOO')
  end
end