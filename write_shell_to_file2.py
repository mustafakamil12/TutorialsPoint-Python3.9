import os, sys, subprocess,re
try:
   file_ = open('/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9/BACKLOG', 'a+')
   print("ps -ef | grep spawn | grep -v grep | wc -l")
   subprocess.run('ps -ef | grep spawn | grep -v grep | wc -l', shell=True, stdout=file_)

except OSError:
   sys.exit()

data = file_.readlines()
print("data = ", data)
file_.close()
data = re.sub(r'\s','',data)
print("data = ", data)
