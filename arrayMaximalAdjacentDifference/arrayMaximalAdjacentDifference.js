function arrayMaximalAdjacentDifference(arr) {
  let diff,
    max = 0;
  for (let i = 0; i < arr.length - 1; i++) {
    diff = Math.abs(arr[i] - arr[i + 1]);
    if (diff > max) max = diff;
  }
  return max;
}

console.log(arrayMaximalAdjacentDifference([2, 4, 1, 0]));
