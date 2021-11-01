##oho=[1,2,3,4,5]
##for i in range(len(oho)):
##        oho[i]=oho[i]*2
##
##ofo=[1,2,3,4,5]
##ofo=[i*2 for i in ofo]
##print(oho,ofo)
#列表推导式

##x=[i+1 for i in range(10)]
##print(x)
##
##x=[]
##for i in range(10):
##    x.append(i+1)
##
##y=[c*2 for c in "rinonin"]
##print(y)
##
##code=[ord(c) for c in "RINONIN"]
##print(code)

martix=[[1,2,3],[4,5,6],[7,8,9]]
##col2=[c[1] for c in martix ]
##print(col2)
##
##diag=[martix[i][i] for i in range(len(martix))]
##print(diag)

diag=[martix[i][2-i] for i in range(len(martix))]
print(diag)
