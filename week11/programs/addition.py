#matrix addition
def matrix_addition(A,B):
    rows,cols=len(A),len(A[0])
    result=[[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]
    return result
A=[
    [1,2,3],
    [3,4,5]
    ]
    
B=[
    [9,5,4],
    [8,7,2]
    ]


sum_matrix=matrix_addition(A,B)
for row in sum_matrix:
    print(row)