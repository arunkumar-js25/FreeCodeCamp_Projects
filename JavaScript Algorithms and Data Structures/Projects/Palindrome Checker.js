/* palindrome("eye"); */
function palindrome(str) {
  const replaced = str.replace(/[^a-z0-9]/gi, '').toLowerCase();
  let len = replaced.length;
  let i= 0, j=len-1;
  while(j >=i ){
    if(replaced[i] != replaced[j]){
      return false;
    }
    i++;
    j--;
  }

  return true;
}

export { palindrome };