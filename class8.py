#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print ("Calling parent constructor")

   def parentMethod(self):
      print ('Calling parent method')

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print ("Parent attribute :", Parent.parentAttr)
   
   def myMethod(self):
       print ("myMethod in parent class...")

class Child(Parent): # define child class
   def __init__(self):
      print ("Calling child constructor")

   def childMethod(self):
      print ('Calling child method')
   
   def myMethod(self):                      # override myMethod ...
       print ("myMethod in child class...")


c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method
c.myMethod()         # call myMethod to check if it's in parent or in child