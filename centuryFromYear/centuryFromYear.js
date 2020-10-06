let centuryFromYear = (y) =>
  y % 100 ? Math.floor(y / 100) + 1 : Math.floor(y / 100);

console.log(centuryFromYear(200));
