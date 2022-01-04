"""
作者：RINO
日期: 2022年01月04日
时间: 15:47
"""
# %百分号模式
# "%s" % string
# format功能更多
# "{}".format()
# f格式化字符串
# f"{n}"
# 修改字符串
# string.strip()
# string.replace()
# string.lower()
# string.upper()
# string.split()
# ",".join([])
# string.startswith()
# string.endswith()

# -----------------------------------------

# name = "rino"
# print("我的名字是" + name + "！")
# print("我的名字是%s!" % name)
#
# name = "rino"
# age = 18
# gender = "男"
# print("我的名字是" + name + "！我" + str(age) + "岁了，我是" + gender + "的~")
# print("我的名字是%s ! 我%d岁了，我是%s的~" % (name, age, gender))
#
# name = "rino"  # 用字典格式来储存，无需担心顺序问题
# age = 18
# gender = "男"
# print("我的名字是 %(nm)s !我 %(age)d 岁了，我是 %(gd)s 的~" % {"nm": name, "age": age, "gd": gender})
#
# # %d	整数
# # %i	整数
# # %f	小数
# # %s	字符
#
# name = "rino"
# age = 18
# height = 1.8
# print("我的名字是 %s !我 %d 岁了，我 %f米高~" % (name, age, height))
# print("%f" % (1/3))     # 后面不限制
# print("%.2f" % (1/3))   # 后面限制 2 个位置
# print("%4d" % (1/3))    # 前面补全最大 4 个位置
# print("%5d" % 12)       # 前面补全最大 5 个位置

# -----------------------------------------
# name = "rinonin"
# age = 188
# height = 1.88
# print("我的名字是 %s !我 %d 岁了，我 %f 米高~" % (name, age, height))
# print("我的名字是 {} !我 {} 岁了，我 {} 米高~".format(name, age, height))
# # 放上数字有索引
# print("我的名字是 {0} !我 {1} 岁了，我 {2} 米高~我是{0}".format(name, age, height))


# name = "rinonin"
# age = 18
# height = 1.8
# print("我的名字是 {nm} !我 {age} 岁了，我 {ht} 米高~我是{nm}".format(nm=name, age=age, ht=height))
# print("我 {:.3f} 米高".format(1.12345))
# print("我 {ht:.1f} 米高".format(ht=1.12345))
# print("我 {:3d} 米高".format(1))
# print("我 {:3d} 米高".format(21))
#
# txt = "You scored {:%}"
# print(txt.format(2.1234))
#
# txt = "You scored {:.2%}"
# print(txt.format(2.1234))
#
#
# 方式	意思
# :,	每 3 个 0 就用逗号隔开，比如 1,000
# :b	该数字的二进制
# :d	整数型
# :f	小数模式
# :%	百分比模式

# -----------------------------------------

# name = "rinonin"
# age = 18
# height = 1.8
# print(f"我的名字是 {name} !我 {age} 岁了，我 {height} 米高~")
#
# print(f"我 {age} 岁了，明年我就{age + 1}岁了~")
#
# score = 2.1234
# print(f"You scored {score:.2%}")
# print(f"You scored {score:.3f}")
# print(f"You scored {12:5d}")

# -----------------------------------------

# 方式	意思
# strip	去除两端的空白符
# replace	替换字符
# lower	全部做小写处理
# upper	全部做大写处理
# title	仅开头的字母大写
# split	按要求分割
# join	按要求合并
# startswith	判断是否为某字段开头
# endswith	判断是否为某字段结尾

print("  我不想要前后的空白，但是  中间 的可以有 ".strip())
print("帮我替换掉莫烦".replace("莫烦", "沫凡"))
print("How ABOUT lower CaSe?".lower())
print("And upper CaSe?".upper())
print("do tiTle For me".title())
print("你|帮|我|拆分|一下|这句话".split("|"))
print(" ".join(["你","帮", "我", "重组", "一下", "这句话"]))

print("我在街头看到你".startswith("我在"))
print("我在街头看到你".startswith("街头"))
print("我在巷尾看到你".endswith("看到你"))
print("我在巷尾看到你".endswith("巷尾"))