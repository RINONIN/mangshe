"""
作者：RINO
日期: 2021年12月13日
时间: 21:45
"""

import numpy as np

p = r'F:\mangshe\numpy\covid.csv'
# with open(p,encoding = 'utf-8') as f:
#     data = np.loadtxt(f,delimiter = ",")
#     print(data[:5])

# with open(p,encoding = 'utf-8') as f:
#     data = np.loadtxt(f,str,delimiter = ",", skiprows = 1)
#     print(data[:5])

with open(p, encoding='utf-8') as f:
    covid = np.loadtxt(f, str, delimiter=",")
    print(covid[:2])

print('数据标题：', covid[:0])
print('前两行数据:', covid[1:3])
print("一共数据行数（记录天数）：", len(covid[1:]))
print("记录开始日期：", covid[1][0], ";记录结束日期：", covid[-1][0])  # 第一个参数是行，第二个是列

print("日期列表摘取：", covid[1:5, 0])

data = np.array(covid)
dateindex = data[:, 0].tolist()
date_idx = dateindex.index('2020-01-22')  # 日期->索引转换
headerindex = data[0, :].tolist()
column_idx = headerindex.index("Confirmed")  # 标题->索引转换

# header = data[0]
# number = data[date_idx]

for header, number in zip(data[0], data[date_idx]):
    print(header, ":", number)

row_idx = dateindex.index("2020-01-24")  # 获取日期索引
column_idx = headerindex.index("Confirmed")  # 获取标题的索引
confirmed0124 = data[row_idx, column_idx]
print("截止 1 月 24 日的累积确诊数：", confirmed0124)

row_idx = dateindex.index("2020-04-30")  # 获取日期索引
column_idx = headerindex.index("New deaths")  # 获取标题的索引
result = data[row_idx, column_idx]
print("截止 4 月 30 日的新增死亡数：", result)

row1_idx = dateindex.index("2020-01-25")
row2_idx = dateindex.index("2020-04-29")
new_cases_idx = headerindex.index("New cases")

# 注意要 row1_idx+1 得到从 01-25 这一天的新增
# row2_idx+1 来包含 7 月 22 的结果
new_cases = (data[row1_idx + 1: row2_idx + 1, new_cases_idx])
new_case = []

i = 0
for i in range(0, len(new_cases)):
    new_case.append(1)
    new_case[i] = int(new_cases[i])

overall = np.sum(new_case)
print("共新增：", overall)

confirm_idx = headerindex.index("Confirmed")
confirmed = data[:, confirm_idx]
overall2 = int(confirmed[row2_idx]) - int(confirmed[row1_idx])
print("共新增：", overall2)

confirmed = data[:, confirm_idx]
new_cases = data[:, new_cases_idx]

for i in range(row1_idx, row2_idx + 1):
    diff = int(new_cases[i]) - (int(confirmed[i]) - int(confirmed[i - 1]))
    if diff != 0:
        print("date index:", i, ";差异：", diff)

new_cases_idx = headerindex.index("New cases")
new_recovered_idx = headerindex.index("New recovered")

# 比例
ratio = data[:, new_cases_idx] / data[:, new_recovered_idx]
print("比例样本：", ratio[:5])
