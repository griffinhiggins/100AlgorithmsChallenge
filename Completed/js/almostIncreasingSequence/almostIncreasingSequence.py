def almostIncreasingSequence(a):
    flag = False
    for i in range(len(a) - 1):
        if(flag):
            return False
        else if(a[i] >= a[i+1]):
            flag = True
    return True


print(almostIncreasingSequence([1, 3, 2, 1]))
print(almostIncreasingSequence([1, 3, 2]))
