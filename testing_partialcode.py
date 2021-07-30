import time
import GFS_timezone
from GFS_timezone import *

end_time = time.time()

min = int((end_time - GFS_timezone.start_time[process_slot]) / 60)
sec = (end_time - GFS_timezone.start_time[process_slot]) - min * 60
elapsed = '%02d:%02d' % ( min,sec)
