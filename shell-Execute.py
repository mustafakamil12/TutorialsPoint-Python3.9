import os

#os.system('sh ' + './gfs_alert')

def gfs_alert(message):
    try:
        GFS_ALERT=open('|','w')
        print(file=GFS_ALERT)
        GFS_ALERT.f.close
    except OSError:
        sys.exit()

message = "Testing Example"

gfs_alert(message)
