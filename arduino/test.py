"""
作者：RINO
日期: 2022年03月21日
时间: 10:57
"""
import serial

serialPort = "COM5"  # 串口
baudRate = 9600  # 波特率
ser = serial.Serial(serialPort, baudRate, timeout=0.5)
print("参数设置：串口=%s ，波特率=%d" % (serialPort, baudRate))

demo1 = b"0"  # 将0转换为ASCII码方便发送
demo2 = b"1"  # 同理
while 1:
    c = input('请输入指令:')
    c = ord(c)  # 将c转换为UTF-8标准数字
    if c == 48:
        ser.write(demo1)  # ser.write在于向串口中写入数据
    if c == 49:
        ser.write(demo2)
