#coding:utf-8

import sys, urllib2, urllib

def addGETdata(url, data):
    return url + '?' + urllib.urlencode(data)

zipcode = sys.argv[1]
url = addGETdata('http://www.yourserver.com/cgi-bin',[('query', zipcode)])
print "Using URL", url
req = urllib2.Request(url)
fd = urllib2.urlopen(req)

while 1:
    data = fd.read(1024)
    if not len(data):
        break
    sys.stdout.write(data)
