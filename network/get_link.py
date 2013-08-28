#coding:utf-8

import re
from urllib import urlopen
webpage = urlopen('http://www.python.org')

text = webpage.read()
m = re.search('<a href="([^"]+)">Tutorial</a>', text, re.IGNORECASE)
print m.groups
