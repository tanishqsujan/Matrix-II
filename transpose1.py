x= [[1,2,3],
    [4,5,6],
    [7,8,9]]

y= [[9,8,7],
    [6,5,4],
    [3,2,1]]

ansx= [[0,0,0],
       [0,0,0],
       [0,0,0]]

ansy= [[0,0,0],
       [0,0,0],
       [0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        ansx[i][j] = x[j][i]
        
for k in range(len(y)):
    for l in range(len(y[0])):
        ansy[k][l] = y[l][k]
        
for r in ansx:
    print(r)

for s in ansy:
    print(s)