#Matrix multiplication(dot product)

def matrix_multiplication(A,B):
    rows_A,cols_A=len(A),len(A[0])
    rows_B,cols_B=len(B),len(B[0])
    if cols_A != rows_B:
        return "Not possible"
    result =[[sum(A[i][k]*B[k][j] for k in range(cols_A)) for j in range(cols_B)]for i in range (rows_A)]    
    return result

A=[
    [1,2,3],
    [3,4,5]
    ]
B=[
    [9,5,4],
    [8,7,2],
    [12,15,16]
    ]

mul_matrix=matrix_multiplication(A,B)
for row in mul_matrix:
    print(row)
    
def dot_product(A,B):
    return sum(a*b for a,b in zip(A,B))

A=[2,3,4]
B=[1,0,-1]

result=dot_product(A,B)
print("Dot Product:", result)



A=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
    
    
B=[
    [9,12,63],
    [34,53,96],
    [71,84,49]
    ]



#matrix multiplication
    
def multiplication(A,B):
    if len(A[0])!=len(B):
        return "Not possible"
    result=[[0]* len(B[0]) for _ in range(len(A)) ]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                result[i][j]+=A[i][k] * B[k][j]
                
    return result
    
x=multiplication(A,B)

for row in x:
    print(row)
    
    
    
    
    
    
    
    
