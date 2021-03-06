#coding:utf-8

import socket, traceback, time

host = '127.0.0.1'
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

while 1:
    try:
        clientsock, clientaddr = s.accept()

        print "Got connection from", clientsock.getpeername()
        while 1:
            try:
                clientsock.sendall(time.asctime() + "\n")
            except:
                break
            time.sleep(5)

        clientsock.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
