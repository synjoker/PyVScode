import threading
import time
import re
import serial
#from yinyong import camera
def seRial1():
    ser = serial.Serial("COM3", 115200, timeout=5)  # 开启com3口，波特率115200，超时5
    ser.flushInput()  # 清空缓冲区
    while True:
        count = ser.inWaiting()  # 获取串口缓冲区数据
        if count != 0:
            recv = ser.read(ser.in_waiting).decode("gbk")  # 读出串口数据，数据采用gbk编码
            print(time.time(), "磊哥数据：", recv)  # 打印一下子
        time.sleep(0.1)  # 延时0.1秒，免得CPU出问题
    # ser = serial.Serial("COM3", 115200, timeout=5)  # 开启com6口，波特率115200，超时5
    # ser.flushInput()  # 清空缓冲区
    # i = 0
    # while True:
    #     count = ser.inWaiting()  # 获取串口缓冲区数据
    #     if count != 0:
    #         recv = ser.read(ser.in_waiting).decode("gbk")  # 读出串口数据，数据decode成gbk编码
    #         print(recv)  # 打印一下子
    #         b = re.findall(r"\d+\.?\d*", recv)  # 获取打捆次数
    #         if 1:
    #             c = int(b[0])
    #             if c > i:
    #                 i = c
    #                 camera(1)  # print('调用摄像头')#调用摄像头
    #             else:
    #                 continue
    #     time.sleep(0.5)  # 延时0.1秒，免得CPU出问题
def seRial2():
    ser = serial.Serial("COM7",460800, timeout=5)  # 开启com3口，波特率115200，超时5
    ser.flushInput()  # 清空缓冲区
    while True:
        count = ser.inWaiting()  # 获取串口缓冲区数据
        if count != 0:
            recv = ser.read(ser.in_waiting).decode("gbk")  # 读出串口数据，数据采用gbk编码
            print(time.time(), " 导航数据：", recv)  # 打印一下子
        time.sleep(0.1)  # 延时0.1秒，免得CPU出问题
def main():
    x = threading.Thread(target=seRial1)
    y = threading.Thread(target=seRial2)
    x.start()
    y.start()

if __name__=='__main__':
    main()