def tasksType(arr,day):
    retArr = [0,0,0]
    for i in arr:
        if i <= day:
            retArr[0]+=1
        elif i <= 7 + day:
            retArr[1]+=1
        else:
            retArr[2]+=1
    return retArr

print(tasksType([1, 2, 3, 4, 5],2))
print(tasksType([1, 2, 4, 2, 10, 3, 1, 4, 5, 4, 9, 8],1))