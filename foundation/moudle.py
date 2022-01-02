"""
作者：RINO
日期: 2022年01月02日
时间: 13:53
"""
import file
import file as f1

from file import create_name

print(create_name())

print(file.create_name())
print("f1:", f1.create_name())


class File:
    def create_name(self):
        return "new_file.txt"


f2 = File()
print("f2:", f2.create_name())

from file import create_name, create_time

print(create_name())
print(create_time())
