import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore SSL cert Errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all the span tags
tags = soup('span')

countTotal = 0
contentSum = 0
for tag in tags:
    #print('Contents:', tag.contents[0])
    temp = int(tag.contents[0])
    #print(temp)
    countTotal = countTotal + 1
    contentSum = contentSum + temp
print('Count Total: ', countTotal)
print('Sum of contents: ', contentSum)
