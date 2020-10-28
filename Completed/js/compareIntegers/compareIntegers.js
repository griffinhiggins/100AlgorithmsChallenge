function compareIntegers(i, j) {
  i = parseInt(i);
  j = parseInt(j);
  return i > j ? 'greater' : i < j ? 'less' : 'equal';
}
console.log(compareIntegers('12', '23'));
console.log(compareIntegers('875', '799'));
console.log(compareIntegers('1000', '1000'));
