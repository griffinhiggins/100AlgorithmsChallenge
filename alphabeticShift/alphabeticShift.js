alphabeticShift = str =>
    str
    .split("")
    .map(i => String.fromCharCode(
        (i.charCodeAt(0) % 122 == 0) ?
        97 :
        i.charCodeAt(0) + 1))
    .join("");

console.log(alphabeticShift('crazy'));
console.log(alphabeticShift('aaavd'));