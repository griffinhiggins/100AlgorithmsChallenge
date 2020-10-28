def arrayConversion(arr):
    isOdd = True
    while(len(arr) > 1):
        retArr = []
        for i in range(0,len(arr),2):
            if(isOdd):
                retArr.append(arr[i] + arr[i+1])
            else:
                retArr.append(arr[i] * arr[i+1])
        isOdd = not isOdd
        arr = retArr
    return arr[0]

print(arrayConversion([1]));
print(arrayConversion([1, 2]));
print(arrayConversion([1, 2, 3, 4, 5, 6, 7, 8]));