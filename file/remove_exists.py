#coding:utf-8

import os

oldFileName = "test.txt"
newFileName = "test.old"

for file in os.listdir("/tmp/"):
    if file.startswith("output"):
        print file

if os.access(newFileName, os.X_OK):
    print "Removing " + newFileName
    os.remove(newFileName)

os.rename(oldFileName, newFileName)

for file in os.listdir("/tmp/"):
    if file.startswith("output"):
        print file
