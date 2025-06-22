
def missing_num(list):
    exp=(len(list)+1)*(len(list)+2)//2
    act=0
    for i in list:
        act+=i
    missing=exp-act
    return missing
list=[1,2,3,4,5,6,8,9]
v=missing_num(list)
print(v)
