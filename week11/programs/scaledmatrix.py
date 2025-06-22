#scalalr multiplication

scalar=3
A=[
    [1,2,3],
    [3,4,5],
    [4,7,8],
    ]
scaled_matrix=[[scalar * element for element in row] for row in A]
for row in scaled_matrix:
    print (row)