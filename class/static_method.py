#coding:utf-8

class Employee:
   numberOfEmployees = 0 
   maxEmployees = 10     

   def isCrowded():
      return Employee.numberOfEmployees > Employee.maxEmployees

   isCrowded = staticmethod( isCrowded )

   def __init__( self, firstName, lastName ):
      self.first = firstName
      self.last = lastName
      Employee.numberOfEmployees += 1

   def __del__( self ):
      Employee.numberOfEmployees -= 1      

   def __str__( self ):
      return "%s %s" % ( self.first, self.last )

answers = [ "No", "Yes" ] 
employeeList = []         

print answers[ Employee.isCrowded() ]

for i in range( 11 ):
   employeeList.append( Employee( "John", "Doe" + str( i ) ) )

   print "Employees are crowded?",
   print answers[ employeeList[ i ].isCrowded() ]

del employeeList[ 0 ]

print "Employees are crowded?", answers[ Employee.isCrowded() ]
