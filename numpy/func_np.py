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

# cars = np.array([5, 10, 12, 6])
# print("数据：", cars, "\n维度：", cars.ndim)
#
# cars1 = np.array([
# [5, 10, 12, 6],
# [5.1, 8.2, 11, 6.3],
# [4.4, 9.1, 10, 6.6]
# ])
#
# print("数据：\n", cars1, "\n维度：", cars1.ndim)

# cars = np.array([
#     [
#         [5, 10, 12, 6],
#         [5.1, 8.2, 11, 6.3],
#         [4.4, 9.1, 10, 6.6]
#     ],
#     [
#         [6, 11, 13, 7],
#         [6.1, 9.2, 12, 7.3],
#         [5.4, 10.1, 11, 7.6]
#     ],
# ])
#
# print("总维度：", cars.ndim)
# print("场地 1 数据：\n", cars[0], "\n场地 1 维度：", cars[0].ndim)
# print("场地 2 数据：\n", cars[1], "\n场地 2 维度：", cars[1].ndim)

cars1 = np.array([5, 10, 12, 6])
cars2 = np.array([5.2, 4.2])
cars = np.concatenate([cars1, cars2])
print(cars)

test1 = np.array([5, 10, 12, 6])
test2 = np.array([5.1, 8.2, 11, 6.3])

# 首先需要把它们都变成二维，下面这两种方法都可以加维度
# 扩展维度 后面的参数是增加维度数，0加一维，1加二维
test1 = np.expand_dims(test1, 0)
# 增加维度
test2 = test2[np.newaxis, :]
test3 = np.expand_dims(test1, 1)

print("test1加维度后 ", test1)
print("test2加维度后 ", test2)
# print("test3加维度后 ", test3)

# 然后再在第一个维度上叠加
all_tests = np.concatenate([test1, test2])
print("括展后\n", all_tests)

print("第一维度叠加：\n", np.concatenate([all_tests, all_tests], axis=0))
print("第二维度叠加：\n", np.concatenate([all_tests, all_tests], axis=1))