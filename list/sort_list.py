#coding:utf-8

x = [4, 6, 2, 1, 7, 9]
x.sort()
print x

x = ['clda', 'ab', 'ac', 'add', 'ae']
#指定比较函数
x.sort(key=len)
print x

x = [4, 6, 2, 1, 7, 9]
#指定反转
x.sort(reverse=True)
print x

caseList = ['d', 'B', 'F', 'A', 'E', 'c']
caseList.sort()
print caseList
caseList.sort(key=str.lower)
print caseList
