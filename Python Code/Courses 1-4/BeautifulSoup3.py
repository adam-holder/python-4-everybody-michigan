import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))
tempCount = 1
tempPosition = 1
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')

for tag in tags:
    currenttag = tag.get('href', None)
    print(currenttag)
    #print(tag.get('href', None))
    print('Position?: ',tempPosition)
    print(position)
    if position == tempPosition:
        tempCount = tempCount + 1
        tempPosition = 1
        print('TEST')
        break
    else:
        tempPosition = tempPosition + 1


#FOR FUTURE ADAM
#Create a function that inputs the new soup/tagsself.
#Create a Loop that calls that function, until the count is reached
