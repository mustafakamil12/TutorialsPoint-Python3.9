#!/usr/bin/python3
#     Revision: 0.0.1     Modtime: 02/24/21 09:00 pm     Author: Mustafa Al Ogaidi
#
#   Python module:
#
#      GFS_syslog
#
#   Description:
#
#      Functions to send log information via syslog.
#
#   Copyright (C) 2021, WSI Corporation
#
#   These coded instructions, statements, and computer programs contain
#   unpublished proprietary information of WSI Corporation, and are
#   protected by Federal copyright law.  They may not be disclosed
#   to third parties or copied or duplicated in any form, in whole or
#   in part, without the prior written consent of WSI Corporation.
#
#------------------------------------------------------------------------------

import sys,os,re
import fileinput,subprocess,inspect
from os import environ

if environ.get('GFS_DB_DRIVER') is not None:
    scripts_dir = os.environ['GFS_DB_DRIVER'] + "/bin/"
    print(scripts_dir)

def gfs_log(facility, severity, message):
    #print("facility: ", facility, "severity: ", severity, "message: ", message)
    #print("logger -t " + facility + " -p \"local0."+ severity + "\" " + "\"" + message + "\"")
    os.system("logger -t " + facility + " -p \"local0."+ severity + "\" " + "\"" + message + "\"")


def gfs_alert(message):
    try:
        os.system('sh ' + scripts_dir + '/gfs_alert')
    except OSError:
        sys.exit()


def db_log(severity,message):
    gfs_log ("GFS_DB", severity, message)

def db_log_info(message):
    db_log ("info", message)

def db_log_error(message):
    db_log ("err", message)

def db_log_alert(message):
    db_log_error(message)
    gfs_alert(message)

def frmt_log(severity, message):
    gfs_log("GFS_FRMT", severity, message)

def frmt_log_info(message):
    frmt_log ("info", message)
    

def frmt_log_error(message):
    frmt_log ("err", message)  

def frmt_log_alert(message):
    frmt_log_error(message)
    gfs_alert(message)

def db_tool_log(severity, message):
    gfs_log('DB_TOOL', severity, message)

def db_tool_log_info(severity, message):
    db_tool_log('info', severity, message)

def db_tool_log_error(severity, message):
    db_tool_log('err', severity, message)

def db_tool_log_alert(severity, message):
    db_tool_log_error(severity, message)
    gfs_alert(message)

#
# Executing Modules as Script.
#
if __name__ == "__main__":
    #frmt_log_info("Completed product send for 1 1 with fatal error, 10:10")
    print("Completed product send for 1 1 with fatal error, 10:10")
