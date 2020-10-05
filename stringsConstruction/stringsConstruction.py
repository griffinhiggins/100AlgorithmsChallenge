def stringsConstruction(a,b):
    count = 0
    for i in range(len(a)):
        print(a[i])
        if len(b) == 0:
            break
        for j in range(len(b)):
            if a[i] == b[j]:
                b[j] = ''
                i += 1
            if i == len(a):
                count += 1
                i = 0
    return count

stringsConstruction('abc','abccba')