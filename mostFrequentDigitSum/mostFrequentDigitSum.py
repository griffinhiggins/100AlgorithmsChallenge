def mostFrequentDigit(n):
    nums = [n]
    i = 0
    while n > 0:
        n0 = nums[i]
        n = 0
        while n0 > 0:
            n += n0 % 10
            n0 //= 10
        nums.append(nums[i]-n)
        if nums[i]-n == 0:
            break;
        nums[i] = n
        i += 1
    mc = 0
    m = 0
    for i in set(nums):
        c = nums.count(i)
        if c > mc:
            mc = c
            m = i
        elif c == mc and i > m:
            m = i
    return m

print(mostFrequentDigit(88))
print(mostFrequentDigit(8))