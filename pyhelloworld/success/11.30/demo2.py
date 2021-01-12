import threading
import time
import socket
import struct
import sys

BUFSIZE = 1024
IP0 = ('0.0.0.0')
IP1 = ('127.0.0.1')
PORT = 8003
IPORT = (IP1, PORT)

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1',8003))

    # 需要传输的文件路径
    filepath = 'ThreadTest.jpg'
    # 定义定义文件信息。128s表示文件名为128bytes长，l表示一个int或log文件类型，在此为文件大小
    fileinfo_size = struct.calcsize('64si')
    # 定义文件头信息，包含文件名和文件大小
    fhead = struct.pack('64si', filepath.encode('utf-8'), 65536)
    # 发送文件名称与文件大小
    s.send(fhead)
    # 将传输文件以二进制的形式分多次上传至服务器
    print('send head already!')
    print(s.recv(BUFSIZE).decode('utf-8'))
    # while 1:
    #     data = fp.read(1024)
    #     if not data:
    #         print ('{0} file send over...'.format(os.path.basename(filepath)))
    #         break
    #     s.send(data)
    # # 关闭当期的套接字对象
    if input('>>>') == 'ok':
        s.close()



if __name__=='__main__':
    main()
