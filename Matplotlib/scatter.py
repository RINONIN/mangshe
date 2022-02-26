"""
作者：RINO
日期: 2022年02月23日
时间: 10:51
"""
import matplotlib.pyplot as plt
import numpy as np

n = 2048  # data size
X = np.random.normal(0, 1, n)  # 每一个点的X值
Y = np.random.normal(0, 1, n)  # 每一个点的Y值
T = np.arctan2(Y, X)  # for color value
# 输入X和Y作为location，size=75，颜色为T，color map用默认值，透明度alpha 为 50%
plt.scatter(X, Y, s=75, c=T, alpha=.5)
plt.xlim(-5, 5)
plt.xticks(())  # ignore xticks
plt.ylim(-5, 5)
plt.yticks(())  # ignore yticks

plt.show()
