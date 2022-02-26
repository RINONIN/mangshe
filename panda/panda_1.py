"""
作者：RINO
日期: 2022年03月14日
时间: 09:14
"""
''''''
# 在 Numpy 中， 如果你不特别在其他地方标注，你是不清楚记录的这里边记录的是什么信息的。
# 而 Pandas 记录的信息可以特别丰富， 你给别人使用传播数据的时，这些信息也会一起传递过去。或者你自己处理数据时对照着信息来加工数据，也会更加友善。
# 这就是在我看来 Pandas 对比 Numpy 的一个最直观的好处。
# 另外 Pandas 用于处理数据的功能也比较多，信息种类也更丰富，特别是你有一些包含字符的表格，Pandas 可以帮你处理分析这些字符型的数据表。
# 当然还有很多其它功能，比如处理丢失信息，多种合并数据方式，读取和保存为更可读的形式等等。
# 这些都让 Pandas 绽放光彩。但是，Pandas 也有不足的地方：运算速度稍微比 Numpy 慢。
''''''

import pandas as pd
import numpy as np

a_list = [1, 2, 3]
a_dict = {"a": 1, "b": 2, "c": 3}
print("list:", a_list)
print("dict:", a_dict)

a_array = np.array([
    [1, 2],
    [3, 4]
])
# panda有标签 而numpy没有
a_df = pd.DataFrame(
    {"a": [1, 3],
     "b": [2, 4]}
)

print("numpy array:\n", a_array)
print("\npandas df:\n", a_df)
