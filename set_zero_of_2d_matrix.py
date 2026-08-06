# A 3x4 matrix declaration
matrix = [
    [1, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 1, 0]
]
nr=len(matrix)
nc=len(matrix[0])
zeror=set()
zeroc=set()
for i in range(0,nr):
    for j in range(0,nc):
        if matrix[i][j]==0:
            zeror.add(i)
            zeroc.add(j)
for i in range(0,nr):
    for j in range(0,nc):
        if i in zeror or j in zeroc:
            matrix[i][j]=0
for i in range(0,nr):
    for j in range(0,nc):
        print(matrix[i][j],end="")
    print()
       
