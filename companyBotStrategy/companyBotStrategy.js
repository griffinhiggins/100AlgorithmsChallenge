function companyBotStrategy(X) {
  let sum = 0,
    i = 0,
    avg;
  X.forEach((e) => {
    if (e[1] > 0) {
      sum += e[0];
      i++;
    }
  });
  avg = Math.round((sum / i) * 10) / 10;
  return isNaN(avg) ? 0 : avg;
}

console.log(
  companyBotStrategy([
    [3, 1],
    [6, 1],
    [4, 1],
    [5, 1],
  ]),
);
console.log(
  companyBotStrategy([
    [4, 1],
    [4, -1],
    [0, 0],
    [6, 1],
  ]),
);
console.log(
  companyBotStrategy([
    [4, -1],
    [0, 0],
    [5, -1],
  ]),
);
