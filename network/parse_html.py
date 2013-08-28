#coding:utf-8

import urlparse

URLscheme = "http"
URLlocation = "www.python.org"
URLpath = "lib/module-urlparse.html"

modList = ("urllib", "urllib2", "httplib", "cgilib")

parsedTuple = urlparse.urlparse("http://www.google.com/search?hl=en&q=urlparse&btnG=Google+Search")
print parsedTuple

unparsedURL = urlparse.urlunparse((URLscheme, URLlocation, URLpath, '', '', ''))
print unparsedURL

for mod in modList:
    newURL = urlparse.urljoin(unparsedURL, "module-%s.html" % (mod))
    print newURL

newURL = urlparse.urljoin(unparsedURL,"module-urllib2/request-objects.html")
print newURL
