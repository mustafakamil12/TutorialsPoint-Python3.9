import sys,os,re
import fileinput,subprocess,inspect

try:
   TOTALS = open('/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Perl/MISSGEDD_TOTALS,'r')
except OSError:
   sys.exit()

count = 0

while TOTALS.readline():
    print ("default_var")
