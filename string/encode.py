#coding:utf-8

locStr = "El "
uniStr = u"Ni\u00F1o"

#iso-8859-1
newStr = locStr+uniStr
print newStr.encode('iso-8859-1')

#utf-8
uniStr = u"Ni\u00F1o"
print uniStr.encode('utf-8')

#utf-16
uniStr = u"Ni\u00F1o"
print uniStr.encode('utf-16')
