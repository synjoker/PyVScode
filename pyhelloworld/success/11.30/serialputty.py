import threading
import time
import re
import serial
# from socket import *
import socket
import struct

def seRial():
    ser = serial.Serial("COM7",460800, timeout=5)  # 开启com3口，波特率115200，超时5
    ser.flushInput()  # 清空缓冲区
    myname = socket.getfqdn(socket.gethostname())
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('10.49.55.125', 8888))
    while True:
        count = ser.inWaiting()  # 获取串口缓冲区数据
        # 获取本机ip
        myaddr = socket.gethostbyname(myname)
        if count != 0:
            recv1 = ser.read(ser.in_waiting).decode("gbk")  # 读出串口数据，数据采用gbk编码
            recv = myaddr + recv1
            head = struct.pack('i',len(recv))
            client.send(head)
            client.send(recv.encode('utf-8'))
        time.sleep(0.2)
        continue# 延时0.1秒，免得CPU出问题

   
if __name__=='__main__':
    # x = threading.Thread(target=seRial1)
    y = threading.Thread(target=seRial)
  #  x.start()
    y.start()