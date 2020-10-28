def alternatingSums(a):
    sumA = 0
    sumB = 0
    for i in range(len(a)):
        if(i % 2 == 0):
            sumA += a[i]
        else:
            sumB += a[i]
    return [sumA, sumB]


print(alternatingSums([50, 60, 60, 45, 70]))
