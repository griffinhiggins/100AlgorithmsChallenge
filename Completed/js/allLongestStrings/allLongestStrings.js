function allLongestStrings(a) {
    let max = 0;
    a.forEach(e => {
        max = (e.length > max) ? e.length : max;
    });
    return a.filter(e => e.length == max);
}
console.log(allLongestStrings(["aba", "aa", "ad", "vcd", "aba"]));