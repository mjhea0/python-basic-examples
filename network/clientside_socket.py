#coding:utf-8

import sys
from socket import *

serverHost = 'localhost'
serverPort = 50008
message = ['Client Message1', 'Client Message2']
sSock = socket(AF_INET, SOCK_STREAM)

sSock.connect((serverHost, serverPort))

for item in message:
    sSock.send(item)
    data = sSock.recv(1024)
    print 'Client received: ', 'data'

sSock.close()
