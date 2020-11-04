# dates in python

import datetime # importing datetime module

def date_time(): # date and time function
    a = datetime.datetime.now() # it will display datetime with seconds mins and micro seconds
    print(a)

    print(a.strftime("%A")) # display todays day in full version
    print(a.strftime("%a")) # display todays day in short version
    print(a.strftime("%d")) # display todays date
    print(a.strftime("%w")) # display weekdays as numbers 0-6 sun-sat
    print(a.strftime("%d")) # day of month
    print(a.strftime("%b")) # month name short version
    print(a.strftime("%B")) # month name full version
    print(a.strftime("%m")) # month as num
    print(a.strftime("%y")) # year short version without century
    print(a.strftime("%H")) # hour 00-23
    print(a.strftime("%I")) # hour 00-12
    print(a.strftime("%Y")) # year full version
    print(a.strftime("%p")) # AM/PM
    print(a.strftime("%M")) # minute 00-59
    print(a.strftime("%S")) # seconds 00-59
    print(a.strftime("%f")) # micro seconds

    print(a.strftime("%c")) # local version of date and time


    print(a.strftime("%x")) # local version of date

    print(a.strftime("%X")) # local version of time
date_time() # calling function





