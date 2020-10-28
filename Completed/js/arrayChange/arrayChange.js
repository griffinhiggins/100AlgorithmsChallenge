function arrayChange(a) {
    let flag = true,
        count = 0;
    while (flag) {
        flag = false
        for (let i = 0; i < a.length - 1; i++) {
            console.log(a[i], a[i + 1]);
            if (a[i] < a[i + 1] - 1) {
                a[i]++;
                count++;
                flag = true
            } else if (a[i] > a[i + 1] - 1) {
                a[i]++;
                count++;
                flag = true
            }
        }
    }
    return count;
};

console.log(arrayChange([1, 1, 1]));