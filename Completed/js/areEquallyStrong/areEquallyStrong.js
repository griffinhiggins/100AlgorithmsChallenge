function areEquallyStrong(a0, a1, b0, b1) {
    return Math.max(a0, a1) == Math.max(b0, b1) && Math.min(a0, a1) == Math.min(b0, b1);
}

console.log(areEquallyStrong(10, 15, 15, 10))
console.log(areEquallyStrong(15, 10, 15, 10))
console.log(areEquallyStrong(15, 10, 15, 9))