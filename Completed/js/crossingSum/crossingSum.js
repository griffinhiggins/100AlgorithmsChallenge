let crossingSum = (arr, i, j) =>
  arr[i].reduce((t, i) => (t += i)) +
  arr.map((row, k) => (k != i ? row[j] : 0)).reduce((t, i) => (t += i));

console.log(
  crossingSum(
    [
      [1, 1, 1, 1],
      [2, 2, 2, 2],
      [3, 3, 3, 3],
    ],
    1,
    3,
  ),
);
