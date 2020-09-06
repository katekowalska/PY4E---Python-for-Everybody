shours = input('Enter Hours: ') # string hours
srate = input('Enter Rate: ')    # string rate
try:
    fhours = float(shours) # floating point hours
    frate = float(srate)  # floating point rate
except:
    print('Error, please enter numeric input')
    quit()

print(fhours, frate)
if fhours > 40:
    reg = frate * fhours    # regular pay
    overtp = (fhours - 40.0) * (frate * 0.5) # overtime pay
    pay = reg + overtp
else:
    pay = fhours * frate
print('XYZ Pay:', pay)
