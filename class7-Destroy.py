#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9

class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name, "destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt1
print (" pt1 id: ",id(pt1),"\n", "pt2 id: ", id(pt2), "\n", "pt3 id: ", id(pt3))   # prints the ids of the obejcts
del pt1
del pt2
del pt3