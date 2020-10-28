function containsDuplicates(a) {
  a.sort();
  for (let i = 0, j = 1; j < a.length; i++, j++) {
    if (a[i] == a[j]) {
      return true;
    }
  }
  return false;
}
console.log(containsDuplicates([1, 2, 3, 1]));
console.log(containsDuplicates([3, 1]));
