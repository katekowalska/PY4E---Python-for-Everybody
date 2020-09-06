import urllib.request, urllib.parse, urllib.error
import json
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

    info = json.loads(urlhand)
    # print(json.dumps(info, indent=4))

    sum = 0
    counts = 0
    for item in info['comments']:
        counts = counts + 1
        sum = sum + int(item['count'])
        # print(item['count'])
    print('Count: ', counts)
    print('Sum: ', sum)
