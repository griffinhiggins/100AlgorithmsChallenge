function addBorder(a) {
    let r = a.length,
        c = a[0].length,
        str = "*".repeat(c + 2);
    for (let i = 0; i < r; i++) {
        a[i] = "*".concat(a[i], "*")
    };
    a.unshift(str);
    a.push(str);
    return a
}
console.log(addBorder(["a"]));
console.log(addBorder(["abc", "ded"]));