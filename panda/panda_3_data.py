"""
作者：RINO
日期: 2022年03月14日
时间: 09:58
"""
# 数据序列Series
# 创建
# 转换 Numpy
import pandas as pd
import numpy as np

# l = [11, 22, 33]
# s = pd.Series(l)
# print("list:", l)
# print("series:\n", s)
#
# s = pd.Series(l, index=["a", "b", "c"])
# print(s)
#
# s = pd.Series({"a": 11, "b": 22, "c": 33})
# print(s)

# 数据表DataFrame
# 创建
# 转换 Numpy

# s = pd.Series(np.random.rand(3), index=["a", "b", "c"])
# print(s)
# print("array:", s.to_numpy())
# print("list:", s.values.tolist())

# df = pd.DataFrame([
#     [1, 2],
#     [3, 4]
# ])
# print(df)
# print(df.at[0, 1])

# df = pd.DataFrame({"col1": [1, 3], "col2": [2, 4]})
# print(df)
#
# print(df["col1"], "\n")
# print("取出来之后的 type：", type(df["col1"]))
#
# df = pd.DataFrame({"col1": pd.Series([1,3]), "col2": pd.Series([2, 4])})
# print(df)

s = pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"])
df = pd.DataFrame({"col1": [1,3], "col2": [2, 4]}, index=["a", "b"])
print(s, "\n")
print(df)

print(df.index, "\n")
print(df.columns)
# 这里使用时，当前形式只能作为列的标签，需要自加行标签
my_json_data = [
  {"age": 12, "height": 111},
  {"age": 13, "height": 123}
]
print(pd.DataFrame(my_json_data, index=["jack", "rose"]))