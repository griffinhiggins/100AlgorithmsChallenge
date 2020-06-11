import math
def absoluteValuesSumMinimization(a):
    return a[math.floor(len(a) // 2)] if (len(a) % 2) else a[(len(a) // 2) - 1]


print(absoluteValuesSumMinimization([2, 4, 7]));
print(absoluteValuesSumMinimization([2, 4, 6, 7]));
print(absoluteValuesSumMinimization([2, 4, 6, 6, 7]));
print(absoluteValuesSumMinimization([2, 4, 6, 6, 7, 8]));