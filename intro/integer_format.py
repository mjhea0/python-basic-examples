#coding:utf-8

print "%+d" % 4
print "%+d" % -4
print "%d%%" % 100
print "host is:%s" % 'earth'
print "host:%s, port:%s" % ('mars', 8080)

num = 123
print 'dec:%d, oct: %#o, hex:%#X' % (num, num, num)
print 'MM/DD/YYYY = %02d/%02d/%04d' % (2, 15, 2013)

w, p = 'web', 'page'
print 'http://xxx.yyy.zzz/%s/%s.html' % (w, p)
