def tri_recursion(k):
    if k>0:
        result=k+tri_recursion(k-1)
        print(result)
        
    else:
        result=0
    return result
    
print("Recursion example result")
tri_recursion(6)