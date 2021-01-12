import threading
import time
import re
import serial
import socket
import sys
import struct
import os
import cv2
#from yinyong import camera
def seRial():
    ser = serial.Serial("COM7",460800, timeout=5)  # 开启com3口，波特率115200，超时5
    ser.flushInput()  # 清空缓冲区
    myname = socket.getfqdn(socket.gethostname())
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('10.49.32.12', 8888))
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

def socket_client():
    cap = cv2.VideoCapture(1)
    ret, frame = cap.read()
    # 展示图片
    cv2.imshow("capture", frame)
    while cv2.waitKey(1) != 0:
        # 存储图片
        cv2.imwrite("camera.jpg", frame)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('10.49.32.12', 8003))
        # s.connect(('10.49.32.56', 1060))
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print(s.recv(1024))

    # 需要传输的文件路径
    filepath = 'camera.jpg'
    # 判断是否为文件
    if os.path.isfile(filepath):
        # 定义定义文件信息。128s表示文件名为128bytes长，l表示一个int或log文件类型，在此为文件大小
        fileinfo_size = struct.calcsize('128sl')
        # 定义文件头信息，包含文件名和文件大小
        fhead = struct.pack('128sl', os.path.basename(filepath).encode('utf-8'), os.stat(filepath).st_size)
        # 发送文件名称与文件大小
        s.send(fhead)

        # 将传输文件以二进制的形式分多次上传至服务器
        fp = open(filepath, 'rb')
        while 1:
            data = fp.read(1024)
            if not data:
                print('{0} file send over...'.format(os.path.basename(filepath)))
                break
            s.send(data)
        # 关闭当期的套接字对象
        s.close()


def main():
    ser = serial.Serial("COM5", 115200, timeout=5)
    ser.flushInput()
    while True:
      count = ser.inWaiting()
      if count != 0:
        x = threading.Thread(target=socket_client)
        x.start()
        continue
      else:
         y = threading.Thread(target= seRial)
         y.start()

if __name__=='__main__':
    main()
