import os,sys

sys.path.append("/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9")

import secondModule
secondModule.loader()

from secondModule import myVar
print(myVar)
