def seatsInTheater(nCols,nRows,col,row):
    return (nCols-col+1) * (nRows-row)
print(seatsInTheater(16, 11, 5 ,3));
