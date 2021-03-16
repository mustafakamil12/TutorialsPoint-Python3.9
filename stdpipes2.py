import os,sys
import time
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', buffering=1)
sys.stderr = os.fdopen(sys.stderr.fileno(), 'w', buffering=1)
sys.stdin = os.fdopen(sys.stdin.fileno(), 'r', buffering=1)
print('out')
line = sys.stdin.readline()
for i in line:
    print(i)
    time.sleep(.2)
