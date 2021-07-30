import os

child_pid = os.fork()
print(child_pid)
if child_pid != 0:
    pid,status = os.waitpid(-1, os.WNOHANG)
    print(f"pid = {pid} and status = {status}")
