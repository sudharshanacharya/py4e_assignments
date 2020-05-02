fname = input('Enter file name: ')

try:
    fhandle = open(fname)
except:
    print("Coudn't open the file",fname)
    quit()

count = dict()
for line in fhandle:
    if line.startswith('From:'):
        line = line.split()
        email = line[1]
        count[email] = count.get(email,0)+1


email_name =0
no_of_msg = 0

#---- count is a dictionary here----
for e,c in count.items():
    if c > no_of_msg:
        no_of_msg = c
        email_name = e
print(email_name,no_of_msg)

