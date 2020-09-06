from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

count = 0
numlist = list()
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    # print('TAG:', tag)
    # print('Contents:', tag.contents[0])
    numbers = int(tag.contents[0])
    # print(numbers)
    numlist.append(numbers)
    count = count + 1

# print(numlist)
print('Count', count)
print('Sum', sum(numlist))
