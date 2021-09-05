from datetime import datetime
cur_time = '210830:1808CDT'
update_time = '210831:1808CDT'
FMT = "%y%m%d:%H%M%Z"

cur_time = datetime.strptime(cur_time,FMT)
update_time = datetime.strptime(update_time,FMT)
print(cur_time)
print(update_time)
timeDiff =  update_time - cur_time
timeDiff = timeDiff.days
print(f"timeDiff = {timeDiff}")
