# Importing necessary libraries
import datetime  # Module for handling dates and times
import pytz  # Module for handling time zones

# Asking user to input a time zone abbreviation
tzinput = input('Enter TZ :')

# Getting the current time in the specified time zone
ustime = datetime.datetime.now(pytz.timezone(tzinput))

# Formatting the current time to display in a specific format
a = ustime.strftime("%Y-%m-%d %H:%M:%S")

# Printing the formatted current time
print(a)
