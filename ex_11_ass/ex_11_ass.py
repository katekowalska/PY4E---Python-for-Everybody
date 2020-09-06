import re

fhand = open('regex_sum_635427.txt')

numlist = list()
for line in fhand:
    line = line.rstrip()
    # print(line)
    numbers = re.findall('([0-9]+)', line)
    if len(numbers) > 0:
        # print(numbers)
        for x in numbers:
            numlist.append(x)
# print(numlist)

# using list comprehension to perform conversion str to int
test_list = [int(x) for x in numlist]
print(sum(test_list))
