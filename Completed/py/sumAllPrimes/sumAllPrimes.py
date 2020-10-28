def sumAllPrimes(n):
    primeSum = 0
    i = 2
    while i <= n:
        if isPrime(i):
            primeSum += i
        i += 1
    return primeSum


def isPrime(n):
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                return False
        return True
    return False

print(sumAllPrimes(10))
print(sumAllPrimes(977))