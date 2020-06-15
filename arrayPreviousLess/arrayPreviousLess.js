function arrayPreviousLess(arr) {
  let index;
  for (let i = arr.length - 1; i >= 0; i--) {
    index = -1;
    for (let j = i - 1; j >= 0; j--) {
      if (arr[j] < arr[i]) {
        index = j;
        break;
      }
    }
    arr[i] = index;
  }
  return arr;
}
console.log(arrayPreviousLess([3, 5, 2, 4, 5]));
