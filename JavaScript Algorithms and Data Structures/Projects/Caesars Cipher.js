/*
Caesars Cipher
One of the simplest and most widely known ciphers is a Caesar cipher, also known as a shift cipher. 
In a shift cipher the meanings of the letters are shifted by some set amount.
A common modern use is the ROT13 cipher, where the values of the letters are shifted by 13 places. Thus A ↔ N, B ↔ O and so on.
Write a function which takes a ROT13 encoded string as input and returns a decoded string.
All letters will be uppercase. Do not transform any non-alphabetic character (i.e. spaces, punctuation), but do pass them on.

rot13("SERR PBQR PNZC");
*/

function rot13(str) {
  let newStr="";
  for(let i=0;i< str.length;i++){
    let asciiVal = str.charCodeAt(i);
    if(asciiVal >= 65 && asciiVal<=90){
      asciiVal+=13;
      if(asciiVal > 90){
        asciiVal = 64 + (asciiVal-90);
      }
      newStr += String.fromCharCode(asciiVal);
    }
    else{
      newStr += str[i];
    }
  }
  return newStr;
}

export { rot13 };