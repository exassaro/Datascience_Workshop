#Find inverse of a nxn Matrix

def determinant(matrix):
    size=len(matrix)
    if size==1:
        return matrix[0][0]
    if size==2:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    det=0
    for col in range(size):
        sub_matrix=[row[:col]+row[col+1:] for row in matrix[1:]] 
        det+=((-1)**col) * matrix[0][col]*determinant(sub_matrix)
        
    return det

def cofactor(matrix):
    size=len(matrix)
    cofactor_matrix=[[0]* size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            sub_matrix=[row[:j]+row[j+1:] for row in (matrix[:i] + matrix[i+1:])] 
            cofactor_matrix[i][j]=((-1)**(i+j)) * determinant(sub_matrix)
            
    return cofactor_matrix

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def inverse(matrix):
    det=determinant(matrix)
    if det==0:
        return None
    cofactor_matrix=cofactor(matrix)
    adjugate_matrix=transpose(cofactor_matrix)
    inverse_matrix=[[adjugate_matrix[i][j]/ det for j in range(len(matrix))] for i in range(len(matrix))]
    
    return inverse_matrix

A = [[4, 7, 2],
     [3, 6, 1],
     [2, 5, 3]]

# Compute Inverse
inv_A = inverse(A)

if inv_A:
    print("Inverse Matrix:")
    for row in inv_A:
        print(row)
else:
    print("Matrix is non-invertible.")