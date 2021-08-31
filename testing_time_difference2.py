import time
from datetime import datetime

cur_time = int(time.time())
print(f"cur_time = {cur_time}")
update_time = cur_time + (24*60*60)
print(f"update_time = {update_time}")

timeDiff = cur_time - update_time
timeDiff = int(timeDiff / (24*60*60))
print(f"timeDiff = {timeDiff}")

products = {'WEFFECTS_FIVDAY_FL_CONUS.gif':'TRADER_1-5DAY','WEFFECTS_6TO10_FL_AVG6TO10.gif':'TRADER_6-10DAY','WEFFECTS_11TO15_FL_CONUS.gif':'TRADER_11-15DAY'}
image = 'WEFFECTS_FIVDAY_FL_CONUS.gif'
print(f"products[image] = {products[image]}")
