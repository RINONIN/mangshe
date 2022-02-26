"""
作者：RINO
日期: 2022年02月26日
时间: 13:46
"""
import numpy as np
import time

t0 = time.time()
# python list
l = list(range(100))
for _ in range(10000):  # "_" is a kind of circular sign
    for i in range(len(l)):
        l[i] += 1

t1 = time.time()
# numpy array
a = np.array(l)
for _ in range(10000):
    a += 1

print("Python list spend {:.3f}s".format(t1-t0))
print("Numpy array spend {:.3f}s".format(time.time()-t1))