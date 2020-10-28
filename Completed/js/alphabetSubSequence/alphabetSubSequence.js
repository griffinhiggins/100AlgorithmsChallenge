function alphabetSubsequence(str) {
    for (let i = 0; i < str.length - 1; i++) {
        if (str[i] >= str[i + 1]) {
            return false;
        }
    }
    return true
}
console.log(alphabetSubsequence('zab'))
console.log(alphabetSubsequence('effg'))
console.log(alphabetSubsequence('cdce'))
console.log(alphabetSubsequence('ace'))
console.log(alphabetSubsequence('bxz'))