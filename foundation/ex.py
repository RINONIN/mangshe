"""
作者：RINO
日期: 2021年09月14日
"""


print('hello world')


import requests

# print('hello world')
# 命令行编程

# print(sys.argv)
# print(sys.argv[1])

# 三方库引用
response = requests.get("http://www.baidu.com")
print(response.text)

