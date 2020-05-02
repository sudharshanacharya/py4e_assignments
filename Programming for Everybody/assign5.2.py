
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :break

    #----if the number is other than the integer print appropriate message & continue ----
    try:
        num = int(num)
    except:
        print("Invalid input")
        continue

    #----logical section----        
    if largest is None:
        largest = num
    if smallest is None:
        smallest = num
    else:
        if num > largest : largest = num
        if num < smallest : smallest = num


print("Maximum is", largest)
print("Minimum is",smallest)
