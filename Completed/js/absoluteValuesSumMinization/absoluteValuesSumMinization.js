function absoluteValuesSumMinimization(a){
    return (a.length % 2) ? a[Math.floor(a.length / 2)] : a[a.length / 2 - 1]
}

console.log(absoluteValuesSumMinimization([2, 4, 7]));
console.log(absoluteValuesSumMinimization([2, 4, 6, 7]));
console.log(absoluteValuesSumMinimization([2, 4, 6, 6, 7]));
console.log(absoluteValuesSumMinimization([2, 4, 6, 6, 7, 8]));