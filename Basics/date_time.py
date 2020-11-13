# dates in python

import datetime # importing datetime module

def date_time(): # date and time function
    date_time = datetime.datetime.now() # it will display datetime with seconds mins and micro seconds
    print(date_time)
   # display todays day in full version
   
    print(date_time.strftime("%d")) # display todays date
    print(date_time.strftime("%w")) # display weekdays as numbers 0-6 sun-sat
    print(date_time.strftime("%d")) # day of month
    print(date_time.strftime("%b")) # month name short version
    print(date_time.strftime("%B")) # month name full version
    print(date_time.strftime("%m")) # month as num
    print(date_time.strftime("%y")) # year short version without century
    print(date_time.strftime("%H")) # hour 00-23
    print(date_time.strftime("%I")) # hour 00-12
    print(date_time.strftime("%Y")) # year full version
    print(date_time.strftime("%p")) # AM/PM
    print(date_time.strftime("%M")) # minute 00-59
    print(date_time.strftime("%S")) # seconds 00-59
    print(date_time.strftime("%f")) # micro seconds
    print(date_time.strftime("%c")) # local version of date and time
    print(date_time.strftime("%x")) # local version of date
    print(date_time.strftime("%X")) # local version of time
    
def main():
    date_time() # calling function
    

if __name__ == '__main__':
    main()





