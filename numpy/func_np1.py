"""
作者：RINO
日期: 2021年11月08日
"""
import numpy as np

"""
创建数据
np.array()
array.ndim 返回维度
添加数据
np.concatenate()
np.expand_dims()
合并数据
np.concatenate()
np.vstack()
np.hstack()
观察形态
array.size
array.shape
"""

# a = np.array([[1, 2, 3], [4, 5, 6]])
# b = np.array([[7, 8], [9, 10]])
# # 这个没问题
# print(a)
# print(b)
# print(np.concatenate([a, b], axis=1))
# # np.vstack 竖直合并
# # np.hstack 水平合并
# a = np.array([
#     [1, 2],
#     [3, 4]
# ])
# b = np.array([
#     [5, 6],
#     [7, 8]
# ])
# print("竖直合并\n", np.vstack([a, b]))
# print("水平合并\n", np.hstack([a, b]))

cars = np.array([
    [5, 10, 12, 6],
    [5.1, 8.2, 11, 6.3],
    [4.4, 9.1, 10, 6.6]
])

count = 0
for i in range(len(cars)):
    for j in range(len(cars[i])):
        count += 1
print("总共多少测试数据：", count)
print("总共多少测试数据：", cars.size)

print("第一个维度：", cars.shape[0])
print("第二个维度：", cars.shape[1])
print("所有维度：", cars.shape)
