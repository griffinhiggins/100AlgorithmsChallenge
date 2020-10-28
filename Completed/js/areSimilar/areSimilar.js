function areSimilar(a, b) {
    let flag = false,
        len = a.length;
    for (let i = 0; i < len; i++) {
        if (a[i] != b[i]) {
            if (i == len || flag) {
                return false
            }
            if (a[i + 1] == b[i]) {
                swap(a, i, i + 1);
            } else if (a[i] == b[i + 1]) {
                swap(b, i, i + 1);
            }
            flag = true;
        }
    }
    return true
}
let swap = (a, i, j) => {
    let temp = a[i];
    a[i] = a[j];
    a[j] = temp;
}

console.log(areSimilar([1, 2, 3], [1, 2, 3]));
console.log(areSimilar([1, 2, 3], [2, 1, 3]));
console.log(areSimilar([1, 2, 2], [2, 1, 1]));
console.log(areSimilar([1, 3, 2, 1], [3, 1, 2, 1]));
console.log(areSimilar([1, 3, 2, 1], [3, 1, 1, 2]));