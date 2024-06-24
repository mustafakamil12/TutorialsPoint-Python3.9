import os

def gfs_log(facility, severity, message):
    os.system("logger -is -t " + facility + " -p \"local0."+ severity + "\" " + "\"" + message + "\"")
    print("send message to the syslog")


gfs_log("gfs_test", "INFO", "Hello This is Mustafa")