let chessBoardCellColor = (a, b) =>
  a.charCodeAt(0) % 2 == b.charCodeAt(0) % 2 &&
  parseInt(a[1]) % 2 == parseInt(b[1]) % 2;

console.log(chessBoardCellColor('A1', 'C3'));
console.log(chessBoardCellColor('A1', 'H3'));
