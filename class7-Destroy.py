#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9

import point

pt1 = point.Point()
pt2 = pt1
pt3 = pt1
print (" pt1 id: ",id(pt1),"\n", "pt2 id: ", id(pt2), "\n", "pt3 id: ", id(pt3))   # prints the ids of the obejcts
del pt1
del pt2
del pt3