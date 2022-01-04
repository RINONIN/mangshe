"""
作者：RINO
日期: 2022年01月04日
时间: 15:13
"""


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        # 这里我们得处理一个异常
        if b == 0:
            print("b cannot be 0")
        else:
            return a / b

        # 生产一个实例


c = Calculator()
print(c.add(1, 2))
print(c.divide(1, 2))
c.divide(1, 0)


class Calculator1:
    def subtract(self, a, b):
        return a - b

    def batch_subtract(self, a_list, b_list):
        res_list = []
        for i in range(len(a_list)):
            res_list.append(self.subtract(a_list[i], b_list[i]))
        return res_list


c = Calculator1()
print(c.subtract(2, 1))
print(c.batch_subtract([3, 2, 1], [2, 3, 4]))