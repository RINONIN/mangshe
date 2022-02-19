"""
作者：RINO
日期: 2022年02月23日
时间: 09:24
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = 2*x + 1

plt.figure()
plt.plot(x, y)
plt.show()
