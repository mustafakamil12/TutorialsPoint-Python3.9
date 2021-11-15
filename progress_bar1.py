import sys
import time

def progressBar(length, totalTime):
    t = totalTime / length

    sys.stdout.write("[{}]".format(" " * length))
    sys.stdout.write("\b" * (length + 1))
    sys.stdout.flush()

    for i in range(length):
        sys.stdout.write("-")
        sys.stdout.flush()
        time.sleep(t)

progressBar(30, 2) # first value = the length of the progress bar
                   # second value = the total of time to fill the progress bar

# Code by Yoann Bertel
