import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Data collection
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

print('Retrieving: ', url)

taglist = list()
for i in range(0, count):
    # Retrieve all of the anchor tags
    tags = soup('a')
    mytags = tags[position - 1]
    neededtag = mytags.get('href', None)
    url = str(neededtag)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    print('Retrieving: ', mytags.get('href', None))
