import datetime

def days_until_event(future_event):
    return future_event - datetime.datetime.today()

def convert_to_date_objects(stuff):
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
    date = datetime.datetime(year, month, day)

    return date
        
def read_file(f='events.txt'):
    events = []
    with open(f, 'r') as f:
        for line in f:
            events.append(line.strip().split(':'))
    return events

def main():
    event_list = read_file()
    date_objs = convert_to_date_objects(event_list)
    data_to_display = []
    data = {}
    for name, date in date_objs.items():
         
         timeleft = days_until_event(date)

         # print '{} left until {}.\n'.format(timeleft, name)
         data_to_display.append('{} left until {}\n'.format(timeleft, name))

    return date_objs

def add_event_manually():
    event_entry = ''
    with open('events.txt', 'a') as f:
        while True:
            name = raw_input('Enter Name of Event')

            month = raw_input('Enter Month')
            day = raw_input('Enter Day')
            year = raw_input('Enter Year')

            event_entry = '{}:{}:{}:{}\n'.format(year, month, day, name)
            f.write(event_entry)

def add_event(date, name):
    ''' date coming in from kivy calendar as [day, month, year] as a str format '''
    # eval converts '[25, 10, 2017]' into list
    date = eval(date)
    event_entry = ''
    with open('events.txt', 'a') as f:
        day = date[0]
        month = date[1]
        year = date[2]
        event_entry = '{}:{}:{}:{}\n'.format(year, month, day, name)
        print event_entry

        # NEED TO VALIDATE ENTRY TO PREVENT ERRORS
        f.write(event_entry)



if __name__ == '__main__':
    main()



