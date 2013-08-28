#coding:utf-8

import struct 

F = open('/tmp/data.bin', 'wb')

bytes = struct.pack('>i4sh', 7, 'spam', 8)
print bytes 

F.write(bytes)                            
F.close() 

F = open('/tmp/data.bin', 'rb') 
data = F.read()                         
print data 

values = struct.unpack('>i4sh', data)     
print values
