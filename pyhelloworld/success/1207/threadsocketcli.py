import socket
from multiprocessing import Process

IP = '127.0.0.1'
BUFSIZE = 1024
def processsocket(PORT, args):
    print("process {} is running".format(args))
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    client.bind((IP, PORT))
    client.listen(5)
    print("process {} is listening at {}".format(args, (IP, PORT)))
    while True:
        conn, addr = client.accept()
        print('make connection from {}.{}'.format(addr, PORT))



if __name__ == "__main__":
    t1 = Process(target=processsocket, args=(8009, '1'))
    t2 = Process(target=processsocket, args=(8010, '2'))
    t1.start()
    t2.start()
    
    print('end socket')