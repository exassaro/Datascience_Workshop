# reflectiion mwans flipping a matrix horizontal or vertical
scalar=3
A=[
    [1,2,3],
    [3,4,5],
    [4,7,8],
    ]
def flip_horizontal(matrix):
    return matrix[::-1]
    
def flip_vertical(matrix):
    return [row[::-1] for row in matrix]
flip_h=flip_horizontal(A)
flip_v=flip_vertical(A)

print("horizontal")
for row in flip_h:
    print (row)
    
print("vertical")
for row in flip_v:
    print (row)