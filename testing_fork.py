import os

def child():
   print('\nA new child ',  os.getpid())
   os._exit(0)

def parent():
   while True:
      newpid = os.fork()
      if newpid == 0:
         child()
      else:
         pids = (os.getpid(), newpid)
         print("parent: %d, child: %d\n" % pids)
      reply = input("q for quit / c for new fork")
      if reply == 'c':
          continue
      else:
          break

min = 33
sec = 44
elapsed = '%02d:%02d' % ( min,sec)
print(f"elapsed = {elapsed}")
parent()
