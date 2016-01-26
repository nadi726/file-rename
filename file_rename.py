# Bug when renaming file name if the name already exits

import os
import time

directory = raw_input('Enter a directory: ')
if not directory: directory = os.getcwd()
print '\n'

def sort_files(order='time'):
    """
    Returns a list of the files in the order they should be renamed"""
    
    files = os.listdir(directory)
    lst = []
    # Make a list of tuples each having the time for sorting
    # and the file name.
    for f in files:
        join = os.path.join(directory, f)
        times = time.gmtime(os.path.getmtime(join))
        times = [times.tm_year, times.tm_yday, times.tm_hour, times.tm_min, times.tm_sec]
        lst.append( (times, f) )

    # Sort only be the time value, not the file name
    lst.sort(key=lambda lst: lst[0])
    return lst

names_lst = sort_files()

for count, file_tuple in enumerate(names_lst):
    name = file_tuple[1]
    ext = os.path.splitext(name)[1]
    
    old_join = os.path.join(directory, name)
    new_join = os.path.join(directory, str(count)) + ext
    os.rename(old_join, new_join)
    
    print 'Old: ' + old_join
    print
    print 'New: ' + new_join
    print '-----------------------'
    
print 'Done'

