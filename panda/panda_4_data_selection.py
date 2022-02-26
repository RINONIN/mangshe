"""
作者：RINO
日期: 2022年03月14日
时间: 10:45
"""
# 选Column/Index

import pandas as pd
import numpy as np

# data = np.arange(-12, 12).reshape((6, 4))
# df = pd.DataFrame(
#     data,
#     index=list("abcdef"),
#     columns=list("ABCD"))
# print(df)
#
# print(df["B"])
# print("numpy:\n", data[:, [2, 1]])
# print("\ndf:\n", df[["C", "B"]])
# loc
# print(data[2:3, 1:3])  # 选取时并不包括最后的数字
# print(df.loc["c":"d", "B":"D"])  # 选取时并不包括最后的数字
# print("numpy:\n", data[[3,1], :])  #第三行和第一行的全部元素
# print("\ndf:\n", df.loc[["d", "b"], :]) # 同上

# df2 = pd.DataFrame(
#   data,
#   index=list("beacdf"),
#   columns=list("ABCD"))
# print(df2)
# print(df2.loc["e":"c"])

# iloc #类似于numpy，只是多了标签信息

# print("numpy:\n", data[2:3, 1:3])
# print("\ndf:\n", df.iloc[2:3, 1:3])
# print("numpy:\n", data[[3,1], :])
# print("\ndf:\n", df.iloc[[3, 1], :])

# loc和iloc混搭

# row_labels = df.index[2:4]  #先把标签列出来，然后在索引传给loc或者iloc
# print("row_labels:\n", row_labels)
# print("\ndf:\n", df.loc[row_labels, ["A", "C"]])

# col_labels = df.columns[[0, 3]]
# print("col_labels:\n", col_labels)
# print("\ndf:\n", df.loc[row_labels, col_labels])
#
# col_index = df.columns.get_indexer(["A", "B"])
# print("col_index:\n", col_index)
# print("\ndf:\n", df.iloc[:2, col_index])

# 条件过滤筛选
# print(df["A"]<0)
# print(df[df["A"] < 0])  # 先选取A列中小于0的数据，然后将其所在的行输出

# print(df.iloc[:, 0])  # 取第一列
# print(df.iloc[:0])  # 取第一行
# print("~:\n", df.loc[:, ~(df.iloc[0] < -10)])
#
# print("\n>=:\n", df.loc[:, df.iloc[0] >= -10])
#
# i0 = df.iloc[0]
# print(df.loc[:, ~(i0 < -10) | (i0 < -11)])  # 不小-10或小于-11的数据
# print(~(df.iloc[0] < -10))
# print(df.loc[:, ~(df.iloc[0] < -10)])  # iloc不能接受bool，loc可以

# Series和DataFrame类似
list_data = list(range(-4, 4))
s = pd.Series(
  list_data,
  index=list("abcdefgh"))
print(s)

print(s.loc[["a", "g", "c"]], "\n")  #loc按标签筛选
print(s.loc["c": "f"])

print(s.iloc[[3, 1, 5]], "\n")
print(s.iloc[2: 4])  #iloc按索引，不包括end

print(s.iloc[s.index.get_indexer(["c", "d"])], "\n")
print(s.loc[s.index[[3,2]]])

print(s.loc[s < 3], "\n")
print(s.loc[(s < 0) & (s > -2)], "\n")
print(s.loc[(s < 0) | (s > 2)], "\n")