let checkPalindrome = (s) => checkPalindromeHelper(s, 0, s.length - 1);

function checkPalindromeHelper(s, i, j) {
  if (i >= j) {
    return true;
  } else if (s[i] != s[j]) {
    return false;
  } else {
    return checkPalindromeHelper(s, i + 1, j - 1);
  }
}

console.log(checkPalindrome('aabaa'));
console.log(checkPalindrome('abac'));
console.log(checkPalindrome('a'));
