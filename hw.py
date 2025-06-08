x= [[1,4,9],
    [2,5,8],
    [3,6,7]]

answer= 0

for i in range(len(x)):
    for j in range(len(x[0])):
        answer += x[i][j]
        
    print(answer, end= " ")
    answer= 0
    
y= [[7,8,9],
    [4,5,6],
    [1,2,3]]

ans= 0

for k in range(len(y)):
    for l in range(len(y[0])):
        ans = ans + y[k][l]
    
    print(ans, end= " ")
    ans= 0