#Matthew Walker
#sept 21
import calendar
import time

def gmtnow():
    seconds = calendar.timegm(time.gmtime())
    currentSecond = seconds%60
    minutes = seconds // 60
    currentMinute = minutes % 60
    hours = minutes // 60
    currentHour = hours%24
    return currentHour, currentMinute, currentSecond


x = True
while x == True:
    h,m,s = gmtnow()
    print(h,":",m,":",s)
