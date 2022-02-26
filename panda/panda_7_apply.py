"""
作者：RINO
日期: 2022年03月20日
时间: 22:28
"""
import pandas as pd
import numpy as np

# data = np.arange(-12, 12).reshape((6, 4))
# df = pd.DataFrame(
#     data,
#     index=list("abcdef"),
#     columns=list("ABCD"))
# print(df)
#
# df["A"] *= 0
# print(df)
#
# df.loc["a", "A"] = 100
# df.iloc[1, 0] = 200
# print(df)
#
# df.loc["a", :] = df.loc["a", :] * 2
# print(df)
#
# df["A"][df["A"] == 0] = -1
# print(df)

# Apply方法

df = pd.DataFrame([[4, 9]] * 3, columns=['A', 'B'])
print(df)
print(np.sqrt(df))
print(df.apply(np.sqrt))


def func(x):
    return x[0] * 2, x[1] * -1


print(df.apply(func, axis=1, result_type='expand'))  # 输出的结果可以生成多 column
print(df.apply(func, axis=1, result_type='broadcast'))  # 原 column 和 index 名会继承到新生成的数据中


def func(x):
    return x["A"] * 4


print(df.apply(func, axis=1))

df["A"] = df.apply(func, axis=1)
print(df)


def func(r):
    return r[2] * 4


last_row = df.apply(func, axis=0)
print("last_row:\n", last_row)

df.iloc[2, :] = last_row
print("\ndf:\n", df)
