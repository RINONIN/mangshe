"""
作者：RINO
日期: 2022年02月23日
时间: 09:40
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2
#
# plt.figure()
# plt.plot(x, y2)
# plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

# plt.xlim((-1, 2))
# plt.ylim((-2, 3))
# plt.xlabel('I am x')
# plt.ylabel('I am y')
# plt.show()

# new_ticks = np.linspace(-1, 2, 5)
# print(new_ticks)
# plt.xticks(new_ticks)
# plt.yticks([-2, -1.8, -1, 1.22, 3], [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])
# plt.show()

plt.figure()
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
plt.xlim((-1, 2))
plt.ylim((-2, 3))

new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3], [r'$really\ bad$', '$bad$', '$normal$', '$good$', r'$really\ good$'])
ax = plt.gca()

ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')


# set the coordinate number position
ax.xaxis.set_ticks_position('bottom')
# set the spines position
ax.spines['top'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['right'].set_position(('data', 0))
plt.show()



