#----define a function computepay()----
def computepay(hours,rate):
    if hours<=40:
        return hours*rate
    else:
        normal_pay = 40*rate
        extra_hours = hours-40
        extra_pay = extra_hours * (rate * 1.5)
        return normal_pay + extra_pay
      

hrs = input("Enter Hours:")
hrs = float(hrs)
rt = input("Enter rate:")
rt = float(rt)
pay = computepay(hrs,rt)
print ("Pay",pay)
