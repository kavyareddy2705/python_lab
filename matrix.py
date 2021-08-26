X = [[1,2,3],  
       [4,5,6],  
       [7,8,9]]  
  
Y = [[0,1,2],  
      [3,4,5],  
      [6,7,8]]  
  
Result = [[0,0,0],  
               [0,0,0],  
              [0,0,0]]  
  
# iterate through rows of X  
for i in range(len(X)):  
   for j in range(len(Y[0])):  
       for k in range(len(Y)):  
           Result[i][j] += X[i][k] * Y[k][j]  
for r in Result:  
   print(Result)  
