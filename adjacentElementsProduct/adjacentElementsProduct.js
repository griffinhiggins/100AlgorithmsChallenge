function adjacentElementsProduct(arr) {
    let max = 0
    for (let i = 0; i < arr.length - 1; i++) {
        temp = arr[i] * arr[i + 1];
        if (temp > max) {
            max = temp;
        }
    }
    return max;
}
console.log(adjacentElementsProduct([3, 6, -2, -5, 7, 3]));