def makeArrayConsecutive2(arr):
    count = 0
    LENGTH = len(arr) - 1
    arr.sort()
    for i,e in enumerate(arr):
        if i < LENGTH and e != arr[i+1] - 1: 
            count += arr[i+1] - e - 1
    return count

print(makeArrayConsecutive2([6, 2, 3, 8]))
