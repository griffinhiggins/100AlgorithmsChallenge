function characterParity(c) {
  return Number.isNaN(parseInt(c))
    ? 'not a digit'
    : parseInt(c) % 2 == 0
    ? 'even'
    : 'odd';
}
console.log(characterParity('1'));
console.log(characterParity('2'));
console.log(characterParity('a'));
