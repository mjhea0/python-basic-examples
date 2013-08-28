#coding:utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "done."

s.connect(("www.google.com", 80))
print "done."
