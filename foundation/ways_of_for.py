##for i in range(11):
##    print(i)
##for i in range(5,10):
##    print(i)
##for i in range(5,10,2):
##    print(i)
##for i in range(10,5,-2):
##    print(i)

##sum=0
##for i in range(1000001):
##    sum+=i
##print(sum)

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,"=",x,"*",n//x)
            break
    else:
        print(n,"sushu")
