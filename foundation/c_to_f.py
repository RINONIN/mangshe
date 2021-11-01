def temp_conversion(c) :
    f=c*1.8 +32
    return f

c=float(input("请输入摄氏度:"))
f = temp_conversion(c)
print("转换成华氏度是:"+str(f))
