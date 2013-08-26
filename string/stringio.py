#coding:utf-8

import string
import StringIO 

contents = "<grammar><ref id='bit'><para>0</para><para>1</para></ref></grammar>" 
ssock = StringIO.StringIO(contents)          
print ssock.read()                                      
print ssock.read()                                     
print ssock.seek(0)                                      
print ssock.read(15)                                       
print ssock.read(15) 
print ssock.read() 
ssock.close()
