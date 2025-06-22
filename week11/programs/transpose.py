# Transpose of a matrix
A=[
    [1,2,3],
    [3,4,5],
    [4,7,8],
    ]

transpose_A=[[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

for row in transpose_A:
    print(row)