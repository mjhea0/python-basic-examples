#coding:utf-8

print 'This is a test'.replace('is', 'eez')
question = "What is the air speed velocity of an unlaiden swallow?"
print question.replace("swallow", "European swallow")

string = "One, one, one, one, one, one"

print "Original:", string
print 'Replaced "one" with "two":', string.replace( "one", "two" )
print "Replaced 3 maximum:", string.replace( "one", "two", 3 )
