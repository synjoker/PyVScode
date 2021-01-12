# https://www.cnblogs.com/zhouxuchong/p/11576275.html
from socket import *
import subprocess
import struct
import json

server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 8000))
server.listen(5)

print('start...')
while True:
    conn, client_addr = server.accept()
    print(conn, client_addr)

    while True:
        cmd = conn.recv(1024)

        obj = subprocess.Popen(cmd.decode('utf8'),
                               shell=True,
                               stderr=subprocess.PIPE,
                               stdout=subprocess.PIPE)

        stderr = obj.stderr.read()
        stdout = obj.stdout.read()

        # 制作报头
        header_dict = {
            'filename': 'a.txt',
            'total_size': len(stdout) + len(stderr),
            'hash': 'xasf123213123'
        }
        header_json = json.dumps(header_dict)
        header_bytes = header_json.encode('utf8')

        # 1. 先把报头的长度len(header_bytes)打包成4个bytes，然后发送
        conn.send(struct.pack('i', len(header_bytes)))
        # 2. 发送报头
        conn.send(header_bytes)
        # 3. 发送真实的数据
        conn.send(stdout)
        conn.send(stderr)

    conn.close()

server.close()
