"""
作者：RINO
日期: 2022年01月02日
时间: 14:31
"""
# 文件目录操作
# os.getcwd()
# os.listdir()
# os.makedirs()
# os.path.exists()
# 文件管理系统
# os.removedirs()
# shutil.rmtree()
# os.rename()
# 文件目录多种检验
# os.path.isfile()
# os.path.exists()
# os.path.isdir()
# os.path.basename()
# os.path.dirname()
# os.path.split()
#
# import os

# print("当前目录：", os.getcwd())
# print("当前目录里有什么：", os.listdir())

# os.makedirs("project", exist_ok=True)
# print(os.path.exists("project"))
#
# if os.path.exists("user/rino"):
#     print("user exist")
# else:
#     os.makedirs("user/rino")
#     print("user created")
# print(os.listdir("user"))

# if os.path.exists("user/mofan"):
#     os.removedirs("user/mofan")
#     print("user removed")
# else:
#     print("user not exist")

# os.makedirs("user/mofan", exist_ok=True)
# with open("user/mofan/a.txt", "w") as f:
#     f.write("nothing")
# os.removedirs("user/mofan")  # 这里会报错

# import shutil  # delete all
#
# shutil.rmtree("user/mofan")
# print(os.listdir("user"))

# os.makedirs("user/mofan", exist_ok=True)
# os.rename("user/mofan", "user/mofanpy")  # change name
# print(os.listdir("user"))

# import os
#
# os.makedirs("user/mofan", exist_ok=True)
# with open("user/mofan/a.txt", "w") as f:
#     f.write("nothing")
# print(os.path.isfile("user/mofan/a.txt"))  # True
# print(os.path.exists("user/mofan/a.txt"))  # True
# print(os.path.isdir("user/mofan/a.txt"))  # False
# print(os.path.isdir("user/mofan"))  # True

import os


def copy(path):
    filename = os.path.basename(path)  # 文件名
    dir_name = os.path.dirname(path)  # 文件夹名
    new_filename = "new_" + filename  # 新文件名
    return os.path.join(dir_name, new_filename)  # 目录重组


def copy(path):
    dir_name, filename = os.path.split(path)
    new_filename = "new_" + filename  # 新文件名
    return os.path.join(dir_name, new_filename)  # 目录重组


print(copy("user/mofan/a.txt"))

print(copy("user/mofan/a.txt"))
