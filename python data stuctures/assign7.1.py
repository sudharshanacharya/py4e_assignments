#----prompt for a filename----
fname = input('enter the file name: ')

#----print error meassage if file doesn't exist----
try:
    fh = open(fname,)
except:
    print('cant open the file:',fname)
    quit()

#----strip the white spaces from the right end of the line----
#----convert to uppercase & print line by line----
for line in fh:
    line = line.rstrip()
    print(line.upper())
