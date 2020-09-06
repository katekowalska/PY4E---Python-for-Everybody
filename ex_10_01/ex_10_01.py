counts = dict()
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    words = line.split()
    # guardian in a compound statement
    if len(words) < 3 or words[0] != 'From':
        continue
    host = words[1]
    # print(host)
    # idiom: retrieve/create/update counter
    counts[host] = counts.get(host, 0) + 1
# print(counts)

# Sort the dictionary by value
temp = list()
for key, value in counts.items():
    # print(key, value)
    newtup = (value, key)
    temp.append(newtup)
# print('Flipped', temp)

temp = sorted(temp, reverse = True)
# print('Sorted', temp)

for value, key in temp[:1]:
    print(key, value)
