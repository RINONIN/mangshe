"""
作者：RINO
日期: 2022年02月14日
时间: 19:55
"""


# items = []  # 假设这里在记录一个很大的列表
# for item in range(5):
#     if item % 2 == 0:
#         items.append(item)
#
# for i in items:
#     print(i)

# 生成器能够将大规模的运算进行筛选，以减少内存
# def need_return():
#     for item in range(5):
#         if item % 2 == 0:
#             print("我要扔出去一个 item=%d 了" % item)
#             yield item  # 这里就会返回给下面的 for 循环
#             print("我又回到里面了")
#
#
# for i in need_return():
#     print("我在外面接到了一个 item=%d\n" % i)

def need_return():
    tmp = 2
    for item in range(300):
        if item == tmp:
            tmp *= item
            yield item


for i in need_return():
    print(i)
