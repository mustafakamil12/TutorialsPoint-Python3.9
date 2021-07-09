import re


regex1 = r'(\d+ years |)(\d+ mons |)(\d+ |)(\d\d):(\d\d)(:\d\d|)'
regex2 = r'([-+]{0,1}\d*) hour*'
regex3 = r'([-+]{0,1}\d*) minute*'
regex4 = r'([-+]{0,1}\d*) day*'
regex5 = r'([-+]{0,1}\d*) second*'
regex6 = r'([-+]{0,1}\d*) month*'
regex7 = r'([-+]{0,1}\d*) year*'

regex100 = r'hour'

#time_interval = "1979 years 08 mons 17 10:10:02"
time_interval = "0"
test = re.findall(regex2,time_interval)
if(re.findall(regex2, time_interval)):
    print("regex7 match someting ...")
    secCheck = re.findall(regex2, time_interval)

    print("secCheck = ", secCheck)
    if secCheck[0] == "":
        seconds = 3600
    else:
        seconds = int(secCheck[0]) * 3600

    print("seconds = ", seconds)
