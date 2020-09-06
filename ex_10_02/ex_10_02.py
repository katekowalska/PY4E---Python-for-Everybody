counts = dict()
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    words = line.split()
    # guardian in a compound statement
    if len(words) < 3 or words[0] != 'From':
        continue
    piece = words[5]
    # print(piece)
    colpos = piece.find(':')
    # print(colpos)
    hour = piece[:colpos]
    # print(hour)
    # idiom: retrieve/create/update counter
    counts[hour] = counts.get(hour, 0) + 1
# print(counts)

# Sort the dictionary by key
temp = list(counts.items())
temp = sorted(temp)
# print(temp)

for key, value in temp:
    print(key, value)
