const BRAILLE_DICT_ALPHA = {
  "O.....": "a",
  "O.O...": "b",
  "OO....": "c",
  "OO.O..": "d",
  "O..O..": "e",
  "OOO...": "f",
  "OOOO..": "g",
  "O.OO..": "h",
  ".OO...": "i",
  ".OOO..": "j",
  "O...O.": "k",
  "O.O.O.": "l",
  "OO..O.": "m",
  "OO.OO.": "n",
  "O..OO.": "o",
  "OOO.O.": "p",
  "OOOOO.": "q",
  "O.OOO.": "r",
  ".O.OO.": "s",
  ".OOOO.": "t",
  "O...OO": "u",
  "O.O.OO": "v",
  ".OOO.O": "w",
  "OO..OO": "x",
  "OO.OOO": "y",
  "O..OOO": "z",
  "......": " ",
};

const BRAILLE_DICT_NUM = {
  "O.....": "1",
  "O.O...": "2",
  "OO....": "3",
  "OO.O..": "4",
  "O..O..": "5",
  "OOO...": "6",
  "OOOO..": "7",
  "O.OO..": "8",
  ".OO...": "9",
  ".OOO..": "0",
};

const ALPHA_DICT_BRAILLE = {
  a: "O.....",
  b: "O.O...",
  c: "OO....",
  d: "OO.O..",
  e: "O..O..",
  f: "OOO...",
  g: "OOOO..",
  h: "O.OO..",
  i: ".OO...",
  j: ".OOO..",
  k: "O...O.",
  l: "O.O.O.",
  m: "OO..O.",
  n: "OO.OO.",
  o: "O..OO.",
  p: "OOO.O.",
  q: "OOOOO.",
  r: "O.OOO.",
  s: ".O.OO.",
  t: ".OOOO.",
  u: "O...OO",
  v: "O.O.OO",
  w: ".OOO.O",
  x: "OO..OO",
  y: "OO.OOO",
  z: "O..OOO",
  " ": "......",
};

const NUM_DICT_BRAILLE = {
  1: "O.....",
  2: "O.O...",
  3: "OO....",
  4: "OO.O..",
  5: "O..O..",
  6: "OOO...",
  7: "OOOO..",
  8: "O.OO..",
  9: ".OO...",
  0: ".OOO..",
};

const brailleToAlpha = (msg) => {
  let out = "";
  let numMode = false;
  for (let i = 6; i <= msg.length; i += 6) {
    const cur = msg.substring(i - 6, i);
    if (numMode) {
      if (cur === "......") {
        out += " ";
        numMode = false;
      } else {
        out += BRAILLE_DICT_NUM[cur];
      }
    } else if (cur === ".....O") {
      i += 6;
      const nextChar = BRAILLE_DICT_ALPHA[msg.substring(i - 6, i)];
      out += nextChar.toUpperCase();
    } else if (cur === ".O.OOO") {
      numMode = true;
    } else {
      out += BRAILLE_DICT_ALPHA[cur];
    }
  }
  return out;
};

const alphaToBraille = (msg) => {
  let out = "";
  let numMode = false;
  for (let i = 0; i < msg.length; i++) {
    if (numMode) {
      if (msg[i] === " ") {
        out += "......";
        numMode = false;
      } else {
        out += NUM_DICT_BRAILLE[msg[i]];
      }
    } else if (!isNaN(parseInt(msg[i]))) {
      numMode = true;
      out += ".O.OOO";
      out += NUM_DICT_BRAILLE[msg[i]];
    } else if (msg[i] === msg[i].toUpperCase() && msg[i] != " ") {
      out += ".....O";
      out += ALPHA_DICT_BRAILLE[msg[i].toLowerCase()];
    } else {
      out += ALPHA_DICT_BRAILLE[msg[i]];
    }
  }
  return out;
};

const translator = () => {
  const args = process.argv;
  args.shift();
  args.shift();
  if (args.length === 0) {
    console.log("");
    return;
  }
  const msg = args.join(" ");
  let out = "";
  if (msg[0] === ".") {
    out = brailleToAlpha(msg);
  } else {
    out = alphaToBraille(msg);
  }
  console.log(out);
};

translator();
