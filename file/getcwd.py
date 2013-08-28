#coding:utf-8

import os

print os.path.isdir('/tmp')
os.chdir('/tmp')
cwd = os.getcwd()
print cwd
