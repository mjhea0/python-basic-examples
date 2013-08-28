#coding:utf-8

import os

os.mkdir('/tmp/example')
os.chdir('/tmp/example')
cwd = os.getcwd()
print cwd

fobj = open('test', 'w')
fobj.write('foo\n')
fobj.write('bar\n')
fobj.close()

print os.listdir(cwd)
print os.listdir('/tmp')
