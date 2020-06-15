def validTime(time):
    return int(time[0:2]) < 23 and int(time[3:-1]) < 59
print(validTime("01:20"))
print(validTime("24:20"))
