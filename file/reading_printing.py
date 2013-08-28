#coding:utf-8

import sys

try:
   file = open( "test.txt", "r" )
except IOError:
   print >> sys.stderr, "File could not be opened"
   sys.exit( 1 )
   
records = file.readlines()      # retrieve list of lines in file

print "Account".ljust( 10 ),
print "Name".ljust( 10 ),
print "Balance".rjust( 10 )

for record in records:          # format each line
   fields = record.split()
   print fields[ 0 ].ljust( 10 ),
   print fields[ 1 ].ljust( 10 ),
   print fields[ 2 ].rjust( 10 )

file.close()
