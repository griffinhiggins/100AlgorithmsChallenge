def uniqueDigitProducts(arr):
    retArr = []
    for i in arr:
        temp = 1
        for j in str(i):
            temp *= int(j)
        if not temp in retArr: 
            retArr.append(temp)
    return len(retArr)

print(uniqueDigitProducts([2, 8, 121, 42, 222, 23]))