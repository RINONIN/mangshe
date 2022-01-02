rhyme=(1,2,3,4,5,"abbbbbb")
print(rhyme)

#元组内容不可修改，切片和列表相同

nums=(3,1,9,6,8,3,5,3)
nums.count(3)

heros=("rino","nino","rinonin")
heros.index("rino")

s=(1,2,3)
t=(4,5,6)

s*3
t*3
s+t 

s=(1,2,3,4,5)
[each* 2 for each in s]

x=(520,)#加逗号,才是元组，否则为int

t = (123,"rino", 3.14)
x,y,z=t#解包和打包，列表也行，字符串也行

s =[1,2,3]
t =[4,5,6]
w = (s, t)
w[0][0] = 0
#元组不可修改，但是元组内的元素如果可变，则可以修改
