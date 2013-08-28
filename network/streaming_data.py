#coding:utf-8

import sys
from socket import *

serverHost = 'localhost'
serverPort = 50008

if len(sys.argv) > 1:
    serverHost = sys.argv[1]

sSock = socket(AF_INET, SOCK_STREAM)
sSock.connect((serverHost, serverPort))
line = ""

while line != 'bye':
    line = raw_input("Send to %s: " % (serverHost))
    sSock.send(line+'\n')
    data = sSock.recv(1024)
    print 'data'

sSock.shutdown(0)
sSock.close()
