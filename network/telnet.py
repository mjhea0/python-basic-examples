#coding:utf-8

import telnetlib

hostserver = "http://www.telnetServer.com"
newline = "\n"
username = "user02" + newline
password = "qwerty0987" + newline

telnet = telnetlib.Telnet(hostserver)
telnet.read_until("login: ")
telnet.write(username)
telnet.read_until("Password: ")
telnet.write(password)

while 1:
    command = raw_input("[shell]: ")
    telnet.write(command)

    if command == "exit":
        break

    telnet.read_all()
