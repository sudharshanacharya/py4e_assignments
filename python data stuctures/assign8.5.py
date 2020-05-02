#----prompt for file name----
fname = input('Enter file name: ')

#----print error message if file not found----
try:
    fhandle = open(fname)
except:
    print("Coudn't open file:",fname)
    quit()

count = 0
mail_id = list()
for line in fhandle:
    if line.startswith('From:'):
        count+=1
        mail_id = line.split()
        print(mail_id[1])

print('There were {} lines in the file with From as the first word'.format(count))
