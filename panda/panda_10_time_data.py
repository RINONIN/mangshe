"""
作者：RINO
日期: 2022年03月23日
时间: 14:48
"""
# 读时间序列数据
# pd.to_datetime()
# 自建时间序列
# pd.date_range()
# 选取时间

import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# df = pd.DataFrame({
#     "time": ["2022/03/12", "2022/03/13", "2022/03/14"],
#     "value": [1,2,3]
# })
# print(df)
# print("\n\ntime:\n",df["time"])
#
# print(pd.to_datetime(df["time"]))
# print(pd.to_datetime(
#     ["2022/03/12", "2022.03.13", "14/03/2022"]
# ))  # 将非时间格式转化为时间格式


# spe=pd.to_datetime(
#     [
#         "1@21@2022%%11|11|32",
#         "12@01@2022%%44|02|2",
#         "4@01@2022%%14|22|2"
#     ],
#     format="%m@%d@%Y%%%%%S|%H|%M"  # 按照人为格式来解析
# )
# print(spe)
# %m 月
# %d 日
# %Y 年的全称
# %% 比配一个 %
# %S 秒
# %H 时
# %M 分



# start = datetime.datetime(2022, 3, 12)
# end = datetime.datetime(2022, 3, 18)
#
# index = pd.date_range(start, end)
# print(index)
#
# print(
#     "range(1, 10, 2)\n",
#     list(range(1, 10, 2))
# )
# print(
#     "\n\npd.date_range()\n",
#     pd.date_range(start, end, freq="48h")
# )
#
# print(
#     "np.linspace(-1, 1, 5)\n",
#     np.linspace(-1, 1, 5)
# )
# print(
#     "\n\npd.date_range(start, end, periods=5)\n",
#     pd.date_range(start, end, periods=5)
# )


# start = datetime.datetime(2022, 3, 1)
# end = datetime.datetime(2022, 5, 3)
#
# rng = pd.date_range(start, end)  #生成时间序列
# ts = pd.Series(np.random.randn(len(rng)), index=rng) #时间序列赋值
#
# print(ts.index)
# # ts.plot()
# ts[1:8].plot()
# plt.show()
# import datetime

# t1 = datetime.datetime(2022, 3, 12)
# t2 = datetime.datetime(2022, 3, 18)
# ts[t1: t2].plot()

# ts["2022-03-12": "2022-03-18"].plot()
# ts["2022-03"].plot()
# plt.show()

# 时间运算
# pd.Timedelta()
# dt.dayofyear; dt.dayofweek; dt.weekofyear; dt.weekday
# dt.strftime(); dt.day_name(); dt.month_name()
# 时区
# tz_localize(); tz_convert()
# pytz.country_timezones()

# rng = pd.date_range("2022-01-01", "2022-01-07")
# rng + pd.Timedelta(weeks=1)
#
# rng + 2*pd.Timedelta(days=3)
# rng = pd.date_range("2022-01-08", "2022-01-11")
# print(rng.dayofyear)
#
# print(rng.strftime("%m/%d/%Y"))# 按规则输出日期形式

rng = pd.date_range("2022-01-08", "2022-01-11")
print(rng.tz is None)

s = pd.to_datetime(
    ["2022/03/12 22:11", "2022/03/12 12:11", "2022/03/12 2:11"]
)
s_us = s.tz_localize("America/New_York")
print(s_us)

s_cn = s_us.tz_convert("Asia/Shanghai")
print(s_cn)

rng = pd.date_range(
    "2022-01-08", "2022-01-11",
    tz="America/New_York")
print(rng)