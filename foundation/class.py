"""
作者：RINO
日期: 2022年01月01日
时间: 18:32
"""


# class File:
#     def __init__(self):
#         self.name = "f1"
#         self.create_time = "today"
#
#
# my_file = File()
# print(my_file.name)
# print(my_file.create_time)
# my_file.name = "new_name"
# print(my_file.name)


class File:
    def __init__(self, name, create_time="today"):
        self.name = name
        self.create_time = create_time


my_file = File("my_file")
print(my_file.name)
print(my_file.create_time)


class File:
    def __init__(self, name, create_time="today"):
        self.name = name
        self.create_time = create_time

    def change(self, new_name):
        self.name = new_name


my_file = File("my_file")
# 调用实例中，类的功能
my_file.change("rino")
print(my_file.name)


class File:
    def __init__(self, name, create_time="today"):
        self.name = name
        self.create_time = create_time

    def get_info(self):
        return self.name + "is created at " + self.create_time


my_file = File("my_file")
print(my_file.get_info())
