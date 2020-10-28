function covertString(s, t) {
  for (let i = 0, j = 0; i < s.length; i++) {
    if (s[i] == t[j]) j++;
    if (j == t.length) return true;
  }
  return false;
}

console.log(covertString('ceoydefthf5iyg5h5yts', 'codefights'));
console.log(covertString('addbyca', 'abcd'));
