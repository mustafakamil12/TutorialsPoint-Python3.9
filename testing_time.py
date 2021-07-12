import sys,os,re
import fileinput,subprocess,inspect
import time,calendar
import datetime
#sys.path.append("/Users/mustafaalogaidi/Desktop/TWC/energy-pgs/")
from GFS_time_interval import *
#from GFS_log import *

class GFS_time:
    ISO_FORMAT='%Y-%m-%d %H:%M:%S%z'


    def __init__(self,timeArr):
        print("timeArr: ", timeArr)
        self.timeStr = timeArr
        #time_t = None
        if self.timeStr:
            print("timeStr exist")
            if isinstance(self.timeStr, GFS_time):
                self.other = timeArr # Need to be checked again
                time_t = int(self.other.time_t_Res())
                print("time_t where it's an object = ", time_t)
            else:
                time_t = self.parse_time_string(self.timeStr)
        else:
            print("timeStr not exist")
            time_t = int(time.time())
            print("time_t = ", time_t)

        self.time_t = time_t

    def timegmt(timeArr):
        print("---------timegmt-------------")
        print("timeArr = ", timeArr)
        struct_tm_ref = timeArr
        #
        # We can't support years prior to 1970, or after 2037
        # This code insures that any time outside of this range
        # will be set to the closest time inside the range.
        #
        if struct_tm_ref[0] < 70:
            struct_tm_ref[5] = 0
            struct_tm_ref[4] = 0
            struct_tm_ref[3] = 0
            struct_tm_ref[2] = 1
            struct_tm_ref[1] = 0
            struct_tm_ref[7] = 36
        if struct_tm_ref[0] > 137:
            struct_tm_ref[5] = 59
            struct_tm_ref[4] = 59
            struct_tm_ref[3] = 23
            struct_tm_ref[2] = 31
            struct_tm_ref[1] = 11
            struct_tm_ref[7] = 137
        print("struct_tm_ref = ", struct_tm_ref)
        return(calendar.timegm(tuple(struct_tm_ref)))


    def parse_time_string(self,timeArr):
        str = timeArr
        struct_tm = None
        time_t = -1
        default_match = re.match(r'^(\d+)-(\d+)-(\d+)$',str)
        print("default_match = ", default_match)

        default_match1 = re.match(r'(\d+)-(\d+)-(\d+) (\d+):(\d+):(\d+)$',str)
        print("default_match1 = ", default_match1)

        default_match2 = re.match(r'(\d+)-(\d+)-(\d+) (\d+):(\d+):(\d+)([+-]\d+)',str)
        print("default_match2 = ", default_match2)



        if default_match:
            #
            #  Time string starts with a date of the form "YYYY-MM-DD"
            #
            print('default_match is defined')
            struct_tm.append(int(default_match1.group(1))-1900)   # years since 1900
            struct_tm.append(int(default_match1.group(2))-1)      # month -1
            struct_tm.append(int(default_match1.group(3)))        # day of month
            struct_tm.append(int(default_match1.group(4)))        # hour
            struct_tm.append(int(default_match1.group(5)))        # minute
            struct_tm.append(int(default_match1.group(6)))        # second
            struct_tm.append(-1)                                  # daylight savings time unknown


            #
            #  Convert the broken-down time to a Unix time, assuming time is
            #  specified as UTC.
            #
            time_t = GFS_time.timegmt(struct_tm)

        elif default_match1:
            #
            #  Time string is a date time of form "YYYY-MM-DD hh:mm:ss".
            #  Fill in the time-of-day variables.
            #
            struct_tm = []
            print("default_match1 is defined")

            struct_tm.append(int(default_match1.group(1))-1900)   # years since 1900
            struct_tm.append(int(default_match1.group(2))-1)      # month -1
            struct_tm.append(int(default_match1.group(3)))        # day of month
            struct_tm.append(int(default_match1.group(4)))        # hour
            struct_tm.append(int(default_match1.group(5)))        # minute
            struct_tm.append(int(default_match1.group(6)))        # second
            struct_tm.append(-1)                                  # daylight savings time unknown

            print("struct_tm = ", struct_tm)
            #
            #  Convert the broken-down time to a Unix time, assuming time is
            #  specified as UTC.
            #

            time_t = GFS_time.timegmt(struct_tm)


        elif default_match2:
            #
            #  Time string is an ISO datetime string, with time zone offset
            #  (in hours) after the seconds.  We assumed the time was in UTC,
            #  so subtract the timezone offset to correct this assumption.
            #  Note: the offset is the number of hours that must be added to
            #  a UTC time to get the local time.
            #
                time_t -= int(default_match2.group(7)) * 3600
            #
            #  Add more time formats here....
            #
        else:
            #
            #  If the time cannot be parsed, warn the user.
            #
            print("Error: parse_time_string: $str not in a known datetime format\n")
        return time_t

    def copy_from(self,newtime_t):
        if self.timeStr == None:
            return(0)

        self.time_t = newtime_t
        return(1)


    def time_t_Res(self):
        print("-----------time_t_Res-----------")
        resultArr = self.time_t
        print("resultArr inside the function of it's name = ", resultArr)
        return resultArr


    def set_to_now(self):
        print("return time in secs...")
        time_t = int(time.time())
        self.time_t = time_t
        return(time_t)


    def add_seconds(self,secsOffset):

        time_t = self.time_t
        if time_t == -1:
            return(0)

        secs = 0
        if secsOffset:
            secs = secsOffset
            self.time_t += secs
            #print("need to check type of self.time_t = ", type(self.time_t))
        return secs


    def increment_by(self,incrBy):
        self.time_interval = str(incrBy)
        time_t = self.time_t
        if time_t == -1:
            return(0)

        if self.time_interval == '':
            print('GFS_time.increment_by: a time interval must be specified',self.time_interval,'',file=sys.stderr)
            return(0)
        #print(("type(self.time_interval).__name__ = ", type(self.time_interval).__name__))
        if type(self.time_interval).__name__ != 'GFS_time_interval':
            print("GFS_time -> self.time_interval as not GFS_time_interval", self.time_interval)
            gfs_time_interval = GFS_time_interval(self.time_interval)
            print("gfs_time_interval = ", gfs_time_interval)
            if gfs_time_interval == None:
                print('GFS_time.increment_by: invalid time interval ',self.time_interval,'',file=sys.stderr)
                return(0)
            print("Will assign gfs_time_interval to time_interval")
            time_interval = gfs_time_interval

        months = time_interval.monthsFun()
        print("months = ", months)
        seconds = time_interval.secondsFun()
        print("seconds = ", seconds)

        self.time_t += seconds

        if months != 0:
            #
            #  Create a "broken down" time structure w/o any local time adjustments
            #
            time_t = self.time_t
            print("time_t = self.time_t =>", time_t)
            time_tm = GFS_time.gmttime(time_t)

            years_to_add = months/12
            months_to_add = months%12

            months = time_tm[1] + 1
            years_since_1900 = time_tm[0] - 1900

            month_sum = months + months_to_add
            if month_sum > 12:
                years_to_add += 1
                months = month_sum - 12
            elif month_sum < 0:
                years_to_add -= 1
                months = month_sum + 12
            else:
                months = month_sum

                years_since_1900 += years_to_add

                time_tm[1] = months -1
                #time_tm[5] = years_since_1900

                new_time_t = GFS_time.timegmt(time_tm)
                print("new_time_t will be added to time_t = ", new_time_t)
                print("time_t = ", time_t)
                seconds += (new_time_t - time_t)
                self.time_t = new_time_t

        return(seconds)


    def gmttime(epoch_time):
        print("gmttime inpurt arg: ", epoch_time)
        struct_tm_py_way = time.gmtime(epoch_time)
        print("struct_tm_py_way: ", struct_tm_py_way)
        struct_tm = []

        for elem in struct_tm_py_way:
            struct_tm.append(elem)

        print("struct_tm = ", struct_tm)
        struct_tm[8] = -1

        print("struct_tm before return = ", struct_tm)
        return struct_tm

    def seconds_after(self):
        print("----------seconds_after-----------")

        time_t = self.time_t
        if time_t == -1:
            return(0)

        #GFS_time.other = GFS_time(timeArr)
        other_time_t = int(self.other.time_t_Res())
        if other_time_t == -1:
            return(0)

        print(f"{time_t} - {other_time_t}")
        return(time_t - other_time_t)

    def time_interval_in_seconds(self,time_interval):
        print("--------time_interval_in_seconds-------")
        className = self.__class__.__name__
        print("className = ", className)
        self.time_interval = time_interval

        time_int_secs = 0
        default_match = re.match(r' *([-+]{0,1}\d*) *hour',self.time_interval)
        default_match1 = re.match(r' *([-+]{0,1}\d*) *minute',self.time_interval)
        default_match2 = re.match(r' *([-+]{0,1}\d*) *day',self.time_interval)

        print("default_match = ", default_match)
        print("default_match1 = ", default_match1)
        print("default_match2 = ", default_match2)


        if default_match:
            print("default_match.group(1) = ", default_match.group(1))
            if default_match.group(1) == '':
                time_int_secs = 3600
            else:
                time_int_secs = int(default_match.group(1)) * 3600

        elif default_match1:
            if default_match1.group(1) == '':
                time_int_secs = 60
            else:
                time_int_secs = int(default_match1.group(1)) * 60

        elif default_match2:
            if default_match2.group(1) == '':
                time_int_secs = 86400
            else:
                time_int_secs = int(default_match2.group(1)) * 86400
        else:
            print('Unsupported time unit ',self.time_interval,'',file=sys.stderr)

        return(time_int_secs)

    def truncate_to(self,time_unit):
        self.time_unit = time_unit
        print("self.time_unit = ", self.time_unit)

        if self.time_unit == None:
            print("Can't truncate invalid GFS_time",self.time_unit,'',file=sys.stderr)
            return(0)

        time_t = self.time_t
        if time_t == -1:
            GFS_log.warning(GFS_log.PARAMETER,"Can't truncate invalid GFS_time")
            return(0)
        time_int_secs = GFS_time.time_interval_in_seconds(self,self.time_unit)

        if time_int_secs > 0:
            time_t = int(time_t / time_int_secs) * time_int_secs
            #print("time_t = ", time_t)

        else:
            if time_int_secs < 0:
                GFS_log.warning(GFS_log.PARAMETER,'Cannot truncate time using a negative time interval')
            else:
                GFS_log.warning(GFS_log.PARAMETER,'Unsupported time unit %s',time_unit)
            return(0)

        self.time_t = time_t
        return(1)


    def as_text(self,fmtin,utc_offsetin,tz_abbrevin):
        print("--------as_text--------")
        time_t = self.time_t
        print("time_t = ", time_t)

        if time_t == -1:
         return('')

        #
        #  Interpret the function's arguments.
        #

        fmt = GFS_time.ISO_FORMAT
        utc_offset = 0
        tz_abbrev = 'UTC'

        if fmtin != '':                     # first argument = format
            print("First Arg")
            fmt = fmtin
            if utc_offsetin:                # second argument = UTC offset
                print("Second Arg")
                utc_offset = utc_offsetin
                print("Third Arg")
                if tz_abbrevin:             # third argument = timezone abbrev
                    tz_abbrev = tz_abbrev


        print("fmt = ", fmt)
        print("utc_offset = ", utc_offset)
        print("tz_abbrev = ", tz_abbrev)
        #
        #  Handle the special formatting group %z to denote utc offset.
        #
        default_match = re.findall('\%z',fmt)
        print("default_match: ", default_match)

        if default_match:
            print("Format the UTC offset")
            #
            #  Format the UTC offset as "[+-]HH[:MM[:SS]]"
            #
            hours = int(utc_offset / 3600)
            minutes = int(utc_offset / 60) - hours * 60
            seconds = int(utc_offset) - 3600 * hours - 60 * minutes
            print("hours = ",hours)
            print("minutes = ",minutes)
            print("seconds = ",seconds)

            if minutes < 0:
                minutes = -1 * minutes
            if seconds < 0:
                seconds = -1*seconds

            utc_offset_str = None
            if seconds != 0:
                utc_offset_str = "%+2.2d:%2.2d:%2.2d" % (hours,minutes,seconds)
            elif minutes != 0:
                utc_offset_str = "%+2.2d:%2.2d" % (hours,minutes)
            else:
                utc_offset_str = "%+2.2d" % (hours)

            print("utc_offset_str = ", utc_offset_str)

            #
            #  Substitute the %z in the format string with the UTC offset string.
            #
            fmt = re.sub(r'\%z',utc_offset_str,fmt)
            print("fmt = ", fmt)

        #
        #  Handle the timezone abbreviation to avoid dependency on environment
        #  variable TZ.  This allows formatting for many local times, not just
        #  the one you happen to be in.
        #
        fmt = re.sub(r'\%Z',tz_abbrev,fmt)
        print("fmt = ", fmt)
        #
        #  Offset the seconds since 1970 from UTC time as needed.
        #

        print("time_t = ", time_t)
        time_t += utc_offset
        print("time_t = ", time_t)

        #
        #  Create a "broken down" time structure w/o any local time adjustments.
        #
        time_tm = GFS_time.gmttime(time_t)
        print("time_t after calling  gmttime = ", time_tm)

        #
        #  Return the textual representation of the time.
        #
        print("fmt: ", fmt)
        print("time_tm: ", time_tm)

        date_time = time.strftime(fmt,tuple(time_tm))
        print("date_time = ", date_time)

        return(date_time)

