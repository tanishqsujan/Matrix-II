x= [[8,4,1],
    [2,4,6],
    [3,5,9]]

answer= [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        #transpose of a matrix
        answer[i][j] = x[j][i]
        
for r in answer:
    print(r)