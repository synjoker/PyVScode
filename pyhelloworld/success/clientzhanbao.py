from socket import *
import json
import struct

BUFSIZE = 1024
PORT = 1060
ip_port = ('192.168.1.115', PORT)



client = socket(AF_INET, SOCK_STREAM)
client.connect(ip_port)

while True:
    # cmd = input('please enter your cmd you want>>>')
    cmd = 'hello!'

    if len(cmd) == 0: continue

    client.send(cmd.encode('utf-8'))

    # 1. 先收4个字节，这4个字节中包含报头的长度
    header_len = struct.unpack('i', client.recv(4))[0]

    # 2. 再接收报头
    header_bytes = client.recv(header_len)

    # 3. 从包头中解析出想要的东西
    header_json = header_bytes.decode('utf-8')
    header_dict = json.loads(header_json)
    total_size = header_dict['total_size']

    # 4. 再收真实的数据
    recv_size = 0
    res = b''
    while recv_size < total_size:
        data = client.recv(1024)

        res += data
        recv_size += len(data)

    print(res.decode('utf-8','ignore'))

client.close()