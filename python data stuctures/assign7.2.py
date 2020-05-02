#----prompt for file-name----
fname = input('Enter file name: ')

#----print error if file not found----
try:
    fhandle = open(fname)
except:
    print('Cannot open file',fname)
    quit()

#----use startswith() method to take line into consideration----
total = 0
count = 0
for line in fhandle:
    if line.startswith('X-DSPAM-Confidence'):
        count+=1
        
        #----index of ':'----
        index = line.find(':')
        #----increment the index by one to go to next index----
        index = index+1
        #----slice & get everything after the ':'----
        slice = line[index : ]
        value = float(slice)
        total+=value
if count is 0:
    print("no line found starting with 'X-DSPAM-Confidence'")
    quit()

print('Average spam confidence:',total/count)
