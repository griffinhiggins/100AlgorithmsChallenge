def sumOffFibonacciNums(n):
    fib_i = 1
    fib_j = 1
    oddFibSum = 2
    while oddFibSum < n:
        temp = fib_i + fib_j
        if temp % 2 == 1:
            oddFibSum += temp
        fib_i = fib_j
        fib_j = temp
    return oddFibSum
    
print(sumOffFibonacciNums(10))
print(sumOffFibonacciNums(1000))
print(sumOffFibonacciNums(4000000))