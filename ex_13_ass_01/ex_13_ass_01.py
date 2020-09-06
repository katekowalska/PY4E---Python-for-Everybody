import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter URL: ')
    if len(url) < 1:
        break

    print('Retrieving', url)
    urlhand = urllib.request.urlopen(url, context=ctx).read()
    print('Retrieved', len(urlhand), 'characters')

    tree = ET.fromstring(urlhand)
    counts = tree.findall('.//count')
    print('Count: ', len(counts))

    sum = 0
    for count in counts:
        sum = sum + int(count.text)
    print('Sum: ', sum)
