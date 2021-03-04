#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

class JustCounter:
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
#print (counter.__secretCount)       # your unable to access hiding class var.
print (counter._JustCounter__secretCount)