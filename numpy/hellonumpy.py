"""
作者：RINO
日期: 2021年11月08日
"""
# import numpy as np
# print(np.array([1, 2, 3]))
#
# my_list = [1, 2, 3]
# print(my_list[0])
#
# my_array = np.array([1, 2, 3])
# print(my_array[0])
#
# my_list[0] = -1
# my_array[0] = -1
# print(my_list)
# print(my_array)

import numpy as np
import time

t0 = time.time()
# python list
L = list(range(100))
for _ in range(10000):
    for i in range(len(L)):
        L[i] += 1
t1 = time.time()

# numpy array
a = np.array(L)
for _ in range(10000):
    a += 1

print("Python list spend {:.3f}s".format(t1 - t0))
print("Numpy array spend {:.3f}s".format(time.time() - t1))
