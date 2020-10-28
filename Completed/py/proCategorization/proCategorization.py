def proCategorization(pros,preferences):
    prefSet = set()
    for i in preferences:
        for j in i:
            prefSet.add(j)
    retList = []
    for i in prefSet:
        prosList = []
        for j in range(len(preferences)):
            if i in preferences[j]:
                prosList.append(pros[j])
        retList.append([[i],prosList])
    return retList

pros = ["Jack", "Leon", "Maria"]
preferences = [["Computer repair", "Handyman", "House cleaning"],
               ["Computer lessons", "Computer repair", "Data recovery service"],
               ["Computer lessons", "House cleaning"]]
print(proCategorization(pros, preferences))