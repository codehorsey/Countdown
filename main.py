from datetime import date
import time

# create date object
today = date.today()
event_in_future = date(2017, 12, 18)


def days_until_event(future_event):
    return future_event - date.today()

def convert_mylist_into_date_objs(stuff):
    converted_list = []
    mydict = {}
    for entry in stuff:
        converted_list.append(return_date(entry))
        mydict[entry[-1]] = return_date(entry)
    return mydict

def return_date(data):
    year = int(data[0])
    month = int(data[1])
    day = int(data[2])
    d = date(year, month, day)
    return d
        
mylist = []
with open('events.txt' , 'r') as f:
    for line in f:
        mylist.append(line.strip().split(':'))
        
cleaned_dates = convert_mylist_into_date_objs(mylist)


for name, date in cleaned_dates.items():
     timeleft = days_until_event(date)
     print '{} left until {}.'.format(timeleft, name)

'''
        
##event_entry = ''
##with open('events.txt', 'a') as handle:
##    
##    while True:
##        name = raw_input('Enter Name of Event')
##        
##        month = raw_input('Enter Month')
##        day = raw_input('Enter Day')
##        year = raw_input('Enter Year')
##
##        
##        # format for date object
##        event_entry = '{}:{}:{}:{}\n'.format(year, month, day, name)
##
##        handle.write(event_entry)
##        

'''
