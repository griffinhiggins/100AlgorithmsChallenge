def arrayMaxConsecutiveSum(arr):
    maxEl = 0
    for i in range(0,len(arr)-1):
        if(arr[i] + arr[i+1] > maxEl):
            maxEl = arr[i] + arr[i+1]
    return maxEl

print(arrayMaxConsecutiveSum([1, 2, 3, 4, 5]));