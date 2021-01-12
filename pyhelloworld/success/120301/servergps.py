import threading
import time
import struct
import sys
import socket
import serial

"""
客户端发送两个数据包，分别是txt数据和jpg数据，当检测为txt时，
调用server_gps接收gps信号并解包，在服务端读取检测到jpg时触发
启动线程，调用server_pic函数,接收完图片后关闭线程。
"""
BUFSIZE = 1024
IP0 = ('0.0.0.0')
IP1 = ('127.0.0.1')
PORT = 8888
IPORT = (IP0, PORT)

# def serverinit():
#     try:
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         s.bind(IPORT)
#         s.listen(10)
#         return s
#     except socket.error as msg:
#         print(msg)
#         sys.exit(1)

def serverpic(conn, addr, filename, filesize):
    """
    输入：conn， addr——socket对象和地址
         filename， filesize——文件格式、文件大小
    """
    while True:
        try:
            recvd_size = 0  # 定义已接收文件的大小
            # 存储在该脚本所在目录下面
            fp = open('./' + str(filename), 'wb')
            print('pic start receiving...')

            # 将分批次传输的二进制流依次写入到文件
            while not recvd_size == filesize:
                if filesize - recvd_size > 1024:
                    data = conn.recv(1024)
                    recvd_size += len(data)
                else:
                    data = conn.recv(filesize - recvd_size)
                    recvd_size = filesize
                fp.write(data)
            fp.close()
            print('pic end receive...')
        except ConnectionResetError:
            print('导航信息输入错误')
            break

def servergps(conn, addr, filename, filesize):

    print('threading-gps is running!')
    while True:
        try:
            data = conn.recv(filesize)
            print('收到导航信息：', data.decode('utf-8'))
        except ConnectionResetError:
            print('导航信息输入错误')
            break

def judgement(conn, addr):
    """
    conn:64si
    """
    # 收到请求后的回复
    conn.send('Hi, Welcome to the server!'.encode('utf-8'))
    fileinfo_size = struct.calcsize('32si')
    buf = conn.recv(fileinfo_size)
    if buf:
        filename, filesize = struct.unpack('32si', buf)
        fn = filename.strip(b'\00')
        fn = fn.decode()
        print('file  name is {0}, filesize if {1}'.format(str(fn), filesize))

        if fn[-3:] == 'jpg':
            return str(filename), filesize
        return str(''), filesize

def main():
    # sock = serverinit()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(IPORT)
    sock.listen(10)
    while True:
        conn, addr = sock.accept()#接受TCP连接并返回（conn,address）,其中conn是新的套接字对象，可以用来接收和发送数据。address是连接客户端的地址。
        print('make connection from {0}'.format(addr))
        judgename, size = judgement(conn, addr)
        """
        cli:1.接受gps 产生包头 发送包头 ？？包头文件和gps信号是否会冲突 接受gps
        ser:1.接收包头 执行judgement 2.判断执行程序
        """
        if judgename.endswith('jpg'):
            t1 = threading.Thread(target=serverpic, args=(conn, addr, judgename, size))
            t1.start()
            t1.join()
            continue

        t0 = threading.Thread(target=servergps, args=(conn, addr, judgename, size))
        t0.start()
        t0.join()

if __name__ == "__main__":
    main()