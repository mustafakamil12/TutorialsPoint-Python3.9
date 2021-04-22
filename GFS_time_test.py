import os,sys,re,time

class GFS_time:

  ISO_FORMAT='%Y-%m-%d %H:%M:%S%z'

  def __init__(self,timeArr):

    print("timeArr: ", timeArr)
    self.timeArr = timeArr
    time_t = None
    if self.timeArr:
       if inspect.isclass(self.timeArr):  # Copying another GFS_time object
          GFS_time.other = GFS_time(timeArr) # Need to be checked again
          time_t = other.time_t()
       else:                # Initializing from a formatted time string.
          time_t = self.parse_time_string(self.timeArr)
    else:
       time_t = time.time()

    self.time_t = time_t


  def __repr__(self):
      return repr(self.time_t)

  def __getitem__(self):
      return self.time_t


  def as_text(self,timeSer):

     time_t = self.time_t
     if time_t == -1:
        return('')

     #
     #  Interpret the function's arguments.
     #
     fmt = GFS_time.ISO_FORMAT
     utc_offset = 0
     tz_abbrev = 'UTC'

     if timeSer[0] != None:   # first argument = format
        fmt = timeSer.pop(0)
        if timeSer[0] != None: # second argument = UTC offset
           utc_offset = timeSer.pop(0)
           if timeSer[0] != None:   # third argument = timezone abbrev
              tz_abbrev = timeSer.pop(0)

     #
     #  Handle the special formatting group %z to denote utc offset.
     #
     default_match = re.match('\%z',fmt)
     if default_match.group(0):
        #
        #  Format the UTC offset as "[+-]HH[:MM[:SS]]"
        #
        hours = int(utc_offset/3600)
        minutes = int(utc_offset/60)-hours*60
        seconds = utc_offset-3600*hours-60*minutes

        if minutes < 0:
           minutes = -1 * minutes
        if seconds < 0:
           seconds = -1*seconds

        utc_offset_str = None
        if seconds != 0:
           utc_offset_str = '%+2.2d:%2.2d:%2.2d' % (hours,minutes,seconds)
        elif minutes != 0:
           utc_offset_str = '%+2.2d:%2.2d' % (hours,minutes)
        else:
           utc_offset_str = '%+2.2d' % (hours)

        #
        #  Substitute the %z in the format string with the UTC offset string.
        #
        fmt = re.sub('\%z',utc_offset_str,fmt)

     #
     #  Handle the timezone abbreviation to avoid dependency on environment
     #  variable TZ.  This allows formatting for many local times, not just
     #  the one you happen to be in.
     #
     fmt = re.sub('\%Z',tz_abbrev,fmt)

     #
     #  Offset the seconds since 1970 from UTC time as needed.
     #
     time_t += utc_offset

     #
     #  Create a "broken down" time structure w/o any local time adjustments.
     #
     time_tm = gmttime(time_t)

     #
     #  Return the textual representation of the time.
     #
     return(strftime(fmt,time_tm))


# --------------Main-------------
global_format_time = GFS_time([])
global_format_time_Arr = []
global_format_time_Arr.append(global_format_time)

format_time = global_format_time.as_text(global_format_time)

print(mytimeObj)
