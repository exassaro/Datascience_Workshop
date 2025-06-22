class example:
    def sum(self,a=None,b=None):
        if a is not None and b is not None:
            return a+b
        elif a is not None:
            return a
        else:
            return 0
        
Example = example()

print (Example.sum(2,3))
print (Example.sum(3))
print (Example.sum())
        