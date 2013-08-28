#coding:utf-8

f = open(r'/tmp/somefile.txt', 'r')
lines = f.readlines()
f.close()

lines[1] = "isn't a\n"
f = open(r'/tmp/somefile.txt', 'w')
f.writelines(lines)
f.close()
