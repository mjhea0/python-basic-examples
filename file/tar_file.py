#coding:utf-8

import os
import tarfile

#Create Tar file
tFile = tarfile.open("files.tar", 'w')

files = os.listdir(".")
for f in files:
    tFile.add(f)

#List files in tar
for f in tFile.getnames():
    print "Added %s" % f

tFile.close()
