#coding:utf-8

myDict = {'host': 'earth', 'port': 80}
print myDict.keys()
print myDict.items()

#80
print myDict.setdefault('port', 8080)
print myDict.setdefault('prot', 'tcp')

#[('host', 'earth'), ('prot', 'tcp'), ('port', 80)]
print myDict.items()
