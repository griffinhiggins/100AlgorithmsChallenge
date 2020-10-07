function chunkyMonkey(a, n) {
  let retArr = [],
    i,
    j;
  for (i = 0, j = n; j <= a.length; i += n, j += n) {
    retArr.push(a.slice(i, j));
  }
  if (i < a.length) {
    retArr.push(a.slice(i, a.length));
  }
  return retArr;
}
console.log(chunkyMonkey(['a', 'b', 'c', 'd'], 2));
console.log(chunkyMonkey([0, 1, 2, 3, 4, 5], 4));
