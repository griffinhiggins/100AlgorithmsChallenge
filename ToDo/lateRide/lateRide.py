def lateRide(n):
    sum = 0
    for i in divmod(n,60):
        while i > 0:
            sum += i % 10
            i = i // 10
    return sum
    
print(lateRide(240))
print(lateRide(808))
