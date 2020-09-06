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
    counts[host] = counts.get(host, 0) + 1
# print(counts)

largest = -1
theword = None
for key,value in counts.items():
    if value > largest:
        largest = value
        theword = key
print(theword, largest)
