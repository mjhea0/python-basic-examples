#coding:utf-8

import re

pat = '{name}'
text = 'Dear {name}'

print re.sub(pat, 'Mr. Gumby', text)
