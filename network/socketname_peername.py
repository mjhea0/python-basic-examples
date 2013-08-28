#coding:utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = socket.getservbyname('http', 'tcp')
s.connect(("www.google.com", port))

print "Connected from", s.getsockname()
print "Connected to", s.getpeername()
