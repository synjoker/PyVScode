#客户端融合代码（稿一）
import threading
import time
import serial
import socket
import sys
import struct
import os
import cv2

BUFSIZE = 1024
IP0 = ('0.0.0.0') # 需要连接啥IP在这里修改
IP1 = ('127.0.0.1')
PORT = 18888
IPORT = (IP0, PORT)

def GnssData(client):
    sergps = serial.Serial("COM7",115200, timeout=5)  # 开启com7口，波特率460800，超时5
    sergps.flushInput()  # 清空缓冲区
    serpic = serial.Serial("COM3", 115200, timeout=5)  # 开启com3口，波特率115200，超时5
    serpic.flushInput()  # 清空缓冲区
    # # 准备头文件并发送
    # filepath = 'gps'
    # fhead = struct.pack('32si', os.path.basename(filepath).encode('utf-8'), 79)
    # client.send(fhead)
    while True:
        count = serpic.inWaiting()  # 获取串口缓冲区数据
        if count != 0:
            t1 = threading.Thread(target=CameraData, args=(client, ))#实列化进程
            t1.run()
            continue
        count = sergps.inWaiting()  # 获取串口缓冲区数据
        if count != 0:
            # 读出串口数据，数据采用gbk编码
            recvgps = sergps.read(sergps.in_waiting).decode("gbk")
            print(recvgps)
            if recvgps[0] != '$' or count != 79:
                continue
            else:
                client.send(recvgps.encode('utf-8'))
        time.sleep(0.2)
        continue# 延时0.1秒，免得CPU出问题
        
def CameraData(client):
    while True:
        count = serpic.inWaiting()  # 获取串口缓冲区数据
        if count != 0:
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            # # 展示图片
            # cv2.imshow("capture", frame)
            while cv2.waitKey(1) != 0:
                # 存储图片
                cv2.imwrite("camera.jpg", frame)
            
            print(client.recv(1024))

            # 需要传输的文件路径
            filepath = 'camera.jpg'
            # 判断是否为文件
            if os.path.isfile(filepath):
                # 定义定义文件信息。128s表示文件名为128bytes长，l表示一个int或log文件类型，在此为文件大小
                fileinfo_size = struct.calcsize('32si')
                # 定义文件头信息，包含文件名和文件大小
                fhead = struct.pack('32si', os.path.basename(filepath).encode('utf-8'), os.stat(filepath).st_size)
                # 发送文件名称与文件大小
                client.send(fhead)

                # 将传输文件以二进制的形式分多次上传至服务器
                fp = open(filepath, 'rb')
                while 1:
                    data = fp.read(1024)
                    if not data:
                        print('{0} file send over...'.format(os.path.basename(filepath)))
                        break
                    client.send(data)
                # 关闭当期的套接字对象
                client.close()

def main():
    # myname = socket.getfqdn(socket.gethostname())
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(IPORT)
    #myaddr = socket.gethostbyname(myname)#本机ip
    while True:
        t0 = threading.Thread(target=GnssData, args=(client, ))#实列化进程
        t0.run()


if __name__=='__main__':
    main()