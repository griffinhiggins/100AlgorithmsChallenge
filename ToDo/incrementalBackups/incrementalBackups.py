import bisect 
def incrementalBackups(n,arr):
    temp = []
    for time, file in arr:
        if time > n: 
            temp.append(file)
    temp = list(set(temp))
    temp.sort()
    return temp

lastBackupTime = 461620205

changes = [[461620203, 1], 
           [461620204, 2], 
           [461620205, 6],
           [461620206, 5], 
           [461620207, 3], 
           [461620207, 5], 
           [461620208, 1]]

print(incrementalBackups(lastBackupTime, changes))
# = [1, 3, 5].
