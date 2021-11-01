"""
作者：RINO
日期: 2021年11月15日
"""
import numpy as np
# np.max(a), np.min(a)
# a.max(), a.min()
# a = np.array([150, 166, 183, 170])
# print("最大：", np.max(a))
# print("最小：", a.min())
# print(a.sum())
#
# a = np.array([150, 166, 183, 170])
# print("累乘：", a.prod())
# print("总数：", a.size)
#
# a = np.array([0, 1, 2, 3])
# print("非零总数：", np.count_nonzero(a))
# month_salary = [1.2, 20, 0.5, 0.3, 2.1]
# print("平均工资：", np.mean(month_salary))
# print("工资中位数：", np.median(month_salary))
# month_salary = [1.2, 20, 0.5, 0.3, 2.1]
# print("标准差：", np.std(month_salary))
# 将序号最大或最小的值输出
a = np.array([150, 166, 183, 170])
name = ["小米", "OPPO", "Huawei", "诺基亚"]
high_idx = np.argmax(a)
low_idx = np.argmin(a)
print("{} 最高".format(name[high_idx]))
print("{} 最矮".format(name[low_idx]))

a = np.array([150.1, 166.4, 183.7, 170.8])
# ceil是向上取最大整数，floor是向下取最大整数
print("ceil:", np.ceil(a))
print("floor:", np.floor(a))
# 截取值的上下限
a = np.array([150.1, 166.4, 183.7, 170.8])
print("clip:", a.clip(160, 180))