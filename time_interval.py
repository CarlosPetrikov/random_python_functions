from datetime import datetime, timedelta

# Function that will return a list of dates in descending order, based on the number of days the user needs to "go back in time" 
def time_interval(days, datetime_format):
    day = days
    interval = []
    
    while day != 0:
        data_m1 = datetime.now() - timedelta(days = day)
        data_m2 = data_m1.strftime(datetime_format)
        interval.append(data_m2)
        day -= 1
    
    return interval

# Example where the list starts to be generated from 15 days ago, until today
# Where the datetime pattern will be: Day/Month/Year 
a = time_interval(15, "%d/%m/%Y")
print(a)
