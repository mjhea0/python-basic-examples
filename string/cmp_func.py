#coding:utf-8 

str1 = 'abc'
str2 = 'lmn'
str3 = 'xyz'

#-1
print cmp(str1, str2)

#1
print cmp(str3, str1)

#0
print cmp(str2, 'lmn')
