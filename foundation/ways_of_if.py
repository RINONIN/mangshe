##if 3 < 5:
##    print("我在里面~")
##    print("我也在里面~")
##print("我在外面~")
##
##
##if 3 > 5:
##    print("我在里面~")
##    print("我也在里面~")
##print("我在外面~")
##

##if "rino"=='nino':
##    print("yes")
##else:
##    print("no")

##score=input("your socre=")
##score=int(score)
##
##if 0 <= score < 60:
##    print("D")
##elif 60 <= score < 80:
##    print("C")
##elif 80 <= score < 90:
##    print("B")
##elif 90 <= score < 100 :
##    print("A")
##elif score == 100:
##    print("S")
##else:
##    print("0-100?")

##age=input("age=")
##age=int(age)
##print("抱款，未满18岁禁止访问。") if age < 18 else print("欢迎您来^o^")

##a=3
##b=5
##
##small=a if a<b else b
##print(small)

##score = 66
##level = ("D" if 0 <= score < 60 else
##         "c" if 60 <= score < 80 else
##         "B" if 80 <= score < 90 else
##         "A" if 90 <= score < 1e2 else
##         "S" if score == 100 else
##        "请输入0~100之间的分值^o^")
##print(level)

age = 18
isMale = True
if age < 18:
    print("抱歉，未满18岁禁止访问。")
else:
    if isMale:
        print("任君选购! ")
    else:
        print("抱歉，本店商品可能不适合小公举哦~")


