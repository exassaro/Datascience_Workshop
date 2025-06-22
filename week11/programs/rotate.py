#rotate matrix in 90 degree angle for that first we have to tarnspose the matrix then reverse
#we use zip *(inpacking operator) here to transpose 

def rotate_90(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]
    
A=[
    [1,2,3],
    [3,4,5],
    [4,7,8],
    ]
rotated_matrix=rotate_90(A)
for row in rotated_matrix:
    print(row)
    
def rotate(matrix):
    return [[matrix[j][i] for j in range(len(matrix)-1,-1,-1)] for i in range(len(matrix[0]))]
    
A=[[1,2,3],
    [4,5,6],
    [7,8,9]]
    
print(rotate(A))