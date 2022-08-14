def matrixElementsSum(arr):
    sum = 0
    length = len(arr) - 1
    for i,x in enumerate(arr):
        for j,y in enumerate(x):
            if i < length: 
                if arr[i+1][j] == 0:
                    continue
            sum += y
    return sum
     
matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0], 
          [2, 0, 3, 3],
          [0, 0, 0, 0]]
print(matrixElementsSum(matrix))
