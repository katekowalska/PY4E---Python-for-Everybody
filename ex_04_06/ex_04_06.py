def computepay(hours, rate):
    # print("In computepay", hours, rate)
    if hours > 40:
        reg = rate * hours    # regular pay
        overtp = (hours - 40.0) * (rate * 0.5) # overtime pay
        pay = reg + overtp
    else:
        pay = hours * rate
    # print("Returning", pay)
    return pay

shours = input('Enter Hours: ') # string hours
srate = input('Enter Rate: ')    # string rate
fhours = float(shours) # floating point hours
frate = float(srate)  # floating point rate

xp = computepay(fhours, frate)

print('Pay:', xp)
