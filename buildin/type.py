#coding:utf-8

print type('')
s = 'xyz'
print type(s) 
print type(100)
print type(0+0j)
print type(0L)
print type(0.0)
print type([])
print type(())
print type({})
print type(type)

class Foo: pass            # new-style class
foo = Foo()

class Bar(object): pass    # new-style class
bar = Bar()

#<type 'classobj'>
print type(Foo)

#<type 'instance'>
print type(foo)

#<type 'type'>
print type(Bar)

#<class '__main__.Bar'>
print type(bar)
