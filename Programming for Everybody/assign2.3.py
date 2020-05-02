#----input hour & convert into float----
hour = input('Enter hour-')
hour = float(hour)

#----input rate & convert into floar----
rate = input('Enter rate-')
rate = float(rate)

#---- calculate gross pay----
pay = hour*rate
print('Pay:',pay)
