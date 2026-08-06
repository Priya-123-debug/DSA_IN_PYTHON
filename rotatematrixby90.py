matrix=[
    [ 1, -7, -4,  0],
    [ 2, -8,  0, -1],
    [ 3,  0, -5, -2],
    [ 0, -9, -6, -3]
]
n=len(matrix)
result=[[0 for _ in range(n)] for _ in range(n)]

for i in range(0,n):
    for j in range(0,n):
        result[j][n-i-1]=matrix[i][j]
for i in range(0,n):
    for j in range(0,n):
        print(result[i][j],end="")
    print()

