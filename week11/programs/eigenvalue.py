import numpy as np
A=np.array([[4,-2],
            [1,1]])

eigenvalues,eigenvectors=np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)


#Manual computation
import numpy as np

def compute_eigenvalues(A):
    a,b,c,d=A[0,0],A[0,1],A[1,0],A[1,1]
    
    trace=a+d
    determinant=(a*d)-(b*c)
    
    eigenvalue1=(trace+np.sqrt(trace**2-4*determinant))/2
    eigenvalue2=(trace-np.sqrt(trace**2-4*determinant))/2
    
    return eigenvalue1, eigenvalue2

def compute_eigenvectors(A,eigenvalue):
    I=np.eye(A.shape[0])
    A_lambda_I=A-eigenvalue*I
    
    if A_lambda_I[0,0] !=0:
        x=1
        y= -A_lambda_I[0,1]/A_lambda_I[0,0]
        
    else:
        x=-A_lambda_I[1,1]/A_lambda_I[1,0]
        y=1
        
    eigenvector=np.array([x,y])
    return eigenvector/np.linalg.norm(eigenvector)


A=np.array([[4,-2],
            [1,1]])

eigenvalues = compute_eigenvalues(A)
print("Eigenvalues:", eigenvalues)

# Compute eigenvectors
eigenvectors = [compute_eigenvectors(A, ev) for ev in eigenvalues]
print("Eigenvectors:")
for v in eigenvectors:
    print(v)
    
    
    
    
#compute Eigen values and Eigen vectors from scratch
import math
def determinant_2x2(A):
    return A[0][0]*A[1][1] - A[0][1]*A[1][0]

def solve_quadratic(a,b,c):
    discriminant=b**2-4*a*c
    if discriminant<0:
        return []
    sqrt_d=math.sqrt(discriminant)
    lambda1=(-b + sqrt_d) / (2*a)
    lambda2=(-b - sqrt_d) / (2*a)
    return lambda1,lambda2

def compute_eigenvalues(A):
    trace=A[0][0] + A[1][1]
    determinant=determinant_2x2(A)
    return solve_quadratic(1,-trace,determinant)

def compute_eigenvectors(A,eigenvalue):
    A_lambda_I=[A[0][0]-eigenvalue,A[0][1]],
    [A[1][0],eigenvalue-A[1][1]]
    
    if A_lambda_I[0][0]!=0:
        x=1
        y=-A_lambda_I[0][1]/A_lambda_I[0][0]
    elif A_lambda_I[1][0]!=0:
        y=1
        x=-A_lambda_I[0][1]/A_lambda_I[0][0]
    else:
        return None
    
    return [x,y]

def normalize(vector):
    magnitude=math.sqrt(vector[0]**2 + vector[1]**2)
    return [vector[0]/magnitude,vector[1]/magnitude]


A = [[4, -2], 
     [1, 1]]

# Compute Eigenvalues
eigenvalues = compute_eigenvalues(A)
print("Eigenvalues:", eigenvalues)

# Compute Eigenvectors
eigenvectors = [compute_eigenvectors(A, ev) for ev in eigenvalues]
normalized_eigenvectors = [normalize(v) for v in eigenvectors]

print("Eigenvectors:")
for v in normalized_eigenvectors:
    print(v)
    
    
    

def determinant(matrix):
    size=len(matrix)
    if size==1:
        return matrix[0][0]
    if size==2:
        return (matrix[0][0]*matrix[1][1]-(matrix[0][1]*matrix[1][0]))
    det=0
    for col in range(size):
        sub_matrix=[row[:col]+row[col+1:] for row in matrix[1:]]
        det+=((-1)**col)*matrix[0][col]*determinant(sub_matrix)
    return det
    
def solve_quadratic(a,b,c):
    discriminant=b**2-(4*a*c)
    if discriminant<0:
        return
    sqrt=(discriminant)**0.5
    lambda1=(-b+sqrt)/2*a
    lambda2=(-b-sqrt)/2*a
    return lambda1,lambda2

def compute_ev(A):
    trace=A[0][0]+A[1][1]
    det=determinant(A)
    return solve_quadratic(1,-trace,det)
    
def compute_eve(A,eigenvalue):
    A_lambda_I=[A[0][0]-eigenvalue,A[0][1]],[A[1][0],A[1][1]-eigenvalue]
    if A[0][0]!=0:
        x=1
        y=-A_lambda_I[0][1]/A_lambda_I[0][0]
    elif A[1][0]!=0:
        y=1
        x=-A_lambda_I[0][1]/A_lambda_I[0][0]
    else:
        return None
    return [x,y] 
    
def normalize(vector):
    magnitude=(vector[0]**2+vector[1]**2)**0.5
    return [vector[0]/magnitude,vector[1]/magnitude]
    
A = [[4, -2], 
     [1, 1]]

# Compute Eigenvalues
eigenvalues = compute_ev(A)
print("Eigenvalues:", eigenvalues)

# Compute Eigenvectors
eigenvectors = [compute_eve(A, ev) for ev in eigenvalues]
normalized_eigenvectors = [normalize(v) for v in eigenvectors]

print("Eigenvectors:")
for v in normalized_eigenvectors:
    print(v)
    
    
    

