#coding:utf-8

import re 

phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')    
print phonePattern.search('000-888-1234').groups()             

#有$结尾
print phonePattern.search('000-888-1234-1234')
