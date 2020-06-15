def switchLights(arr):
    for i in range(len(arr)):
        if arr[i] == 1:
            for j in range(i,-1,-1):
                arr[j] = abs(arr[j]-1)
    return arr

print(switchLights([1,1,1,1,1]))
print(switchLights([0,0]))