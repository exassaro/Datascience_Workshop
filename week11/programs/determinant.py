#determinant of 2X2 mattrix
def determinant_2X2(matrix):
    if len(matrix)!=2 or len(matrix[0])!=2:
        return "Determinant cannot be found"
    return (matrix[0][0]*matrix[1][1]-(matrix[0][1]*matrix[1][0]))
    
A=[
    [1,2],
    [3,4]
    ]
print(determinant_2X2(A))

#determinant of more than 2x2 matrix using recursiion
def determinant(matrix):
    if len(matrix)==1:
        return matrix[0][0]
    if len(matrix)==2:
        return (matrix[0][0]*matrix[1][1]-(matrix[0][1]*matrix[1][0]))
    det=0
    for col in range(len(matrix)):
        sub_martrix=[row[:col]+row[col+1:] for row in matrix[1:]]
        det+=((-1)**col)*matrix[0][col]*determinant(sub_martrix)
    return det
    
M3=[[1,2,3],
    [4,5,6],
    [7,8,9]]
print("Determinant of 3x3 Matrix:", determinant(M3))