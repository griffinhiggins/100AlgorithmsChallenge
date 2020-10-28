confirmEnding = (i, j) => i.substr(i.length - j.length, i.length) == j;

console.log(confirmEnding('Abstraction', 'action'));
console.log(confirmEnding('Open sesame', 'pen'));
