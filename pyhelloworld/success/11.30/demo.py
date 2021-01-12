import threading
import time
import struct
import sys
import socket
"""
客户端发送两个数据包，分别是txt数据和jpg数据，当检测为txt时，
调用server_gps接收gps信号并解包，在服务端读取检测到jpg时触发
启动线程，调用server_pic函数,接收完图片后关闭线程。
"""
BUFSIZE = 1024
IP0 = ('0.0.0.0')
IP1 = ('127.0.0.1')
PORT = 8003
IPORT = (IP1, PORT)

def serverinit():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(IPORT)
        s.listen(10)
        return s
    except socket.error as msg:
        print (msg)
        sys.exit(1)

def serverpic(conn, addr):
    """
    """
    print('threading-pic is running!')

    buf = conn.recv(fileinfo_size)
    # 判断是否接收到文件头信息
    if buf:
        # 获取文件名和文件大小
        filename, filesize = struct.unpack('64si', buf)
        fn = filename.strip(b'\00')
        fn = fn.decode()
        print ('file new name is {0}, filesize if {1}'.format(str(fn),filesize))

        recvd_size = 0  # 定义已接收文件的大小
        # 存储在该脚本所在目录下面
        fp = open('./' + str(fn), 'wb')
        print ('pic start receiving...')
        
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
        print ('pic end receive...')
    
def servergps(conn, addr, size):
    """
    """
    print('threading-gps is running!')
    
def judgement(conn, addr):
    """
    conn:64si
    """
    # 收到请求后的回复
    conn.send('Hi, Welcome to the server!'.encode('utf-8'))
    fileinfo_size = struct.calcsize('64si')
    buf = conn.recv(fileinfo_size)
    if buf:
        filename, filesize = struct.unpack('64si',buf)
        fn = filename.strip(b'\00')
        fn = fn.decode()
        if fn[-3:] == 'jpg':
            return str('recvjpg'), filesize

        return str(''), filesize
        
def main():
    sock = serverinit()
    while True:
        conn, addr = sock.accept()
        print('make connection from {0}'.format(addr))
        judge, size = judgement(conn, addr)
        if judge == 'recvjpg':
            t1 = threading.Thread(target=serverpic, args=(conn, addr))
            t1.start()
            t1.join()
            continue
        else:
            servergps(conn, addr, size)

if __name__ == "__main__":
    main()