x="12321"
"yes" if x==x[::-1] else "no"

#变大小写
x="rinonin is rino"
x.capitalize() #首字母大写
x.casefold()#所有字符都是小写
x.tilte()#首字母大写，其他小写
x.swapcase()#字符串大小写翻转
x.upper()#都变大写
x.lower()#都变小写

##左中右对齐,宽度小于原字符串则直接输出原字符串
x=("阿巴巴巴，阿巴巴啊巴")
x.center(15,"a")#后面的字符可以随意填
x.rjust(15)
x.ljust(15)#中右左对齐
x.zfill(15)#用0填充左边

##查找
x="上海自来水来自海上"
x.count("海",0,5)
x.find("海")
x.rfind("海")#从左向右，从右向左找到该字符并返回位置
x.index("?")
x.rindex("?")

#替换
code = """
    print( "I love Fishc" )
  print( "I love my wife" ) """
new_code = code.expandtabs(4)#一个tab 等于几个空格
print(new_code)

"ababbabababab ,阿巴".replace("阿巴","呼呼呼")

table = str.maketrans( "ABCDEFG","1234567")
"I love Fishc".translate(table)




