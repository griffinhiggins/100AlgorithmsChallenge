function alternatingSums(a) {
    let sumA = 0,
        sumB = 0;
    a.forEach((e, i) => {
        if (i % 2 == 0) {
            sumA += e;
        } else {
            sumB += e;
        }
    });
    return [sumA, sumB]
}

console.log(alternatingSums([50, 60, 60, 45, 70]))