#coding:utf-8

import os
import tarfile

extractPath = "/bin/py"

#Open Tar file
tFile = tarfile.open("files.tar", 'r')

#Extract py files in tar
for f in tFile.getnames():
    if f.endswith("py"):
        print "Extracting %s" % f
        tFile.extract(f, extractPath)
    else:
        print "%s is not a Python file." % f

tFile.close()
