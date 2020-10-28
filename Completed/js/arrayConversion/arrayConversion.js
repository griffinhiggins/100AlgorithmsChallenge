function arrayConversion(arr) {
    let isOdd = true,
        retArr;
    while (arr.length > 1) {
        retArr = [];
        for (let i = 0; i < arr.length; i += 2) {
            retArr.push((isOdd) ? arr[i] + arr[i + 1] : arr[i] * arr[i + 1]);
        }
        arr = retArr;
        isOdd = !isOdd;
    }
    return arr[0]
}

console.log(arrayConversion([1]));
console.log(arrayConversion([1, 2]));
console.log(arrayConversion([1, 2, 3, 4, 5, 6, 7, 8]));