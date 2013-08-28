#coding:utf-8

import poplib
import getpass

mServer = poplib.POP3('mail.sfcn.org')

mServer.user(getpass.getuser())
mServer.pass_(getpass.getpass())
numMessages = len(mServer.list()[1])

print "You have %d messages." % 
