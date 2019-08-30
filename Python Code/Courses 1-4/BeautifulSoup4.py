import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Initializing each variable
url = input('Enter - ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))
tempCount = 1
tempPosition = 1
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')

#This function loops through the a tags in the current site for was many times
#as defined by the chosen position at the beginning of the code.
#When it reaches that position it returns to the below loop with the new
#site to scrape through. tempPosition has to be defined as a global variable
#because of a scope issue that causes a traceback error. (can't see tempPosition locally)
def findsite(tags):
    global tempPosition
    for tag in tags:
        currenttag = tag.get('href', None)
        #print(currenttag)
        #print(tag.get('href', None))
        #print('Position?: ',tempPosition)
        #print(position)
        if position == tempPosition:
            tempPosition = 1
            return currenttag
        else:
            tempPosition = tempPosition + 1

# This loop runs the above function until the count is reached.
# When it reaches that count, it uses a Regular Expression to print the Name
# of the final site.
for siteAttempt in range(count):
    if count != tempCount:
        newsite = findsite(tags)
        print('Retriving: ',newsite)
        html = urllib.request.urlopen(newsite, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        tempCount = tempCount + 1
    else:
        newsite = findsite(tags).strip()
        findName = re.findall('by_(.+).html',newsite)
        print('Final site retrieved: ',newsite)
        print(findName)
