function avoidObstacles(arr) {
  arr.sort();
  let i = 1,
    max = arr[arr.length - 1] + 1;
  while (i < max) {
    if (arr.every((e) => e % i != 0)) return i;
    i++;
  }
  return i;
}
console.log(avoidObstacles([5, 3, 6, 7, 9]));
console.log(avoidObstacles([1, 6]));
