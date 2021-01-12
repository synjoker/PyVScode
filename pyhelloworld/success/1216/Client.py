#客户端融合代码（稿一）
import threading
import time
import serial
import socket
import sys
import struct
import os
import cv2
#from yinyong import camera
def GnssData():
    ser = serial.Serial("COM7",115200, timeout=5)  # 开启com7口，波特率460800，超时5
    ser.flushInput()  # 清空缓冲区
    myname = socket.getfqdn(socket.gethostname())
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('10.49.54.15',8888))
    #myaddr = socket.gethostbyname(myname)#本机ip
    # 准备头文件并发送
    filepath = 'gps'
    fhead = struct.pack('32si', os.path.basename(filepath).encode('utf-8'), 79)
    client.send(fhead)

    while True:
        count = ser.inWaiting()  # 获取串口缓冲区数据
        if count != 0:
            # 读出串口数据，数据采用gbk编码
            recvgps = ser.read(ser.in_waiting).decode("gbk")
            print(recvgps)
            if recvgps[0] != '$' or count != 79:
                continue
            else:
                client.send(recvgps.encode('utf-8'))
        time.sleep(0.2)
        continue# 延时0.1秒，免得CPU出问题

def CameraData():
 ser = serial.Serial("COM3", 115200, timeout=5)  # 开启com3口，波特率115200，超时5
 ser.flushInput()  # 清空缓冲区
 while True:
    count = ser.inWaiting()  # 获取串口缓冲区数据
    if count != 0:
                cap = cv2.VideoCapture(0)
                ret, frame = cap.read()
                # 展示图片
                cv2.imshow("capture", frame)
                while cv2.waitKey(1) != 0:
                    # 存储图片
                    cv2.imwrite("camera.jpg", frame)
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect(('10.49.54.15', 8888))
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
    t1 = threading.Thread(target=CameraData)#实列化进程
    t1.start()
    t0 = threading.Thread(target= GnssData)#实列化进程
    t0.run()


if __name__=='__main__':
    main()