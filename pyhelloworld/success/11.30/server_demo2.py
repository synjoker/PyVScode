from socket import  *
import subprocess
import struct
server_socket=socket(AF_INET,SOCK_STREAM)
server_socket.bind(('0.0.0.0',8003))
server_socket.listen(5)
 
while True:
    # try:
    #     con,addr=server_socket.accept()
    #     while True:
    #         data=con.recv(1024)
    #         if not data:break
    #         cmd=data.decode('utf-8')
    #         print(cmd)
    #         p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    #         res_err=p.stderr.read()
    #         print(res_err)
    #         res = p.stdout.read()
    #         if res_err:
    #             res=res_err
    #         elif not res_err and not res:
    #             res='run success'.encode('gbk')
    #         size=len(res)
    #         print(size)
    #         length=struct.pack('i',size)
    #         con.send(length)
    #         con.send(res)
    #     con.close()
    # except Exception  as e:
    #      print(e)
    #      continue
    read_sockets, write_sockets, error_sockets = select.select(connected_clients_sockets, [], [])	
	
    for sock in read_sockets:	
	
        if sock == server_socket:	
	
            sockfd, client_address = server_socket.accept()	
            connected_clients_sockets.append(sockfd)	
	
        else:	
            try:	
	
                data = sock.recv(4096)	
                txt = str(data)	
	
                if data:	
	
                    if data.startswith('SIZE'):	
                        tmp = txt.split()	
                        size = int(tmp[1])	
	
                        print 'got size'	
	
                        sock.sendall("GOT SIZE")	
	
                    elif data.startswith('BYE'):	
                        sock.shutdown()	
	
                    else :	
	
                        myfile = open(basename % imgcounter, 'wb')	
                        myfile.write(data)	
	
                        data = sock.recv(40960000)	
                        if not data:	
                            myfile.close()	
                            break	
                        myfile.write(data)	
                        myfile.close()	
	
                        sock.sendall("GOT IMAGE")	
                        sock.shutdown()	
            except:	
                sock.close()	
                connected_clients_sockets.remove(sock)	
                continue	
        imgcounter += 1	
server_socket.close()