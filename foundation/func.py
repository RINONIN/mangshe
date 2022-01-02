"""
作者：RINO
日期: 2022年01月01日
时间: 18:11
"""


# f1 = "f1"
# f2 = "f2"
#
# f1 += ".txt"
# f1 = "my_" + f1
# f2 += ".txt"
# f2 = "my_" + f2
# print(f1, f2)


# def modify_name(filename):
#     filename += ".txt"
#     filename = "my_" + filename
#     print(filename)
#
#
# modify_name("f1")
# modify_name("f2")
#
#
# def my_func():
#     filename = "f1"
#     ext = ".txt"
#     total_name = filename + ext
#     print(total_name)
#
#
# my_func()
#
#
# def modify_name(filename):
#     filename += ".txt"
#     filename = "my_" + filename
#     return filename
#
#
# new_filename = modify_name("f1")
# print(new_filename)


def f(x, a, b, c):
    return a * x ** 2 + b * x + c * 1


print(f(2, 1, 1, 0))  # 忽略参数名，按顺序传参
print(f(x=2, a=1, b=1, c=0))  # 写上参数名，按名字传参
print(f(a=1, c=0, x=2, b=1))  # 若用参数名，可以打乱顺序传参


def f(x, a=1, b=1, c=0):  # 必须设置默认值
    return a * x ** 2 + b * x + c * 1


print(f(2, a=2))
print(f(2))
