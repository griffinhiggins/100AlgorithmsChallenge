//STRING WAY
let addTwoDigitsStr = (n) => n.toString().split("").reduce((i, j) => parseInt(i) + parseInt(j));

//MATH WAY
function addTwoDigitsMath(n) {
    let sum = 0;
    while (n % 10 > 0) {
        sum += n % 10;
        n = Math.floor(n / 10)
    }
    return sum;
}

console.time("String Function: ");
console.log(addTwoDigitsStr(29));
console.timeEnd("String Function: ");
console.time("Math Function: ");
console.log(addTwoDigitsMath(29));
console.timeEnd("Math Function: ");