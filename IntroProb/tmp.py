import operator
compute_list=[1,'-',2,'//',3,'+',4,'+',5,'*',6]
ops = {
        "+":operator.add,
        "-":operator.sub,
        "*":operator.mul,
        "//":operator.floordiv
    }
tmp=compute_list[0]
for i in range(1,len(compute_list),2):
    if tmp < 0 and compute_list[i]=='//':
        result=(ops[compute_list[i]](abs(tmp),compute_list[i+1]))*(-1)
    else:
        result=(ops[compute_list[i]](tmp,compute_list[i+1]))
    
    tmp = result
print(result)
print(ops["*"](-2,compute_list[4]))