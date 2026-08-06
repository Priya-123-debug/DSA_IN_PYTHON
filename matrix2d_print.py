matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row = len(matrix)
col = len(matrix[0])

for i in range(row):
    for j in range(col):
        print(matrix[i][j], end=" ")
    print()