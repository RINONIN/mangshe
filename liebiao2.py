##s=[1,2,3]
##t=[4,5,6]
##martix=[[1,2,3],[4,5,6],[7,8,9]]
##print(martix)
##
##for i in martix:
##    for each in i:
##        print(each)
##
##for i in martix:
##    for each in i:
##        print(each,end=" ")
##    print()
##
##print(martix[0][0])
##
##A=[0]*3
##for i in range(3):
##        A[i]=[0]*3
##print(A)
##

##x=[1,2,3]
##y=x

#copy 拷贝整个列表 y=x只是地址
#浅拷贝
##x=[[1,2,3],[4,5,6],[7,8,9]]
##y=x.copy()
##x[1][1]=0
##print(x,y)

import copy
x=[[1,2,3],[4,5,6],[7,8,9]]
y=copy.copy(x)

#深拷贝
x=[[1,2,3],[4,5,6],[7,8,9]]
y=copy.deepcopy(x)
x[1][1]=0
print(x,y)
