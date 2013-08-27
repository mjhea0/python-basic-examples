#coding:utf-8

name = list('Perl')
#['P', 'e', 'r', 'l']
print name
name[2:] = list('ar')
#['P', 'e', 'a', 'r']
print name

name = list('Perl')
name[1:] = list('ython')
#['P', 'y', 't', 'h', 'o', 'n']
print name

numbers = [1, 5]
numbers[1:1] = [2, 3, 4]
#[1, 2, 3, 4, 5]
print numbers

numbers = [1, 2, 3, 4, 5]
numbers[1:4] = []
#[1, 5]
print numbers
