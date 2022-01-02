"""
作者：RINO
日期: 2022年01月01日
时间: 18:51
"""


# class Video:
#     def __init__(self, name, window_size=(1080, 720)):
#         self.name = name
#         self.window_size = window_size
#         self.create_time = "today"
#
#
# class Text:
#     def __init__(self, name, language="zh-cn"):
#         self.name = name
#         self.language = language
#         self.create_time = "today"


class File:
    def __init__(self, name, create_time="today"):
        self.name = name
        self.create_time = create_time

    def get_info(self):
        return self.name + " is created at " + self.create_time


class Video(File):  # 继承了 File 的属性和功能
    def __init__(self, name, window_size=(1080, 720)):
        # 将共用属性的设置导入 File 父类
        super().__init__(name=name, create_time="today")
        self.window_size = window_size


class Text(File):  # 继承了 File 的属性和功能
    def __init__(self, name, language="zh-cn"):
        # 将共用属性的设置导入 File 父类
        super().__init__(name=name, create_time="today")
        self.language = language

    # 也可以在子类里复用父类功能
    def get_more_info(self):
        return self.get_info() + ", using language of " + self.language


v = Video("my_video")
t = Text("my_text")
print(v.get_info())  # 调用父类的功能
print(t.create_time)  # 调用父类的属性
print(t.language)  # 调用自己的属性
print(t.get_more_info())  # 调用自己加工父类的功能


class File:
    def __init__(self):
        self.name = "f1"
        self.__deleted = False  # 我不让别人用这个变量
        self._type = "txt"  # 我不想别人使用这个变量

    def delete(self):
        self.__force_delete()

    def __force_delete(self):  # 我不让别人使用这个功能
        self.__deleted = True
        return True

    def _soft_delete(self):  # 我不想让别人使用这个功能
        self.__force_delete()  # 我自己可以在内部随便调用
        return True


f = File()
print(f._type)  # 可以拿到值，但是这个类的作者不想让你直接这样拿到
print(f._soft_delete())  # 可以调用，但是这个类的作者不想让你直接调用

# 接下来的两个实验都会报错
# f.__deleted
# f.__force_delete()
