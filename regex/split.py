#coding:utf-8

import re

some_text = 'alpha, beta,,,,gamma delta'
print re.split('[, ]+', some_text)
