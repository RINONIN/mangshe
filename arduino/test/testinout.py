import serial
import time

ser = serial.Serial('COM5', baudrate=9600, timeout=1)
time.sleep(3)
numPoints = 6
dataList = [0] * numPoints


def getvalues():
    ser.write(b'i')
    arduinoData = ser.readline().decode('ascii')

    return arduinoData


def outputvalues():
    ser.write(b'o')
    output = 250

    return output


while 1:

    userInput = input('Get data points?')

    if userInput == 'i':
        for i in range(0, numPoints):
            data = getvalues()
            dataList[i] = data

        print(dataList)

    if userInput == 'o':
        # num=0
        out = ['100', '100', '200', '200', '300', '300', '0', '0']
        out1 = ['0', '0', '0', '0', '0', '0', '0', '0']
        # out2=['100','200','300','400','500','0']
        for i in range(8):
            out1[i] = 'o' + out[i]
            # out2[i]='p'+out[i]

            print(out1[i])
            ser.write(out1[i].encode('utf-8'))
            time.sleep(2)

            # print(out2[i])
            # ser.write(out2[i].encode('utf-8'))
            # time.sleep(0.5)
            # num+=1
            # if num%2==0:
            # time.sleep(1)
