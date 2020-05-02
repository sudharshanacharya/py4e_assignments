#----prompt for file-name----
fname = input('Enter file name: ')

#----print error message if file not found----
try:
    fhandle = open(fname)
except:
    print("Coudn't open file", fname)
    quit()

list1 = list()

for line in fhandle:
    for x in line.split():
        if not x in list1:
            list1.append(x)
list1.sort()
print(list1)
