import syslog
# Define identifier
syslog.openlog("Python")
# Record a message
syslog.syslog(syslog.LOG_ALERT, "This is Mustafa message ...")