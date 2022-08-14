def launchSequenceChecker(names,nums):
    tab = {}
    for name,num in zip(names,nums):
        if name in tab and tab[name] >= num: 
            return False
        tab[name] = num
    return True

    
systemNames =  ["stage_1",  "stage_2",  "dragon", "stage_1",  "stage_2", "dragon"] 
stepNumbers  = [1,  10, 11,  2, 12,  111]
print(launchSequenceChecker(systemNames, stepNumbers))

systemNames = ["stage_1",  "stage_1", "stage_2", "dragon"] 
stepNumbers =  [2, 1,  12,  111]
print(launchSequenceChecker(systemNames, stepNumbers))
