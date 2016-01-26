# Bug when renaming file name if the name already exits

import os
import time

directory = raw_input('Enter a directory: ')
if not directory: directory = os.getcwd()

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

    lst.sort()
    return lst

lst = sort_files()
names_lst = []
backup = open('backup.txt', 'w')

for t, name in lst:
    # Writes filenames for the sake of backup and makes a list
    # Without the now unnecessery time values
    backup.write( name + '\n' )
    names_lst.append(name)
backup.close()

# Stringed numbers for the filenames
filenames_list = map(str, range(1, len(names_lst)+1))

for count, name in enumerate(names_lst):
    ext = os.path.splitext(name)[1]
    join = os.path.join(directory, name)
    print 'Old: ' + join
    print
    new_join = os.path.join(directory, filenames_list[count]) + ext
    print 'New: ' + new_join
    os.rename(join, new_join)
print 'Done'

