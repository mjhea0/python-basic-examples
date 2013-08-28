#coding:utf-8

import sys

try:
   file = open( "clients.dat", "w" )  
except IOError, message:              
   print >> sys.stderr, "File could not be opened:", message
   sys.exit( 1 )

print >> file, "account"
      
file.close()
