"""
作者：RINO
日期: 2022年02月14日
时间: 19:46
"""
from copy import deepcopy

# l = [1, 2, 3]
# _l = l.copy()
# _l[0] = -1
# print(_l)
# print(l)
#
# l = [[1], [2], 3]
# _l = l.copy()
# _l[0][0] = -1
# print(_l)
# print(l)
#
#
# class File:
#     def __init__(self, name):
#         self.name = name
#
#
# audio = File("mp3")
# file = File("txt")
# l = [audio, file]
# _l = l.copy()
# _l[0].name = "mp4"
# print(audio.name)  # "mp4"

# 深拷贝 Python 他在创造之初，就有这么个约定
# 列表中直接存放的数值，字符，和存 class 实例，列表，字典不同
# 对数值字符的复制，直接是复制的值，而不是一个投影。

l = [[1], [2], 3]
_l = deepcopy(l)
_l[0][0] = -1
print(_l)
print(l)
