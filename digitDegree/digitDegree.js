function digitDegree(n) {
  let sum = 0;
  while (Math.floor(n / 10) > 0) {
    n = n
      .toString()
      .split('')
      .map((i) => parseInt(i))
      .reduce((s, i) => (s += i));
    sum++;
  }
  return sum;
}

console.log(digitDegree(5));
console.log(digitDegree(10));
console.log(digitDegree(91));
