#coding:utf-8

import socket, sys

port = 51423
host = 'localhost'
data = "x" * 10485760

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

bytesSent = 0

while bytesSent < len(data):
    startpos = bytesSent
    endpos = min(bytesSent + 1024, len(data))
    bytesSent += s.send(data[startpos:endpos])
    sys.stdout.write("Wrote %d bytes\r" % bytesSent)
    sys.stdout.flush()
    
s.shutdown(1)

print "All data sent."

while 1:
    buf = s.recv(1024)
    if not len(buf):
        break

    sys.stdout.write(buf)
