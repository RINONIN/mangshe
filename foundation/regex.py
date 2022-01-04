"""
作者：RINO
日期: 2022年01月04日
时间: 08:54
"""
# 不用正则的判断
# re.compile()
# ptn.search()
# 正则给额外信息
# re.search()
# 中文
# string.encode()
# 查找替换等更多功能
# re.search()
# re.match()
# re.findall()
# re.finditer()
# re.split()
# re.sub()
# re.subn()
import re

# pattern1 = "file"
# pattern2 = "files"
# string = "the file is in the folder"
# print("file in string", pattern1 in string)
# print("files in string", pattern2 in string)

# ptn = re.compile(r"\w+?@\w+?\.com")  # 用“r”是代表原始文本输入，不在乎有多少“/”
#
# matched = ptn.search("mofan@mofanpy.com")
# print("mofan@mofanpy.com is a valid email:", matched)
# matched = ptn.search("mofan@mofanpy+com")
# print("mofan@mofanpy+com is a valid email:", matched)
#
# matched = re.search(r"\w+?@\w+?\.com", "mofan@mofanpy.com")
# print("mofan@mofanpy.com:", matched)
# matched = re.search(r"\w+?@\w+?\.com", "the email is mofan@mofanpy.com.")
# print("the email is mofan@mofanpy.com:", matched)

# match = re.search(r"run", "I run to you")
# print(match)
# print(match.group())
#
# print(re.search(r"ran", "I run to you"))
# print(re.search(r"run", "I run to you"))
#
# re.search(r"ran|run", "I run to you")
#
# re.search(r"r[au]n", "I run to you")
#
# print(re.search(r"f(ou|i)nd", "I find you"))
# print(re.search(r"f(ou|i)nd", "I found you"))

# 特定标识	含义	范围
# \d	任何数字	[0-9]
# \D	不是数字的
# \s	任何空白字符	[ \t\n\r\f\v]
# \S	空白字符以外的
# \w	任何大小写字母,数字和 _	[a-zA-Z0-9_]
# \W	\w 以外的
# \b	匹配一个单词边界	比如 er\b 可以匹配 never 中的 er，但不能匹配 verb 中的 er
# \B	匹配非单词边界	比如 er\B 能匹配 verb 中的 er，但不能匹配 never 中的 er
# \\	强制匹配 \
# .	    匹配任何字符 (除了 \n)
# ?	前面的模式可有可无
# *	    重复零次或多次
# +	重复一次或多次
# {n,m}	重复 n 至 m 次
# {n}	重复 n 次
# +?	非贪婪，最小方式匹配 +
# *?	非贪婪，最小方式匹配 *
# ??	非贪婪，最小方式匹配 ?
# ^	    匹配一行开头，在 re.M 下，每行开头都匹配
# $	匹配一行结尾，在 re.M 下，每行结尾都匹配
# \A	匹配最开始，在 re.M 下，也从文本最开始
# \B	匹配最结尾，在 re.M 下，也从文本最结尾

# print(re.search(r"138\d{8}", "13812345678"))
# print(re.search(r"138\d{8}", "138123456780000"))
#
# print(re.search(r"不?爱", "我爱你"))
# print(re.search(r"不?爱", "我不爱你"))
# print(re.search(r"不.*?爱", "我不是很爱你"))

# print("我爱你".encode("unicode-escape"))
# print("我爱你".encode("gbk"))


print("search:", re.search(r"run", "I run to you"))
print("match:", re.match(r"run", "I run to you"))
print("findall:", re.findall(r"r[ua]n", "I run to you. you ran to him"))

for i in re.finditer(r"r[ua]n", "I run to you. you ran to him"):
    print("finditer:", i)

print("split:", re.split(r"r[ua]n", "I run to you. you ran to him"))
print("sub:", re.sub(r"r[ua]n", "jump", "I run to you. you ran to him"))
print("subn:", re.subn(r"r[ua]n", "jump", "I run to you. you ran to him"))

# re.search()	扫描查找整个字符串，找到第一个模式匹配的
# re.match()	从字符的最开头匹配，找到第一个模式匹配的即使用
# re.findall()	返回一个不重复的 pattern 的匹配列表
# re.finditer()	和 findall 一样，只是用迭代器的方式使用
# re.split()	    用正则分开字符串
# re.sub()	    用正则替换字符
# re.subn()	    和 sub 一样，额外返回一个替代次数

found = []
for i in re.finditer(r"[\w-]+?\.jpg", "I have 2021-02-01.jpg, 2021-02-02.jpg, 2021-02-03.jpg"):
    found.append(re.sub(r".jpg", "", i.group()))
print(found)

string = "I have 2021-02-01.jpg, 2021-02-02.jpg, 2021-02-03.jpg"
print("without ():", re.findall(r"[\w-]+?\.jpg", string))
print("with ():", re.findall(r"([\w-]+?)\.jpg", string))

string = "I have 2021-02-01.jpg, 2021-02-02.jpg, 2021-02-03.jpg"
match = re.finditer(r"(\d+?)-(\d+?)-(\d+?)\.jpg", string)
for file in match:
    print("matched string:", file.group(0), ",year:", file.group(1), ", month:", file.group(2), ", day:", file.group(3))

string = "I have 2021-02-01.jpg, 2021-02-02.jpg, 2021-02-03.jpg"
match = re.finditer(r"(?P<y>\d+?)-(?P<m>\d+?)-(?P<d>\d+?)\.jpg", string)
for file in match:
    print("matched string:", file.group(0),
        ", year:", file.group("y"),
        ", month:", file.group("m"),
        ", day:", file.group("d"))

# 模式	全称	说明
# re.I	re.IGNORECASE	忽略大小写
# re.M	re.MULTILINE	多行模式，改变'^'和'$'的行为
# re.S	re.DOTALL	点任意匹配模式，改变'.'的行为, 使".“可以匹配任意字符
# re.L	re.LOCALE	使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
# re.U	re.UNICODE	使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
# re.X	re.VERBOSE	详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。以下两个正则表达式是等价的

ptn, string = r"r[ua]n", "I Ran to you"
print("without re.I:", re.search(ptn, string))
print("with re.I:", re.search(ptn, string, flags=re.I))

ptn = r"^ran"
string = """I
ran to you"""
print("without re.M:", re.search(ptn, string))
print("with re.M:", re.search(ptn, string, flags=re.M))
print("with re.M and match:", re.match(ptn, string, flags=re.M))

ptn = r"^ran"
string = """I
Ran to you"""
print("with re.M and re.I:", re.search(ptn, string, flags=re.M|re.I))

string = """I
Ran to you"""
re.search(r"(?im)^ran", string)

import time
n = 1000000
# 不提前 compile
t0 = time.time()
for _ in range(n):
    re.search(r"ran", "I ran to you")
t1 = time.time()
print("不提前 compile 运行时间：", t1-t0)

# 先做 compile
ptn = re.compile(r"ran")
for _ in range(n):
    ptn.search("I ran to you")
print("提前 compile 运行时间：", time.time()-t1)