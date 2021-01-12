from socket import  *
import struct
socket_client=socket(AF_INET,SOCK_STREAM)
socket_client.connect(('192.168.1.115',8003))
while True:
    cmd=input('>>> ')
    socket_client.send(cmd.encode('utf-8'))
    data=socket_client.recv(4)
    if not data:break
    size=struct.unpack('i',data)[0]
    recv_size=0
    recv_msg=b''
    while recv_size<size:
        recv_msg +=socket_client.recv(1024)
        recv_size=len(recv_msg)
    print(recv_msg.decode('gbk'))
    # try:	
        
    #     # open image	
    #     myfile = open(image, 'rb')	
    #     bytes = myfile.read()	
    #     size = len(bytes)	
            
    #     # send image size to server	
    #     sock.sendall("SIZE %s" % size)	
    #     answer = sock.recv(4096)	
        
    #     print 'answer = %s' % answer	
        
    #     # send image to server	
    #     if answer == 'GOT SIZE':	
    #         sock.sendall(bytes)	
        
    #         # check what server send	
    #         answer = sock.recv(4096)	
    #         print 'answer = %s' % answer	
        
    #         if answer == 'GOT IMAGE' :	
    #             sock.sendall("BYE BYE ")	
    #             print 'Image successfully send to server'	
        
    #     myfile.close()	
        
    # finally:	
    #     sock.close()