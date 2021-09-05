#!/usr/bin/env python

import subprocess
import sys,os

print("  Started a.py")
pid = subprocess.Popen([sys.executable, "/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9/b.py"])
print(f"pid = {pid}")

print("  End of a.py")

pid, status = os.waitpid(-1,os.WNOHANG)
print(f"pid = {pid} and status = {status}")
#status = subprocess_rc # Need to be checked again
