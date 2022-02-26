"""
作者：RINO
日期: 2022年03月21日
时间: 12:32
"""
from pyfirmata import Arduino
import time

board = Arduino('COM5')
while 1:
    board.digital[13].write(0)  # 向端口13写入0   0代表灭灯
    time.sleep(1)
    board.digital[13].write(1)  # 向端口13写入1   1代表亮灯
    time.sleep(1)
