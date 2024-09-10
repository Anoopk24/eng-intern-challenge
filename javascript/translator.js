class Braille {

    static charToBraille_Map =new Map([
        ['a','O.....'],
        ['b','O.O...'],
        ['c','OO....'],
        ['d','OO.O..'],
        ['e','O..O..'],
        ['f','OOO...'],
        ['g','OOOO..'],
        ['h','O.OO..'],
        ['i','.OO...'],
        ['j','.OOO..'],
        ['k','O...O.'],
        ['l','O.O.O.'],
        ['m','OO..O.'],
        ['n','OO.OO.'],
        ['o', 'O..OO.'],
        ['p', 'OOO.O.'], 
        ['q', 'OOOOO.'], 
        ['r', 'O.OOO.'], 
        ['s', '.OO.O.'], 
        ['t', '.OOOO.'],
        ['u', 'O...OO'], 
        ['v', 'O.O.OO'], 
        ['w', '.OOO.O'], 
        ['x', 'OO..OO'], 
        ['y', 'OO.OOO'],
        ['z', 'O..OOO'], 
        ['1', 'O.....'], 
        ['2', 'O.O...'], 
        ['3', 'OO....'], 
        ['4', 'OO.O..'], 
        ['5', 'O..O..'],
        ['6', 'OOO...'], 
        ['7', 'OOOO..'], 
        ['8', 'O.OO..'], 
        ['9', '.OO...'], 
        ['0', '.OOO..'],
        ['space', '......'],
        ['capital', '.....O'],
        ['number', '.O.OOO'],
    ]);

    static brailleToChar_Map = new Map([
        ['O.....', 'a'], 
        ['O.O...', 'b'], 
        ['OO....', 'c'], 
        ['OO.O..', 'd'], 
        ['O..O..', 'e'],
        ['OOO...', 'f'], 
        ['OOOO..', 'g'], 
        ['O.OO..', 'h'], 
        ['.OO...', 'i'], 
        ['.OOO..', 'j'],
        ['O...O.', 'k'], 
        ['O.O.O.', 'l'], 
        ['OO..O.', 'm'], 
        ['OO.OO.', 'n'], 
        ['O..OO.', 'o'],
        ['OOO.O.', 'p'], 
        ['OOOOO.', 'q'], 
        ['O.OOO.', 'r'], 
        ['.OO.O.', 's'], 
        ['.OOOO.', 't'],
        ['O...OO', 'u'], 
        ['O.O.OO', 'v'], 
        ['.OOO.O', 'w'], 
        ['OO..OO', 'x'], 
        ['OO.OOO', 'y'],
        ['O..OOO', 'z'], 
        ['......', 'space'],
        ['.....O', 'capital'],
        ['.O.OOO', 'number']
    ]);

    static brailleToNumber_map = new Map([
        ['O.....', '1'], 
        ['O.O...', '2'], 
        ['OO....', '3'], 
        ['OO.O..', '4'], 
        ['O..O..', '5'],
        ['OOO...', '6'], 
        ['OOOO..', '7'], 
        ['O.OO..', '8'], 
        ['.OO...', '9'], 
        ['.OOO..', '0']
    ]);

    static isBraille(text){
        //check if the input text is braille
        return (/^[O. ]+$/.test(text));
    }

    static toBraille(text){
        let brailleText='';
        let isNumber=false;

        for(let char of text){
            if (char >= '0' && char <= '9'){
                //check for number
                if (!isNumber){
                    //first number
                    brailleText+=this.charToBraille_Map.get('number');
                    isNumber=true;
                }
                brailleText+=this.charToBraille_Map.get(char);
            }
        }
        return brailleText;
    }
}