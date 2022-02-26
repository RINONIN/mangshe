"""
作者：RINO
日期: 2022年03月14日
时间: 14:02
"""

# 快速总结
# 日常一般用法
# 均值中位数
# df.mean()；df.median()
# 累加累乘
# df.sum()；df.prod()
# 最大最小
# df.max();
# df.min()
# 处理空值
# df.isnull();
# df.notnull();
# df.dropna();
# df.fillna()
# 获取索引
# df.idxmin();
# df.idxmax()

import pandas as pd
import numpy as np

# data = np.array([
#     [1.39, 1.77, None],
#     [0.34, 1.91, -0.05],
#     [0.34, 1.47, 1.22],
#     [None, 0.27, -0.61]
# ])
# df = pd.DataFrame(data, index=["r0", "r1", "r2", "r3"], columns=["c0", "c1", "c2"])
# print(df)
# print(df.describe())
#
#
# df1 = pd.DataFrame(np.random.random((4,3)), columns=["c0", "c1", "c2"])
# print(df1)
# print("\ndescribe:\n", df1.describe())  #std均方差

# print(df.mean(axis=1))  # axis=0 输出每一列的值，axis=1 输出没一行的值
# print(df.mean(axis=0, skipna=False))  # 直接略过nan和none

# 最后一个为高收入人
# s = pd.Series([1000, 2000, 4000, 100000])
# print("mean():", s.mean())  # 拉高平均收入，拉高仇恨
# print("median():", s.median())  # 比较合理

# df = pd.DataFrame(np.arange(12).reshape((4, 3)), columns=["c0", "c1", "c2"])
# print(df)

# print("sum():\n", df.sum())
# print("\nsum(axis=0):\n", df.sum(axis=0))
# print("\nsum(axis=1):\n", df.sum(axis=1))
#
# print("prod():\n", df.prod())  # 元素连乘
# print("\nprod(axis=0):\n", df.prod(axis=0))
# print("\nprod(axis=1):\n", df.prod(axis=1))
#
# print("max():\n", df.max())
# print("\nmin():\n", df.min())
#
# print(df.max().max())
# print(df.values.ravel().max())  # 用 Numpy 的方式运算

# 处理空值
# df.isnull();
# df.notnull();
# df.dropna();
# df.fillna()

df = pd.DataFrame([[1, 2, 3, 0],
                   [3, 4, None, 1],
                   [None, None, None, None],
                   [None, 3, None, 4]],
                  columns=list("ABCD"))
print(df)
print("\nisnull():\n", df.isnull())  # True 就是空
print("\nnotnull()\n", df.notnull())  # False 为空

print("默认：\n", df.dropna())  # 默认按 axis=0
print("\naxis=1:\n", df.dropna(axis=1))  # 可以换一个 axis drop

df1 = pd.DataFrame([[None, None, None], [1, None, 3]])
print(df1.dropna(how="all"))  # how 默认为 "any"

df.fillna(111)  # 填充 111

values = {"A": 0, "B": 1, "C": 2, "D": 3}
df.fillna(value=values)

df2 = pd.DataFrame(np.arange(16).reshape((4, 4)), columns=list("ABCD"))
print("df2:\n", df2)
print("\nfillna(df2):\n", df.fillna(df2))

# 获取索引
# df.idxmin();
# df.idxmax()

df = pd.DataFrame([[1, 2, 3, 0],
                   [3, 4, None, 1],
                   [3, 5, 2, 1],
                   [3, 2, 2, 3]],
                  columns=list("ABCD"))
print(df)
print("\nidxmax():\n", df.idxmax())
print("\nidxmax(skipna=False):\n", df.idxmax(skipna=False))
print("\nidxmin():\n", df.idxmin())
