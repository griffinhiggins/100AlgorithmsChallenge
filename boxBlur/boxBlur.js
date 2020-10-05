function boxBlur(img) {
  img = [].concat(...img);
  return [[Math.floor(img.reduce((i, j) => i + j) / img.length)]];
}

console.log(
  boxBlur([
    [1, 1, 1],
    [1, 7, 1],
    [1, 1, 1],
  ]),
);
