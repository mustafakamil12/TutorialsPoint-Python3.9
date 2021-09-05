import time,sys
import GFS_timezone
from GFS_timezone import *


process_slot = 0
sys.path.append("/Users/mustafaalogaidi/Desktop/MyWork/TutorialsPoint-Python3.9")
end_time = time.time()
print(f"end_time = {end_time}")
print(f"GFS_timezone.start_time[process_slot] = {GFS_timezone.start_time}")


min = int((end_time - GFS_timezone.start_time[process_slot]) / 60)
sec = (end_time - GFS_timezone.start_time[process_slot]) - min * 60
elapsed = '%02d:%02d' % ( min,sec)
