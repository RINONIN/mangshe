"""
作者：RINO
日期: 2021年11月08日
"""
import numpy as np

'''''
单个选取
array[1]
array[1,2,3]
array[1][1]
切片划分
array[:3]
array[2:4, 1:3]
条件筛选
array[array<0]
np.where(array, array < 0)
'''''

# a = np.array([1, 2, 3])
# print("a[0]:", a[0])
# print("a[1]:", a[1])
#
# print("a[[0,1]]:\n", a[[0, 1]])
# print("a[[1,1,0]]:\n", a[[1, 1, 0]])
#
# b = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ])
#
# # 选第 2 行所有数
# print("b[1]:\n", b[1])
#
# # 选第 2 行，第 1 列的数
# print("b[1,0]:\n", b[1, 0])
#
# # 这个看着有点纠结，如果对应到数据，
# # 前一个为行数，后一个为列数
# print("b[[1,0],[2,3]]:\n",
#       b[[1, 0],
#         [2, 3]])

# a = np.array([1, 2, 3])
# print("a[0:2]：\n", a[0:2])
# print("a[1:]：\n", a[1:])
# print("a[-2:]：\n", a[-2:])
#
# b = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ])
# # python的分号不包括右边界，是前一个数
# print("b[:2]:\n", b[:2])
# print("b[:2, :3]:\n", b[:2, :3])
# print("b[1:3, -2:]:\n", b[1:3, -2:])

a = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

# print(a[a < 7])
#
# condition = a > 7
# print(condition)
# print(a[condition])
# condition = (a > 7) & (a != 10)
# print(a[condition])
# # 利用where进行数据筛选和替换
# condition = a > 7
# print(np.where(condition, 1,a))
# 前面是符合条件的替换，后面是不符合条件的
# 若不替换后面需要写上替换的矩阵名
# condition = a > 7
# print(np.where(condition, -1, 2))
condition = a > 7
b = -a - 1
print(np.where(condition, a, b))