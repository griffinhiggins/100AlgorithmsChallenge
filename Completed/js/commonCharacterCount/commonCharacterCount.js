function commonCharacterCount(s1, s2) {
  let counter = 0,
    foundIndex;

  s1 = s1.split('');
  s2 = s2.split('');

  if (s2.length < s1.length) {
    temp = s1;
    s1 = s2;
    s2 = s1;
  }

  s1.forEach((e) => {
    foundIndex = s2.indexOf(e, 0);
    if (foundIndex >= 0) {
      counter++;
      s2.splice(foundIndex, 1);
    }
  });

  return counter;
}
console.log(commonCharacterCount('aabcc', 'adcaa'));
