function almostIncreasingSequence(a) {
    let flag = false;
    for (let i = 0; i < a.length - 1; i++) {
        if (flag) {
            return false;
        } else if (a[i] >= a[i + 1]) {
            flag = true;
        }
    }
    return true
}

console.log(almostIncreasingSequence([1, 3, 1, 2]))
console.log(almostIncreasingSequence([1, 3, 2]))