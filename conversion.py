import datetime
import pytz
tzinput=input('Enter TZ :')
ustime = datetime.datetime.now(pytz.timezone(tzinput))
a=ustime.strftime("%Y-%m-%d %H:%M:%S")
print(a)