#coding:utf-8

import linecache

filePath = "/tmp/input.txt"

print linecache.getline(filePath, 1)
print linecache.getline(filePath, 3)

linecache.clearcache()
