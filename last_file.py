import os
from datetime import datetime, timezone

# Function that will return the most recent file from a directory, filtering by extension 
def last_file(path, extension):
    directory = os.scandir(path)
    dict_file = {}
    
    for file in directory:
        if file.name[-3:] in (extension.lower(), extension.upper()):
            dict_file[datetime.fromtimestamp(file.stat().st_mtime, tz=timezone.utc)] = file.name
    
    time_file = sorted(dict_file)
    return dict_file[time_file[-1]]

#Example
a = last_file('C:/Users/user/Downloads', 'exe')
print(a)

