import os, sys

filePath = '/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9/testfile.txt'
payLoad = ''
try:
    FILE1 = open(filePath,'r')
    for line in FILE1:
        payLoad += line
    FILE1.close()
except OSError:
    sys.exit()

print(f"payLoad = {payLoad}")


#print(f"myfile = {myfile.readlines()}")
