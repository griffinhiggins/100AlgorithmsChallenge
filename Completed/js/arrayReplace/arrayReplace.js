function arrayReplace(arr, find, rep) {
  return arr.map((e) => (e == find ? (e = rep) : e));
}
console.log(arrayReplace([1, 2, 1], 1, 3));
