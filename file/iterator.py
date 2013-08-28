#coding:utf-8

filename = raw_input('Enter file name: ')

f = open(filename, 'r')
for eachLine in f:
    print eachLine,

f.close()
