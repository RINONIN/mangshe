"""
作者：RINO
日期: 2022年01月01日
时间: 18:24
"""


def modify_name():
    filename = "f1.txt"
    print("local filename:", filename)


# modify_name()
# print("global filename:", filename)  # 这里会报错

# filename = "f1.txt"
#
#
# def modify_name():
#     print("local filename:", filename)
#
#
# modify_name()
# print("global filename:", filename)

filename = "f1.txt"


def modify_name():
    filename = "f2.txt"
    print("local filename:", filename)


modify_name()
print("global filename:", filename)

filename = "f1.txt"


def modify_name():
    global filename  # 提出申请
    filename = "f2.txt"
    print("local filename:", filename)


modify_name()
print("global filename:", filename)
