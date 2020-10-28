import math


def addTwoDigitsStr(n):
    return sum([int(i) for i in list(str(n))])


def addTwoDigitsMath(n):
    num = 0
    while(n % 10 > 0):
        num += n % 10
        n = math.floor(n/10)
    return num


print(addTwoDigitsStr(29))
print(addTwoDigitsMath(29))
