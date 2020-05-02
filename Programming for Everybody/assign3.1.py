#----input hour & convert into float----
hour = input('Enter hour-')
hour = float(hour)

#----input rate & convert into floar----
rate = input('Enter rate-')
rate = float(rate)

#---- calculate gross pay----
if hour <= 40:
    pay = hour*rate
    print(pay)
else:
    pay = 40*rate
    extra_hour = hour-40
    extra_pay = extra_hour * (rate*1.5)
    print(pay + extra_pay)


