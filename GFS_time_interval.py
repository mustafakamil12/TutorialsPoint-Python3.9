#!/usr/bin/python3
#     Revision: 0.0.1     Modtime: 02/26/21 09:00 pmam     Author: Mustafa Al Ogaidi
#
#   Python module:
#
#      GFS_time_interval
#
#   Description:
#
#      Object to represent an interval of time within the Global Forecast
#      System.
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

#
#  Method       - init
#  Description  - Converts a textual time interval into an integral number of
#                 seconds and/or months.
#  Arguments    - $1 = textual time interval, must be one of:
#                     years, months, days, hours, minutes, seconds
#                 The trailing 's' is optional.
#                 The time inteval can be prefaced by an integer value, e.g.
#                     "6 hours" or "10 minutes"
#                 The SQL format used by Postgres for interval type is also
#                 supported
#  Returns      - Reference to a GFS_time_interval, or undef on failure.

import sys,os,re
import fileinput,subprocess,inspect

class GFS_time_interval:
    def __init__(self,time_interval):
        self.time_interval = time_interval
        print("GFS_time -> self.time_interval = ", self.time_interval)
        seconds = 0
        months = 0

        regex1 = r'(\d+ years |)(\d+ mons |)(\d+ |)(\d\d):(\d\d)(:\d\d|)'
        regex2 = r'([-+]{0,1}\d*) hour*'
        regex3 = r'([-+]{0,1}\d*) minute*'
        regex4 = r'([-+]{0,1}\d*) day*'
        regex5 = r'([-+]{0,1}\d*) second*'
        regex6 = r'([-+]{0,1}\d*) month*'
        regex7 = r'([-+]{0,1}\d*) year*'

        if(time_interval is None):
            # Assume time interval is 0 seconds....
            print("Assume time interval is 0 seconds")
        elif ((re.findall(regex1,self.time_interval) != None and re.findall(regex1,self.time_interval) != [])):
            #
            #  PostgreSQL interval format.  TO DO - Determine if this an ANSI
            #  standard for all SQL-compliant databases.
            #
            print("regex1 match someting ...")
            timeIntRegArrTmp    = re.findall(regex1,self.time_interval)
            timeIntRegArr       = list(timeIntRegArrTmp[0])
            self.years          = int(timeIntRegArr[0])
            self.mons           = int(timeIntRegArr[1])
            self.days           = int(timeIntRegArr[2])
            self.hours          = int(timeIntRegArr[3])
            self.minutes        = int(timeIntRegArr[4])
            self.secs           = int(timeIntRegArr[5])

            yearsReg = r'(\d+) years '
            monsReg = r'(\d+) mons '
            secsReg = r':(\d+)'

            if re.match(yearsReg,self.years):
                self.years = re.search(yearsReg, self.years)

            if re.match(monsReg, self.mons):
                self.mons = re.search(monsReg, self.mons)

            if re.match(secsReg, self.secs):
                self.secs = re.search(secsReg, self.secs)

            months += self.years * 12 + self.mons
            seconds += self.days * 86400 + self.hours * 3600 + self.minutes * 60 + self.secs

        elif(re.findall(regex2, self.time_interval)):
            print("regex2 match something ...")
            secCheck = re.findall(regex2, self.time_interval)
            if secCheck[0] == "":
                seconds = 3600
            else:
                seconds = int(secCheck[0]) * 3600

        elif(re.findall(regex3, self.time_interval)):
            print("regex3 match someting ...")
            minCheck = re.findall(regex3, self.time_interval)
            if minCheck[0] == "":
                seconds = 60
            else:
                seconds = int(minCheck[0]) * 60

        elif(re.findall(regex4, self.time_interval)):
            print("regex4 match someting ...")
            dayCheck = re.findall(regex4, self.time_interval)
            if dayCheck[0] == "":
                seconds = 86400
            else:
                seconds = int(dayCheck[0]) * 86400

        elif(re.findall(regex5, self.time_interval)):
            print("regex5 match someting ...")
            secCheck1 = re.findall(regex5, self.time_interval)
            if secCheck1[0] == "":
                seconds = 1
            else:
                seconds = int(secCheck1[0])

        elif(re.findall(regex6, self.time_interval)):
            print("regex6 match someting ...")
            monthCheck = re.findall(regex6, self.time_interval)
            if monthCheck[0] == "":
                months = 1
            else:
                months = int(monthCheck[0])

        elif(re.findall(regex7, self.time_interval)):
            print("regex7 match someting ...")
            yearCheck = re.findall(regex7, self.time_interval)
            if yearCheck[0] == "":
                months = 12
            else:
                months = int(yearCheck[0]) * 12

        else:
            print("Unsupported time unit ", self.time_interval, file=sys.stderr)

        self.seconds = seconds
        print("self.seconds = ", self.seconds)
        self.months = months
        print("self.months = ", self.months)


    def secondsFun(self):
        return self.seconds

    def monthsFun(self):
        return self.months

    def make_negative(self):
        if(self.months > 0):
            self.months = -1 * self.months

        if(self.seconds > 0):
            self.seconds = -1 * self.seconds

    def make_positive(self):
        if(self.months < 0):
            self.months = -1 * self.months
        if(self.seconds < 0):
            self.seconds = -1 * self.seconds
