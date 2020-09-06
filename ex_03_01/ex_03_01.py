shours = input('Enter Hours: ') # string hours
srate = input('Enter Rate: ')    # string rate
fhours = float(shours) # floating point hours
frate = float(srate)  # floating point rate
# print(fhours, frate)
if fhours > 40:
    # print('Overtime')
    reg = frate * fhours    # regular pay
    overtp = (fhours - 40.0) * (frate * 0.5) # overtime pay
    # print(reg, overtp)
    pay = reg + overtp
else:
    # print('Regular')
    pay = fhours * frate
print('Pay:', pay)
