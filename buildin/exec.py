#coding:utf-8

exec "print 'Hello, world!'"

cards = ['A', 'K', 'Q', 'J']
codeStr = "for card in cards: print \"Card = \" + card"
exec(codeStr)

exec """
x = 0
print 'x is currently:', x
while x < 5:
    x += 1
    print 'incrementing x to:', x
"""

#exec can accept file
f = open(r'./complex.py')
exec f
