def areSimilar(a, b):
    flag = False
    for i in range(len(a)):
        if(a[i] != b[i]):
            if(i == len(a) or flag):
                return False
            if(a[i+1] == b[i]):
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
            elif(a[i] == b[i+1]):
                temp = b[i]
                b[i] = b[i+1]
                b[i+1] = temp
            flag = True
    return True


print(areSimilar([1, 2, 3], [1, 2, 3]))
print(areSimilar([1, 2, 3], [2, 1, 3]))
print(areSimilar([1, 2, 2], [2, 1, 1]))
print(areSimilar([1, 3, 2, 1], [3, 1, 2, 1]))
print(areSimilar([1, 3, 2, 1], [3, 1, 1, 2]))
