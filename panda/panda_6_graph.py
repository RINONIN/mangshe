"""
作者：RINO
日期: 2022年03月14日
时间: 15:21
"""
# 散点图 scatter
# 折线图 plot


# c: 对于这组数据中每个（x,y）数据点的颜色值
# s: 画点的大小（size）
# alpha：不透明度
# cmap：colormap，你可以在这里找到非常丰富的案例

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# n = 1024    # data size
# df = pd.DataFrame({
#     "x": np.random.normal(0, 1, n),
#     "y": np.random.normal(0, 1, n),
# })
# color = np.arctan2(df["y"], df["x"])
# df.plot.scatter(x="x", y="y", c=color, s=60, alpha=.5, cmap="rainbow")
#
# n = 20    # data size
# x = np.linspace(-1, 1, n)
# y = x * 2 + 0.4 + np.random.normal(0, 0.3, n)
# df = pd.DataFrame({
#     "x": x,
#     "y": y,
# })
# df.plot(x="x", y="y", alpha=.5, c="r")
#
# n = 20    # data size
# x = np.linspace(-1, 1, n)
# y1 = x * -1 - 0.1 + np.random.normal(0, 0.3, n)
# y2 = x * 2 + 0.4 + np.random.normal(0, 0.3, n)
# df = pd.DataFrame({
#     "x": x,
#     "y1": y1,
#     "y2": y2,
# })
# df.plot(x="x", y=["y1", "y2"], alpha=.5)
# plt.show()

# 条形图 bar
# 分布图 histograms
# 饼图 pie
# 面积图 area

# df = pd.DataFrame(np.random.rand(5, 3), columns=["a", "b", "c"])
# df.plot.bar()
# df.plot.bar(stacked=True)
# df.plot.barh()  # 水平
# plt.show()

# df = pd.DataFrame({"a": np.random.randn(1000)})
# df.plot.hist()
#
# df = pd.DataFrame(
#     {
#         "a": np.random.randn(1000) + 1,
#         "b": np.random.randn(1000),
#         "c": np.random.randn(1000) - 4,
#     }
# )
#
# df.plot.hist(alpha=0.5, bins=30)
#
#
# df = pd.DataFrame(
#     {"boss": np.random.rand(4)},
#     index=["meeting", "supervise", "teaching", "team building"],
# )
# df.plot.pie(y="boss", figsize=(7,7))

# df = pd.DataFrame(
#     {
#         "bigBoss": np.random.rand(4),
#         "smallBoss": np.random.rand(4),
#     },
#     index=["meeting", "supervise", "teaching", "team building"],
# )
# df.plot.pie(subplots=True, figsize=(9,9), legend=False)


df = pd.DataFrame(
    np.random.rand(10, 4),
    columns=["a", "b", "c", "d"]
)
df.plot.area()

df.plot.area(stacked=False)
plt.show()