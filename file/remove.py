#coding:utf-8

import os

emptyDirs = []
path = "/tmp/"

def deleteFiles(dirList, dirPath):
    for file in dirList:
        print "Deleting " + file
        os.remove(dirPath + "/" + file)

def removeDirectory(dirEntry):
    print "Deleting files in " + dirEntry[0]
    deleteFiles(dirEntry[2], dirEntry[0])
    #放在最前面
    emptyDirs.insert(0, dirEntry[0])

tree = os.walk(path)

for directory in tree:
    removeDirectory(directory)

for dir in emptyDirs:
    print "Removing " + dir
    os.rmdir(dir)
