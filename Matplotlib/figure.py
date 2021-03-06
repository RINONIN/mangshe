"""
作者：RINO
日期: 2022年02月23日
时间: 09:37
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

plt.figure()
plt.plot(x, y1)
plt.show()

plt.figure(num='aba', figsize=(5, 5),)
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
plt.show()