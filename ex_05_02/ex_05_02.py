largest = None
smallest = None
while True :
    snum = input('Entera number: ')
    if snum == 'done' :
        break
    try:
        num = int(snum)
    except:
        print('Invalid input')
        continue
    # print(fval)
    if largest is None:
        largest = num
    elif num > largest:
        largest = num

    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)