#argArr.pop(0)
#global_format_time = GFS_time('2015-10-17 00:00:00')
#print("global_format_time = ", global_format_time.time_t)


#global_format_time.copy_from('2018-10-17 00:00:00')
#print("global_format_time.time_t = ", global_format_time.time_t)
#----------------------------------------------------------------------------
global_format_time = GFS_time('2021-07-09 00:00:00')

print("global_format_time.time_t_Res() = ", global_format_time.time_t_Res())
print("global_format_time.set_to_now() = ", global_format_time.set_to_now())
print("global_format_time.add_seconds(10) = ", global_format_time.add_seconds(10))
print("global_format_time.increment_by('+1 month') = ", global_format_time.increment_by("+1 month"))

global_format_time1 = GFS_time('2021-07-08 00:00:00')
obj2nd = GFS_time(global_format_time1)
print(obj2nd.seconds_after())
print("global_format_time.time_interval_in_seconds('6 day') = ", global_format_time.time_interval_in_seconds("6 day "))
print("global_format_time.truncate_to('10 minutes') = ", global_format_time.truncate_to("10 minutes"))

print('global_format_time.as_text("%Y-%m-%d %H:%M:%S%z",1,"UTC") = ', global_format_time.as_text('%Y-%m-%d %H:%M:%S%z',85000,'UTC'))
#----------------------------------------------------------------------------
