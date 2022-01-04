"""
作者：RINO
日期: 2022年01月04日
时间: 09:27
"""
import json

# data = {"filename": "f1.txt", "create_time": "today", "size": 111}
# j = json.dumps(data)
# print(j)
# print(type(j))
#
#
# data = {"filename": "f1.txt", "create_time": "today", "size": 111}
# with open("data.json", "w") as f:
#     json.dump(data, f)
#
# print("直接当纯文本读：")
# with open("data.json", "r") as f:
#     print(f.read())
#
# print("用 json 加载了读：")
# with open("data.json", "r") as f:
#     new_data = json.load(f)
# print("字典读取：", new_data["filename"])


class File:
    def __init__(self, name, create_time, size):
        self.name = name
        self.create_time = create_time
        self.size = size

    def change_name(self, new_name):
        self.name = new_name


data = File("f4.txt", "now", 222)
# # 存，会报错 但是 json 不能序列化保存 class 只能挑出来重要的信息，放到字典或列表里，然后再用 json 打包字典
# with open("data.json", "w") as f:
#     json.dump(data, f)

# 对比	Pickle	Json
# 存储格式	Python 特定的 Bytes 格式	通用 JSON text 格式，可用于常用的网络通讯中
# 数据种类	类，功能，字典，列表，元组等	基本和 Pickle 一样，但不能存类，功能
# 保存后可读性	不能直接阅读	能直接阅读
# 跨语言性	只能用在 Python	可以跨多语言读写
# 处理时间	长（需编码数据）	短（不需编码）
# 安全性	不安全（除非你信任数据源）	相对安全

