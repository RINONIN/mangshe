###列表推导式
##B=[[0]*3]*3
##A=[0]*3
##for i in range(3):
##    A[i]=[0]*3
##
##S=[[0]*3 for i in range(3)]
##S[1][2]=3
##print(S)
##
##even=[i for i in range(10) if i % 2 == 0]
##print(even)
###先执行for，然后if，最后是赋值
##even=[i+1 for i in range(10) if i % 2 == 0]
##print(even)

##words=["i","love","you","3","thousand"]
##fwords=[w for w in words if w[0]=="l"]
##print(fwords)
##
##martix=[[1,2,3],[4,5,6],[7,8,9]]
##flatten=[col for row in martix for col in row]
##print(flatten)
#外层循环在前，内层循环在后
##[x + y for x in "RINONIN" for y in "rinonin"]

a=[[x,y] for x in range(10) if x % 2 == 0 for y in range(10)if y % 3 == 0]
print(a)
#相当于
_=[]
for x in range(10):
    if x %2 ==0:
        for y in range(10):
            if y % 3 == 0:
                _.append([x,y])
