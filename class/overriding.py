#coding:utf-8

class Employee:
   def __init__( self, first, last ):
      self.firstName = first
      self.lastName = last

   def __str__( self ):
      return "%s %s" % ( self.firstName, self.lastName )

class HourlyWorker( Employee ):
   def __init__( self, first, last, initHours, initWage ):
      Employee.__init__( self, first, last )
      self.hours = float( initHours )
      self.wage = float( initWage )

   def getPay( self ):
      return self.hours * self.wage

   def __str__( self ):
      print "HourlyWorker.__str__ is executing"""      
      return "%s is an hourly worker with pay of $%.2f" % ( Employee.__str__( self ), self.getPay() )

hourly = HourlyWorker( "Bob", "Smith", 40.0, 10.00 )

print hourly 
print hourly.__str__()  
print HourlyWorker.__str__( hourly )
