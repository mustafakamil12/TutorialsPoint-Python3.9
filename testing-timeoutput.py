import time,datetime

mytime = datetime.datetime(2017, 11, 28, 23, 55, 59, 342380)
print("mytime = ", mytime)
mystr = mytime.strftime('%Y')
print("mystr = ", mystr)

hours =  23
minutes =  36
seconds =  40
#decoDate = datetime.time(hours,minutes,seconds)
#print("decoDate = ", decoDate)
mystrtime = "%+2.2d:%2.2d:%2.2d" % (hours,minutes,seconds)
print(mystrtime)
