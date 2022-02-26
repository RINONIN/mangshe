"""
作者：RINO
日期: 2022年03月23日
时间: 14:06
# """
# 找到NaN数据
# pd.isna(), pd.notna()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# df = pd.DataFrame([[1, None],[np.nan, 4]])
# print(df)
# print(df.isna())
# print(df.notna())

# NaN的影响
# df = pd.DataFrame({
#     "a": [1, None, 1],
#     "b": [np.nan, 4, 4]
# })
# print("skipped NaN:\n", df.mean(axis=0))
# print("\n\nnot skipped:\n", df.mean(axis=0, skipna=False))

# 移除NaN
# df.dropna()

# df = pd.DataFrame({
#     "a": [1, None, 3],
#     "b": [4, 5, 6]
# })
# print(df.dropna(axis=0))  # 此时直接丢弃带nan的一整行
# print(df.dropna(axis=1))

# 填充NaN
# df.fillna()

# df = pd.DataFrame({
#     "a": [1, None, 3],
#     "b": [4, 5, 6]
# })
# a_mean = df["a"].mean()
# new_col = df["a"].fillna(a_mean)
# df["a"] = new_col
# print(df)

# df = pd.DataFrame({
#     "a": [1, None, 3, None],
#     "b": [4, 8, 12, 12]
# })
# a_nan = df["a"].isna()
# a_new_value = df["b"][a_nan] / 4
# new_col = df["a"].fillna(a_new_value)
# df["a"] = new_col
# print(df)
#
# df = pd.DataFrame({
#     "a": [1, None, 3, None],
#     "b": [4, 8, 12, 12]
# })
# a_nan = df["a"].isna()
# df.loc[a_nan, "a"] =  df["b"][a_nan] / 4
# print(df)

# 不符合范围的值
# df.clip()

df = pd.DataFrame({
    "a": [1, 1, 2, 1, 2, 40, 1, 2, 1],
})
df.plot()

df["a"] = df["a"].clip(lower=0, upper=3)
df.plot()
plt.show()