#coding:utf-8

import os
import zipfile

tFile = zipfile.ZipFile("files.zip", 'w')
files = os.listdir(".")

for f in files:
    tFile.write(f)

for f in tFile.namelist():
    print "Added %s" % f

tFile.close()
