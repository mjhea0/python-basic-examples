#coding:utf-8

name = raw_input('What is your name?')

if name.endswith('Gumby'):
    if name.startswith('Mr.'):
        print 'Hello, Mr. Gumby' 
    elif name.startswith('Mrs.'):
        print 'Hello, Mrs. Gumby' 
    else: 
        print 'Hello, Gumby'
else: 
    print 'Hello, stranger'
