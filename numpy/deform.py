"""
作者：RINO
日期: 2021年11月15日
"""
import numpy as np

"""
改变形态
array[np.newaxis, :]
array.reshape()
array.ravel(), array.flatten()
array.transpose()
合并
np.column_stack(), np.row_stack()
np.vstack(), np.hstack(), np.stack()
np.concatenate()
拆解
np.vsplit(), np.hsplit(), np.split()
改变形态 
"""
# # 增维
# a = np.array([1, 2, 3, 4, 5, 6])
# a_2d = a[np.newaxis, :]
# print(a.shape, a_2d.shape)
#
# a = np.array([1, 2, 3, 4, 5, 6])
# a_none = a[:, None]
# a_expand = np.expand_dims(a, axis=1)
# print(a_none.shape, a_expand.shape)
# # 降维
# a_squeeze = np.squeeze(a_expand)
# a_squeeze_axis = a_expand.squeeze(axis=1)
# print(a_squeeze.shape)
# print(a_squeeze_axis.shape)
# # 改变维度
# a = np.array([1, 2, 3, 4, 5, 6])
# a1 = a.reshape([6, 1])
# a2 = a.reshape([6, 1, 1])
# print("a1 shape:", a1.shape)
# print(a1)
# print("a2 shape:", a2.shape)
# print(a2)
# 矩阵转置
# a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape([3, 3])
# aT1 = a.T
# aT2 = np.transpose(a)
# print(aT1)
# print(aT2)
# 合并
# feature_a = np.array([1,2,3,4,5,6])
# feature_b = np.array([11,22,33,44,55,66])
# c_stack = np.column_stack([feature_a, feature_b])
# print(c_stack)
#
# sample_a = np.array([0, 1.1])
# sample_b = np.array([1, 2.2])
# c_stack = np.row_stack([sample_a, sample_b])
# print(c_stack)
# # hstack和vstack需要保证维度信息是正确的才能合并
# feature_a = np.array([1,2,3,4,5,6])[:, None]
# feature_b = np.array([11,22,33,44,55,66])[:, None]
# c_stack = np.hstack([feature_a, feature_b])
# print(c_stack)
#
# sample_a = np.array([0, 1.1])[None, :]
# sample_b = np.array([1, 2.2])[None, :]
# c_stack = np.vstack([sample_a, sample_b])
# print(c_stack)

# a = np.array([
#     [1, 2],
#     [3, 4]
# ])
# b = np.array([
#     [5, 6],
#     [7, 8]
# ])
#
# print(np.concatenate([a, b], axis=0))
# print(np.concatenate([a, b], axis=1))

# 拆解
# a = np.array(
#     [[1, 11, 2, 22],
#      [3, 33, 4, 44],
#      [5, 55, 6, 66],
#      [7, 77, 8, 88]]
# )
# print(np.vsplit(a, indices_or_sections=2))  # 分成两段
# print(np.vsplit(a, indices_or_sections=[1, 3]))  # 0~2 一段，2~3 一段，3~一段

a = np.array(
    [[1, 11, 2, 22],
     [3, 33, 4, 44],
     [5, 55, 6, 66],
     [7, 77, 8, 88]]
)
print(a)
print(np.split(a, indices_or_sections=2, axis=0))  # 分成两段
print(np.split(a, indices_or_sections=[2, 3], axis=0))  # 在第二维度， 0~2 一段，2~3 一段，3~一段
