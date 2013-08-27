#coding:utf-8

def fibonacci( n ):
    if n < 0: 
       print "Cannot find the fibonacci of a negative number"

    if n == 0 or n == 1:  # base case
       return n
    else:
       return fibonacci( n - 1 ) + fibonacci( n - 2 )

number = int( raw_input( "Enter an integer: " ) )
result = fibonacci( number )
print "Fibonacci(%d) = %d" % ( number, result )
