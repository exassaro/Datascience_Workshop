
#square matrix

def is_square_matrix(matrix):
    return len(matrix)==len(matrix[0])
    
A=[[1,2],
    [3,4]]
    
print(is_square_matrix(A))


#Diagonal matrices  
def is_diagonal(matrix):
    for i in range (len(matrix)):
        for j in range(len(matrix)):
            if i!=j and matrix[i][j]!=0:
                return False
    return True
    
D=[ [5,0,0],
    [0,4,0],
    [0,0,3]]
    
print(is_diagonal(D))


#Identity Martrix
def is_identity(matrix):
    for i in range (len(matrix)):
        for j in range(len(matrix)):
            if (i==j and matrix[i][j]!=1) or (i!=j and matrix[i][j]!=0):
                return False
    return True
    
C=[ [1,0,0],
    [0,1,0],
    [0,0,1]]
    
print(is_diagonal(C))


#Symmetric matrix
def is_symmetric(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]!=matrix[j][i]:
                return False
    return True
    
S=[ [1,2,3],
    [2,4,5],
    [3,5,6] ]
    
print(is_symmetric(S))


#sparse matrix

def is_sparse(matrix):
    total_elements=len(matrix)*len(matrix[0])
    zero_count=sum(matrix[i][j]==0 for i in range(len(matrix)) for j in range(len(matrix[0])))
    return zero_count>(total_elements/2)
    
S=[ [0,0,0,1],
    [0,2,0,0],
    [0,0,0,0]]
    
print(is_sparse(S))

#dense matrix

#sparse matrix

def is_dense(matrix):
    total_elements=len(matrix)*len(matrix[0])
    zero_count=sum(matrix[i][j]==0 for i in range(len(matrix)) for j in range(len(matrix[0])))
    return zero_count<(total_elements/2)
    
S=[ [0,70,2,1],
    [7,2,0,8],
    [5,0,4,0]]
    
print(is_dense(S))