#coding:utf-8

import re

pat = '[a-zA-Z]+'
text = '"Hm Err -- are you sure?" he said, sounding insecure.'
print re.findall(pat, text)

pat = r'[.?\-",]+'
print re.findall(pat, text)

print re.findall('car', 'car')
print re.findall('car', 'scary')
print re.findall('car', 'carry')
