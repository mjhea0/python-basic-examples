#coding:utf-8

import sys, urllib2, urllib

zipcode = sys.argv[1]
url = 'http://www.yourserver.com/cgi-bin'
data = urllib.urlencode([('query', zipcode)])
req = urllib2.Request(url)
fd = urllib2.urlopen(req, data)

while 1:
    data = fd.read(1024)
    if not len(data):
        break
    sys.stdout.write(data)
