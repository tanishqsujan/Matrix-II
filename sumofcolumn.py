x= [[9,2,5],
    [6,7,8],
    [1,2,3]]

answer= 0

for i in range(len(x)):
    for j in range(len(x[0])):
        #column-wise sum of items
        answer = answer + x[j][i]
        
    print(answer, end= " ")
    answer= 0