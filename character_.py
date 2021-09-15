##hhh=[1,2,3,4,5,"abababab"]
##print(hhh)
##for each in hhh:
##    print(each)
##hhh[1]
##hhh[-6]

#增
##heros=["ironman","hulk"]
##heros.append("blackwidow")#每次放一个
##heros.extend(["a","b","c"])#放一堆

s=[1,2,3,4,5]
s[len(s):]=[6]
s[len(s):]=[7,8,9]
print(s)

#insert
s=[1,3,4,5]
s.insert(1,2)
s.insert(0,0)
s.insert(len(s),6)
print(s)

#remove
s.remove(5)
print(s)

s.pop(5)
s.clear()
print(s)
