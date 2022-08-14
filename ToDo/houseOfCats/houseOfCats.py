def houseOfCats(legs):
    temp = []
    i = 0 
    while legs >= 0:
        legs -= 2
        i += 1
        if legs >= 0 and legs % 4 == 0: 
            temp.append(i)
    return temp

legs = 6
print(houseOfCats(legs))
# = [1, 3].
legs = 2
print(houseOfCats(legs))
