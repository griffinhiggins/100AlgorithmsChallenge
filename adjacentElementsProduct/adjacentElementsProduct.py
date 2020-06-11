def adjacentElementsProduct(arr):
    num = 0
    for i in range(0, len(arr)-1):
        temp = arr[i] * arr[i+1]
        if(temp > num):
            num = temp
    return num


print(adjacentElementsProduct([3, 6, -2, -5, 7, 3]))
