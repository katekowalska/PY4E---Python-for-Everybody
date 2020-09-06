import re

fname = input('Enter the file name: ')
fhand = open(fname)

numlist = list()
for line in fhand:
    line = line.rstrip()
    x = re.findall('New Revision: ([0-9]+)', line)
    if len(x) > 0:
        # print(x)
        number = float(x[0])
        numlist.append(number)
        average = sum(numlist)/len(numlist)
        average = int(average)
print('Average:', average)
