#coding:utf-8

d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}

it = d.iteritems()

#<dictionary-itemiterator object at 0x104e8ed60>
print it

print list(it) # Convert the iterator to a list

it = d.iteritems()

#('url', 'http://www.python.org')
print it.next()

#('spam', 0)
print it.next()

#('title', 'Python Web Site')
print it.next()

