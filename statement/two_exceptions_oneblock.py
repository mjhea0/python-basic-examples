#coding:utf-8

try:
   x = input('Enter the first number: ')
   y = input('Enter the second number: ')
   print x/y 
except (ZeroDivisionError, TypeError):
   print 'Your numbers were bogus...'
