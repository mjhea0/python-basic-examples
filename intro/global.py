#coding:utf-8

_count = 0

def counter():
    global _count
    _count += 1
    return _count

print counter()