let caseInsensitivePalindrome = (s) =>
  s.toLowerCase() == s.toLowerCase().split('').reverse().join('');

console.log(caseInsensitivePalindrome('AaBaa'));
console.log(caseInsensitivePalindrome('abac'));
