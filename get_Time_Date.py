import datetime
now = datetime.datetime.now()
# print('Current time and date: ', now)
# print('Current year: ', now.year)
# print('Current month: ', now.month)
# print('Current day: ', now.day)
# print('Current hour: ', now.hour)
# print('Current minute: ', now.minute)
day_format = '-'.join((str(now.year), str(now.month), str(now.day)))
if now.minute < 10 and now.hour < 10:
    time_format = ':'.join(('0' + str(now.hour),'0' + str(now.minute)))
elif now.hour < 10:
    time_format = ':'.join(('0' + str(now.hour), str(now.minute)))
elif now.minute < 10:
    time_format = ':'.join((str(now.hour),'0' + str(now.minute)))
else:
    time_format = ':'.join((str(now.hour),str(now.minute)))
'''print('Today is:', day_format)
print('Current time is: ', time_format)'''

def TalkingClock(time):
#Define the hour and minutes
    hour = time[0:2]
    minute = time[3:]
#Create the string for output
    current_time = 'It\'s '
#List to contain the names of the hours
    hours = ['midnight', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
#The first part of the names of minutes
    tens = ['oh', 'twenty', 'thirty', 'forty', 'fifty']
#The name of the minutes between 11 and 19
    ten_fwd = ['ten','eleven', 'twelve', 'thirteen', 'forteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
#Hours    
#12-23
    if int(hour) > 12:
        current_time += hours[int(hour) - 12]
#Noon
    elif int(hour) == 12 and int(minute) == 0:
        current_time += 'noon'
#1-12
    else:
        current_time += hours[int(hour)]

#Minutes
    if int(minute) == 0:
        pass
    else:
#Zero-Nine
        if int(minute) < 10 and int(minute) > 0:
            current_time += ' ' + tens[0] + ' ' + hours[int(minute[1])]
#Tens
        elif int(int(minute)/10) == 1:
            current_time += ' ' + ten_fwd[int(minute)-10]
#Twenties
        elif int(int(minute)/10) == 2:
            current_time += ' ' + tens[1]
    #Test if it's exact hour or not
            if int(minute) == 0:
                pass
            else:
    #Test if the minute is a multiple of ten
                if int(minute[1]) != 0:
                    current_time += ' ' + hours[int(minute[1])]
#Thirties
        elif int(int(minute)/10) == 3:
            current_time += ' ' + tens[2]
    #Test if it's exact hour or not
            if int(minute) == 0:
                pass
            else:
    #Test if the minute is a multiple of ten
                if int(minute[1]) != 0:
                    current_time += ' ' + hours[int(minute[1])]
#Forties
        elif int(int(minute)/10) == 4:
            current_time += ' ' + tens[3]
    #Test if it's exact hour or not
            if int(minute) == 0:
                pass
            else:
    #Test if the minute is a multiple of ten
                if int(minute[1]) != 0:
                    current_time += ' ' + hours[int(minute[1])]
#Fifties
        elif int(int(minute)/10) == 5:
            current_time += ' ' + tens[4]
    #Test if it's exact hour or not
            if int(minute) == 0:
                pass
            else:
    #Test if the minute is a multiple of ten
                if int(minute[1]) != 0:
                    current_time += ' ' + hours[int(minute[1])]
#am/pm
#Midnight/Noon
    if int(hour) == 0 or int(hour) == 12:
#Test if it is Noon or between 12am-13pm
        if int(minute) == 0:
            pass
        else:
            current_time += ' am'
#am
    elif int(hour) <= 12:
        current_time += ' am'
#pm
    else:
        current_time += ' pm'
    return current_time
    
# print(TalkingClock(time_format))

def current_date(today):
#Split the date by hifens (-)
    split_today = today.split('-')
#Year will be the first split result
    year = split_today[0]
    months_list =['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
#Month will be the second result of the split, then retrieve its "translation" from 'months_list'
    month = months_list[int(split_today[1]) - 1]
#Day will be the last result from the split
#Convert 'day' to a string to make it better to use in the next conditional chain
    day = int(split_today[2])
    # print(today)
#Check if today's day should be written in a different way than just prefixing it with "th"
    if day == 1 or day == 21 or day == 31:
        ord_suffix = "st"
    elif day == 2 or day == 22:
        ord_suffix = "nd"
    elif day == 3 or day == 23:
        ord_suffix = "rd"
    else:
        ord_suffix = "th"

    return 'Today is {} {}{} of the year {}.'.format(month, day, ord_suffix, year)

# print(current_date(day_format))

if __name__ == "__main__":
    print(TalkingClock(time_format))
    print(current_date(day_format))