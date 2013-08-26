#coding:utf-8

try:
    try:
         ccfile = open('data.txt', 'r')
         txns = ccfile.readlines()
    except IOError:
        log.write('no txns this month\n')
finally:
        ccfile.close()
