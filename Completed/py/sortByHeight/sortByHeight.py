def sortByHeight(a):
    for i in range(len(a)):
        if a[i] >= 0:
            for j in range(i,len(a)):
                if a[j] >= 0 and a[j] < a[i]:
                    temp = a[i]
                    a[i] = a[j]
                    a[j] = temp
    return a


print(sortByHeight([10, 9, -1, 5, 4, -1, 3, 2]))
print(sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180]))
