function candies(n, m) {
  return Math.floor(m - (m % n));
}
console.log(candies(3, 10));
console.log(candies(31, 100));
