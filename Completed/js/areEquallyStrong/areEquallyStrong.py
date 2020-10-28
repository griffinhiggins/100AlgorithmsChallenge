def areEquallyStrong(a0, a1, b0, b1):
    return max(a0, a1) == max(b0, b1) and min(a0, a1) == min(b0, b1)


print(areEquallyStrong(10, 15, 15, 10))
print(areEquallyStrong(15, 10, 15, 10))
print(areEquallyStrong(15, 10, 15, 9))
