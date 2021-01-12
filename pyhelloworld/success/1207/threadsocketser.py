import threading
import socket

IP = '127.0.0.1'
BUFSIZE = 1024
def threadsocket(PORT, args):
    print("thread {} is running".format(args))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((IP, PORT))
    sock.listen(5)
    print("thread {} is listening at {}".format(args, (IP, PORT)))
    while True:
        conn, addr = sock.accept()
        print('make connection from {}.{}'.format(addr, PORT))



if __name__ == "__main__":
    t1 = threading.Thread(target=threadsocket, args=(8009, '1'))
    t2 = threading.Thread(target=threadsocket, args=(8010, '2'))
    t1.start()
    t2.start()
    
    print('end socket')