import math
def squareDigitsSequence(n):
    nums = []
    while not n in nums:
        nums.append(n)
        m = 0
        while n > 0:
            o = n % 10
            m += o**2
            n = math.floor(n / 10)
        n = m
    nums.append(n)
    return len(nums)

print(squareDigitsSequence(16))
print(squareDigitsSequence(103))