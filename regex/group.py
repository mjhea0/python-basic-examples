#coding:utf-8

import re

m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
print m.group()
print m.group(1)
print m.group(2)
print m.groups()
