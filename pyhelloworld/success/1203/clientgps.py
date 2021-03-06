#客户端融合代码（稿一）
import threading
import time
import re
import serial
import socket
import sys
import struct
import os
import cv2

BUFSIZE = 1024
IP0 = ('0.0.0.0') # 连接外机
IP1 = ('127.0.0.1') # 本机测试
IP2 = ('10.49.33.80') #外机IP
PORT = 8899 # 默认端口8899
IPORT = (IP1, PORT)

def GnssData():
    # 开启com3口，波特率115200，超时5
    ser = serial.Serial("COM7",460800, timeout=5)  
    ser.flushInput()  # 清空缓冲区
    # 获取本机ip
    myname = socket.getfqdn(socket.gethostname())
    myaddr = socket.gethostbyname(myname)
    # 开启socket通信
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(IPORT)
    # 准备头文件并发送
    filepath = 'gps'
    fhead = struct.pack('32si', os.path.basename(filepath).encode('utf-8'), len(recvgps))
    client.send(fhead)
    print('头文件发送成功！！')
    while True:
        # 获取串口缓冲区数据
        count = ser.inWaiting()  
        if count != 0:
            # 读出串口数据，数据采用gbk编码
            recvgps = ser.read(ser.in_waiting).decode("gbk")
            client.send(recvgps.encode('utf-8'))
        # 延时0.2秒，免得CPU出问题
        time.sleep(0.2) 

def CameraData():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(IPORT)
        print('连接成功')
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    cap = cv2.VideoCapture(1)
    ret, frame = cap.read()
    # # 展示图片
    # cv2.imshow("capture", frame)
    while cv2.waitKey(1) != 0:
        # 存储图片
        cv2.imwrite("camera.jpg", frame)
    
    print(sock.recv(1024))

    # 需要传输的文件路径
    filepath = 'camera.jpg'

    # 判断是否为文件
    if os.path.isfile(filepath):
        # 定义定义文件信息。128s表示文件名为32bytes长，l表示一个int或log文件类型，在此为文件大小
        fileinfo_size = struct.calcsize('32si')
        # 定义文件头信息，包含文件名和文件大小
        fhead = struct.pack('32si', os.path.basename(filepath).encode('utf-8'), os.stat(filepath).st_size)
        # 发送文件名称与文件大小
        sock.send(fhead)

        # 将传输文件以二进制的形式分多次上传至服务器
        fp = open(filepath, 'rb')
        while 1:
            data = fp.read(1024)
            if not data:
                print('{0} file send over...'.format(os.path.basename(filepath)))
                break
            sock.send(data)
        # 关闭当期的套接字对象
        s.close()

def main():
    while True:
      ser = serial.Serial("COM3", 115200, timeout=0.1)
      ser.flushInput()
      count = ser.inWaiting()
      if count != 0:
        t1 = threading.Thread(target=CameraData)#实列化进程
        t1.start()
        t1.join()
        continue
      else:
         t0 = threading.Thread(target= GnssData)#实列化进程
         t0.start()
         t0.join()

if __name__=='__main__':
    main()