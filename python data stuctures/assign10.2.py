
#----function to file handle----
def file_handle():
    fname = input('Enter file name: ')
    try:
        fhandle = open(fname)
    except:
        print("Coudn't open the file",fname)
        quit()
    return fhandle


count = dict()

#----function to get dictionary of hours & no_of times hours repeated----
def get_hours(fhandle):

    for line in fhandle:
        if line.startswith('From'):
            line = line.split()
            if len(line) < 5:
                continue
            time = line[5]
            list1 = time.split(':')
            hr = list1[0]
            #----get(key,0) method will return the actual value of key if found----
            #----if not it will return default value '0'----
            count[hr] = count.get(hr,0)+1

fhandle = file_handle()
get_hours(fhandle)

#----sorted() function sorted dictionary by key (hour) in ascending order---- 
for h,v in sorted(count.items()):
    print(h,v)


